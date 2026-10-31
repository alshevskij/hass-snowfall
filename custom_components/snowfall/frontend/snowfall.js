
(() => {
  if (window.__haSnowfallLoaded) return;
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
    mode: "always",
    months: [12, 1, 2],
    excluded_paths: [],
    flake_count: 120,
    speed: 100,
    size: 100,
    opacity: 85,
  };

  let settings = { ...defaults };

  let width = 0;
  let height = 0;
  let pixelRatio = 1;

  let flakes = [];
  let lastCount = -1;

  let lastSettingsUpdate = 0;
  let lastFrameTime = 0;
  let animationFrame = null;

  let isVisible = false;

  const clamp = (value, min, max, fallback) => {
    const number = Number(value);

    return Number.isFinite(number)
      ? Math.max(min, Math.min(max, number))
      : fallback;
  };

  const resize = () => {
    width = window.innerWidth;
    height = window.innerHeight;

    pixelRatio = Math.min(window.devicePixelRatio || 1, 2);

    canvas.width = Math.round(width * pixelRatio);
    canvas.height = Math.round(height * pixelRatio);

    ctx.setTransform(
      pixelRatio,
      0,
      0,
      pixelRatio,
      0,
      0
    );

    lastCount = -1;
  };

  const getSwitchState = () =>
    document.querySelector("home-assistant")?.hass?.states?.[ENTITY];

  const updateSettings = () => {
    const entity = getSwitchState();

    if (!entity?.attributes) return;

    const a = entity.attributes;

    settings = {
      mode: a.mode ?? defaults.mode,

      months: Array.isArray(a.months)
        ? a.months
            .map(Number)
            .filter(
              (month) =>
                Number.isInteger(month) &&
                month >= 1 &&
                month <= 12
            )
        : defaults.months,

      excluded_paths: Array.isArray(a.excluded_paths)
        ? a.excluded_paths.filter(
            (path) => typeof path === "string"
          )
        : defaults.excluded_paths,

      flake_count: clamp(
        a.flake_count,
        10,
        300,
        defaults.flake_count
      ),

      speed: clamp(
        a.speed,
        25,
        200,
        defaults.speed
      ),

      size: clamp(
        a.size,
        25,
        200,
        defaults.size
      ),

      opacity: clamp(
        a.opacity,
        10,
        100,
        defaults.opacity
      ),
    };
  };

  const isExcluded = () => {
    const path = window.location.pathname;

    return settings.excluded_paths.some((excludedPath) => {
      const normalized = excludedPath.trim();

      if (!normalized) return false;

      return (
        path === normalized ||
        path.startsWith(
          normalized.endsWith("/")
            ? normalized
            : `${normalized}/`
        )
      );
    });
  };

  const isInSeason = () => {
    if (settings.mode === "always") return true;

    const month = new Date().getMonth() + 1;

    if (settings.mode === "winter") {
      return [12, 1, 2].includes(month);
    }

    if (settings.mode === "custom") {
      return settings.months.includes(month);
    }

    return false;
  };

  const createFlakes = () => {
    const count = settings.flake_count;

    flakes = Array.from({ length: count }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      baseRadius: 1 + Math.random() * 3,
      speed: 0.4 + Math.random() * 1.2,
      phase: Math.random() * Math.PI * 2,
    }));

    lastCount = count;
  };

  const setVisibility = (visible) => {
    if (isVisible === visible) return;

    isVisible = visible;
    canvas.style.display = visible ? "block" : "none";

    if (!visible) {
      ctx.clearRect(0, 0, width, height);
    }
  };

  const frame = (timestamp) => {
    if (timestamp - lastSettingsUpdate >= SETTINGS_UPDATE_INTERVAL) {
      updateSettings();
      lastSettingsUpdate = timestamp;
    }

    const deltaTime = lastFrameTime
      ? Math.min(timestamp - lastFrameTime, 50) / 16.67
      : 1;

    lastFrameTime = timestamp;

    const state = getSwitchState();

    const shouldShow =
      state?.state === "on" &&
      isInSeason() &&
      !isExcluded() &&
      !document.hidden;

    setVisibility(shouldShow);

    if (shouldShow) {
      if (settings.flake_count !== lastCount) {
        createFlakes();
      }

      ctx.clearRect(0, 0, width, height);

      ctx.fillStyle = `rgba(255,255,255,${settings.opacity / 100})`;

      const speedMultiplier = settings.speed / 100;
      const sizeMultiplier = settings.size / 100;

      for (const flake of flakes) {
        const radius = flake.baseRadius * sizeMultiplier;

        flake.y +=
          flake.speed *
          (radius / 2 + 0.5) *
          speedMultiplier *
          deltaTime;

        flake.x +=
          Math.sin(timestamp * 0.001 + flake.phase) *
          0.4 *
          deltaTime;

        if (flake.y > height + 5) {
          flake.y = -5;
          flake.x = Math.random() * width;
        }

        ctx.beginPath();
        ctx.arc(
          flake.x,
          flake.y,
          radius,
          0,
          Math.PI * 2
        );
        ctx.fill();
      }
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

  document.addEventListener(
    "visibilitychange",
    handleVisibilityChange
  );

  resize();

  animationFrame = window.requestAnimationFrame(frame);
})();
