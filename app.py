import streamlit as st
import random
from datetime import datetime

# ========== НАСТРОЙКА СТРАНИЦЫ ==========
st.set_page_config(
    page_title="СетьБезОбид",
    page_icon="🛡️",
    layout="centered"
)

# ========== КАСТОМНЫЙ CSS ==========
st.markdown("""
<style>
    /* Фон с картинкой интернет-сети */
    .stApp {
        background: url('https://www.transparenttextures.com/patterns/hexellence.png'), 
                    linear-gradient(135deg, #0a0a2a 0%, #1a1a3e 50%, #0d0d2b 100%);
        background-attachment: fixed;
    }
    
    /* Контент поверх фона */
    .main .block-container {
        background: rgba(0, 0, 0, 0.6);
        border-radius: 20px;
        padding: 20px;
        backdrop-filter: blur(2px);
    }
    
    /* Заголовки */
    h1, h2, h3 {
        color: #ff6b35 !important;
        font-family: 'Segoe UI Black', 'Impact', sans-serif !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* Текст */
    p, li, .stMarkdown, .stCaption {
        color: #f0f0f0 !important;
        font-family: 'Segoe UI', sans-serif !important;
        font-size: 16px;
    }
    
    /* Кнопки */
    .stButton > button {
        background: linear-gradient(90deg, #ff6b35, #f7931e);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 30px;
        padding: 10px 24px;
        border: none;
        transition: transform 0.2s;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #f7931e, #ff6b35);
        cursor: pointer;
    }
    
    /* Боковое меню */
    [data-testid="stSidebar"] {
        background: rgba(15, 12, 41, 0.95);
    }
    
    [data-testid="stSidebar"] * {
        color: #ff6b35 !important;
    }
    
    /* Radio buttons в меню */
    .stRadio > div {
        background: rgba(255, 107, 53, 0.2);
        border-radius: 15px;
        padding: 10px;
    }
    
    /* Информационные блоки */
    .info-box {
        background: rgba(255, 107, 53, 0.2);
        border-left: 5px solid #ff6b35;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    
    /* Блоки success/error/warning */
    .stAlert {
        border-radius: 15px;
    }
    
    /* Стикеры */
    .sticker-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        justify-content: center;
        margin-top: 20px;
    }
    
    .sticker-card {
        background: linear-gradient(145deg, #2a235a, #1a1542);
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        width: 120px;
        transition: transform 0.3s;
        cursor: pointer;
    }
    
    .sticker-card:hover {
        transform: translateY(-5px);
    }
    
    .sticker-img {
        width: 60px;
        height: 60px;
        margin-bottom: 10px;
    }
    
    .sticker-name {
        color: #ff6b35;
        font-weight: bold;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ========== ЗАГОЛОВОК ==========
st.title("🛡️ СетьБезОбид")
st.markdown("*Твоя безопасная сеть без мошенников и обид*")
st.markdown("---")

# ========== БОКОВОЕ МЕНЮ ==========
menu = st.sidebar.radio(
    "📱 **МЕНЮ**",
    ["🔍 Проверь ссылку", "⚡ Челлендж дня", "🎭 Распознай дипфейк", "📜 Твои права в сети", "😎 Стикер-пак"]
)

# ========== 1. ПРОВЕРКА ССЫЛКИ ==========
if menu == "🔍 Проверь ссылку":
    st.header("🔍 Проверь ссылку")
    st.markdown('<div class="info-box">Вставь ссылку — система проверит её на фишинг</div>', unsafe_allow_html=True)
    
    suspicious_words = ["login", "verify", "secure", "update", "confirm", "bank", "paypal", "password", "account"]
    suspicious_domains = ["bit.ly", "tinyurl", "goo.gl", "rb.ly", "clck.ru"]
    
    link = st.text_input("🌐 Вставь ссылку:")
    
    if link:
        link_lower = link.lower()
        found_words = [w for w in suspicious_words if w in link_lower]
        found_domains = [d for d in suspicious_domains if d in link_lower]
        
        if found_words or found_domains:
            st.error("🚨 ВНИМАНИЕ! Это похоже на ФИШИНГ!")
            st.info("💡 Совет: никогда не переходи по подозрительным ссылкам!")
        else:
            st.success("✅ Ссылка выглядит безопасно")
            st.info("💡 Даже хорошие сайты могут подделать — проверяй адрес!")

# ========== 2. ЧЕЛЛЕНДЖ ДНЯ ==========
elif menu == "⚡ Челлендж дня":
    st.header("⚡ Челлендж дня")
    
    challenges = [
        {
            "question": "📞 Тебе звонит «сотрудник банка» и просит назвать код из SMS. Твои действия?",
            "options": ["Назову код", "Положу трубку и сам позвоню в банк", "Спрошу имя сотрудника"],
            "correct": "Положу трубку и сам позвоню в банк",
            "explanation": "✅ Молодец! Банки никогда не просят код из SMS."
        },
        {
            "question": "💬 Друг в Telegram просит скинуть код подтверждения. Что делать?",
            "options": ["Скину код", "Позвоню другу и спрошу", "Проигнорирую"],
            "correct": "Позвоню другу и спрошу",
            "explanation": "✅ Правильно! Аккаунт друга могли взломать."
        },
        {
            "question": "🎁 «Ты выиграл iPhone! Перейди по ссылке». Твои действия?",
            "options": ["Перейду", "Проверю на официальном сайте", "Введу данные"],
            "correct": "Проверю на официальном сайте",
            "explanation": "✅ Бесплатный сыр только в мышеловке!"
        }
    ]
    
    if "challenge_num" not in st.session_state:
        st.session_state.challenge_num = random.randint(0, 2)
    
    challenge = challenges[st.session_state.challenge_num]
    
    st.markdown(f"**{challenge['question']}**")
    answer = st.radio("Выбери ответ:", challenge["options"])
    
    if st.button("🛡️ Проверить"):
        if answer == challenge["correct"]:
            st.balloons()
            st.success(challenge["explanation"])
        else:
            st.error("❌ Неправильно! " + challenge["explanation"])
    
    if st.button("🔄 Следующий"):
        st.session_state.challenge_num = random.randint(0, 2)
        st.rerun()

# ========== 3. ДИПФЕЙК ==========
elif menu == "🎭 Распознай дипфейк":
    st.header("🎭 Как распознать дипфейк")
    
    st.markdown("""
    <div class="info-box">
    <b>Дипфейк</b> — фальшивое видео или голос, созданные ИИ.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**5 признаков:**")
        st.markdown("""
        1. 👁️ Странное моргание
        2. 👄 Губы не совпадают
        3. 🌑 Неправильные тени
        4. 🤖 Роботизированный голос
        5. 🔄 Размытые края
        """)
    
    with col2:
        st.markdown("**Что делать:**")
        st.markdown("""
        - Попроси показать что-то в реальном времени
        - Перезвони по номеру
        - Расскажи взрослым
        """)
    
    st.warning("📌 Даже если видишь знакомое лицо — перепроверь!")

# ========== 4. ПРАВА В СЕТИ ==========
elif menu == "📜 Твои права в сети":
    st.header("📜 Твои права в интернете")
    st.caption("*По законодательству Республики Беларусь*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**✅ Ты имеешь право:**")
        st.markdown("""
        - Не давать данные незнакомцам
        - Удалить свою информацию
        - Не отвечать на оскорбления
        - Сообщить в милицию (102)
        """)
    
    with col2:
        st.markdown("**⚠️ Твои обязанности:**")
        st.markdown("""
        - Не распространять чужие данные
        - Не заниматься кибербуллингом
        - Не переходить по подозрительным ссылкам
        """)
    
    st.info("📞 **Куда звонить в Беларуси:** Милиция 102 | mir.pravo.by")

# ========== 5. СТИКЕР-ПАК ==========
elif menu == "😎 Стикер-пак":
    st.header("😎 Стикер-пак «СетьБезОбид»")
    
    stickers = [
        {"name": "🛡️ Щит", "desc": "Я в безопасности"},
        {"name": "🎣 Фишинг", "desc": "Не клюй!"},
        {"name": "😭 Хакер", "desc": "Не вышло!"},
        {"name": "🔒 Пароль", "desc": "Пароль — тайна"},
        {"name": "🔍 Проверка", "desc": "Доверяй, но проверяй"},
        {"name": "📞 Банк", "desc": "Клади трубку!"},
        {"name": "⛔ Стоп", "desc": "Мошенник!"},
        {"name": "🛡️ Сеть", "desc": "#КиберПраво"}
    ]
    
    cols = st.columns(4)
    for i, sticker in enumerate(stickers):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="sticker-card">
                <div style="font-size: 50px;">{sticker['name'][:2]}</div>
                <div class="sticker-name">{sticker['name']}</div>
                <small style="color:#aaa;">{sticker['desc']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("🌟 **Хэштеги:** #СетьБезОбид #КиберПраво")

# ========== ПОДВАЛ ==========
st.markdown("---")
st.caption(f"🛡️ Конкурс #КиберПраво 2026 | СетьБезОбид")
