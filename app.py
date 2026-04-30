import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="СетьБезОбид", page_icon="🛡️", layout="centered")

# ========== ФОН С ХАОТИЧНЫМИ КАРТИНКАМИ ==========
# Список картинок для фона
bg_icons = [
    "https://cdn-icons-png.flaticon.com/512/754/754179.png",   # щит
    "https://cdn-icons-png.flaticon.com/512/420/420425.png",   # замок
    "https://cdn-icons-png.flaticon.com/512/2331/2331228.png", # хакер
    "https://cdn-icons-png.flaticon.com/512/1185/1185933.png", # ссылка
    "https://cdn-icons-png.flaticon.com/512/3095/3095201.png", # телефон
    "https://cdn-icons-png.flaticon.com/512/709/709649.png",   # предупреждение
    "https://cdn-icons-png.flaticon.com/512/5666/5666987.png", # deepfake
    "https://cdn-icons-png.flaticon.com/512/2826/2826774.png"  # закон
]

# Генерируем CSS с хаотичными картинками
random_css = ""
positions = []
for i in range(25):  # 25 случайных картинок на фоне
    img = random.choice(bg_icons)
    x = random.randint(0, 95)
    y = random.randint(0, 95)
    size = random.randint(30, 80)
    rot = random.randint(-30, 30)
    opacity = random.uniform(0.1, 0.35)
    positions.append(f"""
    .stApp::before {{
        content: "";
        position: fixed;
        top: {y}%;
        left: {x}%;
        width: {size}px;
        height: {size}px;
        background: url('{img}') no-repeat center;
        background-size: contain;
        opacity: {opacity};
        transform: rotate({rot}deg);
        pointer-events: none;
        z-index: 0;
    }}
    """)

# Объединяем стили
st.markdown(f"""
<style>
    /* Основной фон */
    .stApp {{
        background: linear-gradient(135deg, #0a0f1e 0%, #0d1b2a 30%, #1b263b 70%, #0a0f1e 100%);
    }}
    
    /* Хаотичные картинки */
    {''.join(positions)}
    
    /* Контейнер с контентом (поверх фона) */
    .main .block-container {{
        background: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(3px);
        border-radius: 25px;
        padding: 25px;
        border: 1px solid rgba(0, 255, 255, 0.3);
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.1);
        z-index: 10;
        position: relative;
    }}
    
    /* Заголовки */
    h1, h2, h3 {{
        color: #00ffff !important;
        font-family: 'Courier New', monospace !important;
        text-shadow: 0 0 10px #00ffff, 0 0 20px #0088ff;
        letter-spacing: 2px;
    }}
    
    h1 {{
        font-size: 3rem !important;
        border-bottom: 2px solid #00ffff;
        display: inline-block;
        padding-bottom: 5px;
    }}
    
    /* Текст */
    p, li, .stMarkdown, .stCaption {{
        color: #ccddff !important;
        font-family: 'Segoe UI', 'Roboto', sans-serif !important;
        font-size: 16px;
    }}
    
    /* Кнопки */
    .stButton > button {{
        background: linear-gradient(90deg, #00ccff, #0066ff);
        color: #000;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        transition: all 0.3s;
        font-family: 'Courier New', monospace;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    
    .stButton > button:hover {{
        transform: scale(1.02);
        box-shadow: 0 0 15px #00ccff;
        background: linear-gradient(90deg, #0066ff, #00ccff);
    }}
    
    /* Боковое меню */
    [data-testid="stSidebar"] {{
        background: rgba(10, 20, 40, 0.95);
        border-right: 1px solid #00ffff;
    }}
    
    [data-testid="stSidebar"] * {{
        color: #00ffff !important;
        font-family: 'Courier New', monospace;
    }}
    
    .stRadio > div {{
        background: rgba(0, 255, 255, 0.1);
        border-radius: 10px;
        padding: 10px;
    }}
    
    /* Инфо-блоки */
    .info-box {{
        background: rgba(0, 255, 255, 0.1);
        border-left: 4px solid #00ffff;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }}
    
    /* Стикеры */
    .sticker-grid {{
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        justify-content: center;
    }}
    
    .sticker-card {{
        background: rgba(0, 0, 0, 0.6);
        border: 1px solid #00ffff;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        width: 110px;
        transition: all 0.3s;
        backdrop-filter: blur(5px);
    }}
    
    .sticker-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 0 20px #00ffff;
        border-color: #00ffff;
    }}
    
    .sticker-img {{
        width: 55px;
        height: 55px;
        margin-bottom: 10px;
    }}
    
    .sticker-name {{
        color: #00ffff;
        font-weight: bold;
        font-size: 11px;
        font-family: 'Courier New', monospace;
    }}
    
    /* Картинки в меню */
    .menu-icon {{
        width: 24px;
        margin-right: 10px;
        vertical-align: middle;
    }}
</style>
""", unsafe_allow_html=True)

# ========== ФУНКЦИЯ ДЛЯ КАРТИНОК ==========
def img_tag(url, width=24):
    return f'<img src="{url}" style="width: {width}px; margin-right: 8px; vertical-align: middle;">'

# ========== ЗАГОЛОВОК С КАРТИНКОЙ ==========
st.markdown('<h1><img src="https://cdn-icons-png.flaticon.com/512/754/754179.png" style="width: 50px; vertical-align: middle;"> СетьБезОбид</h1>', unsafe_allow_html=True)
st.markdown("*Твоя безопасная сеть без мошенников*")
st.markdown("---")

# ========== МЕНЮ С КАРТИНКАМИ =========()
menu_icons = {
    "Проверь ссылку": "https://cdn-icons-png.flaticon.com/512/1185/1185933.png",
    "Челлендж дня": "https://cdn-icons-png.flaticon.com/512/2121/2121514.png",
    "Распознай дипфейк": "https://cdn-icons-png.flaticon.com/512/5666/5666987.png",
    "Твои права в сети": "https://cdn-icons-png.flaticon.com/512/2826/2826774.png",
    "Стикер-пак": "https://cdn-icons-png.flaticon.com/512/3159/3159312.png"
}

menu_display = [f'{img_tag(menu_icons[k])}{k}' for k in menu_icons.keys()]
selected = st.sidebar.radio("МЕНЮ", menu_display, format_func=lambda x: x)
# Очищаем HTML для сравнения
clean_selected = selected.split('>')[-1].split('<')[0] if '>' in selected else selected

# ========== 1. ПРОВЕРКА ССЫЛКИ ==========
if "Проверь ссылку" in clean_selected:
    st.header(f"{img_tag('https://cdn-icons-png.flaticon.com/512/1185/1185933.png', 30)} Проверь ссылку", unsafe_allow_html=True)
    st.markdown('<div class="info-box">Вставь ссылку — система проверит её на фишинг</div>', unsafe_allow_html=True)
    
    suspicious = ["login", "verify", "secure", "update", "confirm", "bank", "paypal", "password"]
    link = st.text_input("Вставь ссылку:")
    
    if link:
        if any(w in link.lower() for w in suspicious):
            st.error("🚨 ФИШИНГ! Не переходи!")
        else:
            st.success("✅ Ссылка безопасна")

# ========== 2. ЧЕЛЛЕНДЖ ==========
elif "Челлендж дня" in clean_selected:
    st.header(f"{img_tag('https://cdn-icons-png.flaticon.com/512/2121/2121514.png', 30)} Челлендж дня", unsafe_allow_html=True)
    
    q = {
        "question": "Тебе звонят из «банка» и просят код из SMS. Твои действия?",
        "options": ["Назову код", "Положу трубку и сам позвоню в банк"],
        "correct": "Положу трубку и сам позвоню в банк",
        "explanation": "Банки никогда не просят код из SMS!"
    }
    
    st.markdown(f"**{q['question']}**")
    ans = st.radio("", q["options"])
    if st.button("Проверить"):
        if ans == q["correct"]:
            st.balloons()
            st.success(q["explanation"])
        else:
            st.error("Неправильно! " + q["explanation"])

# ========== 3. ДИПФЕЙК ==========
elif "Распознай дипфейк" in clean_selected:
    st.header(f"{img_tag('https://cdn-icons-png.flaticon.com/512/5666/5666987.png', 30)} Дипфейк детектор", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <b>5 признаков дипфейка:</b><br>
    1. Странное моргание<br>
    2. Губы не совпадают со звуком<br>
    3. Неправильные тени<br>
    4. Роботизированный голос<br>
    5. Размытые края
    </div>
    """, unsafe_allow_html=True)

# ========== 4. ПРАВА ==========
elif "Твои права в сети" in clean_selected:
    st.header(f"{img_tag('https://cdn-icons-png.flaticon.com/512/2826/2826774.png', 30)} Твои права в сети", unsafe_allow_html=True)
    st.markdown("""
    **По законодательству РБ:**<br><br>
    ✅ Не давать данные незнакомцам<br>
    ✅ Сообщить в милицию (102)<br>
    ✅ Удалить свои данные с сайта<br>
    ⚠️ Не заниматься кибербуллингом
    """)

# ========== 5. СТИКЕРЫ ==========
elif "Стикер-пак" in clean_selected:
    st.header(f"{img_tag('https://cdn-icons-png.flaticon.com/512/3159/3159312.png', 30)} Стикер-пак", unsafe_allow_html=True)
    
    stickers = [
        {"img": "https://cdn-icons-png.flaticon.com/512/754/754179.png", "name": "Щит", "desc": "Защита"},
        {"img": "https://cdn-icons-png.flaticon.com/512/709/709649.png", "name": "Фишинг", "desc": "Осторожно"},
        {"img": "https://cdn-icons-png.flaticon.com/512/2331/2331228.png", "name": "Хакер", "desc": "Не вышло"},
        {"img": "https://cdn-icons-png.flaticon.com/512/420/420425.png", "name": "Пароль", "desc": "Тайна"},
        {"img": "https://cdn-icons-png.flaticon.com/512/1185/1185933.png", "name": "Ссылка", "desc": "Проверь"},
        {"img": "https://cdn-icons-png.flaticon.com/512/3095/3095201.png", "name": "Банк", "desc": "Клади трубку"},
        {"img": "https://cdn-icons-png.flaticon.com/512/5666/5666987.png", "name": "Deepfake", "desc": "Не верь"},
        {"img": "https://cdn-icons-png.flaticon.com/512/2826/2826774.png", "name": "Закон", "desc": "#КиберПраво"}
    ]
    
    cols = st.columns(4)
    for i, s in enumerate(stickers):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="sticker-card">
                <img src="{s['img']}" class="sticker-img">
                <div class="sticker-name">{s['name']}</div>
                <small style="color:#88aaff;">{s['desc']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    st.info("📌 Нажми правой кнопкой на стикер → Сохранить картинку")

# ========== ПОДВАЛ ==========
st.markdown("---")
st.caption("🏆 Конкурс #КиберПраво 2026 | СетьБезОбид")
