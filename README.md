# ❄️ Snowfall for Home Assistant

Анимированный снег для вашего Home Assistant!

Добавьте атмосферу зимы на панели управления Home Assistant. Настраивайте снегопад под себя, управляйте им вручную или используйте автоматизации Home Assistant.

<p align="center">
  <a href="#русский">🇷🇺 Русский</a> · <a href="#english">🇬🇧 English</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-2026.10.1-blue" alt="Version">
  <img src="https://img.shields.io/badge/HACS-Custom%20Repository-41BDF5" alt="HACS Custom Repository">
  <img src="https://img.shields.io/github/license/alshevskij/hass-snowfall" alt="License">
  <img src="https://img.shields.io/github/stars/alshevskij/hass-snowfall?style=flat" alt="GitHub Stars">
</p>

<p align="center">
  <a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=alshevskij&repository=hass-snowfall&category=integration">
    <img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Добавить Snowfall в Home Assistant через HACS">
  </a>
</p>

---

## 🇷🇺 Русский

### Возможности

- Анимированный снег непосредственно в интерфейсе Home Assistant.
- Ручное управление снегопадом через отдельный переключатель.
- Три режима работы: Always, Winter и Custom.
- Настройка количества, скорости, размера и прозрачности снежинок.
- Исключение отдельных страниц интерфейса из эффекта.
- Настройка через графический интерфейс Home Assistant.
- Поддержка встроенных автоматизаций Home Assistant для управления снегопадом.

### Установка

**Установка через HACS**

1. Убедитесь, что HACS установлен в Home Assistant.
2. Нажмите на синюю кнопку **Добавить в Home Assistant** в верхней части этой страницы.
3. Откроется ваш Home Assistant с репозиторием Snowfall в HACS.
4. Подтвердите добавление пользовательского репозитория, если потребуется.
5. Найдите Snowfall в HACS и установите интеграцию.
6. Перезагрузите Home Assistant.

Если кнопка не сработала, добавьте репозиторий вручную:

`https://github.com/alshevskij/hass-snowfall`

В HACS выберите категорию **Integration**.

**Ручная установка**

1. Скачайте репозиторий.
2. Скопируйте папку `custom_components/snowfall` в каталог `custom_components` вашей установки Home Assistant.
3. Перезагрузите Home Assistant.

### Настройка

После перезагрузки:

1. Перейдите в **Настройки → Устройства и службы**.
2. Нажмите **Добавить интеграцию**.
3. Найдите **Snowfall for Home Assistant**.
4. Завершите настройку.

Дополнительные параметры доступны в настройках интеграции.

### Параметры снегопада

| Параметр | Описание |
|---|---|
| Режим работы | Always, Winter или Custom |
| Активные месяцы | Выбор месяцев для режима Custom |
| Количество снежинок | 10–300 |
| Скорость | 25–200 |
| Размер | 25–200 |
| Прозрачность | 10–100 |
| Исключённые страницы | Пути страниц, на которых снег не отображается |

Исключённые пути указываются по одному на строку.

### Режимы работы

- **Always** — снегопад разрешён в любое время года.
- **Winter** — снегопад разрешён с декабря по февраль.
- **Custom** — снегопад разрешён только в выбранные месяцы.

### Управление через Home Assistant

Интеграция создаёт переключатель:

`switch.snowfall`

Он позволяет включать и выключать снегопад вручную, через панель управления, скрипты или автоматизации.

#### Необязательно использовать сезонные режимы Snowfall

Вы можете вообще не пользоваться встроенным расписанием по месяцам или зимним режимом.

Для этого выберите **Always**, а расписание полностью настройте средствами самого Home Assistant.

Просто автоматизируйте переключатель `switch.snowfall`:

- Включайте снег в определённую дату.
- Отключайте его весной.
- Запускайте снегопад после захода солнца.
- Включайте эффект только при нахождении дома.
- Используйте любые другие условия и сценарии.

Таким образом, Snowfall отвечает за визуальный эффект, а Home Assistant — за логику его включения и выключения.

Документация: [Автоматизации Home Assistant](https://www.home-assistant.io/docs/automation/).

### Поддержка

Нашли ошибку или хотите предложить новую возможность?

[Создать Issue на GitHub](https://github.com/alshevskij/hass-snowfall/issues).

### Лицензия

Проект распространяется под лицензией, указанной в файле [LICENSE](LICENSE).

---

## 🇬🇧 English

### Features

- Animated snowfall directly in the Home Assistant frontend.
- Manual control through a dedicated switch.
- Three operating modes: Always, Winter, and Custom.
- Adjustable snowflake count, speed, size, and opacity.
- Exclude specific dashboard pages from the effect.
- Configure everything through the Home Assistant UI.
- Native Home Assistant automation support.

### Installation

**Install via HACS**

1. Make sure HACS is installed in Home Assistant.
2. Click the **Add to Home Assistant** button at the top of this page.
3. Your Home Assistant instance will open the Snowfall repository in HACS.
4. Confirm adding the custom repository if prompted.
5. Find Snowfall in HACS and install it.
6. Restart Home Assistant.

Alternatively, add the repository manually:

`https://github.com/alshevskij/hass-snowfall`

Select **Integration** as the category.

**Manual installation**

1. Download this repository.
2. Copy `custom_components/snowfall` into your Home Assistant `custom_components` directory.
3. Restart Home Assistant.

### Configuration

After restarting:

1. Go to **Settings → Devices & services**.
2. Click **Add integration**.
3. Search for **Snowfall for Home Assistant**.
4. Complete the setup.

Additional options are available in the integration settings.

### Snowfall settings

| Setting | Description |
|---|---|
| Operating mode | Always, Winter, or Custom |
| Active months | Select months for Custom mode |
| Snowflake count | 10–300 |
| Speed | 25–200 |
| Size | 25–200 |
| Opacity | 10–100 |
| Excluded paths | Pages where snowfall is hidden |

Enter excluded paths one per line.

### Operating modes

- **Always** — snowfall is allowed throughout the year.
- **Winter** — snowfall is allowed from December through February.
- **Custom** — snowfall is allowed only during selected months.

### Home Assistant control

The integration creates a switch entity:

`switch.snowfall`

Use it to manually enable or disable snowfall, add it to your dashboard, or control it through scripts and automations.

#### You don't have to use Snowfall's seasonal scheduling

You can skip the built-in monthly and winter scheduling entirely.

Simply select **Always** and let Home Assistant handle the schedule through its native automations.

Automate `switch.snowfall` to:

- Enable snowfall on a specific date.
- Disable it when winter ends.
- Start snowfall at sunset.
- Show snow only when someone is at home.
- Use any other conditions and scenarios.

Snowfall handles the visual effect, while Home Assistant controls when it runs.

Documentation: [Home Assistant Automations](https://www.home-assistant.io/docs/automation/).

### Support

Found a bug or have a feature request?

[Open a GitHub Issue](https://github.com/alshevskij/hass-snowfall/issues).

### License

See the [LICENSE](LICENSE) file.
