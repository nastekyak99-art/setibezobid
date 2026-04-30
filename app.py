import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="СетьБезОбид", page_icon="🛡️", layout="centered")

# ========== СПИСОК РАБОЧИХ КАРТИНОК ==========
# (только проверенные, стабильные ссылки)
safe_icons = [
    "https://cdn-icons-png.flaticon.com/512/754/754179.png",   # щит
    "https://cdn-icons-png.flaticon.com/512/420/420425.png",   # замок
    "https://cdn-icons-png.flaticon.com/512/2331/2331228.png", # хакер
    "https://cdn-icons-png.flaticon.com/512/1185/1185933.png", # ссылка
    "https://cdn-icons-png.flaticon.com/512/3095/3095201.png", # телефон
    "https://cdn-icons-png.flaticon.com/512/709/709649.png",   # предупреждение
    "https://cdn-icons-png.flaticon.com/512/2826/2826774.png"  # закон
]

# Генерируем хаотичные картинки на фоне
bg_css = ""
for _ in range(20):  # 20 случайных иконок
    img = random.choice(safe_icons)
    x = random.randint(0, 90)
    y = random.randint(0, 90)
    size = random.randint(35, 85)
    rot = random.randint(-25, 25)
    op = random.uniform(0.08, 0.25)
    bg_css += f"""
    .stApp::before {{
        content: "";
        position: fixed;
        top: {y}%;
        left: {x}%;
        width: {size}px;
        height: {size}px;
        background: url('{img}') no-repeat center;
        background-size: contain;
        opacity: {op};
        transform: rotate({rot}deg);
        pointer-events: none;
        z-index: 0;
    }}
    """

st.markdown(f"""
<style>
    /* Основной фон */
    .stApp {{
        background: linear-gradient(135deg, #0a0f1e 0%, #0d1b2a 50%, #1b263b 100%);
    }}
    
    /* Хаотичные иконки */
    {bg_css}
    
    /* Контейнер с контентом */
    .main .block-container {{
        background: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(4px);
        border-radius: 25px;
        padding: 25px;
        border: 1px solid #00ccff;
        position: relative;
        z-index: 10;
    }}
    
    /* Заголовки */
    h1, h2, h3 {{
        color: #00ccff !important;
        font-family: 'Courier New', monospace !important;
        text-shadow: 0 0 8px #00ccff;
    }}
    
    h1 {{
        border-bottom: 2px solid #00ccff;
        display: inline-block;
    }}
    
    /* Текст */
    p, li, .stMarkdown, .stCaption {{
        color: #e0e0ff !important;
        font-size: 16px;
    }}
    
    /* Кнопки */
    .stButton > button {{
        background: linear-gradient(90deg, #00ccff, #0066aa);
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 8px 20px;
        border: none;
        transition: 0.2s;
    }}
    
    .stButton > button:hover {{
        transform: scale(1.02);
        box-shadow: 0 0 12px #00ccff;
    }}
    
    /* Боковое меню */
    [data-testid="stSidebar"] {{
        background: rgba(10, 20, 40, 0.95);
        border-right: 1px solid #00ccff;
    }}
    
    [data-testid="stSidebar"] * {{
        color: #00ccff !important;
        font-family: 'Courier New', monospace;
    }}
    
    .stRadio > div {{
        background: rgba(0, 204, 255, 0.1);
        border-radius: 10px;
        padding: 8px;
    }}
    
    /* Инфо-блоки */
    .info-box {{
        background: rgba(0, 204, 255, 0.1);
        border-left: 4px solid #00ccff;
        border-radius: 10px;
        padding: 12px;
        margin: 10px 0;
    }}
    
    /* Стикеры */
    .sticker-grid {{
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        justify-content: center;
    }}
    
    .sticker-card {{
        background: rgba(0, 0, 0, 0.6);
        border: 1px solid #00ccff;
        border-radius: 15px;
        padding: 12px;
        text-align: center;
        width: 100px;
        transition: 0.2s;
    }}
    
    .sticker-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 0 15px #00ccff;
    }}
    
    .sticker-img {{
        width: 50px;
        height: 50px;
        margin-bottom: 8px;
    }}
    
    .sticker-name {{
        color: #00ccff;
        font-weight: bold;
        font-size: 11px;
    }}
</style>
""", unsafe_allow_html=True)

# ========== ХЭЛПЕР ДЛЯ КАРТИНОК ==========
def icon_html(url, size=24):
    return f'<img src="{url}" style="width: {size}px; margin-right: 8px; vertical-align: middle;">'

# ========== ЗАГОЛОВОК ==========
st.markdown(f'<h1>{icon_html(safe_icons[0], 45)} СетьБезОбид</h1>', unsafe_allow_html=True)
st.markdown("*Твоя безопасная сеть без мошенников*")
st.markdown("---")

# ========== МЕНЮ С ИКОНКАМИ ==========
menu_items = {
    "Проверь ссылку": safe_icons[3],
    "Челлендж дня": safe_icons[2],
    "Распознай дипфейк": safe_icons[6],
    "Твои права в сети": safe_icons[1],
    "Стикер-пак": safe_icons[4]
}

menu_display = [f'{icon_html(menu_items[k])}{k}' for k in menu_items.keys()]
selected_raw = st.sidebar.radio("МЕНЮ", menu_display, format_func=lambda x: x)

# Определяем выбранный пункт
selected = ""
for k in menu_items.keys():
    if k in selected_raw:
        selected = k
        break

# ========== 1. ПРОВЕРКА ССЫЛКИ ==========
if selected == "Проверь ссылку":
    st.markdown(f'{icon_html(menu_items["Проверь ссылку"], 30)} **Проверь ссылку**', unsafe_allow_html=True)
    st.markdown('<div class="info-box">Вставь ссылку — проверим на фишинг</div>', unsafe_allow_html=True)
    
    suspicious = ["login", "verify", "secure", "update", "confirm", "bank", "paypal", "password"]
    link = st.text_input("Вставь ссылку:")
    
    if link:
        if any(w in link.lower() for w in suspicious):
            st.error("🚨 ВНИМАНИЕ! Это похоже на ФИШИНГ! Не переходи.")
        else:
            st.success("✅ Ссылка выглядит безопасно. Но всегда будь внимателен!")

# ========== 2. ЧЕЛЛЕНДЖ ==========
elif selected == "Челлендж дня":
    st.markdown(f'{icon_html(menu_items["Челлендж дня"], 30)} **Челлендж дня**', unsafe_allow_html=True)
    
    questions = [
        ("Тебе звонят из «банка» и просят код из SMS", "Положу трубку и сам позвоню в банк"),
        ("Друг в Telegram просит код подтверждения", "Позвоню другу и спрошу"),
        ("Пришло письмо: «Твой аккаунт взломали, перейди по ссылке»", "Не переходить, проверить отправителя")
    ]
    
    idx = random.randint(0, 2)
    q_text, correct = questions[idx]
    
    st.markdown(f"**{q_text}**")
    ans = st.radio("Твой выбор:", ["Назову код/перейду", correct])
    
    if st.button("Проверить"):
        if ans == correct:
            st.balloons()
            st.success("✅ Молодец! Это правильный ответ.")
        else:
            st.error("❌ Ошибка! " + correct)

# ========== 3. ДИПФЕЙК ==========
elif selected == "Распознай дипфейк":
    st.markdown(f'{icon_html(menu_items["Распознай дипфейк"], 30)} **Распознай дипфейк**', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
    <b>5 признаков дипфейка:</b><br>
    1. 👁️ Странное моргание (слишком редкое или частое)<br>
    2. 👄 Губы не совпадают со звуком<br>
    3. 🌑 Неправильные тени на лице<br>
    4. 🤖 Роботизированный голос без эмоций<br>
    5. 🔄 Размытые края вокруг лица
    </div>
    """, unsafe_allow_html=True)

# ========== 4. ПРАВА ==========
elif selected == "Твои права в сети":
    st.markdown(f'{icon_html(menu_items["Твои права в сети"], 30)} **Твои права в сети**', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
    <b>По законодательству Республики Беларусь:</b><br><br>
    ✅ Право не давать свои данные незнакомцам<br>
    ✅ Право удалить свои данные с сайта<br>
    ✅ Право сообщить в милицию (102)<br>
    ⚠️ Обязанность не заниматься кибербуллингом
    </div>
    """, unsafe_allow_html=True)

# ========== 5. СТИКЕРЫ ==========
elif selected == "Стикер-пак":
    st.markdown(f'{icon_html(menu_items["Стикер-пак"], 30)} **Стикер-пак #КиберПраво**', unsafe_allow_html=True)
    
    sticker_list = [
        (safe_icons[0], "Щит", "Защита активирована"),
        (safe_icons[5], "Фишинг", "Не клюй!"),
        (safe_icons[2], "Хакер", "Не вышло!"),
        (safe_icons[1], "Пароль", "Твоя тайна"),
        (safe_icons[3], "Ссылка", "Проверь перед переходом"),
        (safe_icons[4], "Звонок", "Из банка? Клади трубку"),
        (safe_icons[6], "Права", "Знай свои права")
    ]
    
    cols = st.columns(3)
    for i, (img, name, desc) in enumerate(sticker_list):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="sticker-card">
                <img src="{img}" class="sticker-img">
                <div class="sticker-name">{name}</div>
                <small style="color:#aaa;">{desc}</small>
            </div>
            """, unsafe_allow_html=True)
    
    st.info("📌 Кликни правой кнопкой мыши на стикер → Сохрани картинку")
    st.markdown("**Хэштеги:** #СетьБезОбид #КиберПраво")

# ========== ПОДВАЛ ==========
st.markdown("---")
st.caption("🏆 Конкурс #КиберПраво 2026 | СетьБезОбид | Защити себя от кибермошенников")
