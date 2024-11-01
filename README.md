# AI-SEO: Генератор SEO Описаний на базе GPT-2

**AI-SEO** — инструмент для генерации SEO-оптимизированных описаний продуктов с использованием модели GPT-2, реализованной вручную.

## Содержание

- [Демонстрация](#демонстрация)
- [Использование](#использование)
- [Структура проекта](#структура-проекта)

## Демонстрация

![AI-SEO Демонстрация](https://github.com/alexey0101/ai-seo/raw/main/demo.gif)


## Использование

1. **Запустите приложение**

   Запустите приложение Streamlit с помощью `Makefile`:

   ```bash
   make seo
   ```

2. **Генерация SEO Описаний**

   - Откройте веб-браузер и перейдите по адресу `http://localhost:8501`.
   - Введите **Название нового продукта** в поле ввода.
   - Нажмите кнопку **Generate Description**.
   - Просмотрите сгенерированное SEO-оптимизированное описание продукта.

3. **Остановить приложение**

   Чтобы остановить приложение Streamlit, используйте `Makefile`:

   ```bash
   make seo-stop
   ```

## Структура проекта

```
ai-seo/
├── app.py                # Основное приложение Streamlit
├── encoder.py            # Энкодер (взято из https://github.com/openai/gpt-2/blob/master/src/encoder.py)
├── gpt2.py               # Реализованная модель GPT-2
├── Makefile              # Команды для управления приложением
├── products.txt          # Примеры продуктов для генерации описаний
├── util.py               # Вспомогательные утилиты
└── README.md             # Документация проекта
```

**Примечание:** Файл `encoder.py` был заимствован из официального репозитория GPT-2 от OpenAI: [encoder.py](https://github.com/openai/gpt-2/blob/master/src/encoder.py).