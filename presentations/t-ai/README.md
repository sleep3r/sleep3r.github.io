# ТАИ: Презентации

Автоматический каталог PDF-презентаций для занятий.

## Быстрый старт

1. Компилируй PDF в папку `pdf/`:
   ```bash
   cd latex
   quarto render "название.md" --to beamer --pdf-engine xelatex --output-dir "../pdf" --output "название.pdf"
   ```

2. Обнови манифест:
   ```bash
   cd ..
   ./generate-manifest.js
   ```

3. Пуш:
   ```bash
   git add .
   git commit -m "feat: добавлена презентация X"
   git push
   ```

Или всё в одну строку:
```bash
cd latex && quarto render "название.md" --to beamer --pdf-engine xelatex --output-dir "../pdf" && cd .. && ./generate-manifest.js && git add . && git commit -m "feat: название" && git push
```

## Структура

```
presentations/t-ai/
├── index.html              # Веб-каталог
├── logo.jpg               # Логотип
├── generate-manifest.js   # Скрипт генерации манифеста
├── latex/                 # Исходники презентаций
│   ├── *.md
│   └── xeheader.tex
└── pdf/                   # Скомпилированные PDF
    ├── manifest.json      # Автогенерируемый манифест
    └── *.pdf
```

## Автоматизация (опционально)

Чтобы не запускать `generate-manifest.js` вручную, добавь в конец команды quarto:

```bash
quarto render ... && node ../generate-manifest.js
```

Или создай Git hook в `.git/hooks/pre-commit`:

```bash
#!/bin/sh
cd presentations/t-ai && node generate-manifest.js && git add pdf/manifest.json
```
