import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(page_title="VELOUR — Косметика и Уход", page_icon="🫧", layout="wide")

if "cart" not in st.session_state:
    st.session_state.cart = {}
if "lang" not in st.session_state:
    st.session_state.lang = "RU"
if "promo_active" not in st.session_state:
    st.session_state.promo_active = False
if "active_cat" not in st.session_state:
    st.session_state.active_cat = None
if "scroll_to" not in st.session_state:
    st.session_state.scroll_to = None

# Встроенный переводчик (RU / KZ / EN)
TEXTS = {
    "RU": {
        "subtitle": "Бутик косметики и аппаратного ухода · Оригинальная продукция",
        "skin_nav_title": "Подберите уход по типу кожи — нажмите, чтобы перейти к каталогу:",
        "hero_tag": "ХИТ СЕЗОНА · НОВИНКА",
        "hero_title": "Профессиональный уход и чистка лица у вас дома",
        "hero_desc": "Оригинальная косметика из Кореи и Франции, аппараты для ультразвуковой чистки и подбор ухода от наших дипломированных косметологов.",
        "hero_promo": "Промокод на скидку 10% в корзине: VELOUR10",
        "dev_section": "Наш флагманский аппарат для чистки лица",
        "dev_badge": "СЕРТИФИЦИРОВАННОЕ ОБОРУДОВАНИЕ · 2026",
        "dev_name": "Velour Sonic Pro — Ультразвуковой аппарат 4-в-1",
        "dev_desc": "Профессиональный прибор для глубокой ультразвуковой чистки пор (28 кГц), ионофореза и деликатного микромассажа. Прошёл клинические испытания и безопасен даже для чувствительной кожи.",
        "dev_specs": "• 4 режима работы: пилинг, очищение, питание, лифтинг\n• Медицинская нержавеющая сталь · Защита от влаги IPX5\n• Официальная гарантия 12 месяцев и сертификат соответствия",
        "dev_cert_btn": "Сертификат аппарата",
        "dev_cert_modal": "Сертификат соответствия аппарата",
        "dev_add_btn": "В корзину — 24 900 ₸",
        "skin_cat_title": "Каталог по типам кожи",
        "skin_cat_sub": "Нажмите на нужный раздел, чтобы раскрыть подобранные средства",
        "main_cat_title": "Основной каталог косметики и аппаратов",
        "main_cat_sub": "Отдельный каталог по видам продукции — нажмите на категорию",
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
        "cart_empty": "Корзина пока пуста 🫧\nВыберите товары в каталоге.",
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
        "skin_nav_title": "Тері түріне сай күтімді таңдаңыз — каталогқа өту үшін басыңыз:",
        "hero_tag": "МАУСЫМ ХИТІ · ЖАҢА ӨНІМ",
        "hero_title": "Үй жағдайындағы кәсіби күтім және бет тазалау",
        "hero_desc": "Корея мен Францияның түпнұсқа косметикасы, ультрадыбыстық тазалау аппараттары және дипломды косметологтардың кеңесі.",
        "hero_promo": "Себетте 10% жеңілдік промокоды: VELOUR10",
        "dev_section": "Бет тазалауға арналған флагмандық аппарат",
        "dev_badge": "СЕРТИФИКАТТАЛҒАН ҚҰРЫЛҒЫ · 2026",
        "dev_name": "Velour Sonic Pro — 4-в-1 ультрадыбыстық аппараты",
        "dev_desc": "Тері тесіктерін терең ультрадыбыстық тазалау (28 кГц), ионофорез және микромассажға арналған кәсіби құрылғы. Клиникалық сынақтан өткен.",
        "dev_specs": "• 4 жұмыс режимі: пилинг, тазалау, нәрлендіру, лифтинг\n• Медициналық болат · Ылғалдан қорғау IPX5\n• 12 ай ресми кепілдік және сәйкестік сертификаты",
        "dev_cert_btn": "Аппарат сертификаты",
        "dev_cert_modal": "Аппараттың сәйкестік сертификаты",
        "dev_add_btn": "Себетке — 24 900 ₸",
        "skin_cat_title": "Тері түрлері бойынша каталог",
        "skin_cat_sub": "Таңдалған өнімдерді көру үшін бөлімді басыңыз",
        "main_cat_title": "Косметика және аппараттар каталогы",
        "main_cat_sub": "Өнім түрлері бойынша бөлек каталог — санатты басыңыз",
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
        "cart_empty": "Себет әзірге бос 🫧\nКаталогтан тауар таңдаңыз.",
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
        "skin_nav_title": "Choose your skin type — click to jump directly to the catalog:",
        "hero_tag": "BESTSELLER · NEW ARRIVAL",
        "hero_title": "Professional Skincare & Facial Cleansing at Home",
        "hero_desc": "Authentic Korean & French cosmetics, ultrasonic cleansing devices, and personal care guidance from our certified cosmetologists.",
        "hero_promo": "Use promo code in cart for 10% OFF: VELOUR10",
        "dev_section": "Our Flagship Facial Cleansing Device",
        "dev_badge": "CERTIFIED BEAUTY DEVICE · 2026",
        "dev_name": "Velour Sonic Pro — 4-in-1 Ultrasonic Scrubber",
        "dev_desc": "Professional device for deep ultrasonic pore cleansing (28 kHz), iontophoresis, and gentle micro-massage. Clinically tested and safe for sensitive skin.",
        "dev_specs": "• 4 modes: peeling, deep cleanse, nutrition, lifting\n• Medical-grade stainless steel · IPX5 waterproof\n• Official 12-month warranty & quality certificate",
        "dev_cert_btn": "Device Certificate",
        "dev_cert_modal": "Device Compliance & Safety Certificate",
        "dev_add_btn": "Add to cart — 24 900 ₸",
        "skin_cat_title": "Catalog by Skin Type",
        "skin_cat_sub": "Click any skin concern to expand tailored products",
        "main_cat_title": "Main Cosmetics & Devices Catalog",
        "main_cat_sub": "Browse by product type — click any category to open",
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
        "cart_empty": "Your cart is empty 🫧\nPick something from the catalog.",
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

# CSS: мягко-молочная палитра, тёплые лавовые переливы, отличительная молочная корзина и мыльные пузыри
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;500;600;700&display=swap');

    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #FAF6F0 !important;
        color: #2E241F !important;
        font-family: 'Manrope', sans-serif !important;
    }

    [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background: transparent !important;
        position: relative;
        z-index: 1;
    }

    [data-testid="stHeader"] {
        background: rgba(250, 246, 240, 0.78) !important;
        backdrop-filter: blur(10px);
    }
    [data-testid="stHeader"] * { color: #3D2B22 !important; }

    /* Мягко-молочный фон с плавающими кремовыми переливами */
    .lava-bg {
        position: fixed; inset: 0; overflow: hidden; z-index: 0; pointer-events: none;
        background: linear-gradient(135deg, #FCF9F4 0%, #F6EFE5 100%);
    }
    .lava-blob {
        position: absolute; border-radius: 50%; filter: blur(90px); opacity: 0.75; will-change: transform;
    }
    .blob-1 { width: 460px; height: 460px; background: radial-gradient(circle, #EFE0CE 0%, #F7EDE2 70%); top: -90px; left: -60px; animation: float1 20s ease-in-out infinite alternate; }
    .blob-2 { width: 520px; height: 520px; background: radial-gradient(circle, #E6D2BC 0%, #F3E6D8 70%); bottom: -120px; right: -80px; animation: float2 24s ease-in-out infinite alternate; }
    .blob-3 { width: 400px; height: 400px; background: radial-gradient(circle, #F2DFCE 0%, #FAF2E8 75%); top: 35%; left: 40%; animation: float3 26s ease-in-out infinite alternate; }
    .blob-4 { width: 340px; height: 340px; background: radial-gradient(circle, #DEC5AD 0%, #F2E4D6 75%); opacity: 0.45; bottom: 20%; left: 12%; animation: float4 22s ease-in-out infinite alternate; }

    @keyframes float1 { 0% { transform: translate(0,0) scale(1); } 50% { transform: translate(150px,100px) scale(1.12); } 100% { transform: translate(50px,210px) scale(0.95); } }
    @keyframes float2 { 0% { transform: translate(0,0) scale(1); } 50% { transform: translate(-160px,-110px) scale(1.1); } 100% { transform: translate(-60px,-200px) scale(0.92); } }
    @keyframes float3 { 0% { transform: translate(0,0) scale(1); } 50% { transform: translate(-130px,80px) scale(1.16); } 100% { transform: translate(120px,-90px) scale(0.94); } }
    @keyframes float4 { 0% { transform: translate(0,0) scale(1); } 50% { transform: translate(180px,-100px) scale(1.08); } 100% { transform: translate(80px,70px) scale(0.95); } }

    h1, h2, h3, h4, p, span, label { color: #2E241F !important; }

    .brand-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 54px; font-weight: 700; letter-spacing: 6px;
        color: #3D2B22 !important; margin-bottom: 2px; line-height: 1.05;
    }
    .brand-sub { font-size: 15px; color: #756054 !important; margin-bottom: 12px; }

    .skin-nav-label {
        font-size: 14px; font-weight: 600; color: #5C473B !important;
        margin-bottom: 10px;
    }

    .section-heading {
        font-family: 'Cormorant Garamond', serif;
        font-size: 36px; font-weight: 700; color: #3D2B22 !important;
        margin-top: 28px; margin-bottom: 4px;
    }
    .section-sub { font-size: 14px; color: #756054 !important; margin-bottom: 16px; }

    /* Hero-баннер */
    .hero-banner {
        background: rgba(255, 253, 249, 0.85);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(163, 123, 94, 0.25);
        border-radius: 22px;
        padding: 26px 32px;
        margin-top: 14px;
        margin-bottom: 24px;
        box-shadow: 0 12px 30px rgba(92, 68, 52, 0.06);
    }
    .hero-tag {
        display: inline-block;
        background: linear-gradient(135deg, #9C6B4E, #BC8C6D);
        color: #FFFFFF !important;
        font-size: 11px; font-weight: 700; letter-spacing: 1.2px;
        padding: 5px 12px; border-radius: 999px; margin-bottom: 12px;
    }
    .hero-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 38px; font-weight: 700; color: #2E241F !important;
        line-height: 1.12; margin-bottom: 10px;
    }
    .hero-desc { font-size: 15px; color: #635147 !important; line-height: 1.5; margin-bottom: 14px; max-width: 720px; }
    .hero-promo {
        display: inline-block; background: #F5EBE0; border: 1px dashed #9C6B4E;
        color: #7A4F35 !important; font-size: 13px; font-weight: 600;
        padding: 6px 14px; border-radius: 10px;
    }

    /* Витрина флагманского аппарата */
    .device-showcase {
        background: rgba(255, 253, 250, 0.9);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(156, 107, 78, 0.3);
        border-radius: 20px;
        padding: 22px;
        margin-bottom: 16px;
        box-shadow: 0 10px 28px rgba(92, 68, 52, 0.07);
    }

    /* Аккордеон */
    [data-testid="stExpander"] {
        background: rgba(255, 253, 250, 0.85) !important;
        backdrop-filter: blur(14px);
        border: 1px solid rgba(163, 123, 94, 0.25) !important;
        border-radius: 16px !important;
        margin-bottom: 12px !important;
        box-shadow: 0 8px 24px rgba(92, 68, 52, 0.05);
        overflow: hidden;
    }
    [data-testid="stExpander"] details,
    [data-testid="stExpander"] summary,
    [data-testid="stExpanderDetails"] {
        background-color: rgba(255, 253, 250, 0.72) !important;
        color: #2E241F !important;
    }
    [data-testid="stExpander"] summary { padding: 15px 20px !important; font-size: 17px !important; }
    [data-testid="stExpander"] summary svg { fill: #9C6B4E !important; color: #9C6B4E !important; }
    [data-testid="stExpander"] summary:hover { background-color: rgba(242, 232, 220, 0.65) !important; }

    /* Карточки товаров */
    .product-card-box {
        background: #FFFDFB;
        border: 1px solid rgba(163, 123, 94, 0.22);
        border-radius: 16px; overflow: hidden; margin-bottom: 10px;
        box-shadow: 0 6px 18px rgba(92, 68, 52, 0.06);
        transition: transform 0.2s ease;
    }
    .product-card-box:hover { transform: translateY(-3px); }
    .product-card-img { width: 100%; height: 215px; object-fit: cover; display: block; }
    .product-card-body { padding: 14px 16px 12px 16px; }
    .product-badge {
        display: inline-block; background: #F5EBE0; color: #85563B !important;
        font-size: 11px; font-weight: 600; padding: 3px 9px; border-radius: 999px; margin-bottom: 8px;
    }
    .product-name {
        font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 700;
        color: #2E241F !important; line-height: 1.15; height: 50px; overflow: hidden; margin-bottom: 6px;
    }
    .product-short {
        font-size: 13px; color: #6E5B50 !important; line-height: 1.4; height: 38px; overflow: hidden; margin-bottom: 10px;
    }
    .product-price { font-size: 18px; font-weight: 700; color: #8A5A3E !important; }

    /* Карточки специалистов */
    .spec-card {
        background: #FFFDFB;
        border: 1px solid rgba(163, 123, 94, 0.24);
        border-radius: 18px; overflow: hidden; margin-bottom: 10px;
        box-shadow: 0 8px 22px rgba(92, 68, 52, 0.06);
    }
    .spec-card-lead { border: 2px solid #9C6B4E !important; box-shadow: 0 10px 28px rgba(156, 107, 78, 0.16); }
    .spec-img { width: 100%; height: 260px; object-fit: cover; object-position: top; display: block; }
    .spec-body { padding: 16px; }
    .spec-badge-lead {
        display: inline-block; background: linear-gradient(135deg, #9C6B4E, #BC8C6D);
        color: #FFFFFF !important; font-size: 11px; font-weight: 700;
        padding: 4px 10px; border-radius: 999px; margin-bottom: 8px;
    }
    .spec-badge {
        display: inline-block; background: #F5EBE0; color: #85563B !important;
        font-size: 11px; font-weight: 600; padding: 4px 10px; border-radius: 999px; margin-bottom: 8px;
    }
    .spec-name { font-family: 'Cormorant Garamond', serif; font-size: 24px; font-weight: 700; color: #2E241F !important; margin-bottom: 4px; }
    .spec-role { font-size: 13px; font-weight: 600; color: #8A5A3E !important; margin-bottom: 8px; }
    .spec-bio { font-size: 13px; color: #6E5B50 !important; line-height: 1.45; min-height: 60px; }

    .address-card {
        background: rgba(255, 253, 250, 0.9);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(163, 123, 94, 0.25);
        border-radius: 18px; padding: 24px; height: 100%;
        box-shadow: 0 8px 24px rgba(92, 68, 52, 0.06);
    }

    /* Кнопки */
    div.stButton > button { border-radius: 12px !important; font-weight: 600 !important; transition: all 0.2s ease !important; }
    div.stButton > button[kind="primary"] { background: linear-gradient(135deg, #9C6B4E, #B88667) !important; border: none !important; }
    div.stButton > button[kind="primary"] * { color: #FFFFFF !important; }
    div.stButton > button[kind="secondary"] { background: #FFFDFB !important; border: 1px solid rgba(156, 107, 78, 0.38) !important; }
    div.stButton > button[kind="secondary"] * { color: #5C3D2B !important; }
    div.stButton > button[kind="secondary"]:hover { background: #F5EBE0 !important; border-color: #9C6B4E !important; transform: translateY(-1px); }

    /* Модальные окна */
    div[role="dialog"], div[role="dialog"] > div, [data-testid="stDialog"] div[role="dialog"] {
        background-color: #FCF9F4 !important; color: #2E241F !important;
        border: 1px solid rgba(156, 107, 78, 0.3) !important; border-radius: 18px !important;
    }
    div[role="dialog"] h1, div[role="dialog"] h2, div[role="dialog"] h3, div[role="dialog"] p, div[role="dialog"] span, div[role="dialog"] strong {
        color: #2E241F !important;
    }
    div[role="dialog"] button[aria-label="Close"] svg { fill: #3D2B22 !important; color: #3D2B22 !important; }

    /* Корзина: чуть более плотный мягко-молочный оттенок + мыльные пузыри */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #F3ECE1 0%, #EAE0D2 100%) !important;
        border-right: 1px solid rgba(156, 107, 78, 0.25) !important;
        overflow: hidden !important;
    }
    [data-testid="stSidebarContent"] { position: relative; z-index: 2; }
    [data-testid="stSidebar"] input {
        background-color: rgba(255, 253, 250, 0.95) !important;
        color: #2E241F !important;
        border: 1px solid rgba(156, 107, 78, 0.32) !important;
        border-radius: 8px !important;
    }
    .cart-empty-box {
        background: rgba(255, 253, 250, 0.78); border: 1px dashed rgba(156, 107, 78, 0.4);
        border-radius: 14px; padding: 18px 14px; text-align: center;
        color: #5C473B !important; font-size: 14px; line-height: 1.5; backdrop-filter: blur(6px);
    }
    .cart-item-card {
        background: rgba(255, 253, 250, 0.88); border: 1px solid rgba(156, 107, 78, 0.22);
        border-radius: 12px; padding: 10px 12px; margin-bottom: 8px; backdrop-filter: blur(6px);
    }

    /* Слой с мыльными пузырями в корзине */
    .bubbles-layer {
        position: fixed; top: 0; left: 0; width: 340px; height: 100vh;
        pointer-events: none; overflow: hidden; z-index: 0;
    }
    .bubble {
        position: absolute;
        bottom: -50px;
        border-radius: 50%;
        background: radial-gradient(
            circle at 30% 30%,
            rgba(255, 255, 255, 0.95) 0%,
            rgba(255, 244, 232, 0.35) 35%,
            rgba(222, 238, 255, 0.28) 65%,
            rgba(255, 215, 230, 0.25) 100%
        );
        border: 1px solid rgba(255, 255, 255, 0.85);
        box-shadow:
            inset -3px -3px 8px rgba(180, 155, 135, 0.18),
            inset 2px 2px 6px rgba(255, 255, 255, 0.95),
            0 4px 10px rgba(140, 110, 90, 0.08);
        animation: bubbleRise linear infinite;
    }
    .b1  { left: 10%; width: 22px; height: 22px; animation-duration: 12s; animation-delay: 0s; }
    .b2  { left: 26%; width: 34px; height: 34px; animation-duration: 16s; animation-delay: -4s; }
    .b3  { left: 42%; width: 16px; height: 16px; animation-duration: 10s; animation-delay: -7s; }
    .b4  { left: 58%; width: 28px; height: 28px; animation-duration: 14s; animation-delay: -2s; }
    .b5  { left: 74%; width: 20px; height: 20px; animation-duration: 13s; animation-delay: -9s; }
    .b6  { left: 86%; width: 30px; height: 30px; animation-duration: 17s; animation-delay: -5s; }
    .b7  { left: 18%; width: 14px; height: 14px; animation-duration: 11s; animation-delay: -3s; }
    .b8  { left: 50%; width: 24px; height: 24px; animation-duration: 15s; animation-delay: -8s; }
    .b9  { left: 66%; width: 18px; height: 18px; animation-duration: 12.5s; animation-delay: -1s; }
    .b10 { left: 34%; width: 26px; height: 26px; animation-duration: 18s; animation-delay: -11s; }

    @keyframes bubbleRise {
        0%   { transform: translateY(0) translateX(0px) scale(0.9); opacity: 0; }
        12%  { opacity: 0.85; }
        50%  { transform: translateY(-52vh) translateX(18px) scale(1.04); opacity: 0.8; }
        88%  { opacity: 0.75; }
        100% { transform: translateY(-108vh) translateX(-14px) scale(1.08); opacity: 0; }
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


def p(pid, n_ru, n_kz, n_en, s_ru, s_kz, s_en, d_ru, d_kz, d_en, vol, o_ru, o_kz, o_en, year, sh_ru, sh_kz, sh_en, ing_ru, ing_kz, ing_en, price, img):
    return {
        "id": pid,
        "name": {"RU": n_ru, "KZ": n_kz, "EN": n_en},
        "short": {"RU": s_ru, "KZ": s_kz, "EN": s_en},
        "desc": {"RU": d_ru, "KZ": d_kz, "EN": d_en},
        "volume": vol,
        "origin": {"RU": o_ru, "KZ": o_kz, "EN": o_en},
        "year": year,
        "shelf_life": {"RU": sh_ru, "KZ": sh_kz, "EN": sh_en},
        "ingredients": {"RU": ing_ru, "KZ": ing_kz, "EN": ing_en},
        "price": price,
        "img": img,
    }


# Флагманский аппарат (для отдельной витрины с сертификатом)
FLAGSHIP_DEVICE = p(
    "d1", "УЗ-скрабер Velour Sonic Pro", "Velour Sonic Pro УД-скрабері", "Velour Sonic Pro Scrubber",
    "Глубокая ультразвуковая чистка пор (28 кГц).", "Тері тесіктерін ультрадыбыспен терең тазалау.", "Deep ultrasonic pore cleansing (28 kHz).",
    "Профессиональный аппарат для УЗ-чистки лица. Удаляет чёрные точки и усиливает впитывание сывороток в 3 раза.",
    "Ультрадыбыстық тазалау аппараты. Қара нүктелерді кетіріп, сарысулардың сіңуін 3 есе арттырады.",
    "Professional ultrasonic facial scrubber. Removes blackheads and boosts serum absorption 3x.",
    "4 режима · 95 г", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "Гарантия 12 мес.", "Кепілдік 12 ай", "12-mo warranty",
    "Аппарат, чехол, USB-C кабель, инструкция", "Аппарат, қап, USB-C, нұсқаулық", "Device, cover, USB-C cable, manual",
    24900, "https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?auto=format&fit=crop&w=700&q=80"
)

# 1. КАТАЛОГ ПО ТИПАМ КОЖИ
SKIN_CATALOG = [
    {
        "id": "skin_hydrated",
        "btn_label": {"RU": "💧 Влажная кожа", "KZ": "💧 Ылғалды тері", "EN": "💧 Hydrated Skin"},
        "title": {"RU": "💧 Влажная и сияющая кожа", "KZ": "💧 Ылғалды және жарқыраған тері", "EN": "💧 Hydrated & Dewy Skin"},
        "subtitle": {"RU": "Лёгкое увлажнение, свежесть и защита водного баланса", "KZ": "Жеңіл ылғалдандыру және балғындық", "EN": "Light hydration and moisture balance"},
        "products": [
            p("s1", "Аква-гель Aqua Dew", "Aqua Dew аква-гелі", "Aqua Dew Gel",
              "Невесомый гель для эффекта влажной кожи.", "Ылғалды тері әсеріне арналған жеңіл гель.", "Weightless gel for dewy glass skin.",
              "Освежающий гель с морским коллагеном моментально впитывается, удерживает влагу на 24 часа и дарит естественное сияние.",
              "Теңіз коллагені бар сергітетін гель лезде сіңіп, 24 сағат бойы ылғалды сақтайды.",
              "Refreshing marine collagen gel absorbs instantly and locks in 24h moisture.",
              "50 мл", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "24 месяца", "24 ай", "24 months",
              "Морской коллаген, гиалурон, сок берёзы", "Теңіз коллагені, гиалурон, қайың шырыны", "Marine collagen, hyaluronic acid, birch sap",
              11900, "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=600&q=80"),
            p("s2", "Эссенция Glass Skin", "Glass Skin эссенциясы", "Glass Skin Essence",
              "Эффект зеркальной и свежей кожи.", "Айнадай тегіс әрі балғын тері әсері.", "Mirror-like fresh skin effect.",
              "Концентрированная эссенция с ферментами риса выравнивает микрорельеф и придаёт коже здоровый влажный блеск.",
              "Күріш ферменттері бар эссенция тері реңкін тегістеп, табиғи жылтыр береді.",
              "Concentrated rice ferment essence smooths texture for a healthy dewy sheen.",
              "100 мл", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "24 месяца", "24 ай", "24 months",
              "Фермент риса, ниацинамид 3%, аденозин", "Күріш ферменті, ниацинамид 3%", "Rice ferment, niacinamide 3%, adenosine",
              13400, "https://images.unsplash.com/photo-1608248597279-f99d160bfcbc?auto=format&fit=crop&w=600&q=80"),
            p("s3", "Мист-спрей Water Glow", "Water Glow мист-спрейі", "Water Glow Mist",
              "Мгновенная свежесть поверх макияжа.", "Макияж үстінен лезде сергітеді.", "Instant freshness over makeup.",
              "Ультрамелкий спрей-мист освежает кожу в офисе и на улице, предотвращая потерю влаги в течение дня.",
              "Ұсақ дисперсті мист күні бойы теріні ылғалдандырып, құрғаудан қорғайды.",
              "Ultra-fine mist refreshes skin anytime and prevents moisture loss.",
              "120 мл", "Франция", "Франция", "France", "2026", "30 месяцев", "30 ай", "30 months",
              "Термальная вода, экстракт алоэ, пантенол", "Термалды су, алоэ, пантенол", "Thermal water, aloe extract, panthenol",
              8900, "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=600&q=80"),
        ],
    },
    {
        "id": "skin_dry",
        "btn_label": {"RU": "🌵 Сухая кожа", "KZ": "🌵 Құрғақ тері", "EN": "🌵 Dry Skin"},
        "title": {"RU": "🌵 Сухая и чувствительная кожа", "KZ": "🌵 Құрғақ және сезімтал тері", "EN": "🌵 Dry & Sensitive Skin"},
        "subtitle": {"RU": "Глубокое питание, церамиды и устранение шелушений", "KZ": "Терең нәрлендіру және қабыршақтануды жою", "EN": "Deep nourishment, ceramides and barrier repair"},
        "products": [
            p("s4", "Крем-барьер Ceramide Rich", "Ceramide Rich кремі", "Ceramide Rich Cream",
              "Убирает шелушения и стянутость за ночь.", "Қабыршақтану мен тартылуды бір түнде кетіреді.", "Relieves flakiness and tightness overnight.",
              "Насыщенный питательный крем с 5 видами церамидов восстанавливает липидный слой даже очень сухой кожи.",
              "5 түрлі церамиді бар нәрлендіргіш крем өте құрғақ теріні де қалпына келтіреді.",
              "Rich nourishing cream with 5 ceramides restores the lipid barrier of very dry skin.",
              "50 мл", "Франция", "Франция", "France", "2026", "36 месяцев", "36 ай", "36 months",
              "Церамиды 5 типов, масло ши, сквалан", "5 түрлі церамид, ши майы, сквалан", "5 Ceramides, shea butter, squalane",
              15200, "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd?auto=format&fit=crop&w=600&q=80"),
            p("s5", "Масло-эликсир Squalane Drop", "Squalane Drop майы", "Squalane Drop Oil",
              "Шелковистое питание без забивания пор.", "Тесіктерді бітемейтін жібектей нәрлендіру.", "Silky nourishment without clogging pores.",
              "100% растительный сквалан с витамином E мгновенно смягчает сухие участки и защищает кожу от ветра и холода.",
              "100% өсімдік скваланы мен E дәрумені теріні жел мен суықтан қорғайды.",
              "100% plant squalane with Vitamin E softens dry patches and shields from cold wind.",
              "30 мл", "Италия", "Италия", "Italy", "2026", "24 месяца", "24 ай", "24 months",
              "Растительный сквалан, масло жожоба, витамин E", "Өсімдік скваланы, жожоба майы", "Plant squalane, jojoba oil, vitamin E",
              16400, "https://images.unsplash.com/photo-1601049541289-9b1b7bbbfe19?auto=format&fit=crop&w=600&q=80"),
            p("s6", "Ночная маска Honey Barrier", "Honey Barrier түнгі маскасы", "Honey Barrier Mask",
              "Интенсивное восстановление во время сна.", "Ұйқы кезінде қарқынды қалпына келтіру.", "Intensive overnight recovery.",
              "Несмываемая медовая маска с прополисом насыщает кожу влагой и наутро делает лицо мягким и отдохнувшим.",
              "Прополисі бар түнгі маска теріні ылғалмен қанықтырып, таңертең жұмсақ етеді.",
              "Leave-on propolis sleeping mask deeply hydrates for soft, rested morning skin.",
              "75 мл", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "24 месяца", "24 ай", "24 months",
              "Экстракт прополиса, мёд манука, пантенол", "Прополис, манука балы, пантенол", "Propolis extract, manuka honey, panthenol",
              12900, "https://images.unsplash.com/photo-1570194065650-d99fb4b8ccb0?auto=format&fit=crop&w=600&q=80"),
        ],
    },
    {
        "id": "skin_oily",
        "btn_label": {"RU": "✨ Жирная кожа", "KZ": "✨ Майлы тері", "EN": "✨ Oily Skin"},
        "title": {"RU": "✨ Жирная и проблемная кожа", "KZ": "✨ Майлы және проблемалы тері", "EN": "✨ Oily & Blemish-Prone Skin"},
        "subtitle": {"RU": "Сужение пор, контроль блеска и мягкие кислоты", "KZ": "Тесіктерді тарылту және жылтырды бақылау", "EN": "Pore tightening, shine control and gentle acids"},
        "products": [
            p("s7", "Сыворотка Niacinamide 10% + Zinc", "Niacinamide 10% сарысуы", "Niacinamide 10% Serum",
              "Контроль жирного блеска и сужение пор.", "Майлы жылтырды бақылап, тесіктерді тарылтады.", "Controls shine and minimizes pores.",
              "Мощная формула с ниацинамидом и цинком уменьшает выработку себума, осветляет постакне и предотвращает высыпания.",
              "Ниацинамид пен мырыш тері майын азайтып, бөртпелердің алдын алады.",
              "Potent niacinamide & zinc formula reduces excess sebum and fades blemishes.",
              "30 мл", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "24 месяца", "24 ай", "24 months",
              "Ниацинамид 10%, цинк PCA 1%, экстракт чайного дерева", "Ниацинамид 10%, мырыш PCA 1%", "Niacinamide 10%, Zinc PCA 1%, tea tree",
              11500, "https://images.unsplash.com/photo-1617897903246-719242758050?auto=format&fit=crop&w=600&q=80"),
            p("s8", "Тоник BHA Pore Clear", "BHA Pore Clear тонигі", "BHA Pore Clear Toner",
              "Растворяет чёрные точки и очищает поры.", "Қара нүктелерді ерітіп, тесіктерді тазартады.", "Dissolves blackheads and clears pores.",
              "Отшелушивающий тоник с 2% салициловой кислотой глубоко очищает поры без пересушивания кожи.",
              "2% салицил қышқылы бар тоник теріні құрғатпай тесіктерді терең тазартады.",
              "2% salicylic acid exfoliating toner clears pores deeply without over-drying.",
              "150 мл", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "24 месяца", "24 ай", "24 months",
              "Салициловая кислота (BHA) 2%, кора белой ивы", "Салицил қышқылы 2%, ақ тал қабығы", "Salicylic acid 2%, white willow bark",
              10200, "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?auto=format&fit=crop&w=600&q=80"),
            p("s9", "Флюид Matte Balance", "Matte Balance флюиді", "Matte Balance Fluid",
              "Матовая кожа на 10 часов без тяжести.", "Ауырлықсыз 10 сағат бойы күңгірт тері.", "10-hour matte finish without heaviness.",
              "Лёгкий безмасляный флюид увлажняет жирную кожу и оставляет бархатный матовый финиш, идеальный под тон.",
              "Майсыз жеңіл флюид теріні ылғалдандырып, барқыттай күңгірт финиш береді.",
              "Oil-free lightweight fluid hydrates oily skin with a velvety matte finish.",
              "50 мл", "Франция", "Франция", "France", "2026", "30 месяцев", "30 ай", "30 months",
              "Экстракт зелёного чая, бамбуковая пудра, цинк", "Көк шай, бамбук ұнтағы, мырыш", "Green tea extract, bamboo powder, zinc",
              12800, "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?auto=format&fit=crop&w=600&q=80"),
        ],
    },
    {
        "id": "skin_wrinkles",
        "btn_label": {"RU": "🌸 Морщины", "KZ": "🌸 Әжімдерге қарсы", "EN": "🌸 Anti-Wrinkle"},
        "title": {"RU": "🌸 Против морщин и для упругости", "KZ": "🌸 Әжімдерге қарсы және серпімділік", "EN": "🌸 Anti-Wrinkle & Firming"},
        "subtitle": {"RU": "Ретинол, пептиды и заметный лифтинг-эффект", "KZ": "Ретинол, пептидтер және айқын лифтинг әсері", "EN": "Retinol, peptides and visible lifting effect"},
        "products": [
            p("s10", "Сыворотка Retinol Lift 0.5%", "Retinol Lift 0.5% сарысуы", "Retinol Lift 0.5% Serum",
              "Разглаживает мимические морщины.", "Мимикалық әжімдерді тегістейді.", "Smooths fine lines and wrinkles.",
              "Инкапсулированный ретинол стимулирует выработку коллагена, делает кожу плотной, гладкой и обновлённой.",
              "Инкапсуляцияланған ретинол коллаген өндірісін ынталандырып, теріні тегістейді.",
              "Encapsulated retinol boosts collagen production for firmer, smoother skin.",
              "30 мл", "Франция", "Франция", "France", "2026", "24 месяца", "24 ай", "24 months",
              "Ретинол 0.5%, бакучиол, сквалан, витамин E", "Ретинол 0.5%, бакучиол, сквалан", "Retinol 0.5%, bakuchiol, squalane",
              18500, "https://images.unsplash.com/photo-1620916297397-a4a5402a3c6c?auto=format&fit=crop&w=600&q=80"),
            p("s11", "Пептидный крем Peptide Sculpt", "Peptide Sculpt кремі", "Peptide Sculpt Cream",
              "Подтягивает овал лица и укрепляет кожу.", "Бет пішінін тартып, теріні нығайтады.", "Firms facial contours and strengthens skin.",
              "Антивозрастной крем с комплексом из 9 пептидов повышает эластичность и заметно сокращает глубину морщин.",
              "9 пептид кешені бар крем терінің серпімділігін арттырып, әжімдерді азайтады.",
              "Anti-aging cream with 9 peptides improves elasticity and reduces wrinkle depth.",
              "50 мл", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "36 месяцев", "36 ай", "36 months",
              "Комплекс 9 пептидов, коллаген, аденозин", "9 пептид кешені, коллаген, аденозин", "9-Peptide complex, collagen, adenosine",
              19900, "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?auto=format&fit=crop&w=600&q=80"),
            p("s12", "Крем для глаз Eye Youth", "Eye Youth көз кремі", "Eye Youth Eye Cream",
              "Убирает гусиные лапки и тёмные круги.", "Көз айналасындағы әжімдер мен қара дақты азайтады.", "Targets crow's feet and dark circles.",
              "Деликатный лифтинг-крем для зоны вокруг глаз с кофеином и пептидами снимает отёчность и разглаживает кожу.",
              "Кофеин мен пептидтері бар нәзік крем ісінуді басып, көз айналасын тегістейді.",
              "Delicate eye cream with caffeine and peptides de-puffs and smooths fine lines.",
              "20 мл", "Италия", "Италия", "Italy", "2026", "24 месяца", "24 ай", "24 months",
              "Кофеин, матриксил, гиалуроновая кислота", "Кофеин, матриксил, гиалурон қышқылы", "Caffeine, Matrixyl, hyaluronic acid",
              14200, "https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?auto=format&fit=crop&w=600&q=80"),
        ],
    },
]

# 2. ОСНОВНОЙ ОТДЕЛЬНЫЙ КАТАЛОГ КОСМЕТИКИ И АППАРАТОВ
MAIN_CATALOG = [
    {
        "id": "cat_devices",
        "title": {"RU": "01 · Аппараты для чистки лица", "KZ": "01 · Бет тазалау аппараттары", "EN": "01 · Facial Cleansing Devices"},
        "subtitle": {"RU": "Ультразвуковой пилинг, вакуум и лифтинг дома", "KZ": "Ультрадыбыстық пилинг, вакуум және лифтинг", "EN": "Ultrasonic peeling, pore vacuum and lifting"},
        "products": [
            FLAGSHIP_DEVICE,
            p("d2", "Вакуумный очиститель Pore Vacuum", "Pore Vacuum тазартқышы", "Pore Vacuum Cleanser",
              "Бережное очищение Т-зоны без покраснений.", "Т-аймақты қызарусыз ұқыпты тазалау.", "Gentle T-zone cleansing without redness.",
              "Вакуумный аппарат с 4 сменными насадками и 3 уровнями мощности. Эффективно очищает забитые поры.",
              "4 ауыстырмалы саптамасы және 3 қуат деңгейі бар вакуумдық аппарат.",
              "Vacuum cleanser with 4 heads and 3 suction levels for clogged pores.",
              "4 насадки · 120 г", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "Гарантия 12 мес.", "Кепілдік 12 ай", "12-mo warranty",
              "Аппарат, 4 насадки, фильтры, USB-C", "Аппарат, 4 саптама, сүзгілер", "Device, 4 heads, filters, USB-C",
              19500, "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=600&q=80"),
            p("d3", "LED-массажёр Glow Lift 3-в-1", "Glow Lift 3-в-1 LED-массажері", "Glow Lift 3-in-1 LED",
              "Микротоки + светотерапия для упругости.", "Тері серпімділігіне арналған микроток + LED.", "Microcurrents + LED therapy for firm skin.",
              "Аппарат для домашнего лифтинга: снимает утренние отёки, подтягивает овал лица за 5 минут в день.",
              "Үйдегі лифтинг аппараты: таңғы ісінуді басады, бет пішінін тартады.",
              "Home lifting device: reduces morning puffiness and contours facial lines in 5 min/day.",
              "3 LED-спектра · 110 г", "Япония", "Жапония", "Japan", "2026", "Гарантия 24 мес.", "Кепілдік 24 ай", "24-mo warranty",
              "LED-массажёр, зарядная станция, мешочек", "LED-массажер, станция, қапшық", "LED device, dock, travel pouch",
              32900, "https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?auto=format&fit=crop&w=600&q=80"),
        ],
    },
    {
        "id": "cat_skincare",
        "title": {"RU": "02 · Уход за лицом (6 товаров)", "KZ": "02 · Бет күтімі (6 тауар)", "EN": "02 · Facial Skincare (6 items)"},
        "subtitle": {"RU": "Пенки, сыворотки, кремы, SPF и тонеры", "KZ": "Көбіктер, сарысулар, кремдер және SPF", "EN": "Cleansers, serums, creams, SPF and toners"},
        "products": [
            p("c1", "Сыворотка Hydra Glow", "Hydra Glow сарысуы", "Hydra Glow Serum",
              "Глубокое увлажнение и ровный тон кожи.", "Терең ылғалдандыру және тегіс реңк.", "Deep hydration and even skin tone.",
              "Концентрированная сыворотка мгновенно убирает сухость и возвращает коже естественное сияние без липкости.",
              "Құрғақтықты лезде басатын, жабысқақтықсыз табиғи жарқыл сыйлайтын сарысу.",
              "Concentrated hydrating serum relieves dryness and restores natural glow.",
              "30 мл", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "24 месяца", "24 ай", "24 months",
              "Гиалуроновая кислота 2%, ниацинамид 5%", "Гиалурон 2%, ниацинамид 5%", "Hyaluronic Acid 2%, Niacinamide 5%",
              12500, "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=600&q=80"),
            p("c2", "Крем Velvet Barrier", "Velvet Barrier кремі", "Velvet Barrier Cream",
              "Восстановление и мягкость с церамидами.", "Церамидтермен қалпына келтіру.", "Barrier repair with ceramides.",
              "Нежный барьерный крем укрепляет защитный слой кожи и идеально подходит как база под макияж.",
              "Терінің қорғаныш қабатын нығайтып, макияж астына тамаша негіз болады.",
              "Gentle barrier cream strengthens skin protection and works great under makeup.",
              "50 мл", "Франция", "Франция", "France", "2026", "36 месяцев", "36 ай", "36 months",
              "Церамиды NP/AP, сквалан, масло ши", "Церамидтер NP/AP, сквалан, ши майы", "Ceramides NP/AP, Squalane, Shea Butter",
              14900, "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd?auto=format&fit=crop&w=600&q=80"),
            p("c3", "Тонер Rose Mist", "Rose Mist тонері", "Rose Mist Toner",
              "Освежающий гидролат дамасской розы.", "Дамаск раушанының гидролаты.", "Refreshing Damask rose hydrosol.",
              "Мягкий бесспиртовой тонер выравнивает pH после умывания и подготавливает кожу к крему.",
              "Спиртсіз тонер жуынғаннан кейін pH деңгейін теңестіріп, теріні сергітеді.",
              "Alcohol-free gentle toner balances pH after cleansing and refreshes skin.",
              "150 мл", "Италия", "Италия", "Italy", "2025", "24 месяца", "24 ай", "24 months",
              "Гидролат розы 85%, бетаин, экстракт пиона", "Раушан суы 85%, бетаин, пион", "Rose water 85%, betaine, peony",
              8400, "https://images.unsplash.com/photo-1608248597279-f99d160bfcbc?auto=format&fit=crop&w=600&q=80"),
            p("c4", "Пенка Cloud Cleanser", "Cloud Cleanser көбігі", "Cloud Cleanser Foam",
              "Мягкое умывание без чувства стянутости.", "Тартылусыз жұмсақ жуыну көбігі.", "Gentle cleansing without tightness.",
              "Воздушная пенка с аминокислотами деликатно смывает макияж и загрязнения, сохраняя мягкость кожи.",
              "Аминқышқылды ауадай жеңіл көбік макияж бен кірді ұқыпты тазартады.",
              "Airy amino acid foam gently removes makeup and impurities while keeping skin soft.",
              "150 мл", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "24 месяца", "24 ай", "24 months",
              "Аминокислоты кокоса, экстракт центеллы, ромашка", "Кокос аминқышқылдары, центелла", "Coconut amino acids, centella, chamomile",
              7600, "https://images.unsplash.com/photo-1556228578-8c89e6adf883?auto=format&fit=crop&w=600&q=80"),
            p("c5", "Солнцезащитный флюид SPF 50+", "SPF 50+ күннен қорғау флюиді", "Sun Shield SPF 50+ Fluid",
              "Невидимая защита от солнца без белых следов.", "Ақ із қалдырмайтын күннен қорғаныс.", "Invisible UV protection, zero white cast.",
              "Ультралёгкий SPF-флюид нового поколения надёжно защищает от фотостарения и пигментации каждый день.",
              "Жаңа буынды жеңіл SPF-флюид фотоқартаю мен пигментациядан сенімді қорғайды.",
              "Next-gen ultra-light SPF fluid protects against photoaging and dark spots daily.",
              "50 мл", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "30 месяцев", "30 ай", "30 months",
              "Фотостабильные фильтры, ниацинамид, экстракт риса", "Фототұрақты сүзгілер, күріш", "Photostable UV filters, niacinamide, rice",
              11400, "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=600&q=80"),
            p("c6", "Гидрофильное масло Pure Melt", "Pure Melt гидрофильді майы", "Pure Melt Cleansing Oil",
              "Растворяет стойкий макияж и SPF за 30 сек.", "Төзімді макияж бен SPF-ті 30 сек ерітеді.", "Melts waterproof makeup & SPF in 30 sec.",
              "Шелковистое гидрофильное масло при контакте с водой превращается в нежное молочко и очищает поры.",
              "Сумен жанасқанда жұмсақ сүтке айналып, тесіктерді терең тазартады.",
              "Silky oil transforms into gentle milk with water, dissolving makeup and clearing pores.",
              "200 мл", "Япония", "Жапония", "Japan", "2026", "36 месяцев", "36 ай", "36 months",
              "Масло камелии, миндальное масло, витамин E", "Камелия майы, бадам майы", "Camellia oil, sweet almond oil, vitamin E",
              13200, "https://images.unsplash.com/photo-1601049541289-9b1b7bbbfe19?auto=format&fit=crop&w=600&q=80"),
        ],
    },
    {
        "id": "cat_makeup",
        "title": {"RU": "03 · Макияж (6 товаров)", "KZ": "03 · Макияж (6 тауар)", "EN": "03 · Makeup (6 items)"},
        "subtitle": {"RU": "Тинты, румяна, кушоны, тушь и хайлайтеры", "KZ": "Тинттер, румяна, кушон, тушь және хайлайтер", "EN": "Tints, blushes, cushions, mascara and glow"},
        "products": [
            p("m1", "Тинт для губ Silk Kiss", "Silk Kiss ерін тинті", "Silk Kiss Lip Tint",
              "Бархатный финиш и стойкий оттенок.", "Барқыттай финиш және төзімді реңк.", "Velvet finish and long-lasting tint.",
              "Невесомый тинт с муссовой текстурой не сушит губы и держится до 8 часов.",
              "Ерінді құрғатпайтын, 8 сағатқа дейін сақталатын жеңіл мусс-тинт.",
              "Weightless mousse lip tint that lasts up to 8 hours without drying lips.",
              "6 г", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "24 месяца", "24 ай", "24 months",
              "Масло жожоба, витамин E, гиалурон", "Жожоба майы, E дәрумені", "Jojoba Oil, Vitamin E, Hyaluronic",
              7900, "https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=600&q=80"),
            p("m2", "Румяна Blush Cloud", "Blush Cloud румянасы", "Blush Cloud Cheek",
              "Естественный румянец, тающая текстура.", "Табиғи қызғылт реңк, нәзік текстура.", "Natural flush with a melting texture.",
              "Кремовые румяна легко растушёвываются пальцами, создавая свежий отдохнувший вид.",
              "Саусақпен оңай жағылатын, бетке балғын өң беретін кремді румяна.",
              "Cream blush that blends effortlessly with fingers for a fresh look.",
              "10 г", "Франция", "Франция", "France", "2026", "30 месяцев", "30 ай", "30 months",
              "Сквалан, масло камелии, пигменты", "Сквалан, камелия майы", "Squalane, Camellia Oil, Pigments",
              9500, "https://images.unsplash.com/photo-1596462502278-27bfdc403348?auto=format&fit=crop&w=600&q=80"),
            p("m3", "Хайлайтер Liquid Pearl", "Liquid Pearl хайлайтері", "Liquid Pearl Highlighter",
              "Деликатное влажное сияние кожи.", "Теріге нәзік інжу жарқылын береді.", "Delicate dewy pearl glow.",
              "Жидкий хайлайтер с микрочастицами жемчуга даёт эффект здорового блеска без крупных блёсток.",
              "Ірі жылтырсыз, табиғи әрі сау жарқыл беретін сұйық інжу хайлайтері.",
              "Liquid highlighter with fine pearl particles for a natural healthy glow.",
              "15 мл", "Италия", "Италия", "Italy", "2025", "24 месяца", "24 ай", "24 months",
              "Жемчужная мика, лотос, витамин C", "Інжу микасы, лотос, C дәрумені", "Pearl Mica, Lotus, Vitamin C",
              11200, "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=600&q=80"),
            p("m4", "Кушон Velvet Skin SPF 40", "Velvet Skin кушоны", "Velvet Skin Cushion",
              "Ровный тон без эффекта маски.", "Бетперде әсерінсіз тегіс тон.", "Even coverage without a mask feel.",
              "Увлажняющий кушон перекрывает покраснения, подстраивается под тон кожи и защищает от солнца.",
              "Қызаруды жасырып, тері реңкіне бейімделетін ылғалдандырғыш кушон.",
              "Hydrating cushion covers redness, adapts to skin tone, and protects with SPF 40.",
              "15 г + рефил", "Южная Корея", "Оңтүстік Корея", "South Korea", "2026", "24 месяца", "24 ай", "24 months",
              "Ниацинамид, экстракт центеллы, SPF 40", "Ниацинамид, центелла, SPF 40", "Niacinamide, Centella, SPF 40",
              16800, "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=600&q=80"),
            p("m5", "Тушь Lash Panorama", "Lash Panorama туші", "Lash Panorama Mascara",
              "Объём и удлинение без осыпания.", "Төгілмейтін көлем мен ұзарту.", "Volume and length with zero smudging.",
              "Термостойкая тушь обволакивает каждую ресницу, не отпечатывается и смывается тёплой водой.",
              "Әр кірпікті ұзартып, жылы сумен оңай жуылатын термотөзімді тушь.",
              "Tubing mascara coats every lash, stays smudge-proof, and rinses off with warm water.",
              "9 мл", "Италия", "Италия", "Italy", "2026", "18 месяцев", "18 ай", "18 months",
              "Карнаубский воск, пантенол, касторовое масло", "Карнауб балауызы, пантенол", "Carnauba wax, panthenol, castor oil",
              8700, "https://images.unsplash.com/photo-1631214524020-7e18db9a8f92?auto=format&fit=crop&w=600&q=80"),
            p("m6", "Масло-блеск для губ Gloss Berry", "Gloss Berry ерін майы", "Gloss Berry Lip Oil",
              "Зеркальный глянец и уход за губами.", "Айнадай жылтыр және ерін күтімі.", "Mirror shine with nourishing lip care.",
              "Нелипкое масло-блеск с ягодным ароматом питает губы и визуально придаёт им объём.",
              "Жабыспайтын жидек хош иісті май-жылтыратқыш ерінге көлем береді.",
              "Non-sticky berry-scented lip oil nourishes lips with a plumping mirror shine.",
              "7 мл", "Франция", "Франция", "France", "2026", "24 месяца", "24 ай", "24 months",
              "Масло малиновой косточки, витамин E, сквалан", "Таңқурай майы, E дәрумені", "Raspberry seed oil, vitamin E, squalane",
              7400, "https://images.unsplash.com/photo-1599305090598-fe179d501227?auto=format&fit=crop&w=600&q=80"),
        ],
    },
    {
        "id": "cat_perfume",
        "title": {"RU": "04 · Парфюмерия", "KZ": "04 · Парфюмерия", "EN": "04 · Fragrance"},
        "subtitle": {"RU": "Нишевые и шлейфовые ароматы", "KZ": "Нишалық және ұзақ сақталатын иіссулар", "EN": "Niche and long-lasting scents"},
        "products": [
            p("f1", "Amber Noir EDP", "Amber Noir EDP", "Amber Noir EDP",
              "Тёплая амбра, инжир и кашмирское дерево.", "Жылы амбра, інжір және кашмир ағашы.", "Warm amber, black fig and cashmere wood.",
              "Глубокий вечерний аромат с мягким бархатным шлейфом спелого инжира и тёплой амбры.",
              "Жұмсақ шлейфі бар терең кешкі хош иіс. Қара інжір мен жылы амбра үйлесімі.",
              "Deep evening fragrance with a velvety trail of ripe black fig and warm amber.",
              "50 мл", "Франция (Грасс)", "Франция (Грасс)", "France (Grasse)", "2026", "60 месяцев", "60 ай", "60 months",
              "Верх: инжир; Сердце: амбра; База: кашмир", "Інжір, амбра, кашмир ағашы", "Fig, Amber, Cashmere Wood",
              34500, "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80"),
            p("f2", "White Tea EDP", "White Tea EDP", "White Tea EDP",
              "Свежий белый чай, бергамот и мускус.", "Ақ шай, бергамот және ақ мускус.", "Fresh white tea, bergamot and musk.",
              "Лёгкий повседневный парфюм с ощущением чистоты и утренней свежести.",
              "Таңғы тазалық пен балғындық сезімін сыйлайтын күнделікті жеңіл парфюм.",
              "Light everyday perfume evoking crisp morning freshness.",
              "50 мл", "Италия", "Италия", "Italy", "2025", "60 месяцев", "60 ай", "60 months",
              "Бергамот, белый чай, жасмин, белый мускус", "Бергамот, ақ шай, мускус", "Bergamot, White Tea, White Musk",
              29800, "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=600&q=80"),
            p("f3", "Дымка Vanilla Silk", "Vanilla Silk мисті", "Vanilla Silk Mist",
              "Мадагаскарская ваниль и нежный сандал.", "Мадагаскар ванилі және нәзік сандал.", "Madagascar vanilla and soft sandalwood.",
              "Парфюмированный мист для тела и волос с деликатной сладостью ванили.",
              "Дене мен шашқа арналған нәзік ваниль хош иісті ылғалдандырғыш мист.",
              "Perfumed body and hair mist with delicate vanilla sweetness.",
              "100 мл", "Франция", "Франция", "France", "2026", "36 месяцев", "36 ай", "36 months",
              "Ваниль, сандаловое масло, пантенол", "Ваниль, сандал майы, пантенол", "Vanilla, Sandalwood Oil, Panthenol",
              13500, "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?auto=format&fit=crop&w=600&q=80"),
        ],
    },
]

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
            f"<div style='font-size:22px; font-weight:700; color:#8A5A3E; margin-bottom:10px;'>{product['price']:,} ₸</div>".replace(",", " "),
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


@st.dialog(t["dev_cert_modal"], width="large")
def show_device_certificate():
    st.markdown(f"### {t['dev_name']}")
    st.write("✅ Декларация соответствия ЕАЭС № ЕАЭС N RU Д-KR.РА01.В.44912/26")
    st.write("✅ Международная сертификация безопасности CE / RoHS / KC (Южная Корея)")
    st.write("✅ Дерматологическое тестирование: одобрено для домашнего использования")
    st.markdown(
        """
        <div style="margin-top:16px; padding:22px; border:2px dashed #9C6B4E; border-radius:14px; background:#F6EFE5; text-align:center;">
            <div style="font-family:'Cormorant Garamond', serif; font-size:26px; font-weight:700; color:#5C3D2B;">OFFICIAL QUALITY CERTIFICATE</div>
            <div style="font-size:13px; color:#6E5B50; margin-top:6px;">Ultrasonic Facial Cleansing Device · Velour Sonic Pro (28 kHz)</div>
            <div style="font-size:15px; font-weight:700; color:#2E241F; margin-top:10px;">EAC / CE / KC Approved · Reg #KR-2026-99401</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


@st.dialog(t["cert_modal"], width="large")
def show_certificate(spec):
    st.markdown(f"### {spec['name']}")
    st.markdown(f"**{spec['role'][lang]}**")
    st.divider()
    for item in spec["education"][lang]:
        st.markdown(f"✅ {item}")
    st.markdown(
        """
        <div style="margin-top:16px; padding:20px; border:2px dashed #9C6B4E; border-radius:14px; background:#F6EFE5; text-align:center;">
            <div style="font-family:'Cormorant Garamond', serif; font-size:26px; font-weight:700; color:#5C3D2B;">CERTIFICATE OF EXCELLENCE</div>
            <div style="font-size:13px; color:#6E5B50; margin-top:6px;">Esthetic Pro Europe · Hardware Cosmetology & Dermatology</div>
            <div style="font-size:15px; font-weight:700; color:#2E241F; margin-top:10px;">Amina Nurlanova · ID #KZ-88412</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_catalog_block(categories):
    for category in categories:
        st.markdown(f'<div id="anchor_{category["id"]}"></div>', unsafe_allow_html=True)
        is_open = st.session_state.active_cat == category["id"]
        with st.expander(f"**{category['title'][lang]}**  —  {category['subtitle'][lang]}", expanded=is_open):
            products = category["products"]
            for row_start in range(0, len(products), 3):
                row_items = products[row_start:row_start + 3]
                cols = st.columns(3, gap="medium")
                for i, product in enumerate(row_items):
                    with cols[i]:
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
                st.write("")


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

# 2. ВЫБОР ТИПА КОЖИ СВЕРХУ (НАД ХИТОМ СЕЗОНА)
st.markdown(f'<div class="skin-nav-label">{t["skin_nav_title"]}</div>', unsafe_allow_html=True)
skin_btn_cols = st.columns(4, gap="small")
for idx_sk, sk_cat in enumerate(SKIN_CATALOG):
    with skin_btn_cols[idx_sk]:
        is_selected = st.session_state.active_cat == sk_cat["id"]
        if st.button(
            sk_cat["btn_label"][lang],
            key=f"jump_{sk_cat['id']}",
            type="primary" if is_selected else "secondary",
            use_container_width=True,
        ):
            st.session_state.active_cat = sk_cat["id"]
            st.session_state.scroll_to = f"anchor_{sk_cat['id']}"
            st.rerun()

# 3. HERO-БАННЕР (ХИТ СЕЗОНА)
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

# 4. ОТДЕЛЬНЫЙ БЛОК: АППАРАТ ДЛЯ ЧИСТКИ ЛИЦА + СЕРТИФИКАТ
st.markdown(f'<div class="section-heading">{t["dev_section"]}</div>', unsafe_allow_html=True)
dev_col1, dev_col2 = st.columns([1, 1.5], gap="large")
with dev_col1:
    st.markdown(
        f'<img src="{FLAGSHIP_DEVICE["img"]}" style="width:100%; height:290px; object-fit:cover; border-radius:18px; border:1px solid rgba(156,107,78,0.28);">',
        unsafe_allow_html=True,
    )
with dev_col2:
    st.markdown(
        f"""
        <div class="device-showcase">
            <span class="hero-tag">{t['dev_badge']}</span>
            <div style="font-family:'Cormorant Garamond', serif; font-size:30px; font-weight:700; color:#2E241F; margin-bottom:8px;">
                {t['dev_name']}
            </div>
            <p style="font-size:14px; color:#635147; line-height:1.5; margin-bottom:10px;">{t['dev_desc']}</p>
            <p style="font-size:13px; color:#5C473B; line-height:1.6; white-space:pre-line; margin-bottom:0;">{t['dev_specs']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    db1, db2 = st.columns(2, gap="small")
    with db1:
        if st.button(f"📜 {t['dev_cert_btn']}", key="dev_cert_open", type="secondary", use_container_width=True):
            show_device_certificate()
    with db2:
        if st.button(t["dev_add_btn"], key="dev_buy_now", type="primary", use_container_width=True):
            add_to_cart(FLAGSHIP_DEVICE)
            st.toast(f"{t['added_toast']} {FLAGSHIP_DEVICE['name'][lang]}")

# 5. ОТДЕЛЬНЫЙ КАТАЛОГ ПО ТИПАМ КОЖИ
st.markdown(f'<div class="section-heading">{t["skin_cat_title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="section-sub">{t["skin_cat_sub"]}</div>', unsafe_allow_html=True)
render_catalog_block(SKIN_CATALOG)

# 6. ОТДЕЛЬНЫЙ ОСНОВНОЙ КАТАЛОГ КОСМЕТИКИ И АППАРАТОВ
st.markdown(f'<div class="section-heading">{t["main_cat_title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="section-sub">{t["main_cat_sub"]}</div>', unsafe_allow_html=True)
render_catalog_block(MAIN_CATALOG)

# 7. СПЕЦИАЛИСТЫ (1 ГЛАВНЫЙ + 2 КОЛЛЕГИ)
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

# 8. АДРЕС И КАРТА (САТТАРХАНОВА 5)
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
            <p style="font-size:14px; color:#756054;">Instagram: @velour.beauty.kz</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with addr_col2:
    components.html(
        """
        <div style="border-radius:18px; overflow:hidden; border:1px solid rgba(156,107,78,0.3); box-shadow:0 8px 24px rgba(92,68,52,0.08);">
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

# 9. ПОПУЛЯРНЫЕ ВОПРОСЫ (FAQ)
st.markdown(f'<div class="section-heading">{t["faq_title"]}</div>', unsafe_allow_html=True)
for item_faq in FAQ_LIST:
    with st.expander(f"**{item_faq['q'][lang]}**", expanded=False):
        st.write(item_faq["a"][lang])

# 10. ПЛАВНАЯ ПРОКРУТКА К ВЫБРАННОМУ ТИПУ КОЖИ
if st.session_state.scroll_to:
    target_id = st.session_state.scroll_to
    components.html(
        f"""
        <script>
            setTimeout(function() {{
                const el = window.parent.document.getElementById("{target_id}");
                if (el) {{
                    el.scrollIntoView({{ behavior: "smooth", block: "start" }});
                }}
            }}, 150);
        </script>
        """,
        height=0,
    )
    st.session_state.scroll_to = None

# 11. БОКОВАЯ ПАНЕЛЬ — КОРЗИНА С МЫЛЬНЫМИ ПУЗЫРЯМИ И ПРОМОКОДОМ
with st.sidebar:
    st.markdown(
        """
        <div class="bubbles-layer">
            <div class="bubble b1"></div><div class="bubble b2"></div>
            <div class="bubble b3"></div><div class="bubble b4"></div>
            <div class="bubble b5"></div><div class="bubble b6"></div>
            <div class="bubble b7"></div><div class="bubble b8"></div>
            <div class="bubble b9"></div><div class="bubble b10"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f"## 🫧 {t['cart_title']}")

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
                        <span style="font-size:13px; color:#756054;">
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
