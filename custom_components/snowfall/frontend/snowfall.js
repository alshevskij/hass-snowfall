(() => {
  // Stop a previously injected instance before installing the updated renderer.
  if (typeof window.__haSnowfallCleanup === "function") {
    window.__haSnowfallCleanup();
  }
  window.__haSnowfallLoaded = true;

  const ENTITY = "switch.snowfall";
  const SETTINGS_UPDATE_INTERVAL = 500;
  const canvas = document.createElement("canvas");
  canvas.id = "ha-snowfall-canvas";
  canvas.style.cssText = `
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 5;
    display: none;
  `;
  document.documentElement.appendChild(canvas);

  const ctx = canvas.getContext("2d");
  if (!ctx) {
    canvas.remove();
    return;
  }

  const defaults = {
    mode: "always", months: [12, 1, 2], excluded_paths: [], included_paths: [],
    flake_count: 120, speed: 100, size: 100, opacity: 85, fps: 60,
    flake_style: "mixed", preset: "normal", wind_strength: 0,
    wind_direction: "right", wind_gusts: 20,
  };
  const presets = {
    light: { count: 0.55, speed: 0.75, wind: 0.65 },
    normal: { count: 1, speed: 1, wind: 1 },
    heavy: { count: 1.4, speed: 1.12, wind: 1.15 },
    blizzard: { count: 1.8, speed: 1.35, wind: 1.55 },
  };

  let settings = { ...defaults };
  let width = 0, height = 0, pixelRatio = 1;
  let flakes = [], lastCount = -1, lastStyle = "";
  let lastSettingsUpdate = 0, lastFrameTime = 0;
  let animationFrame = null, isVisible = false;

  const cleanup = () => {
    if (animationFrame !== null) {
      window.cancelAnimationFrame(animationFrame);
      animationFrame = null;
    }
    window.removeEventListener("resize", resize);
    document.removeEventListener("visibilitychange", handleVisibilityChange);
    canvas.remove();
    window.__haSnowfallLoaded = false;
    window.__haSnowfallCleanup = null;
  };

  window.__haSnowfallCleanup = cleanup;

  const clamp = (value, min, max, fallback) => {
    const number = Number(value);
    return Number.isFinite(number) ? Math.max(min, Math.min(max, number)) : fallback;
  };
  const normalizePaths = (value) => {
    if (Array.isArray(value)) return value.filter((path) => typeof path === "string");
    if (typeof value === "string") return value.split(/[,;\n]+/).map((p) => p.trim()).filter(Boolean);
    return [];
  };
  const resize = () => {
    width = window.innerWidth;
    height = window.innerHeight;
    pixelRatio = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(width * pixelRatio);
    canvas.height = Math.round(height * pixelRatio);
    ctx.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
    lastCount = -1;
  };
  const getSwitchState = () => document.querySelector("home-assistant")?.hass?.states?.[ENTITY];

  const updateSettings = () => {
    const entity = getSwitchState();
    if (!entity?.attributes) return;
    const a = entity.attributes;
    settings = {
      mode: a.mode ?? defaults.mode,
      months: Array.isArray(a.months) ? a.months.map(Number).filter((m) => Number.isInteger(m) && m >= 1 && m <= 12) : defaults.months,
      excluded_paths: normalizePaths(a.excluded_paths),
      included_paths: normalizePaths(a.included_paths),
      flake_count: clamp(a.flake_count, 10, 300, defaults.flake_count),
      speed: clamp(a.speed, 25, 200, defaults.speed),
      size: clamp(a.size, 25, 200, defaults.size),
      opacity: clamp(a.opacity, 10, 100, defaults.opacity),
      fps: clamp(a.fps, 30, 60, defaults.fps),
      flake_style: a.flake_style ?? defaults.flake_style,
      preset: a.preset ?? defaults.preset,
      wind_strength: clamp(a.wind_strength, 0, 100, defaults.wind_strength),
      wind_direction: a.wind_direction ?? defaults.wind_direction,
      wind_gusts: clamp(a.wind_gusts, 0, 100, defaults.wind_gusts),
    };
  };

  const pathMatches = (path, rule) => {
    const normalized = rule.trim().replace(/\/+$/, "") || "/";
    return path === normalized || path.startsWith(normalized === "/" ? "/" : `${normalized}/`);
  };
  const isPathAllowed = () => {
    const path = window.location.pathname;
    if (settings.included_paths.length && !settings.included_paths.some((rule) => pathMatches(path, rule))) return false;
    return !settings.excluded_paths.some((rule) => pathMatches(path, rule));
  };
  const isInSeason = () => {
    if (settings.mode === "always") return true;
    const month = new Date().getMonth() + 1;
    if (settings.mode === "winter") return [12, 1, 2].includes(month);
    if (settings.mode === "custom") return settings.months.includes(month);
    return false;
  };

  const effectiveCount = () => {
    const profile = presets[settings.preset] ?? presets.normal;
    return Math.min(300, Math.max(10, Math.round(settings.flake_count * profile.count)));
  };

  const createFlakes = () => {
    flakes = Array.from({ length: effectiveCount() }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      baseRadius: 1 + Math.random() * 3,
      speed: 0.4 + Math.random() * 1.2,
      phase: Math.random() * Math.PI * 2,
      gustPhase: Math.random() * Math.PI * 2,
      rotation: Math.random() * Math.PI * 2,
      rotationSpeed: (Math.random() - 0.5) * 0.025,
      kind: Math.random(),
    }));
    lastCount = effectiveCount();
    lastStyle = settings.flake_style;
  };

  const drawDot = (flake, radius) => {
    ctx.beginPath();
    ctx.arc(flake.x, flake.y, radius, 0, Math.PI * 2);
    ctx.fill();
  };

  const drawSnowflake = (flake, radius, crystal = false) => {
    ctx.save();
    ctx.translate(flake.x, flake.y);
    ctx.rotate(flake.rotation);
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    ctx.lineWidth = Math.max(0.65, radius * (crystal ? 0.24 : 0.3));
    ctx.strokeStyle = ctx.fillStyle;
    const arms = 6;
    for (let i = 0; i < arms; i++) {
      const angle = (Math.PI * 2 * i) / arms;
      const inner = radius * (crystal ? 0.18 : 0.12);
      const outer = radius * (crystal ? 1.8 : 1.45);
      const x1 = Math.cos(angle) * inner, y1 = Math.sin(angle) * inner;
      const x2 = Math.cos(angle) * outer, y2 = Math.sin(angle) * outer;
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      if (crystal) {
        const branchStart = radius * 0.65;
        const branchEnd = radius * 1.05;
        for (const side of [-1, 1]) {
          const bx = Math.cos(angle) * branchStart;
          const by = Math.sin(angle) * branchStart;
          const branchAngle = angle + side * 0.72;
          ctx.moveTo(bx, by);
          ctx.lineTo(bx + Math.cos(branchAngle) * branchEnd * 0.48, by + Math.sin(branchAngle) * branchEnd * 0.48);
        }
      } else {
        const branchBase = radius * 0.72;
        for (const side of [-1, 1]) {
          const bx = Math.cos(angle) * branchBase, by = Math.sin(angle) * branchBase;
          const branchAngle = angle + side * 0.82;
          ctx.moveTo(bx, by);
          ctx.lineTo(bx + Math.cos(branchAngle) * radius * 0.48, by + Math.sin(branchAngle) * radius * 0.48);
        }
      }
      ctx.stroke();
    }
    if (crystal) {
      ctx.beginPath();
      ctx.arc(0, 0, Math.max(0.5, radius * 0.2), 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();
  };

  const drawFlake = (flake, radius) => {
    const style = settings.flake_style;
    if (style === "dots") return drawDot(flake, radius);
    if (style === "snowflakes") return drawSnowflake(flake, radius);
    if (style === "crystals") return drawSnowflake(flake, radius, true);
    if (flake.kind < 0.34) drawDot(flake, radius);
    else if (flake.kind < 0.68) drawSnowflake(flake, radius);
    else drawSnowflake(flake, radius, true);
  };

  const setVisibility = (visible) => {
    if (isVisible === visible) return;
    isVisible = visible;
    canvas.style.display = visible ? "block" : "none";
    if (!visible) ctx.clearRect(0, 0, width, height);
  };

  const frame = (timestamp) => {
    if (timestamp - lastSettingsUpdate >= SETTINGS_UPDATE_INTERVAL) {
      updateSettings();
      lastSettingsUpdate = timestamp;
    }
    const state = getSwitchState();
    const shouldShow = state?.state === "on" && isInSeason() && isPathAllowed() && !document.hidden;
    setVisibility(shouldShow);

    if (shouldShow) {
      const frameInterval = 1000 / settings.fps;
      if (lastFrameTime && timestamp - lastFrameTime < frameInterval) {
        animationFrame = window.requestAnimationFrame(frame);
        return;
      }
      const deltaTime = lastFrameTime ? Math.min(timestamp - lastFrameTime, 50) / 16.67 : 1;
      lastFrameTime = timestamp;
      const count = effectiveCount();
      if (count !== lastCount || settings.flake_style !== lastStyle) createFlakes();

      ctx.clearRect(0, 0, width, height);
      ctx.fillStyle = `rgba(255,255,255,${settings.opacity / 100})`;
      ctx.strokeStyle = ctx.fillStyle;

      const profile = presets[settings.preset] ?? presets.normal;
      const speedMultiplier = (settings.speed / 100) * profile.speed;
      const sizeMultiplier = settings.size / 100;
      const windPower = (settings.wind_strength / 100) * 2.8 * profile.wind;
      const gustPower = windPower * (settings.wind_gusts / 100) * 1.8;

      for (const flake of flakes) {
        const radius = flake.baseRadius * sizeMultiplier;
        const gustWave = Math.sin(timestamp * 0.0015 + flake.gustPhase);
        const variableWave = Math.sin(timestamp * 0.00045 + flake.phase);
        let direction = settings.wind_direction === "left" ? -1 : 1;
        if (settings.wind_direction === "variable") direction = Math.sin(timestamp * 0.00035 + flake.phase) >= 0 ? 1 : -1;
        const wind = direction * (windPower + gustWave * gustPower * 0.55);
        const sway = Math.sin(timestamp * 0.001 + flake.phase) * 0.32;
        flake.x += (wind + sway + variableWave * gustPower * 0.12) * deltaTime;
        flake.y += flake.speed * (radius / 2 + 0.5) * speedMultiplier * deltaTime;
        flake.rotation += flake.rotationSpeed * deltaTime;

        if (flake.y > height + 12) {
          flake.y = -12;
          flake.x = Math.random() * width;
        }
        if (flake.x < -20) flake.x = width + 20;
        else if (flake.x > width + 20) flake.x = -20;
        drawFlake(flake, radius);
      }
    } else {
      lastFrameTime = 0;
    }
    animationFrame = window.requestAnimationFrame(frame);
  };

  const handleVisibilityChange = () => {
    if (document.hidden) {
      setVisibility(false);
      lastFrameTime = 0;
    }
  };
  window.addEventListener("resize", resize, { passive: true });
  document.addEventListener("visibilitychange", handleVisibilityChange);
  resize();
  animationFrame = window.requestAnimationFrame(frame);
})();
