import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(page_title="VELOUR — Косметика и Уход", page_icon="🌸", layout="wide")

if "cart" not in st.session_state:
    st.session_state.cart = {}
if "lang" not in st.session_state:
    st.session_state.lang = "RU"
if "promo_active" not in st.session_state:
    st.session_state.promo_active = False

# Встроенный переводчик (RU / KZ / EN)
TEXTS = {
    "RU": {
        "subtitle": "Бутик косметики и аппаратного ухода · Оригинальная продукция",
        "hero_tag": "ХИТ СЕЗОНА · НОВИНКА",
        "hero_title": "Профессиональный уход и чистка лица у вас дома",
        "hero_desc": "Оригинальная косметика из Кореи и Франции, аппараты для ультразвуковой чистки и подбор ухода от наших дипломированных косметологов.",
        "hero_promo": "Промокод на скидку 10% в корзине: VELOUR10",
        "catalog_title": "Каталог продукции",
        "add_btn": "В корзину",
        "info_btn": "Описание",
        "added_toast": "Добавлено в корзину:",
        "modal_title": "Подробная информация о товаре",
        "volume": "Граммовка / Характеристики",
        "origin": "Страна происхождения",
        "year": "Год выпуска",
        "shelf_life": "Срок годности / Гарантия",
        "ingredients": "Состав / Комплектация",
        "modal_add": "Добавить в корзину",
        "team_title": "Наши специалисты",
        "team_sub": "Поможем подобрать идеальный уход под ваш тип кожи",
        "lead_badge": "★ Главный специалист",
        "colleague_badge": "Специалист",
        "cert_btn": "Сертификат и образование",
        "cert_modal": "Диплом и сертификация специалиста",
        "addr_title": "Адрес и местоположение",
        "addr_text": "пр. Б. Саттарханова, 5",
        "addr_hours": "Ежедневно с 10:00 до 21:00",
        "addr_phone": "+7 (700) 555-35-35",
        "faq_title": "Популярные вопросы",
        "cart_title": "Корзина",
        "cart_empty": "Корзина пока пуста 🌸\nВыберите товары в каталоге.",
        "promo_ph": "Промокод (VELOUR10)",
        "promo_btn": "Применить",
        "promo_ok": "Скидка 10% активирована!",
        "promo_err": "Неверный промокод.",
        "discount": "Скидка (10%)",
        "total": "Итого",
        "name_ph": "Ваше имя",
        "phone_ph": "Телефон / WhatsApp",
        "checkout": "Оформить заказ",
        "fill_err": "Заполните имя и телефон.",
        "order_ok": "Заказ принят! Мы скоро свяжемся с вами.",
        "pcs": "шт.",
    },
    "KZ": {
        "subtitle": "Косметика және аппараттық күтім бутигі · Түпнұсқа өнімдер",
        "hero_tag": "МАУСЫМ ХИТІ · ЖАҢА ӨНІМ",
        "hero_title": "Үй жағдайындағы кәсіби күтім және бет тазалау",
        "hero_desc": "Корея мен Францияның түпнұсқа косметикасы, ультрадыбыстық тазалау аппараттары және дипломды косметологтардың кеңесі.",
        "hero_promo": "Себетте 10% жеңілдік промокоды: VELOUR10",
        "catalog_title": "Өнімдер каталогы",
        "add_btn": "Себетке",
        "info_btn": "Сипаттама",
        "added_toast": "Себетке қосылды:",
        "modal_title": "Тауар туралы толық ақпарат",
        "volume": "Көлемі / Сипаттамасы",
        "origin": "Шыққан елі",
        "year": "Шығарылған жылы",
        "shelf_life": "Жарамдылық мерзімі / Кепілдік",
        "ingredients": "Құрамы / Жинақталуы",
        "modal_add": "Себетке қосу",
        "team_title": "Біздің мамандар",
        "team_sub": "Теріңіздің түріне сай мінсіз күтім таңдауға көмектесеміз",
        "lead_badge": "★ Бас маман",
        "colleague_badge": "Маман",
        "cert_btn": "Сертификат және білімі",
        "cert_modal": "Маманның дипломы мен сертификаттары",
        "addr_title": "Мекенжай және орналасуы",
        "addr_text": "Б. Саттарханов даңғылы, 5",
        "addr_hours": "Күн сайын 10:00-ден 21:00-ге дейін",
        "addr_phone": "+7 (700) 555-35-35",
        "faq_title": "Жиі қойылатын сұрақтар",
        "cart_title": "Себет",
        "cart_empty": "Себет әзірге бос 🌸\nКаталогтан тауар таңдаңыз.",
        "promo_ph": "Промокод (VELOUR10)",
        "promo_btn": "Қолдану",
        "promo_ok": "10% жеңілдік іске қосылды!",
        "promo_err": "Промокод қате.",
        "discount": "Жеңілдік (10%)",
        "total": "Барлығы",
        "name_ph": "Сіздің атыңыз",
        "phone_ph": "Телефон / WhatsApp",
        "checkout": "Тапсырыс беру",
        "fill_err": "Атыңыз бен телефоныңызды жазыңыз.",
        "order_ok": "Тапсырыс қабылданды! Жақында хабарласамыз.",
        "pcs": "дана",
    },
    "EN": {
        "subtitle": "Cosmetics & Beauty Devices Boutique · 100% Original",
        "hero_tag": "BESTSELLER · NEW ARRIVAL",
        "hero_title": "Professional Skincare & Facial Cleansing at Home",
        "hero_desc": "Authentic Korean & French cosmetics, ultrasonic cleansing devices, and personal care guidance from our certified cosmetologists.",
        "hero_promo": "Use promo code in cart for 10% OFF: VELOUR10",
        "catalog_title": "Product Catalog",
        "add_btn": "Add to cart",
        "info_btn": "Details",
        "added_toast": "Added to cart:",
        "modal_title": "Product Details",
        "volume": "Volume / Specs",
        "origin": "Country of origin",
        "year": "Release year",
        "shelf_life": "Shelf life / Warranty",
        "ingredients": "Ingredients / In the box",
        "modal_add": "Add to cart",
        "team_title": "Our Specialists",
        "team_sub": "We help you choose the ideal routine for your skin type",
        "lead_badge": "★ Lead Specialist",
        "colleague_badge": "Specialist",
        "cert_btn": "Certificate & Education",
        "cert_modal": "Specialist Diploma & Certification",
        "addr_title": "Address & Location",
        "addr_text": "5 B. Sattarkhanov Ave",
        "addr_hours": "Daily from 10:00 to 21:00",
        "addr_phone": "+7 (700) 555-35-35",
        "faq_title": "Frequently Asked Questions",
        "cart_title": "Your Cart",
        "cart_empty": "Your cart is empty 🌸\nPick something from the catalog.",
        "promo_ph": "Promo code (VELOUR10)",
        "promo_btn": "Apply",
        "promo_ok": "10% discount applied!",
        "promo_err": "Invalid promo code.",
        "discount": "Discount (10%)",
        "total": "Total",
        "name_ph": "Your name",
        "phone_ph": "Phone / WhatsApp",
        "checkout": "Place order",
        "fill_err": "Please enter your name and phone.",
        "order_ok": "Order received! We will contact you shortly.",
        "pcs": "pcs",
    },
}

# CSS: розовый дизайн, лавовый фон, сакура в корзине, карточки и фикс тёмной темы
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;500;600;700&display=swap');

    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #FFF0F5 !important;
        color: #2D161E !important;
        font-family: 'Manrope', sans-serif !important;
    }

    [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background: transparent !important;
        position: relative;
        z-index: 1;
    }

    [data-testid="stHeader"] {
        background: rgba(255, 240, 245, 0.7) !important;
        backdrop-filter: blur(10px);
    }
    [data-testid="stHeader"] * { color: #4A1525 !important; }

    /* Лавовый фон */
    .lava-bg {
        position: fixed; inset: 0; overflow: hidden; z-index: 0; pointer-events: none;
        background: linear-gradient(135deg, #FFF2F6 0%, #FFE4EC 100%);
    }
    .lava-blob {
        position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.6; will-change: transform;
    }
    .blob-1 { width: 440px; height: 440px; background: radial-gradient(circle, #FF5E7E 0%, #FF8FA3 70%); top: -80px; left: -60px; animation: float1 18s ease-in-out infinite alternate; }
    .blob-2 { width: 500px; height: 500px; background: radial-gradient(circle, #E63956 0%, #FF758F 70%); bottom: -120px; right: -80px; animation: float2 22s ease-in-out infinite alternate; }
    .blob-3 { width: 380px; height: 380px; background: radial-gradient(circle, #FF99B6 0%, #FF4D6D 75%); top: 35%; left: 40%; animation: float3 25s ease-in-out infinite alternate; }
    .blob-4 { width: 320px; height: 320px; background: radial-gradient(circle, #D90429 0%, #FF758F 75%); opacity: 0.32; bottom: 20%; left: 10%; animation: float4 20s ease-in-out infinite alternate; }

    @keyframes float1 { 0% { transform: translate(0,0) scale(1); } 50% { transform: translate(160px,110px) scale(1.15); } 100% { transform: translate(60px,240px) scale(0.95); } }
    @keyframes float2 { 0% { transform: translate(0,0) scale(1); } 50% { transform: translate(-180px,-120px) scale(1.12); } 100% { transform: translate(-70px,-220px) scale(0.9); } }
    @keyframes float3 { 0% { transform: translate(0,0) scale(1); } 50% { transform: translate(-150px,90px) scale(1.2); } 100% { transform: translate(140px,-100px) scale(0.92); } }
    @keyframes float4 { 0% { transform: translate(0,0) scale(1); } 50% { transform: translate(200px,-110px) scale(1.1); } 100% { transform: translate(90px,80px) scale(0.95); } }

    h1, h2, h3, h4, p, span, label { color: #2D161E !important; }

    .brand-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 54px; font-weight: 700; letter-spacing: 6px;
        color: #4A1525 !important; margin-bottom: 2px; line-height: 1.05;
    }
    .brand-sub { font-size: 15px; color: #7A4353 !important; margin-bottom: 18px; }

    .section-heading {
        font-family: 'Cormorant Garamond', serif;
        font-size: 36px; font-weight: 700; color: #4A1525 !important;
        margin-top: 28px; margin-bottom: 6px;
    }
    .section-sub { font-size: 14px; color: #7A4353 !important; margin-bottom: 18px; }

    /* Hero-баннер (импровизация в стиле современных бьюти-сайтов) */
    .hero-banner {
        background: rgba(255, 255, 255, 0.76);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(201, 24, 74, 0.22);
        border-radius: 22px;
        padding: 28px 32px;
        margin-bottom: 24px;
        box-shadow: 0 12px 30px rgba(168, 46, 82, 0.08);
    }
    .hero-tag {
        display: inline-block;
        background: linear-gradient(135deg, #C9184A, #FF5E7E);
        color: #FFFFFF !important;
        font-size: 11px; font-weight: 700; letter-spacing: 1.2px;
        padding: 5px 12px; border-radius: 999px; margin-bottom: 12px;
    }
    .hero-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 38px; font-weight: 700; color: #3D1220 !important;
        line-height: 1.12; margin-bottom: 10px;
    }
    .hero-desc { font-size: 15px; color: #6B3C4B !important; line-height: 1.5; margin-bottom: 14px; max-width: 720px; }
    .hero-promo {
        display: inline-block; background: #FFE3EC; border: 1px dashed #C9184A;
        color: #9E1038 !important; font-size: 13px; font-weight: 600;
        padding: 6px 14px; border-radius: 10px;
    }

    /* Аккордеон (каталог и FAQ) */
    [data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.8) !important;
        backdrop-filter: blur(14px);
        border: 1px solid rgba(217, 79, 112, 0.25) !important;
        border-radius: 16px !important;
        margin-bottom: 12px !important;
        box-shadow: 0 8px 24px rgba(168, 46, 82, 0.06);
        overflow: hidden;
    }
    [data-testid="stExpander"] details,
    [data-testid="stExpander"] summary,
    [data-testid="stExpanderDetails"] {
        background-color: rgba(255, 255, 255, 0.65) !important;
        color: #2D161E !important;
    }
    [data-testid="stExpander"] summary { padding: 15px 20px !important; font-size: 17px !important; }
    [data-testid="stExpander"] summary svg { fill: #A4133C !important; color: #A4133C !important; }
    [data-testid="stExpander"] summary:hover { background-color: rgba(255, 227, 236, 0.65) !important; }

    /* Карточки товаров */
    .product-card-box {
        background: rgba(255, 255, 255, 0.94);
        border: 1px solid rgba(217, 79, 112, 0.2);
        border-radius: 16px; overflow: hidden; margin-bottom: 10px;
        box-shadow: 0 6px 18px rgba(150, 35, 68, 0.07);
        transition: transform 0.2s ease;
    }
    .product-card-box:hover { transform: translateY(-3px); }
    .product-card-img { width: 100%; height: 220px; object-fit: cover; display: block; }
    .product-card-body { padding: 14px 16px 12px 16px; }
    .product-badge {
        display: inline-block; background: #FFE3EC; color: #A4133C !important;
        font-size: 11px; font-weight: 600; padding: 3px 9px; border-radius: 999px; margin-bottom: 8px;
    }
    .product-name {
        font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 700;
        color: #2D161E !important; line-height: 1.15; height: 50px; overflow: hidden; margin-bottom: 6px;
    }
    .product-short {
        font-size: 13px; color: #6B4250 !important; line-height: 1.4; height: 38px; overflow: hidden; margin-bottom: 10px;
    }
    .product-price { font-size: 18px; font-weight: 700; color: #A4133C !important; }

    /* Карточки специалистов */
    .spec-card {
        background: rgba(255, 255, 255, 0.88);
        border: 1px solid rgba(217, 79, 112, 0.22);
        border-radius: 18px; overflow: hidden; margin-bottom: 10px;
        box-shadow: 0 8px 22px rgba(150, 35, 68, 0.08);
    }
    .spec-card-lead {
        border: 2px solid #C9184A !important;
        box-shadow: 0 10px 28px rgba(201, 24, 74, 0.16);
    }
    .spec-img { width: 100%; height: 260px; object-fit: cover; object-position: top; display: block; }
    .spec-body { padding: 16px; }
    .spec-badge-lead {
        display: inline-block; background: linear-gradient(135deg, #C9184A, #E04F73);
        color: #FFFFFF !important; font-size: 11px; font-weight: 700;
        padding: 4px 10px; border-radius: 999px; margin-bottom: 8px;
    }
    .spec-badge {
        display: inline-block; background: #FFE3EC; color: #A4133C !important;
        font-size: 11px; font-weight: 600; padding: 4px 10px; border-radius: 999px; margin-bottom: 8px;
    }
    .spec-name { font-family: 'Cormorant Garamond', serif; font-size: 24px; font-weight: 700; color: #2D161E !important; margin-bottom: 4px; }
    .spec-role { font-size: 13px; font-weight: 600; color: #A4133C !important; margin-bottom: 8px; }
    .spec-bio { font-size: 13px; color: #6B4250 !important; line-height: 1.45; min-height: 60px; }

    /* Блок адреса */
    .address-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(217, 79, 112, 0.25);
        border-radius: 18px; padding: 24px; height: 100%;
        box-shadow: 0 8px 24px rgba(150, 35, 68, 0.07);
    }

    /* Кнопки */
    div.stButton > button { border-radius: 10px !important; font-weight: 600 !important; transition: all 0.2s ease !important; }
    div.stButton > button[kind="primary"] { background: linear-gradient(135deg, #C9184A, #E04F73) !important; border: none !important; }
    div.stButton > button[kind="primary"] * { color: #FFFFFF !important; }
    div.stButton > button[kind="secondary"] { background: rgba(255, 255, 255, 0.92) !important; border: 1px solid rgba(201, 24, 74, 0.35) !important; }
    div.stButton > button[kind="secondary"] * { color: #800F2F !important; }
    div.stButton > button[kind="secondary"]:hover { background: #FFE3EC !important; border-color: #C9184A !important; }

    /* Модальные окна (фикс тёмной темы) */
    div[role="dialog"], div[role="dialog"] > div, [data-testid="stDialog"] div[role="dialog"] {
        background-color: #FFF6F9 !important; color: #2D161E !important;
        border: 1px solid rgba(201, 24, 74, 0.25) !important; border-radius: 18px !important;
    }
    div[role="dialog"] h1, div[role="dialog"] h2, div[role="dialog"] h3, div[role="dialog"] p, div[role="dialog"] span, div[role="dialog"] strong {
        color: #2D161E !important;
    }
    div[role="dialog"] button[aria-label="Close"] svg { fill: #4A1525 !important; color: #4A1525 !important; }

    /* Корзина и падающая сакура */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFF0F5 0%, #FFE0EA 100%) !important;
        border-right: 1px solid rgba(217, 79, 112, 0.25) !important;
        overflow: hidden !important;
    }
    [data-testid="stSidebarContent"] { position: relative; z-index: 2; }
    [data-testid="stSidebar"] input {
        background-color: rgba(255, 255, 255, 0.92) !important;
        color: #2D161E !important;
        border: 1px solid rgba(201, 24, 74, 0.3) !important;
        border-radius: 8px !important;
    }
    .cart-empty-box {
        background: rgba(255, 255, 255, 0.72); border: 1px dashed rgba(201, 24, 74, 0.35);
        border-radius: 14px; padding: 18px 14px; text-align: center;
        color: #6B3144 !important; font-size: 14px; line-height: 1.5; backdrop-filter: blur(6px);
    }
    .cart-item-card {
        background: rgba(255, 255, 255, 0.85); border: 1px solid rgba(217, 79, 112, 0.2);
        border-radius: 12px; padding: 10px 12px; margin-bottom: 8px; backdrop-filter: blur(6px);
    }
    .sakura-layer {
        position: fixed; top: 0; left: 0; width: 340px; height: 100vh;
        pointer-events: none; overflow: hidden; z-index: 0;
    }
    .petal {
        position: absolute; top: -30px; width: 14px; height: 10px;
        background: linear-gradient(135deg, #FFD1DC 0%, #FF8FAB 100%);
        border-radius: 150% 0 150% 0; opacity: 0.75;
        box-shadow: 0 0 6px rgba(255, 143, 171, 0.4);
        animation: sakuraFall linear infinite;
    }
    .p1 { left: 8%;  width: 13px; height: 9px;  animation-duration: 11s; animation-delay: 0s; }
    .p2 { left: 22%; width: 16px; height: 11px; animation-duration: 14s; animation-delay: -3s; }
    .p3 { left: 38%; width: 11px; height: 8px;  animation-duration: 10s; animation-delay: -6s; }
    .p4 { left: 54%; width: 15px; height: 10px; animation-duration: 13s; animation-delay: -2s; }
    .p5 { left: 70%; width: 12px; height: 9px;  animation-duration: 15s; animation-delay: -8s; }
    .p6 { left: 84%; width: 14px; height: 10px; animation-duration: 12s; animation-delay: -4s; }
    .p7 { left: 15%; width: 10px; height: 7px;  animation-duration: 16s; animation-delay: -9s; }
    .p8 { left: 46%; width: 13px; height: 9px;  animation-duration: 11.5s; animation-delay: -5s; }
    .p9 { left: 63%; width: 15px; height: 11px; animation-duration: 14.5s; animation-delay: -1s; }
    .p10{ left: 90%; width: 11px; height: 8px;  animation-duration: 13.5s; animation-delay: -7s; }

    @keyframes sakuraFall {
        0% { transform: translateY(-20px) translateX(0px) rotate(0deg); opacity: 0; }
        10% { opacity: 0.8; }
        50% { transform: translateY(50vh) translateX(28px) rotate(180deg); opacity: 0.75; }
        90% { opacity: 0.7; }
        100% { transform: translateY(105vh) translateX(-18px) rotate(360deg); opacity: 0; }
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

# Каталог товаров (добавлены аппараты для чистки лица!)
CATALOG = [
    {
        "title": {"RU": "01 · Аппараты для чистки лица", "KZ": "01 · Бет тазалау аппараттары", "EN": "01 · Facial Cleansing Devices"},
        "subtitle": {
            "RU": "Ультразвуковой пилинг, вакуум и лифтинг дома",
            "KZ": "Ультрадыбыстық пилинг, вакуум және үйдегі лифтинг",
            "EN": "Ultrasonic peeling, pore vacuum and home lifting",
        },
        "products": [
            {
                "id": "001",
                "name": {"RU": "УЗ-скрабер Velour Sonic Pro", "KZ": "Velour Sonic Pro УД-скрабері", "EN": "Velour Sonic Pro Scrubber"},
                "short": {"RU": "Глубокая ультразвуковая чистка пор (28 кГц).", "KZ": "Тері тесіктерін ультрадыбыспен терең тазалау.", "EN": "Deep ultrasonic pore cleansing (28 kHz)."},
                "desc": {
                    "RU": "Профессиональный аппарат для ультразвуковой чистки лица. Мягко удаляет чёрные точки, ороговевшие клетки и усиливает впитывание сывороток в 3 раза.",
                    "KZ": "Бетті ультрадыбыспен тазалауға арналған кәсіби аппарат. Қара нүктелерді кетіріп, сарысулардың сіңуін 3 есе арттырады.",
                    "EN": "Professional ultrasonic facial scrubber. Gently removes blackheads, dead skin cells, and boosts serum absorption 3x.",
                },
                "volume": "4 режима · 95 г",
                "origin": {"RU": "Южная Корея", "KZ": "Оңтүстік Корея", "EN": "South Korea"},
                "year": "2026",
                "shelf_life": {"RU": "Гарантия 12 мес.", "KZ": "Кепілдік 12 ай", "EN": "12-month warranty"},
                "ingredients": {"RU": "Аппарат, силиконовый чехол, кабель USB-C, инструкция", "KZ": "Аппарат, силикон қап, USB-C кабелі, нұсқаулық", "EN": "Device, silicone cover, USB-C cable, manual"},
                "price": 24900,
                "img": "https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?auto=format&fit=crop&w=600&q=80",
            },
            {
                "id": "002",
                "name": {"RU": "Вакуумный очиститель Pore Vacuum", "KZ": "Pore Vacuum вакуумдық тазартқышы", "EN": "Pore Vacuum Cleanser"},
                "short": {"RU": "Бережное очищение Т-зоны без покраснений.", "KZ": "Т-аймақты қызарусыз ұқыпты тазалау.", "EN": "Gentle T-zone cleansing without redness."},
                "desc": {
                    "RU": "Вакуумный аппарат с 4 сменными насадками и 3 уровнями мощности. Эффективно очищает забитые поры и выравнивает микрорельеф кожи.",
                    "KZ": "4 ауыстырмалы саптамасы және 3 қуат деңгейі бар вакуумдық аппарат. Бітелген тесіктерді тиімді тазартады.",
                    "EN": "Vacuum cleanser with 4 interchangeable heads and 3 suction levels. Effectively clears clogged pores.",
                },
                "volume": "4 насадки · 120 г",
                "origin": {"RU": "Южная Корея", "KZ": "Оңтүстік Корея", "EN": "South Korea"},
                "year": "2026",
                "shelf_life": {"RU": "Гарантия 12 мес.", "KZ": "Кепілдік 12 ай", "EN": "12-month warranty"},
                "ingredients": {"RU": "Аппарат, 4 насадки, сменные фильтры, кабель USB-C", "KZ": "Аппарат, 4 саптама, сүзгілер, USB-C кабелі", "EN": "Device, 4 heads, spare filters, USB-C cable"},
                "price": 19500,
                "img": "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=600&q=80",
            },
            {
                "id": "003",
                "name": {"RU": "LED-массажёр Glow Lift 3-в-1", "KZ": "Glow Lift 3-в-1 LED-массажері", "EN": "Glow Lift 3-in-1 LED Device"},
                "short": {"RU": "Микротоки + светотерапия для упругости кожи.", "KZ": "Тері серпімділігіне арналған микроток + LED.", "EN": "Microcurrents + LED therapy for firm skin."},
                "desc": {
                    "RU": "Аппарат для домашнего лифтинга: снимает утренние отёки, подтягивает овал лица и борется с тусклым цветом кожи за 5 минут в день.",
                    "KZ": "Үйдегі лифтинг аппараты: таңғы ісінуді басады, бет пішінін тартады және күніне 5 минутта теріге жарқыл береді.",
                    "EN": "Home lifting device: reduces morning puffiness, contours facial lines, and brightens dull skin in 5 minutes a day.",
                },
                "volume": "3 LED-спектра · 110 г",
                "origin": {"RU": "Япония", "KZ": "Жапония", "EN": "Japan"},
                "year": "2026",
                "shelf_life": {"RU": "Гарантия 24 мес.", "KZ": "Кепілдік 24 ай", "EN": "24-month warranty"},
                "ingredients": {"RU": "LED-массажёр, зарядная станция, мешочек, инструкция", "KZ": "LED-массажер, қуаттау станциясы, қапшық", "EN": "LED device, charging dock, travel pouch, manual"},
                "price": 32900,
                "img": "https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?auto=format&fit=crop&w=600&q=80",
            },
        ],
    },
    {
        "title": {"RU": "02 · Уход за лицом", "KZ": "02 · Бет күтімі", "EN": "02 · Skincare"},
        "subtitle": {"RU": "Сыворотки, кремы и сияние кожи", "KZ": "Сарысулар, кремдер және тері жарқылы", "EN": "Serums, creams and glowing skin"},
        "products": [
            {
                "id": "101",
                "name": {"RU": "Сыворотка Hydra Glow", "KZ": "Hydra Glow сарысуы", "EN": "Hydra Glow Serum"},
                "short": {"RU": "Глубокое увлажнение и ровный тон кожи.", "KZ": "Терең ылғалдандыру және тегіс реңк.", "EN": "Deep hydration and even skin tone."},
                "desc": {
                    "RU": "Концентрированная увлажняющая сыворотка мгновенно убирает сухость, стянутость и возвращает коже естественное сияние без липкости.",
                    "KZ": "Құрғақтық пен тартылуды лезде басатын, жабысқақтықсыз табиғи жарқыл сыйлайтын сарысу.",
                    "EN": "Concentrated hydrating serum that relieves dryness and restores natural glow without stickiness.",
                },
                "volume": "30 мл",
                "origin": {"RU": "Южная Корея", "KZ": "Оңтүстік Корея", "EN": "South Korea"},
                "year": "2026",
                "shelf_life": {"RU": "24 месяца", "KZ": "24 ай", "EN": "24 months"},
                "ingredients": {"RU": "Гиалуроновая кислота 2%, ниацинамид 5%, пантенол, центелла", "KZ": "Гиалурон қышқылы 2%, ниацинамид 5%, пантенол", "EN": "Hyaluronic Acid 2%, Niacinamide 5%, Panthenol"},
                "price": 12500,
                "img": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=600&q=80",
            },
            {
                "id": "102",
                "name": {"RU": "Крем Velvet Barrier", "KZ": "Velvet Barrier кремі", "EN": "Velvet Barrier Cream"},
                "short": {"RU": "Восстановление и мягкость с церамидами.", "KZ": "Церамидтермен қалпына келтіру және жұмсақтық.", "EN": "Barrier repair and softness with ceramides."},
                "desc": {
                    "RU": "Нежный барьерный крем укрепляет защитный слой кожи, успокаивает раздражения и идеально подходит как база под макияж.",
                    "KZ": "Терінің қорғаныш қабатын нығайтып, тітіркенуді басатын жұмсақ крем.",
                    "EN": "Gentle barrier cream that strengthens skin protection and calms irritation.",
                },
                "volume": "50 мл",
                "origin": {"RU": "Франция", "KZ": "Франция", "EN": "France"},
                "year": "2026",
                "shelf_life": {"RU": "36 месяцев", "KZ": "36 ай", "EN": "36 months"},
                "ingredients": {"RU": "Церамиды NP/AP, сквалан, масло ши, витамин E", "KZ": "Церамидтер NP/AP, сквалан, ши майы", "EN": "Ceramides NP/AP, Squalane, Shea Butter"},
                "price": 14900,
                "img": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd?auto=format&fit=crop&w=600&q=80",
            },
            {
                "id": "103",
                "name": {"RU": "Тонер Rose Mist", "KZ": "Rose Mist тонері", "EN": "Rose Mist Toner"},
                "short": {"RU": "Освежающий гидролат дамасской розы.", "KZ": "Дамаск раушанының сергітетін гидролаты.", "EN": "Refreshing Damask rose hydrosol."},
                "desc": {
                    "RU": "Мягкий бесспиртовой тонер выравнивает pH после умывания, освежает кожу в течение дня и подготавливает её к нанесению крема.",
                    "KZ": "Спиртсіз жұмсақ тонер жуынғаннан кейін pH деңгейін теңестіріп, теріні сергітеді.",
                    "EN": "Alcohol-free gentle toner that balances pH after cleansing and refreshes skin.",
                },
                "volume": "150 мл",
                "origin": {"RU": "Италия", "KZ": "Италия", "EN": "Italy"},
                "year": "2025",
                "shelf_life": {"RU": "24 месяца", "KZ": "24 ай", "EN": "24 months"},
                "ingredients": {"RU": "Гидролат дамасской розы 85%, бетаин, экстракт пиона", "KZ": "Дамаск раушаны 85%, бетаин, пион", "EN": "Damask Rose Water 85%, Betaine, Peony"},
                "price": 8400,
                "img": "https://images.unsplash.com/photo-1608248597279-f99d160bfcbc?auto=format&fit=crop&w=600&q=80",
            },
        ],
    },
    {
        "title": {"RU": "03 · Макияж", "KZ": "03 · Макияж", "EN": "03 · Makeup"},
        "subtitle": {"RU": "Невесомые текстуры и акценты", "KZ": "Жеңіл текстуралар мен нәзік реңктер", "EN": "Weightless textures and accents"},
        "products": [
            {
                "id": "201",
                "name": {"RU": "Тинт для губ Silk Kiss", "KZ": "Silk Kiss ерін тинті", "EN": "Silk Kiss Lip Tint"},
                "short": {"RU": "Бархатный финиш и стойкий оттенок.", "KZ": "Барқыттай финиш және төзімді реңк.", "EN": "Velvet finish and long-lasting tint."},
                "desc": {
                    "RU": "Невесомый тинт с мягкой муссовой текстурой не сушит губы, держится до 8 часов и оставляет аккуратный естественный пигмент.",
                    "KZ": "Ерінді құрғатпайтын, 8 сағатқа дейін сақталатын жеңіл мусс-тинт.",
                    "EN": "Weightless mousse lip tint that lasts up to 8 hours without drying your lips.",
                },
                "volume": "6 г",
                "origin": {"RU": "Южная Корея", "KZ": "Оңтүстік Корея", "EN": "South Korea"},
                "year": "2026",
                "shelf_life": {"RU": "24 месяца", "KZ": "24 ай", "EN": "24 months"},
                "ingredients": {"RU": "Масло жожоба, витамин E, гиалуроновые микросферы", "KZ": "Жожоба майы, E дәрумені", "EN": "Jojoba Oil, Vitamin E, Hyaluronic Microspheres"},
                "price": 7900,
                "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=600&q=80",
            },
            {
                "id": "202",
                "name": {"RU": "Румяна Blush Cloud", "KZ": "Blush Cloud румянасы", "EN": "Blush Cloud Cheek"},
                "short": {"RU": "Естественный румянец, тающая текстура.", "KZ": "Табиғи қызғылт реңк, нәзік текстура.", "EN": "Natural flush with a melting texture."},
                "desc": {
                    "RU": "Кремовые румяна легко растушёвываются пальцами или спонжем, создавая свежий отдохнувший вид без пятен.",
                    "KZ": "Саусақпен немесе спонжбен оңай жағылатын, бетке балғын өң беретін кремді румяна.",
                    "EN": "Cream blush that blends effortlessly with fingers or sponge for a fresh look.",
                },
                "volume": "10 г",
                "origin": {"RU": "Франция", "KZ": "Франция", "EN": "France"},
                "year": "2026",
                "shelf_life": {"RU": "30 месяцев", "KZ": "30 ай", "EN": "30 months"},
                "ingredients": {"RU": "Сквалан, масло семян камелии, натуральные пигменты", "KZ": "Сквалан, камелия майы", "EN": "Squalane, Camellia Seed Oil"},
                "price": 9500,
                "img": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?auto=format&fit=crop&w=600&q=80",
            },
            {
                "id": "203",
                "name": {"RU": "Хайлайтер Liquid Pearl", "KZ": "Liquid Pearl хайлайтері", "EN": "Liquid Pearl Highlighter"},
                "short": {"RU": "Деликатное влажное сияние кожи.", "KZ": "Теріге нәзік інжу жарқылын береді.", "EN": "Delicate dewy pearl glow."},
                "desc": {
                    "RU": "Жидкий хайлайтер со светоотражающими микрочастицами жемчуга даёт эффект здорового блеска без крупных блёсток.",
                    "KZ": "Ірі жылтырсыз, табиғи әрі сау жарқыл беретін сұйық інжу хайлайтері.",
                    "EN": "Liquid highlighter with fine pearl micro-particles for a natural healthy glow.",
                },
                "volume": "15 мл",
                "origin": {"RU": "Италия", "KZ": "Италия", "EN": "Italy"},
                "year": "2025",
                "shelf_life": {"RU": "24 месяца", "KZ": "24 ай", "EN": "24 months"},
                "ingredients": {"RU": "Жемчужная мика, экстракт лотоса, витамин C", "KZ": "Інжу микасы, лотос сығындысы", "EN": "Pearl Mica, Lotus Extract, Vitamin C"},
                "price": 11200,
                "img": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=600&q=80",
            },
        ],
    },
]

# Специалисты: 1 главный специалист (с сертификатом и учёбой) + 2 коллеги
SPECIALISTS = [
    {
        "is_lead": True,
        "name": "Амина Нурланова",
        "role": {"RU": "Главный врач-косметолог · Опыт 7 лет", "KZ": "Бас дәрігер-косметолог · 7 жыл тәжірибе", "EN": "Lead Cosmetologist · 7 years exp."},
        "bio": {
            "RU": "Эксперт по аппаратной чистке лица и лечению проблемной кожи. Лично тестирует всю косметику перед добавлением в каталог.",
            "KZ": "Аппараттық бет тазалау және проблемалы теріні емдеу сарапшысы. Барлық косметиканы өзі тексеріп таңдайды.",
            "EN": "Expert in hardware facial cleansing and acne care. Personally approves every product in our catalog.",
        },
        "img": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=500&q=80",
        "education": {
            "RU": [
                "КазНМУ им. С.Д. Асфендиярова — Дерматовенерология (2019)",
                "Seoul Beauty Academy (Южная Корея) — Аппаратная косметология и УЗ-чистка (2022)",
                "Международный сертификат Esthetic Pro Europe № KZ-88412 (2025)",
            ],
            "KZ": [
                "С.Ж. Асфендияров атындағы ҚазҰМУ — Дерматовенерология (2019)",
                "Seoul Beauty Academy (Оңтүстік Корея) — Аппараттық косметология (2022)",
                "Esthetic Pro Europe халықаралық сертификаты № KZ-88412 (2025)",
            ],
            "EN": [
                "Asfendiyarov KazNMU — Dermatovenereology (2019)",
                "Seoul Beauty Academy (South Korea) — Hardware Cosmetology (2022)",
                "Esthetic Pro Europe International Certificate #KZ-88412 (2025)",
            ],
        },
    },
    {
        "is_lead": False,
        "name": "Мадина Серикова",
        "role": {"RU": "Косметолог-эстетист · Опыт 4 года", "KZ": "Косметолог-эстетист · 4 жыл тәжірибе", "EN": "Aesthetician · 4 years exp."},
        "bio": {
            "RU": "Специализируется на подборе домашнего ухода, восстановлении кожного барьера и мягких уходовых программах.",
            "KZ": "Үй күтімін таңдау, терінің қорғаныш қабатын қалпына келтіру бойынша маман.",
            "EN": "Specializes in home skincare routines, skin barrier repair, and gentle treatments.",
        },
        "img": "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=500&q=80",
    },
    {
        "is_lead": False,
        "name": "Алина Ким",
        "role": {"RU": "Специалист по аппаратному уходу · Опыт 3 года", "KZ": "Аппараттық күтім маманы · 3 жыл тәжірибе", "EN": "Beauty Device Specialist · 3 years exp."},
        "bio": {
            "RU": "Обучает клиентов правильному использованию УЗ-скраберов и LED-массажёров для максимального эффекта без вреда.",
            "KZ": "Клиенттерге УД-скраберлер мен LED-массажерлерді тиімді әрі қауіпсіз қолдануды үйретеді.",
            "EN": "Guides clients on safe and effective home use of ultrasonic scrubbers and LED devices.",
        },
        "img": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=500&q=80",
    },
]

# Популярные вопросы (FAQ)
FAQ_LIST = [
    {
        "q": {"RU": "Вся ли косметика оригинальная?", "KZ": "Барлық косметика түпнұсқа ма?", "EN": "Are all products 100% original?"},
        "a": {
            "RU": "Да, мы работаем напрямую с официальными дистрибьюторами Кореи, Франции и Италии. На каждый товар есть сертификат соответствия и свежие сроки годности.",
            "KZ": "Иә, біз Корея, Франция және Италияның ресми дистрибьюторларымен тікелей жұмыс істейміз. Әр тауардың сертификаты бар.",
            "EN": "Yes, we work directly with official distributors in Korea, France, and Italy. Every product is certified.",
        },
    },
    {
        "q": {"RU": "Безопасен ли аппарат для чистки лица дома?", "KZ": "Бет тазалау аппаратын үйде қолдану қауіпсіз бе?", "EN": "Is the facial cleansing device safe for home use?"},
        "a": {
            "RU": "Абсолютно безопасен при соблюдении инструкции. При покупке наши специалисты подробно объяснят, с каким гелем его использовать и как часто проводить процедуру.",
            "KZ": "Нұсқаулықты сақтаған жағдайда толықтай қауіпсіз. Сатып алғанда мамандарымыз қалай дұрыс қолдану керектігін түсіндіреді.",
            "EN": "Completely safe when following instructions. Our specialists will explain how to use it with your skin type.",
        },
    },
    {
        "q": {"RU": "Как работает доставка и оплата?", "KZ": "Жеткізу және төлем қалай жүзеге асады?", "EN": "How do delivery and payment work?"},
        "a": {
            "RU": "Доставка по городу занимает 1–2 часа курьером, по всему Казахстану — 2–4 дня через СДЭК или Казпочту. Также доступен самовывоз по адресу пр. Б. Саттарханова, 5.",
            "KZ": "Қала бойынша курьермен 1–2 сағатта, Қазақстан бойынша 2–4 күнде жеткіземіз. Сондай-ақ Б. Саттарханов, 5 мекенжайынан өзіңіз алып кете аласыз.",
            "EN": "Local courier delivery takes 1–2 hours, nationwide delivery takes 2–4 days. Pickup is available at 5 B. Sattarkhanov Ave.",
        },
    },
    {
        "q": {"RU": "Можно ли получить бесплатный подбор ухода?", "KZ": "Тегін күтім таңдау кеңесін алуға бола ма?", "EN": "Can I get a free skincare consultation?"},
        "a": {
            "RU": "Да! Оставьте заявку через корзину или приходите в наш бутик — наш главный специалист или её коллеги бесплатно подберут уход под ваш тип кожи.",
            "KZ": "Иә! Себет арқылы өтінім қалдырыңыз немесе бутигімізге келіңіз — мамандарымыз теріңізге сай күтімді тегін таңдап береді.",
            "EN": "Yes! Leave a request via the cart or visit our boutique — our specialists will build a routine for your skin for free.",
        },
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


@st.dialog(t["cert_modal"], width="large")
def show_certificate(spec):
    st.markdown(f"### {spec['name']}")
    st.markdown(f"**{spec['role'][lang]}**")
    st.divider()
    for item in spec["education"][lang]:
        st.markdown(f"✅ {item}")
    st.markdown(
        """
        <div style="margin-top:16px; padding:20px; border:2px dashed #C9184A; border-radius:14px; background:#FFF0F5; text-align:center;">
            <div style="font-family:'Cormorant Garamond', serif; font-size:26px; font-weight:700; color:#800F2F;">CERTIFICATE OF EXCELLENCE</div>
            <div style="font-size:13px; color:#6B4250; margin-top:6px;">Esthetic Pro Europe · Hardware Cosmetology & Dermatology</div>
            <div style="font-size:15px; font-weight:700; color:#2D161E; margin-top:10px;">Amina Nurlanova · ID #KZ-88412</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# 1. ШАПКА + ПЕРЕКЛЮЧАТЕЛЬ ЯЗЫКА
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

# 2. HERO-БАННЕР (ИМПРОВИЗАЦИЯ)
st.markdown(
    f"""
    <div class="hero-banner">
        <span class="hero-tag">{t['hero_tag']}</span>
        <div class="hero-title">{t['hero_title']}</div>
        <div class="hero-desc">{t['hero_desc']}</div>
        <div class="hero-promo">🎁 {t['hero_promo']}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 3. КАТАЛОГ ТОВАРОВ (АККОРДЕОН)
st.markdown(f'<div class="section-heading">{t["catalog_title"]}</div>', unsafe_allow_html=True)

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

# 4. СПЕЦИАЛИСТЫ (1 ГЛАВНЫЙ + 2 КОЛЛЕГИ)
st.markdown(f'<div class="section-heading">{t["team_title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="section-sub">{t["team_sub"]}</div>', unsafe_allow_html=True)

spec_cols = st.columns(3, gap="medium")
for idx_s, spec in enumerate(SPECIALISTS):
    with spec_cols[idx_s]:
        card_cls = "spec-card spec-card-lead" if spec["is_lead"] else "spec-card"
        badge_cls = "spec-badge-lead" if spec["is_lead"] else "spec-badge"
        badge_txt = t["lead_badge"] if spec["is_lead"] else t["colleague_badge"]

        st.markdown(
            f"""
            <div class="{card_cls}">
                <img class="spec-img" src="{spec['img']}" alt="{spec['name']}">
                <div class="spec-body">
                    <span class="{badge_cls}">{badge_txt}</span>
                    <div class="spec-name">{spec['name']}</div>
                    <div class="spec-role">{spec['role'][lang]}</div>
                    <div class="spec-bio">{spec['bio'][lang]}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if spec["is_lead"]:
            if st.button(f"🎓 {t['cert_btn']}", key="lead_cert_btn", type="primary", use_container_width=True):
                show_certificate(spec)

# 5. АДРЕС И КАРТА (САТТАРХАНОВА 5)
st.markdown(f'<div class="section-heading">{t["addr_title"]}</div>', unsafe_allow_html=True)
addr_col1, addr_col2 = st.columns([1, 1.6], gap="large")

with addr_col1:
    st.markdown(
        f"""
        <div class="address-card">
            <h3 style="margin-top:0; font-family:'Cormorant Garamond', serif; font-size:28px;">VELOUR Boutique</h3>
            <p style="font-size:16px; margin-bottom:12px;">📍 <b>{t['addr_text']}</b></p>
            <p style="font-size:15px; margin-bottom:12px;">🕒 {t['addr_hours']}</p>
            <p style="font-size:15px; margin-bottom:12px;">📞 {t['addr_phone']}</p>
            <p style="font-size:14px; color:#7A4353;">Instagram: @velour.beauty.kz</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with addr_col2:
    # Встроенная интерактивная карта (пр. Б. Саттарханова, 5)
    components.html(
        """
        <div style="border-radius:18px; overflow:hidden; border:1px solid rgba(217,79,112,0.3); box-shadow:0 8px 24px rgba(150,35,68,0.08);">
            <iframe
                width="100%"
                height="260"
                frameborder="0"
                scrolling="no"
                marginheight="0"
                marginwidth="0"
                src="https://www.openstreetmap.org/export/embed.html?bbox=68.2410%2C43.2910%2C68.2620%2C43.3030&amp;layer=mapnik&amp;marker=43.2973%2C68.2517">
            </iframe>
        </div>
        """,
        height=275,
    )

# 6. ПОПУЛЯРНЫЕ ВОПРОСЫ (FAQ)
st.markdown(f'<div class="section-heading">{t["faq_title"]}</div>', unsafe_allow_html=True)
for item_faq in FAQ_LIST:
    with st.expander(f"**{item_faq['q'][lang]}**", expanded=False):
        st.write(item_faq["a"][lang])

# 7. БОКОВАЯ ПАНЕЛЬ — КОРЗИНА С САКУРОЙ И ПРОМОКОДОМ
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
        subtotal_all = 0
        to_delete = []
        for pid, item in st.session_state.cart.items():
            subtotal = item["price"] * item["qty"]
            subtotal_all += subtotal
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

        # Промокод VELOUR10
        p_col1, p_col2 = st.columns([2, 1.2])
        with p_col1:
            promo_code = st.text_input("promo", label_visibility="collapsed", placeholder=t["promo_ph"])
        with p_col2:
            if st.button(t["promo_btn"], type="secondary", use_container_width=True):
                if promo_code.strip().upper() == "VELOUR10":
                    st.session_state.promo_active = True
                    st.success(t["promo_ok"])
                else:
                    st.session_state.promo_active = False
                    st.error(t["promo_err"])

        discount_val = int(subtotal_all * 0.1) if st.session_state.promo_active else 0
        final_total = subtotal_all - discount_val

        if discount_val > 0:
            st.markdown(f"**{t['discount']}:** −{discount_val:,} ₸".replace(",", " "))
        st.markdown(f"### {t['total']}: {final_total:,} ₸".replace(",", " "))

        with st.form("order_form"):
            name = st.text_input(t["name_ph"])
            phone = st.text_input(t["phone_ph"])
            submitted = st.form_submit_button(t["checkout"], type="primary", use_container_width=True)

            if submitted:
                if not name or not phone:
                    st.error(t["fill_err"])
                else:
                    print(f"\n[ЗАКАЗ {datetime.now().strftime('%H:%M:%S')}] {name} ({phone}) — {final_total} ₸")
                    st.session_state.cart = {}
                    st.session_state.promo_active = False
                    st.success(t["order_ok"])
