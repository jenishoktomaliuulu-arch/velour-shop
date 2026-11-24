import streamlit as st
from datetime import datetime

st.set_page_config(page_title="VELOUR — Косметика", page_icon="🌸", layout="wide")

if "cart" not in st.session_state:
    st.session_state.cart = {}
if "lang" not in st.session_state:
    st.session_state.lang = "RU"

# Словарь встроенного переводчика (RU / KZ / EN)
TEXTS = {
    "RU": {
        "subtitle": "Магазин косметики · Нажмите на раздел каталога, чтобы раскрыть товары",
        "add_btn": "В корзину",
        "info_btn": "Описание",
        "added_toast": "Добавлено в корзину:",
        "modal_title": "Подробная информация о товаре",
        "volume": "Граммовка / Объём",
        "origin": "Страна происхождения",
        "year": "Год выпуска",
        "shelf_life": "Срок годности",
        "ingredients": "Ключевые компоненты",
        "modal_add": "Добавить в корзину",
        "cart_title": "Корзина",
        "cart_empty": "Корзина пока пуста 🌸\nВыберите товары в каталоге.",
        "total": "Итого",
        "name_ph": "Ваше имя",
        "phone_ph": "Телефон / WhatsApp",
        "checkout": "Оформить заказ",
        "fill_err": "Заполните имя и телефон.",
        "order_ok": "Заказ принят! Мы скоро свяжемся с вами.",
        "pcs": "шт.",
    },
    "KZ": {
        "subtitle": "Косметика дүкені · Тауарларды көру үшін бөлімді басыңыз",
        "add_btn": "Себетке",
        "info_btn": "Сипаттама",
        "added_toast": "Себетке қосылды:",
        "modal_title": "Тауар туралы толық ақпарат",
        "volume": "Көлемі / Салмағы",
        "origin": "Шыққан елі",
        "year": "Шығарылған жылы",
        "shelf_life": "Жарамдылық мерзімі",
        "ingredients": "Негізгі құрамы",
        "modal_add": "Себетке қосу",
        "cart_title": "Себет",
        "cart_empty": "Себет әзірге бос 🌸\nКаталогтан тауар таңдаңыз.",
        "total": "Барлығы",
        "name_ph": "Сіздің атыңыз",
        "phone_ph": "Телефон / WhatsApp",
        "checkout": "Тапсырыс беру",
        "fill_err": "Атыңыз бен телефоныңызды жазыңыз.",
        "order_ok": "Тапсырыс қабылданды! Жақында хабарласамыз.",
        "pcs": "дана",
    },
    "EN": {
        "subtitle": "Cosmetics Boutique · Click any category to explore products",
        "add_btn": "Add to cart",
        "info_btn": "Details",
        "added_toast": "Added to cart:",
        "modal_title": "Product Details",
        "volume": "Volume / Weight",
        "origin": "Country of origin",
        "year": "Release year",
        "shelf_life": "Shelf life",
        "ingredients": "Key ingredients",
        "modal_add": "Add to cart",
        "cart_title": "Your Cart",
        "cart_empty": "Your cart is empty 🌸\nPick something from the catalog.",
        "total": "Total",
        "name_ph": "Your name",
        "phone_ph": "Phone / WhatsApp",
        "checkout": "Place order",
        "fill_err": "Please enter your name and phone.",
        "order_ok": "Order received! We will contact you shortly.",
        "pcs": "pcs",
    },
}

# CSS: полное перекрытие тёмной темы, лавовый фон и сакура в корзине
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;500;600;700&display=swap');

    /* 1. Базовая светло-розовая тема (перекрывает dark mode) */
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        background-color: #FFF0F5 !important;
        color: #2D161E !important;
        font-family: 'Manrope', sans-serif !important;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        background: transparent !important;
        position: relative;
        z-index: 1;
    }

    [data-testid="stHeader"] {
        background: rgba(255, 240, 245, 0.7) !important;
        backdrop-filter: blur(10px);
    }

    [data-testid="stHeader"] * {
        color: #4A1525 !important;
    }

    /* 2. Лавовый фон с плавающими кругами */
    .lava-bg {
        position: fixed;
        inset: 0;
        overflow: hidden;
        z-index: 0;
        pointer-events: none;
        background: linear-gradient(135deg, #FFF2F6 0%, #FFE4EC 100%);
    }

    .lava-blob {
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
        opacity: 0.6;
        will-change: transform;
    }

    .blob-1 {
        width: 440px; height: 440px;
        background: radial-gradient(circle, #FF5E7E 0%, #FF8FA3 70%);
        top: -80px; left: -60px;
        animation: float1 18s ease-in-out infinite alternate;
    }

    .blob-2 {
        width: 500px; height: 500px;
        background: radial-gradient(circle, #E63956 0%, #FF758F 70%);
        bottom: -120px; right: -80px;
        animation: float2 22s ease-in-out infinite alternate;
    }

    .blob-3 {
        width: 380px; height: 380px;
        background: radial-gradient(circle, #FF99B6 0%, #FF4D6D 75%);
        top: 35%; left: 40%;
        animation: float3 25s ease-in-out infinite alternate;
    }

    .blob-4 {
        width: 320px; height: 320px;
        background: radial-gradient(circle, #D90429 0%, #FF758F 75%);
        opacity: 0.32;
        bottom: 20%; left: 10%;
        animation: float4 20s ease-in-out infinite alternate;
    }

    @keyframes float1 {
        0% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(160px, 110px) scale(1.15); }
        100% { transform: translate(60px, 240px) scale(0.95); }
    }
    @keyframes float2 {
        0% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(-180px, -120px) scale(1.12); }
        100% { transform: translate(-70px, -220px) scale(0.9); }
    }
    @keyframes float3 {
        0% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(-150px, 90px) scale(1.2); }
        100% { transform: translate(140px, -100px) scale(0.92); }
    }
    @keyframes float4 {
        0% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(200px, -110px) scale(1.1); }
        100% { transform: translate(90px, 80px) scale(0.95); }
    }

    /* 3. Заголовки и текст */
    h1, h2, h3, h4, p, span, label {
        color: #2D161E !important;
    }

    .brand-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 54px;
        font-weight: 700;
        letter-spacing: 6px;
        color: #4A1525 !important;
        margin-bottom: 4px;
        line-height: 1.05;
    }

    .brand-sub {
        font-size: 15px;
        color: #7A4353 !important;
        margin-bottom: 18px;
    }

    /* 4. Фикс аккордеона в тёмном режиме */
    [data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.78) !important;
        backdrop-filter: blur(14px);
        border: 1px solid rgba(217, 79, 112, 0.28) !important;
        border-radius: 16px !important;
        margin-bottom: 14px !important;
        box-shadow: 0 8px 24px rgba(168, 46, 82, 0.06);
        overflow: hidden;
    }

    [data-testid="stExpander"] details,
    [data-testid="stExpander"] summary,
    [data-testid="stExpanderDetails"] {
        background-color: rgba(255, 255, 255, 0.65) !important;
        color: #2D161E !important;
    }

    [data-testid="stExpander"] summary {
        padding: 15px 20px !important;
        font-size: 18px !important;
    }

    [data-testid="stExpander"] summary svg {
        fill: #A4133C !important;
        color: #A4133C !important;
    }

    [data-testid="stExpander"] summary:hover {
        background-color: rgba(255, 227, 236, 0.65) !important;
    }

    /* 5. Ровные карточки товаров */
    .product-card-box {
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid rgba(217, 79, 112, 0.2);
        border-radius: 14px;
        overflow: hidden;
        margin-bottom: 10px;
        box-shadow: 0 6px 18px rgba(150, 35, 68, 0.07);
    }

    .product-card-img {
        width: 100%;
        height: 220px;
        object-fit: cover;
        display: block;
    }

    .product-card-body {
        padding: 14px 16px 12px 16px;
    }

    .product-badge {
        display: inline-block;
        background: #FFE3EC;
        color: #A4133C !important;
        font-size: 11px;
        font-weight: 600;
        padding: 3px 9px;
        border-radius: 999px;
        margin-bottom: 8px;
    }

    .product-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 23px;
        font-weight: 700;
        color: #2D161E !important;
        line-height: 1.15;
        height: 52px;
        overflow: hidden;
        margin-bottom: 6px;
    }

    .product-short {
        font-size: 13px;
        color: #6B4250 !important;
        line-height: 1.4;
        height: 40px;
        overflow: hidden;
        margin-bottom: 10px;
    }

    .product-price {
        font-size: 18px;
        font-weight: 700;
        color: #A4133C !important;
    }

    /* 6. Кнопки */
    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #C9184A, #E04F73) !important;
        border: none !important;
    }

    div.stButton > button[kind="primary"] * {
        color: #FFFFFF !important;
    }

    div.stButton > button[kind="secondary"] {
        background: rgba(255, 255, 255, 0.92) !important;
        border: 1px solid rgba(201, 24, 74, 0.35) !important;
    }

    div.stButton > button[kind="secondary"] * {
        color: #800F2F !important;
    }

    div.stButton > button[kind="secondary"]:hover {
        background: #FFE3EC !important;
        border-color: #C9184A !important;
    }

    /* 7. Фикс модального окна (Описание) в тёмном режиме */
    div[role="dialog"],
    div[role="dialog"] > div,
    [data-testid="stDialog"] div[role="dialog"] {
        background-color: #FFF6F9 !important;
        color: #2D161E !important;
        border: 1px solid rgba(201, 24, 74, 0.25) !important;
        border-radius: 18px !important;
    }

    div[role="dialog"] h1,
    div[role="dialog"] h2,
    div[role="dialog"] h3,
    div[role="dialog"] p,
    div[role="dialog"] span,
    div[role="dialog"] strong {
        color: #2D161E !important;
    }

    div[role="dialog"] button[aria-label="Close"] svg {
        fill: #4A1525 !important;
        color: #4A1525 !important;
    }

    /* 8. Кастомизация корзины + падающая сакура */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFF0F5 0%, #FFE0EA 100%) !important;
        border-right: 1px solid rgba(217, 79, 112, 0.25) !important;
        overflow: hidden !important;
    }

    [data-testid="stSidebarContent"] {
        position: relative;
        z-index: 2;
    }

    [data-testid="stSidebar"] input {
        background-color: rgba(255, 255, 255, 0.92) !important;
        color: #2D161E !important;
        border: 1px solid rgba(201, 24, 74, 0.3) !important;
        border-radius: 8px !important;
    }

    .cart-empty-box {
        background: rgba(255, 255, 255, 0.72);
        border: 1px dashed rgba(201, 24, 74, 0.35);
        border-radius: 14px;
        padding: 18px 14px;
        text-align: center;
        color: #6B3144 !important;
        font-size: 14px;
        line-height: 1.5;
        backdrop-filter: blur(6px);
    }

    .cart-item-card {
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(217, 79, 112, 0.2);
        border-radius: 12px;
        padding: 10px 12px;
        margin-bottom: 8px;
        backdrop-filter: blur(6px);
    }

    /* Падающие лепестки сакуры внутри корзины */
    .sakura-layer {
        position: fixed;
        top: 0;
        left: 0;
        width: 340px;
        height: 100vh;
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
    }

    .petal {
        position: absolute;
        top: -30px;
        width: 14px;
        height: 10px;
        background: linear-gradient(135deg, #FFD1DC 0%, #FF8FAB 100%);
        border-radius: 150% 0 150% 0;
        opacity: 0.75;
        box-shadow: 0 0 6px rgba(255, 143, 171, 0.4);
        animation: sakuraFall linear infinite;
    }

    .p1  { left: 8%;  width: 13px; height: 9px;  animation-duration: 11s; animation-delay: 0s; }
    .p2  { left: 22%; width: 16px; height: 11px; animation-duration: 14s; animation-delay: -3s; }
    .p3  { left: 38%; width: 11px; height: 8px;  animation-duration: 10s; animation-delay: -6s; }
    .p4  { left: 54%; width: 15px; height: 10px; animation-duration: 13s; animation-delay: -2s; }
    .p5  { left: 70%; width: 12px; height: 9px;  animation-duration: 15s; animation-delay: -8s; }
    .p6  { left: 84%; width: 14px; height: 10px; animation-duration: 12s; animation-delay: -4s; }
    .p7  { left: 15%; width: 10px; height: 7px;  animation-duration: 16s; animation-delay: -9s; }
    .p8  { left: 46%; width: 13px; height: 9px;  animation-duration: 11.5s; animation-delay: -5s; }
    .p9  { left: 63%; width: 15px; height: 11px; animation-duration: 14.5s; animation-delay: -1s; }
    .p10 { left: 90%; width: 11px; height: 8px;  animation-duration: 13.5s; animation-delay: -7s; }

    @keyframes sakuraFall {
        0% {
            transform: translateY(-20px) translateX(0px) rotate(0deg);
            opacity: 0;
        }
        10% { opacity: 0.8; }
        50% {
            transform: translateY(50vh) translateX(28px) rotate(180deg);
            opacity: 0.75;
        }
        90% { opacity: 0.7; }
        100% {
            transform: translateY(105vh) translateX(-18px) rotate(360deg);
            opacity: 0;
        }
    }
    </style>

    <div class="lava-bg">
        <div class="lava-blob blob-1"></div>
        <div class="lava-blob blob-2"></div>
        <div class="lava-blob blob-3"></div>
        <div class="lava-blob blob-4"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Каталог с переводами на 3 языка
CATALOG = [
    {
        "title": {"RU": "01 · Уход за лицом", "KZ": "01 · Бет күтімі", "EN": "01 · Skincare"},
        "subtitle": {
            "RU": "Сыворотки, кремы и сияние кожи",
            "KZ": "Сарысулар, кремдер және тері жарқылы",
            "EN": "Serums, creams and glowing skin",
        },
        "products": [
            {
                "id": "101",
                "name": {"RU": "Сыворотка Hydra Glow", "KZ": "Hydra Glow сарысуы", "EN": "Hydra Glow Serum"},
                "short": {
                    "RU": "Глубокое увлажнение и ровный тон кожи.",
                    "KZ": "Терең ылғалдандыру және тегіс реңк.",
                    "EN": "Deep hydration and even skin tone.",
                },
                "desc": {
                    "RU": "Концентрированная увлажняющая сыворотка мгновенно убирает сухость, стянутость и возвращает коже естественное сияние без липкости.",
                    "KZ": "Құрғақтық пен тартылуды лезде басатын, жабысқақтықсыз табиғи жарқыл сыйлайтын ылғалдандырғыш сарысу.",
                    "EN": "Concentrated hydrating serum that relieves dryness and restores natural glow without stickiness.",
                },
                "volume": "30 мл",
                "origin": {"RU": "Южная Корея", "KZ": "Оңтүстік Корея", "EN": "South Korea"},
                "year": "2026",
                "shelf_life": {"RU": "24 месяца", "KZ": "24 ай", "EN": "24 months"},
                "ingredients": {
                    "RU": "Гиалуроновая кислота 2%, ниацинамид 5%, пантенол, центелла",
                    "KZ": "Гиалурон қышқылы 2%, ниацинамид 5%, пантенол, центелла",
                    "EN": "Hyaluronic Acid 2%, Niacinamide 5%, Panthenol, Centella",
                },
                "price": 12500,
                "img": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=600&q=80",
            },
            {
                "id": "102",
                "name": {"RU": "Крем Velvet Barrier", "KZ": "Velvet Barrier кремі", "EN": "Velvet Barrier Cream"},
                "short": {
                    "RU": "Восстановление и мягкость с церамидами.",
                    "KZ": "Церамидтермен қалпына келтіру және жұмсақтық.",
                    "EN": "Barrier repair and softness with ceramides.",
                },
                "desc": {
                    "RU": "Нежный барьерный крем укрепляет защитный слой кожи, успокаивает раздражения и идеально подходит как база под макияж.",
                    "KZ": "Терінің қорғаныш қабатын нығайтып, тітіркенуді басатын жұмсақ крем. Макияж астына тамаша негіз.",
                    "EN": "Gentle barrier cream that strengthens skin protection, calms irritation, and works great under makeup.",
                },
                "volume": "50 мл",
                "origin": {"RU": "Франция", "KZ": "Франция", "EN": "France"},
                "year": "2026",
                "shelf_life": {"RU": "36 месяцев", "KZ": "36 ай", "EN": "36 months"},
                "ingredients": {
                    "RU": "Комплекс церамидов NP/AP, сквалан, масло ши, витамин E",
                    "KZ": "Церамидтер кешені NP/AP, сквалан, ши майы, E дәрумені",
                    "EN": "Ceramides NP/AP, Squalane, Shea Butter, Vitamin E",
                },
                "price": 14900,
                "img": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd?auto=format&fit=crop&w=600&q=80",
            },
            {
                "id": "103",
                "name": {"RU": "Тонер Rose Mist", "KZ": "Rose Mist тонері", "EN": "Rose Mist Toner"},
                "short": {
                    "RU": "Освежающий гидролат дамасской розы.",
                    "KZ": "Дамаск раушанының сергітетін гидролаты.",
                    "EN": "Refreshing Damask rose hydrosol.",
                },
                "desc": {
                    "RU": "Мягкий бесспиртовой тонер выравнивает pH после умывания, освежает кожу в течение дня и подготавливает её к нанесению крема.",
                    "KZ": "Спиртсіз жұмсақ тонер жуынғаннан кейін pH деңгейін теңестіріп, теріні сергітеді.",
                    "EN": "Alcohol-free gentle toner that balances pH after cleansing and refreshes skin throughout the day.",
                },
                "volume": "150 мл",
                "origin": {"RU": "Италия", "KZ": "Италия", "EN": "Italy"},
                "year": "2025",
                "shelf_life": {"RU": "24 месяца", "KZ": "24 ай", "EN": "24 months"},
                "ingredients": {
                    "RU": "Гидролат дамасской розы 85%, бетаин, глицерин, экстракт пиона",
                    "KZ": "Дамаск раушаны 85%, бетаин, глицерин, пион сығындысы",
                    "EN": "Damask Rose Water 85%, Betaine, Glycerin, Peony Extract",
                },
                "price": 8400,
                "img": "https://images.unsplash.com/photo-1608248597279-f99d160bfcbc?auto=format&fit=crop&w=600&q=80",
            },
        ],
    },
    {
        "title": {"RU": "02 · Макияж", "KZ": "02 · Макияж", "EN": "02 · Makeup"},
        "subtitle": {
            "RU": "Невесомые текстуры и акценты",
            "KZ": "Жеңіл текстуралар мен нәзік реңктер",
            "EN": "Weightless textures and accents",
        },
        "products": [
            {
                "id": "201",
                "name": {"RU": "Тинт для губ Silk Kiss", "KZ": "Silk Kiss ерін тинті", "EN": "Silk Kiss Lip Tint"},
                "short": {
                    "RU": "Бархатный финиш и стойкий оттенок.",
                    "KZ": "Барқыттай финиш және төзімді реңк.",
                    "EN": "Velvet finish and long-lasting tint.",
                },
                "desc": {
                    "RU": "Невесомый тинт с мягкой муссовой текстурой не сушит губы, держится до 8 часов и оставляет аккуратный естественный пигмент.",
                    "KZ": "Ерінді құрғатпайтын, 8 сағатқа дейін сақталатын жеңіл мусс-тинт.",
                    "EN": "Weightless mousse lip tint that lasts up to 8 hours without drying your lips.",
                },
                "volume": "6 г",
                "origin": {"RU": "Южная Корея", "KZ": "Оңтүстік Корея", "EN": "South Korea"},
                "year": "2026",
                "shelf_life": {"RU": "24 месяца", "KZ": "24 ай", "EN": "24 months"},
                "ingredients": {
                    "RU": "Масло жожоба, витамин E, гиалуроновые микросферы",
                    "KZ": "Жожоба майы, E дәрумені, гиалурон микросфералары",
                    "EN": "Jojoba Oil, Vitamin E, Hyaluronic Microspheres",
                },
                "price": 7900,
                "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=600&q=80",
            },
            {
                "id": "202",
                "name": {"RU": "Румяна Blush Cloud", "KZ": "Blush Cloud румянасы", "EN": "Blush Cloud Cheek"},
                "short": {
                    "RU": "Естественный румянец, тающая текстура.",
                    "KZ": "Табиғи қызғылт реңк, нәзік текстура.",
                    "EN": "Natural flush with a melting texture.",
                },
                "desc": {
                    "RU": "Кремовые румяна легко растушёвываются пальцами или спонжем, создавая свежий отдохнувший вид без пятен и резких границ.",
                    "KZ": "Саусақпен немесе спонжбен оңай жағылатын, бетке балғын өң беретін кремді румяна.",
                    "EN": "Cream blush that blends effortlessly with fingers or sponge for a fresh look.",
                },
                "volume": "10 г",
                "origin": {"RU": "Франция", "KZ": "Франция", "EN": "France"},
                "year": "2026",
                "shelf_life": {"RU": "30 месяцев", "KZ": "30 ай", "EN": "30 months"},
                "ingredients": {
                    "RU": "Сквалан, масло семян камелии, натуральные розовые пигменты",
                    "KZ": "Сквалан, камелия майы, табиғи қызғылт пигменттер",
                    "EN": "Squalane, Camellia Seed Oil, Natural Rose Pigments",
                },
                "price": 9500,
                "img": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?auto=format&fit=crop&w=600&q=80",
            },
            {
                "id": "203",
                "name": {"RU": "Хайлайтер Liquid Pearl", "KZ": "Liquid Pearl хайлайтері", "EN": "Liquid Pearl Highlighter"},
                "short": {
                    "RU": "Деликатное влажное сияние кожи.",
                    "KZ": "Теріге нәзік інжу жарқылын береді.",
                    "EN": "Delicate dewy pearl glow.",
                },
                "desc": {
                    "RU": "Жидкий хайлайтер со светоотражающими микрочастицами жемчуга даёт эффект здорового блеска без крупных блёсток.",
                    "KZ": "Ірі жылтырсыз, табиғи әрі сау жарқыл беретін сұйық інжу хайлайтері.",
                    "EN": "Liquid highlighter with fine pearl micro-particles for a natural healthy glow.",
                },
                "volume": "15 мл",
                "origin": {"RU": "Италия", "KZ": "Италия", "EN": "Italy"},
                "year": "2025",
                "shelf_life": {"RU": "24 месяца", "KZ": "24 ай", "EN": "24 months"},
                "ingredients": {
                    "RU": "Жемчужная мика, экстракт лотоса, витамин C, глицерин",
                    "KZ": "Інжу микасы, лотос сығындысы, C дәрумені, глицерин",
                    "EN": "Pearl Mica, Lotus Extract, Vitamin C, Glycerin",
                },
                "price": 11200,
                "img": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=600&q=80",
            },
        ],
    },
    {
        "title": {"RU": "03 · Парфюмерия", "KZ": "03 · Парфюмерия", "EN": "03 · Fragrance"},
        "subtitle": {
            "RU": "Нишевые и шлейфовые ароматы",
            "KZ": "Нишалық және ұзақ сақталатын иіссулар",
            "EN": "Niche and long-lasting scents",
        },
        "products": [
            {
                "id": "301",
                "name": {"RU": "Amber Noir EDP", "KZ": "Amber Noir EDP", "EN": "Amber Noir EDP"},
                "short": {
                    "RU": "Тёплая амбра, инжир и кашмирское дерево.",
                    "KZ": "Жылы амбра, інжір және кашмир ағашы.",
                    "EN": "Warm amber, black fig and cashmere wood.",
                },
                "desc": {
                    "RU": "Глубокий вечерний аромат с мягким бархатным шлейфом. Раскрывается спелым чёрным инжиром и оставляет тёплую древесно-амбровую базу.",
                    "KZ": "Жұмсақ шлейфі бар терең кешкі хош иіс. Қара інжір мен жылы амбра үйлесімі.",
                    "EN": "Deep evening fragrance with a velvety trail of ripe black fig and warm amber wood.",
                },
                "volume": "50 мл",
                "origin": {"RU": "Франция (Грасс)", "KZ": "Франция (Грасс)", "EN": "France (Grasse)"},
                "year": "2026",
                "shelf_life": {"RU": "60 месяцев", "KZ": "60 ай", "EN": "60 months"},
                "ingredients": {
                    "RU": "Верх: инжир, розовый перец; Сердце: амбра; База: кашмир",
                    "KZ": "Жоғарғы: інжір, бұрыш; Ортаңғы: амбра; Негізі: кашмир",
                    "EN": "Top: Fig, Pink Pepper; Heart: Amber; Base: Cashmere Wood",
                },
                "price": 34500,
                "img": "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80",
            },
            {
                "id": "302",
                "name": {"RU": "White Tea EDP", "KZ": "White Tea EDP", "EN": "White Tea EDP"},
                "short": {
                    "RU": "Свежий белый чай, бергамот и мускус.",
                    "KZ": "Ақ шай, бергамот және ақ мускус.",
                    "EN": "Fresh white tea, bergamot and musk.",
                },
                "desc": {
                    "RU": "Лёгкий повседневный парфюм с ощущением чистоты и утренней свежести. Ненавязчивый, но стойкий на коже и одежде.",
                    "KZ": "Таңғы тазалық пен балғындық сезімін сыйлайтын күнделікті жеңіл парфюм.",
                    "EN": "Light everyday perfume evoking crisp morning freshness with soft lasting power.",
                },
                "volume": "50 мл",
                "origin": {"RU": "Италия", "KZ": "Италия", "EN": "Italy"},
                "year": "2025",
                "shelf_life": {"RU": "60 месяцев", "KZ": "60 ай", "EN": "60 months"},
                "ingredients": {
                    "RU": "Верх: бергамот; Сердце: белый чай, жасмин; База: мускус",
                    "KZ": "Жоғарғы: бергамот; Ортаңғы: ақ шай; Негізі: ақ мускус",
                    "EN": "Top: Bergamot; Heart: White Tea, Jasmine; Base: White Musk",
                },
                "price": 29800,
                "img": "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=600&q=80",
            },
            {
                "id": "303",
                "name": {"RU": "Дымка Vanilla Silk", "KZ": "Vanilla Silk мисті", "EN": "Vanilla Silk Mist"},
                "short": {
                    "RU": "Мадагаскарская ваниль и нежный сандал.",
                    "KZ": "Мадагаскар ванилі және нәзік сандал.",
                    "EN": "Madagascar vanilla and soft sandalwood.",
                },
                "desc": {
                    "RU": "Парфюмированный мист для тела и волос с деликатной сладостью ванили и увлажняющими компонентами.",
                    "KZ": "Дене мен шашқа арналған нәзік ваниль хош иісті ылғалдандырғыш мист.",
                    "EN": "Perfumed body and hair mist with delicate vanilla sweetness and hydrating extracts.",
                },
                "volume": "100 мл",
                "origin": {"RU": "Франция", "KZ": "Франция", "EN": "France"},
                "year": "2026",
                "shelf_life": {"RU": "36 месяцев", "KZ": "36 ай", "EN": "36 months"},
                "ingredients": {
                    "RU": "Экстракт мадагаскарской ванили, сандаловое масло, пантенол",
                    "KZ": "Мадагаскар ванилі, сандал майы, пантенол",
                    "EN": "Madagascar Vanilla Extract, Sandalwood Oil, Panthenol",
                },
                "price": 13500,
                "img": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?auto=format&fit=crop&w=600&q=80",
            },
        ],
    },
]

lang = st.session_state.lang
t = TEXTS[lang]


def add_to_cart(product):
    pid = product["id"]
    if pid in st.session_state.cart:
        st.session_state.cart[pid]["qty"] += 1
    else:
        st.session_state.cart[pid] = {
            "name_dict": product["name"],
            "price": product["price"],
            "qty": 1,
        }


# Всплывающее окно с полной информацией
@st.dialog(t["modal_title"], width="large")
def show_product_details(product):
    col_img, col_info = st.columns([1, 1.35], gap="large")
    with col_img:
        st.markdown(
            f'<img src="{product["img"]}" style="width:100%; height:290px; object-fit:cover; border-radius:14px;">',
            unsafe_allow_html=True,
        )
    with col_info:
        st.markdown(f"### {product['name'][lang]}")
        st.markdown(
            f"<div style='font-size:22px; font-weight:700; color:#A4133C; margin-bottom:10px;'>{product['price']:,} ₸</div>".replace(",", " "),
            unsafe_allow_html=True,
        )
        st.write(product["desc"][lang])
        st.divider()
        st.markdown(f"**{t['volume']}:** {product['volume']}")
        st.markdown(f"**{t['origin']}:** {product['origin'][lang]}")
        st.markdown(f"**{t['year']}:** {product['year']}")
        st.markdown(f"**{t['shelf_life']}:** {product['shelf_life'][lang]}")
        st.markdown(f"**{t['ingredients']}:** {product['ingredients'][lang]}")
        st.write("")
        if st.button(t["modal_add"], key=f"modal_add_{product['id']}", type="primary", use_container_width=True):
            add_to_cart(product)
            st.toast(f"{t['added_toast']} {product['name'][lang]}")
            st.rerun()


# Шапка + встроенный переключатель языка
head_left, head_right = st.columns([4, 1.4])
with head_left:
    st.markdown('<div class="brand-title">VELOUR</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="brand-sub">{t["subtitle"]}</div>', unsafe_allow_html=True)
with head_right:
    st.write("")
    lang_cols = st.columns(3, gap="small")
    for idx_l, code in enumerate(["RU", "KZ", "EN"]):
        with lang_cols[idx_l]:
            btn_type = "primary" if lang == code else "secondary"
            if st.button(code, key=f"lang_{code}", type=btn_type, use_container_width=True):
                st.session_state.lang = code
                st.rerun()

# Вертикальный аккордеон каталога
for idx, category in enumerate(CATALOG):
    with st.expander(f"**{category['title'][lang]}**  —  {category['subtitle'][lang]}", expanded=(idx == 0)):
        cols = st.columns(3, gap="medium")
        for i, product in enumerate(category["products"]):
            with cols[i % 3]:
                price_str = f"{product['price']:,} ₸".replace(",", " ")
                st.markdown(
                    f"""
                    <div class="product-card-box">
                        <img class="product-card-img" src="{product['img']}" alt="{product['name'][lang]}">
                        <div class="product-card-body">
                            <span class="product-badge">{product['volume']} · {product['origin'][lang]}</span>
                            <div class="product-name">{product['name'][lang]}</div>
                            <div class="product-short">{product['short'][lang]}</div>
                            <div class="product-price">{price_str}</div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                b1, b2 = st.columns([1.1, 1], gap="small")
                with b1:
                    if st.button(t["add_btn"], key=f"add_{product['id']}", type="primary", use_container_width=True):
                        add_to_cart(product)
                        st.toast(f"{t['added_toast']} {product['name'][lang]}")
                with b2:
                    if st.button(t["info_btn"], key=f"info_{product['id']}", type="secondary", use_container_width=True):
                        show_product_details(product)

# Боковая панель — Корзина с падающими лепестками сакуры
with st.sidebar:
    st.markdown(
        """
        <div class="sakura-layer">
            <div class="petal p1"></div><div class="petal p2"></div>
            <div class="petal p3"></div><div class="petal p4"></div>
            <div class="petal p5"></div><div class="petal p6"></div>
            <div class="petal p7"></div><div class="petal p8"></div>
            <div class="petal p9"></div><div class="petal p10"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f"## 🌸 {t['cart_title']}")

    if not st.session_state.cart:
        st.markdown(
            f"<div class='cart-empty-box'>{t['cart_empty'].replace(chr(10), '<br>')}</div>",
            unsafe_allow_html=True,
        )
    else:
        total = 0
        to_delete = []
        for pid, item in st.session_state.cart.items():
            subtotal = item["price"] * item["qty"]
            total += subtotal
            item_name = item["name_dict"][lang]
            c1, c2 = st.columns([3.8, 1])
            with c1:
                st.markdown(
                    f"""
                    <div class="cart-item-card">
                        <b>{item_name}</b><br>
                        <span style="font-size:13px; color:#7A4353;">
                            {item['qty']} {t['pcs']} × {item['price']:,} ₸
                        </span>
                    </div>
                    """.replace(",", " "),
                    unsafe_allow_html=True,
                )
            with c2:
                st.write("")
                if st.button("✕", key=f"del_{pid}", type="secondary"):
                    to_delete.append(pid)

        for pid in to_delete:
            del st.session_state.cart[pid]
            st.rerun()

        st.divider()
        st.markdown(f"### {t['total']}: {total:,} ₸".replace(",", " "))

        with st.form("order_form"):
            name = st.text_input(t["name_ph"])
            phone = st.text_input(t["phone_ph"])
            submitted = st.form_submit_button(t["checkout"], type="primary", use_container_width=True)

            if submitted:
                if not name or not phone:
                    st.error(t["fill_err"])
                else:
                    print(f"\n[ЗАКАЗ {datetime.now().strftime('%H:%M:%S')}] {name} ({phone}) — {total} ₸")
                    st.session_state.cart = {}
                    st.success(t["order_ok"])