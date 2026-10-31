# Snowfall for Home Assistant

Bring animated snowfall to your Home Assistant dashboard.

**Snowfall** is a custom integration that adds a configurable animated snow effect to the Home Assistant frontend. Control snowfall manually with a switch, configure seasonal behavior, or let Home Assistant automations decide when the snow should appear.

## Features

- Animated snowfall directly in the Home Assistant interface
- Enable or disable snowfall using a dedicated switch
- Three operating modes:
  - **Always** — snowfall can be enabled at any time of the year
  - **Winter** — snowfall is active only from December through February
  - **Custom** — choose the months when snowfall is allowed
- Adjustable snowflake count, speed, size, and opacity
- Exclude specific dashboard pages from the effect
- Configure everything through the Home Assistant UI
- Use native Home Assistant automations for complete scheduling control

## Installation

### HACS (Custom repository)

1. Open **HACS** in Home Assistant.
2. Open the integrations section.
3. Select the three-dot menu and choose **Custom repositories**.
4. Add the repository URL:

   `https://github.com/alshevskij/hass-snowfall`

5. Select **Integration** as the category.
6. Click **Add**.
7. Find **Snowfall for Home Assistant** in HACS and install it.
8. Restart Home Assistant.

### Manual installation

1. Download or clone this repository.
2. Copy the `custom_components/snowfall` directory into your Home Assistant `custom_components` directory.
3. Restart Home Assistant.

Your directory structure should look like this:

```text
config/
└── custom_components/
    └── snowfall/
        ├── __init__.py
        ├── manifest.json
        ├── config_flow.py
        ├── const.py
        ├── switch.py
        ├── frontend/
        │   └── snowfall.js
        └── translations/
            ├── en.json
            └── ru.json
```

## Configuration

After restarting Home Assistant:

1. Go to **Settings → Devices & services**.
2. Select **Add integration**.
3. Search for **Snowfall for Home Assistant**.
4. Complete the setup.

After installation, open the integration's options to configure the snowfall effect.

### Available settings

| Setting | Description |
|---|---|
| Operating mode | Always, Winter, or Custom |
| Active months | Select the months when snowfall is allowed (Custom mode) |
| Snowflake count | Number of snowflakes (10–300) |
| Speed | Snowfall speed (25–200) |
| Size | Snowflake size (25–200) |
| Opacity | Snowflake transparency (10–100) |
| Excluded paths | Dashboard paths where snowfall should be hidden |

Excluded paths must be entered one per line.

## Controlling snowfall

The integration creates a switch entity:

`switch.snowfall`

Use this switch to enable or disable the animated snowfall effect.

You can add it to any Home Assistant dashboard, control it from scripts, or use it as an automation target.

## Automation control

You don't have to use the integration's seasonal modes to schedule snowfall.

If you prefer, you can set the operating mode to **Always** and let Home Assistant handle all scheduling through its built-in automations.

This means you can simply automate the `switch.snowfall` entity — no need to configure winter months or custom seasonal schedules inside the integration.

For example, you can:

- Turn snowfall on in December and off in January.
- Enable snowfall at sunset and disable it in the morning.
- Show snow only when someone is at home.
- Control snowfall based on weather conditions.
- Create your own seasonal schedules or dashboard controls.

In an automation, simply use the **Turn on** and **Turn off** actions for `switch.snowfall`.

This approach gives you complete flexibility: Snowfall handles the visual effect, while Home Assistant decides when it should run.

For more information, see the [Home Assistant automation documentation](https://www.home-assistant.io/docs/automation/).

## Seasonal modes explained

**Always**

The integration does not restrict snowfall based on the month. The effect is controlled by the switch.

**Winter**

Snowfall is allowed during December, January, and February.

**Custom**

Choose the months during which snowfall is allowed.

In all modes, the switch remains the main manual control for enabling and disabling the effect.

## Requirements

- Home Assistant
- HACS (only if installing through HACS)

## Support and issues

If you encounter a problem or have a feature request, please open an issue:

[GitHub Issues](https://github.com/alshevskij/hass-snowfall/issues)

## License

See the [LICENSE](LICENSE) file.

---

# Snowfall for Home Assistant

Добавьте анимированный снег на главную панель Home Assistant.

**Snowfall** — пользовательская интеграция, которая добавляет на интерфейс Home Assistant настраиваемый эффект падающего снега. Управляйте снегопадом вручную с помощью переключателя, настройте сезонную работу или полностью доверьте расписание встроенным автоматизациям Home Assistant.

## Возможности

- Анимированный снег непосредственно в интерфейсе Home Assistant
- Включение и выключение снегопада с помощью отдельного переключателя
- Три режима работы:
  - **Always** — снегопад можно включить в любое время года
  - **Winter** — снегопад работает только с декабря по февраль
  - **Custom** — выбор месяцев, в которые разрешён снегопад
- Настройка количества, скорости, размера и прозрачности снежинок
- Исключение отдельных страниц интерфейса из эффекта
- Настройка через графический интерфейс Home Assistant
- Возможность полностью управлять расписанием через встроенные автоматизации Home Assistant

## Установка

### HACS (пользовательский репозиторий)

1. Откройте **HACS** в Home Assistant.
2. Перейдите в раздел интеграций.
3. Откройте меню с тремя точками и выберите **Custom repositories**.
4. Добавьте ссылку на репозиторий:

   `https://github.com/alshevskij/hass-snowfall`

5. В качестве категории выберите **Integration**.
6. Нажмите **Add**.
7. Найдите **Snowfall for Home Assistant** в HACS и установите интеграцию.
8. Перезагрузите Home Assistant.

### Ручная установка

1. Скачайте или клонируйте этот репозиторий.
2. Скопируйте папку `custom_components/snowfall` в каталог `custom_components` вашей установки Home Assistant.
3. Перезагрузите Home Assistant.

Структура каталогов должна выглядеть следующим образом:

```text
config/
└── custom_components/
    └── snowfall/
        ├── __init__.py
        ├── manifest.json
        ├── config_flow.py
        ├── const.py
        ├── switch.py
        ├── frontend/
        │   └── snowfall.js
        └── translations/
            ├── en.json
            └── ru.json
```

## Настройка

После перезагрузки Home Assistant:

1. Перейдите в **Настройки → Устройства и службы**.
2. Нажмите **Добавить интеграцию**.
3. Найдите **Snowfall for Home Assistant**.
4. Завершите установку.

После добавления интеграции откройте её параметры, чтобы настроить эффект снегопада.

### Доступные параметры

| Параметр | Описание |
|---|---|
| Режим работы | Always, Winter или Custom |
| Активные месяцы | Выбор месяцев, когда разрешён снегопад (режим Custom) |
| Количество снежинок | Количество снежинок (10–300) |
| Скорость | Скорость падения (25–200) |
| Размер | Размер снежинок (25–200) |
| Прозрачность | Прозрачность снежинок (10–100) |
| Исключённые страницы | Пути страниц, на которых снегопад не отображается |

Каждый исключённый путь необходимо указывать с новой строки.

## Управление снегопадом

Интеграция создаёт сущность переключателя:

`switch.snowfall`

С помощью неё можно включать и выключать анимированный снегопад.

Добавьте переключатель на любую панель Home Assistant, управляйте им из скриптов или используйте в автоматизациях.

## Управление через автоматизации

Использовать сезонные режимы самой интеграции необязательно.

Если вам удобнее самостоятельно управлять расписанием, установите режим **Always** и поручите всю логику встроенным автоматизациям Home Assistant.

В этом случае достаточно автоматизировать обычное включение и выключение сущности `switch.snowfall` — настраивать зимние месяцы или отдельное сезонное расписание внутри интеграции не потребуется.

Например, можно:

- Включать снегопад в декабре и выключать в январе.
- Запускать снег вечером и отключать утром.
- Показывать снег только тогда, когда кто-то находится дома.
- Управлять снегопадом в зависимости от погодных условий.
- Создавать собственные сезонные расписания и элементы управления на панели.

В автоматизации достаточно использовать действия **Turn on** и **Turn off** для `switch.snowfall`.

Такой подход даёт полную свободу: Snowfall отвечает за визуальный эффект, а Home Assistant самостоятельно решает, когда он должен работать.

Подробнее: [Документация по автоматизациям Home Assistant](https://www.home-assistant.io/docs/automation/).

## Режимы работы

**Always**

Интеграция не ограничивает снегопад по месяцам. Эффект управляется переключателем.

**Winter**

Снегопад разрешён в декабре, январе и феврале.

**Custom**

Вы самостоятельно выбираете месяцы, в которые разрешён снегопад.

В любом режиме переключатель остаётся основным способом ручного включения и выключения эффекта.

## Требования

- Home Assistant
- HACS (только для установки через HACS)

## Поддержка и сообщения об ошибках

Если вы столкнулись с проблемой или хотите предложить новую функцию, создайте обращение:

[GitHub Issues](https://github.com/alshevskij/hass-snowfall/issues)

## Лицензия

См. файл [LICENSE](LICENSE).
