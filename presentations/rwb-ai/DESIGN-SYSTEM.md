# RWB Design System

Шаблон презентации для Reveal.js с фирменным стилем Университета RWB.

---

## Идея дизайна

### Концепция
**"Мягкий градиент"** — элементы презентации визуально "перетекают" друг в друга через плавные цветовые переходы от светло-фиолетового к розовому. Это создает ощущение единства и профессионализма.

### Ключевые принципы

1. **Merged Blocks** — вместо отдельных карточек с промежутками используем единые блоки, разделенные только цветом
2. **Gradient Scale** — 5 уровней фиолетово-розовой градации автоматически применяются к колонкам
3. **Rounded Containers** — все блоки скруглены (20px), создавая мягкий современный вид
4. **Consistent Typography** — Montserrat для заголовков, Inter для текста

---

## Цветовая палитра

```css
/* Основные */
--rwb-dark: #1E1753      /* Глубокий фиолетовый — основной текст */
--rwb-primary: #6B42FB   /* Яркий фиолетовый — акценты, числа */
--rwb-primary-light: #EFD5FF  /* Светло-розовый — хедеры карточек */

/* Градация (от светлого к насыщенному) */
--level-1: #FCFAFF  /* Почти белый */
--level-2: #F9F1FF  /* Очень светлый */
--level-3: #F3E6FF  /* Светлый */
--level-4: #E5D0FF  /* Средний */
--level-5: #EFD5FF  /* Насыщенный розовый */

/* Дополнительные */
--rwb-blue: #C5E0F9  /* Голубой — для pills/тегов */
--rwb-white: #FFFFFF
--rwb-border: #E2E8F0
```

---

## Типы слайдов

### 1. Title Slide (`.slide-title`)
Полноэкранный фон с волнами, белый текст.

```html
<section class="slide-title" data-background-image="assets/bg-waves-1.jpg">
    <div class="header">
        <img src="assets/logo-white.png" alt="Logo">
        <span>Университет RWB</span>
    </div>
    <div class="content">
        <h1>Заголовок презентации</h1>
    </div>
</section>
```

**Фоны:**
- `bg-waves-1.jpg` — основной
- `bg-waves-2.jpg` — альтернатива
- `bg-waves-mirror.jpg` — зеркальный вариант

---

### 2. Standard Slide (`.slide-standard`)
Белый фон, хедер с лейблом и логотипом.

```html
<section class="slide-standard">
    <div class="slide-header">
        <span class="label">Название раздела</span>
        <img src="assets/logo-blue.png" alt="Logo" class="logo">
    </div>
    <div class="slide-body">
        <h2>Заголовок</h2>
        <!-- контент -->
    </div>
</section>
```

---

## Компоненты

### Merged Grid
Единый блок с автоматической градацией цветов.

```html
<div class="merged-grid cols-3">
    <div class="merged-item">
        <h3>Заголовок</h3>
        <p>Описание</p>
    </div>
    <div class="merged-item">...</div>
    <div class="merged-item">...</div>
</div>
```

**Варианты:** `cols-2`, `cols-3`, `cols-4`, `cols-5`

**С цветным хедером:**
```html
<div class="merged-item has-header">
    <div class="item-header">Заголовок карточки</div>
    <p>Описание</p>
</div>
```

**С большими числами:**
```html
<div class="merged-item">
    <div class="number">1</div>
    <p>Описание шага</p>
</div>
```

---

### Steps Split Layout
Разделение на белую левую и градиентную правую части.

```html
<div class="steps-split-layout">
    <div class="steps-left">
        <h2>Заголовок</h2>
    </div>
    <div class="steps-right">
        <div class="step-card level-1">
            <div class="step-number">1</div>
            <div class="step-text">Описание шага</div>
        </div>
        <div class="step-card level-2">...</div>
        <div class="step-card level-3">...</div>
    </div>
</div>
```

**Agenda вариант:**
```html
<div class="steps-split-layout agenda">
    <div class="steps-left accent">
        <h2>План встречи</h2>
    </div>
    <div class="steps-right white">
        <ul class="agenda-list">
            <li>Пункт 1</li>
            <li>Пункт 2</li>
        </ul>
    </div>
</div>
```

---

### Overlay Split
Левая карточка **накладывается** на правый фон. Левый край карточки прямой, правый — скруглённый.

```html
<div class="overlay-split">
    <!-- Фон справа -->
    <div class="bg-layer gradient-mesh"></div>
    <!-- Контент на фоне (опционально) -->
    <div class="bg-content">
        <p>Текст справа</p>
    </div>
    <!-- Карточка слева (накладывается) -->
    <div class="fg-card">
        <h2>Заголовок</h2>
        <div class="fg-card-footer">
            <p>Текст внизу карточки</p>
        </div>
    </div>
</div>
```

**Варианты фона** (`bg-layer`):
- `gradient-mesh` — градиентная сетка (bg-gradient-mesh.png)
- `gradient-purple` — CSS градиент фиолетовый → розовый
- `solid-purple` — сплошной розово-фиолетовый
- `solid-blue` — сплошной голубой

**Варианты карточки** (`fg-card`):
- (без класса) — белый фон
- `blue` — голубой фон
- `purple` — светло-фиолетовый фон

---

### Program Grid
Для программ с секциями "Основы" и "Масштабирование".

```html
<div class="program-grid">
    <div class="program-card">
        <div class="program-header">
            <h3>Название программы</h3>
        </div>
        <div class="program-section basics">
            <h4>Основы</h4>
            <p>Описание</p>
        </div>
        <div class="program-section advanced">
            <h4>Масштабирование</h4>
            <p>Описание</p>
        </div>
    </div>
</div>
```

---

### Pills
Теги/лейблы.

```html
<div class="pills">
    <span class="pill">Школа продактов</span>
    <span class="pill">ИИ буткемп</span>
</div>
```

---

### Divider
Разделитель внутри блоков.

```html
<p>Первый пункт</p>
<div class="divider"></div>
<p>Второй пункт</p>
```

---

### Text Block
Простой текстовый блок со светлым фоном.

```html
<div class="text-block">
    <h3>Заголовок</h3>
    <p>Текст...</p>
</div>
```

---

## Ассеты

| Файл | Описание |
|------|----------|
| `logo-white.png` | Белый логотип для темных фонов |
| `logo-blue.png` | Синий логотип для белых фонов |
| `bg-waves-1.jpg` | Основной волновой фон |
| `bg-waves-2.jpg` | Альтернативный волновой фон |
| `bg-waves-mirror.jpg` | Зеркальный волновой фон |
| `bg-gradient-mesh.png` | Градиентная сетка для split-gradient |

---

## Запуск

```bash
# Установка
npm install

# Запуск сервера
npx reveal-md index.html --port 8000

# Или просто открыть index.html в браузере
```

---

## Советы

1. **Используй `cols-*`** для автоматической градации цветов — не нужно вручную указывать фоны
2. **Для текста с разделителями** используй `<div class="divider"></div>` между параграфами
3. **Для шагов** используй `step-card level-1/2/3/4/5` — цвета применятся автоматически
4. **Избегай inline стилей** — всё должно быть в CSS для консистентности

