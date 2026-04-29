import streamlit as st
import random
from datetime import datetime

# ========== НАСТРОЙКА СТРАНИЦЫ ==========
st.set_page_config(
    page_title="СетьБезОбид",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ========== КАСТОМНЫЙ CSS ==========
st.markdown("""
<style>
    /* Основной фон */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    /* Заголовки */
    h1, h2, h3 {
        color: #ff6b35 !important;
        font-family: 'Segoe UI Black', 'Impact', sans-serif !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* Обычный текст */
    p, li, .stMarkdown {
        color: #f0f0f0 !important;
        font-family: 'Segoe UI', 'Roboto', sans-serif !important;
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
        font-family: 'Segoe UI', sans-serif;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #f7931e, #ff6b35);
        color: white;
    }
    
    /* Боковое меню */
    .css-1d391kg, .css-163ttbj, .stSidebar {
        background-color: rgba(15, 12, 41, 0.95);
    }
    
    /* Radio buttons в меню */
    .stRadio > div {
        background-color: rgba(255, 107, 53, 0.2);
        border-radius: 15px;
        padding: 10px;
    }
    
    .stRadio label {
        color: #ff6b35 !important;
        font-weight: bold;
        font-size: 16px;
    }
    
    /* Успех/ошибка */
    .stAlert {
        border-radius: 15px;
        font-weight: bold;
    }
    
    /* Выделение */
    .highlight {
        background: linear-gradient(120deg, #ff6b35 0%, #ff6b35 40%, transparent 60%);
        padding: 0 5px;
        font-weight: bold;
        color: white;
    }
    
    /* Блоки с информацией */
    .info-box {
        background: rgba(255, 107, 53, 0.2);
        border-left: 5px solid #ff6b35;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    
    /* Стикеры (прямоугольник-превью) */
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
        width: 100px;
        transition: transform 0.3s;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    }
    .sticker-card:hover {
        transform: translateY(-5px);
    }
    .sticker-emoji {
        font-size: 60px;
        display: block;
        margin-bottom: 10px;
    }
    .sticker-text {
        color: #ff6b35;
        font-weight: bold;
        font-size: 12px;
        font-family: monospace;
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
    ["🔍 Проверь ссылку", "⚡ Челлендж дня", "🎭 Распознай дипфейк", "📜 Твои права в сети", "😎 Стикер-пак #КиберПраво"]
)

# ========== 1. ПРОВЕРКА ССЫЛКИ ==========
if menu == "🔍 Проверь ссылку":
    st.header("🔍 Проверь ссылку на безопасность")
    st.markdown('<div class="info-box">Вставь ссылку — ИИ проверит её на фишинг</div>', unsafe_allow_html=True)
    
    suspicious_words = ["login", "verify", "secure", "update", "confirm", "bank", "paypal", "password", "account", "alert", "подтвердить", "войти"]
    suspicious_domains = ["bit.ly", "tinyurl", "goo.gl", "rb.ly", "clck.ru"]
    
    link = st.text_input("🌐 Вставь подозрительную ссылку:")
    
    if link:
        link_lower = link.lower()
        found_words = [w for w in suspicious_words if w in link_lower]
        found_domains = [d for d in suspicious_domains if d in link_lower]
        
        if found_words or found_domains:
            st.error("🚨🚨🚨 **НЕ ПЕРЕХОДИ! Это ФИШИНГ!**")
            if found_words:
                st.warning(f"⚠️ Подозрительные слова: {', '.join(found_words)}")
            if found_domains:
                st.warning(f"⚠️ Короткая ссылка: {', '.join(found_domains)}")
            st.info("💡 Совет: никогда не переходи по подозрительным ссылкам!")
        else:
            st.success("✅ Ссылка безопасна, но будь внимателен!")
            st.info("💡 Даже хорошие сайты могут подделать — проверяй адресную строку!")

# ========== 2. ЧЕЛЛЕНДЖ ДНЯ ==========
elif menu == "⚡ Челлендж дня":
    st.header("⚡ Челлендж дня")
    st.markdown('<div class="info-box">Проверь, сможешь ли ты распознать мошенника?</div>', unsafe_allow_html=True)
    
    challenges = [
        {
            "question": "📞 Звонит «сотрудник банка»: «Вашу карту взламывают! Назовите код из SMS!» Твои действия?",
            "options": ["😨 Назову код", "📞 Положу трубку и сам позвоню в банк", "🤔 Спрошу имя сотрудника"],
            "correct": "📞 Положу трубку и сам позвоню в банк",
            "explanation": "✅ Молодец! Банки никогда не просят код из SMS. Ты не клюнул!"
        },
        {
            "question": "💬 Друг в Telegram просит: «Скинь код подтверждения, мне пришла SMS». Что делать?",
            "options": ["📱 Скину код", "🔍 Позвоню другу и спрошу, он ли это", "😐 Промолчу"],
            "correct": "🔍 Позвоню другу и спрошу, он ли это",
            "explanation": "✅ Правильно! Аккаунт друга могли взломать. Всегда проверяй!"
        },
        {
            "question": "🎁 «Ты выиграл iPhone! Перейди по ссылке и введи данные карты». Твои действия?",
            "options": ["🤑 Ура, перейду!", "🔎 Проверю конкурс на официальном сайте", "💳 Введу данные"],
            "correct": "🔎 Проверю конкурс на официальном сайте",
            "explanation": "✅ Бесплатный сыр только в мышеловке! Ты молодец, не повелся."
        },
        {
            "question": "📧 Письмо: «Ваш аккаунт удалят! Перейдите по ссылке!» Что делать?",
            "options": ["📎 Перейду", "🗑️ Удалю письмо и проверю отправителя", "📝 Напишу ответ"],
            "correct": "🗑️ Удалю письмо и проверю отправителя",
            "explanation": "✅ Это классический фишинг. Ты всё сделал правильно!"
        }
    ]
    
    if "challenge_num" not in st.session_state:
        st.session_state.challenge_num = random.randint(0, 3)
    
    challenge = challenges[st.session_state.challenge_num]
    
    st.markdown(f"### {challenge['question']}")
    answer = st.radio("Выбери ответ:", challenge["options"], key="quiz")
    
    if st.button("🛡️ Проверить ответ"):
        if answer == challenge["correct"]:
            st.balloons()
            st.success(challenge["explanation"])
        else:
            st.error("❌ Неправильно! " + challenge["explanation"])
    
    if st.button("🔄 Следующий челлендж"):
        st.session_state.challenge_num = random.randint(0, 3)
        st.rerun()

# ========== 3. ДИПФЕЙК ==========
elif menu == "🎭 Распознай дипфейк":
    st.header("🎭 Как распознать дипфейк")
    
    st.markdown("""
    <div class="info-box">
    <b>Дипфейк</b> — это фальшивое видео или голос, созданные искусственным интеллектом.
    Мошенники могут подделать голос мамы или папы, чтобы тебя обмануть.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔍 5 признаков дипфейка:")
        st.markdown("""
        1. 👁️ **Странное моргание** — слишком редкое или частое
        2. 👄 **Губы не совпадают** со звуком
        3. 🌑 **Неправильные тени** на лице
        4. 🤖 **Роботизированный голос** без эмоций
        5. 🔄 **Размытые края** вокруг лица
        """)
    
    with col2:
        st.markdown("### 💡 Что делать:")
        st.markdown("""
        - Попроси показать **что-то в реальном времени**
        - **Перезвони** по официальному номеру
        - **Расскажи взрослым**
        """)
    
    st.warning("📌 Золотое правило: даже если видишь знакомое лицо — перепроверь другим способом!")

# ========== 4. ПРАВА В СЕТИ ==========
elif menu == "📜 Твои права в сети":
    st.header("📜 Твои права в интернете")
    st.caption("По законодательству Республики Беларусь")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✅ Ты имеешь право:")
        st.markdown("""
        - Не давать данные незнакомцам
        - Удалить свою информацию
        - Не отвечать на оскорбления
        - Сообщить в милицию (102)
        """)
    
    with col2:
        st.markdown("### ⚠️ Твои обязанности:")
        st.markdown("""
        - Не распространять чужие данные
        - Не заниматься кибербуллингом
        - Не переходить по ссылкам от мошенников
        """)
    
    st.info("📞 **Куда звонить в Беларуси:** Милиция 102 | Детский правовой сайт: mir.pravo.by")

# ========== 5. СТИКЕР-ПАК (ВСТРОЕННЫЙ) ==========
elif menu == "😎 Стикер-пак #КиберПраво":
    st.header("😎 Стикер-пак «СетьБезОбид»")
    st.markdown('<div class="info-box">Наши стикеры — скачивай и делись с друзьями! Используй хэштег #КиберПраво</div>', unsafe_allow_html=True)
    
    # Стикеры прямо в приложении (с эмодзи-иконками)
    stickers = [
        {"emoji": "🛡️💚", "name": "Щит включён", "text": "Я в безопасности!"},
        {"emoji": "🎣📧", "name": "Фишинг пойман", "text": "Не клюй!"},
        {"emoji": "😭💻", "name": "Хакер плачет", "text": "Не вышло!"},
        {"emoji": "🔒🤐", "name": "Не делись паролем", "text": "Пароль — тайна"},
        {"emoji": "🔍👁️", "name": "Проверь источник", "text": "Доверяй, но проверяй"},
        {"emoji": "📞❌", "name": "Звонок из банка", "text": "Клади трубку!"},
        {"emoji": "⛔🦹", "name": "Мошенник обнаружен", "text": "Стоп, обман!"},
        {"emoji": "🛡️😊", "name": "СетьБезОбид", "text": "#КиберПраво"}
    ]
    
    # Отображаем стикеры сеткой
    st.markdown('<div class="sticker-grid">', unsafe_allow_html=True)
    
    cols = st.columns(4)
    for i, sticker in enumerate(stickers):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="sticker-card">
                <span class="sticker-emoji">{sticker['emoji']}</span>
                <span class="sticker-text">{sticker['name']}</span>
                <br>
                <small style="color:#aaa;">{sticker['text']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Инструкция по скачиванию
    st.markdown("---")
    st.markdown("### 📥 Как скачать стикеры?")
    st.markdown("""
    1. **Нажми правой кнопкой мыши** на любой стикер выше
    2. Выбери **«Сохранить картинку как...»**
    3. Сохрани в формате PNG
    4. Добавь в Telegram/WhatsApp/Viber
    5. Делись с друзьями и используй хэштег **#КиберПраво**
    """)
    
    st.info("🌟 **Не забудь хэштеги:** #СетьБезОбид #КиберПраво #БезопасностьДетям")

# ========== ПОДВАЛ ==========
st.markdown("---")
st.caption(f"🛡️ СетьБезОбид — твоя безопасная сеть | Конкурс #КиберПраво 2026 | {datetime.now().year}")
