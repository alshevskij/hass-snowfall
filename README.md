# ❄️ Snowfall for Home Assistant

Добавьте атмосферу зимы на панели управления Home Assistant!

Snowfall — пользовательская интеграция, которая добавляет анимированный эффект падающего снега непосредственно в интерфейс Home Assistant. Настраивайте снегопад под себя, управляйте им вручную или полностью доверьте расписание автоматизациям Home Assistant.

<p align="center">
  <a href="README.md">🇷🇺 Русский</a> · <a href="README.en.md">🇬🇧 English</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-2026.10.1-blue" alt="Version">
  <img src="https://img.shields.io/badge/HACS-Custom%20Repository-41BDF5" alt="HACS">
  <img src="https://img.shields.io/github/license/alshevskij/hass-snowfall" alt="License">
  <img src="https://img.shields.io/github/stars/alshevskij/hass-snowfall?style=flat" alt="GitHub Stars">
</p>

<p align="center">
  <a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=alshevskij&repository=hass-snowfall&category=integration">
    <img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Добавить Snowfall в Home Assistant через HACS">
  </a>
</p>

---

## Возможности

- Анимированный снег непосредственно в интерфейсе Home Assistant.
- Ручное управление снегопадом через отдельный переключатель.
- Три режима работы: Always, Winter и Custom.
- Настройка количества, скорости, размера и прозрачности снежинок.
- Исключение отдельных страниц интерфейса из эффекта.
- Настройка через графический интерфейс Home Assistant.
- Возможность управлять расписанием через встроенные автоматизации Home Assistant.

## Установка

### Через HACS

1. Убедитесь, что HACS установлен в Home Assistant.
2. Нажмите синюю кнопку **Add to Home Assistant** выше.
3. Откроется ваш Home Assistant с репозиторием Snowfall в HACS.
4. Подтвердите добавление пользовательского репозитория, если потребуется.
5. Найдите Snowfall в HACS и установите интеграцию.
6. Перезагрузите Home Assistant.

Если кнопка не сработала, добавьте репозиторий вручную:

`https://github.com/alshevskij/hass-snowfall`

В HACS выберите категорию **Integration**.

### Ручная установка

1. Скачайте репозиторий.
2. Скопируйте папку `custom_components/snowfall` в каталог `custom_components` вашей установки Home Assistant.
3. Перезагрузите Home Assistant.

## Настройка

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

## Режимы работы

- **Always** — снегопад разрешён в любое время года.
- **Winter** — снегопад разрешён с декабря по февраль.
- **Custom** — снегопад разрешён только в выбранные месяцы.

## Управление через Home Assistant

Интеграция создаёт переключатель:

`switch.snowfall`

Он позволяет включать и выключать снегопад вручную, через панель управления, скрипты или автоматизации.

### Необязательно использовать сезонные режимы Snowfall

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

## Поддержка

Нашли ошибку или хотите предложить новую возможность?

[Создать Issue на GitHub](https://github.com/alshevskij/hass-snowfall/issues).

## Лицензия

Проект распространяется под лицензией, указанной в файле [LICENSE](LICENSE).
