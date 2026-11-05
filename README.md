# ❄️ Snowfall for Home Assistant

Добавьте атмосферу зимы на панели управления Home Assistant!

Snowfall — пользовательская интеграция, которая добавляет анимированный эффект падающего снега непосредственно в интерфейс Home Assistant. Управляйте эффектом через штатные сущности Home Assistant, используйте автоматизации и настраивайте внешний вид без YAML.

<p align="center">
  <a href="README.md">🇷🇺 Русский</a> · <a href="README.en.md">🇬🇧 English</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-2026.11.1-blue" alt="Version">
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
- Переключатель включения и выключения снегопада.
- Три режима: новогодний (декабрь–февраль), круглогодичный и пользовательский.
- Отдельные переключатели для каждого из 12 месяцев.
- Настройка количества, скорости, размера и прозрачности снежинок.
- Ограничение частоты отрисовки: 30 или 60 FPS.
- Белый список страниц, на которых разрешён снегопад.
- Чёрный список страниц, на которых снегопад запрещён.
- Все настройки доступны как обычные сущности Home Assistant и могут использоваться в автоматизациях.

## Установка

### Через HACS

1. Убедитесь, что HACS установлен в Home Assistant.
2. Нажмите синюю кнопку **Add to Home Assistant** выше.
3. Откройте репозиторий Snowfall в HACS и подтвердите добавление пользовательского репозитория, если потребуется.
4. Найдите Snowfall и установите интеграцию.
5. Перезагрузите Home Assistant.

Если кнопка не сработала, добавьте репозиторий вручную:

`https://github.com/alshevskij/hass-snowfall`

В HACS выберите категорию **Integration**.

### Ручная установка

1. Скачайте репозиторий.
2. Скопируйте папку `custom_components/snowfall` в каталог `custom_components` Home Assistant.
3. Перезагрузите Home Assistant.

## Настройка и сущности

После добавления интеграции откройте **Настройки → Устройства и службы → Snowfall**. Управление доступно через следующие сущности:

| Сущность | Назначение |
|---|---|
| `switch.snowfall` | Включение и выключение снегопада |
| `select.snowfall_mode` | Режим: новогодний, круглогодичный или выбор месяцев |
| `switch.snowfall_january` … `switch.snowfall_december` | Выбор активных месяцев |
| `number.snowfall_flake_count` | Количество снежинок: 10–300 |
| `number.snowfall_speed` | Скорость: 25–200 |
| `number.snowfall_size` | Размер: 25–200 |
| `number.snowfall_opacity` | Прозрачность: 10–100 |
| `select.snowfall_fps` | Частота отрисовки: 30 или 60 FPS |
| `text.snowfall_excluded_paths` | Чёрный список страниц |
| `text.snowfall_included_paths` | Белый список страниц |

### Режимы работы

- **Новогодний** — снегопад работает с декабря по февраль.
- **Круглогодичный** — снегопад разрешён в любое время года.
- **Выбор месяцев** — снегопад работает только в те месяцы, переключатели которых включены.

Переключатели месяцев влияют на расписание только в режиме **Выбор месяцев**.

### Белый и чёрный списки страниц

Указывайте пути через точку с запятой, например:

`/lovelace/home; /lovelace/lights`

- Если белый список пуст, снегопад разрешён на всех страницах, кроме чёрного списка.
- Если белый список заполнен, снегопад разрешён только на совпадающих страницах.
- Если путь попал в оба списка, приоритет у чёрного списка — снегопад на этой странице не отображается.
- Сопоставление учитывает вложенные страницы: правило `/lovelace` подходит и для `/lovelace/room`.

Каждое текстовое поле Home Assistant ограничено 255 символами. Для длинных списков используйте короткие пути.

### Управление через автоматизации

Все сущности можно добавлять на панели, использовать в скриптах и автоматизациях. Например, включайте `switch.snowfall` по расписанию, меняйте режим по сезону или снижайте FPS на маломощных устройствах.

Документация: [Автоматизации Home Assistant](https://www.home-assistant.io/docs/automation/).

## Поддержка

Нашли ошибку или хотите предложить новую возможность?

[Создать Issue на GitHub](https://github.com/alshevskij/hass-snowfall/issues).

## Лицензия

Проект распространяется под лицензией, указанной в файле [LICENSE](LICENSE).
