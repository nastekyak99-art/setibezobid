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

# ========== ФОН С КАРТИНКОЙ ИНТЕРНЕТ-СЕТИ + ХАОТИЧНЫЕ ИКОНКИ ==========
st.markdown("""
<style>
    /* Основной фон с изображением интернет-сети */
    .stApp {
        background: url('https://www.transparenttextures.com/patterns/dark-matter.png'), 
                    linear-gradient(135deg, #0a0a2a 0%, #1a1a3e 50%, #0d0d2b 100%);
        background-attachment: fixed;
        position: relative;
    }
    
    /* Хаотичные иконки на фоне (псевдоэлемент) */
    .stApp::before {
        content: "🔒🛡️🌐💻📡🔐⚡🕸️🔗📱";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        font-size: 40px;
        opacity: 0.08;
        pointer-events: none;
        white-space: pre;
        overflow: hidden;
        z-index: 0;
        letter-spacing: 30px;
        line-height: 80px;
        transform: rotate(-15deg) scale(1.5);
        font-family: monospace;
    }
    
    /* Дополнительные хаотичные элементы */
    .stApp::after {
        content: "⚙️📊📶🔓🔔📂💾🖥️🖱️⌨️";
        position: fixed;
        bottom: 0;
        right: 0;
        font-size: 35px;
        opacity: 0.06;
        pointer-events: none;
        white-space: pre;
        z-index: 0;
        letter-spacing: 25px;
        line-height: 60px;
        transform: rotate(10deg);
    }
    
    /* Заголовки */
    h1, h2, h3 {
        color: #ff6b35 !important;
        font-family: 'Segoe UI Black', 'Impact', sans-serif !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        position: relative;
        z-index: 1;
    }
    
    /* Обычный текст */
    p, li, .stMarkdown, .stCaption {
        color: #f0f0f0 !important;
        font-family: 'Segoe UI', 'Roboto', sans-serif !important;
        font-size: 16px;
        position: relative;
        z-index: 1;
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
        position: relative;
        z-index: 1;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #f7931e, #ff6b35);
        color: white;
    }
    
    /* Боковое меню */
    .css-1d391kg, .css-163ttbj, .stSidebar {
        background-color: rgba(15, 12, 41, 0.95);
        position: relative;
        z-index: 1;
    }
    
    /* Radio buttons */
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
    
    /* Информационные блоки */
    .info-box {
        background: rgba(255, 107, 53, 0.2);
        border-left: 5px solid #ff6b35;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        position: relative;
        z-index: 1;
    }
    
    /* Стикеры */
    .sticker-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        justify-content: center;
        margin-top: 20px;
        position: relative;
        z-index: 1;
    }
    
    .sticker-card {
        background: linear-gradient(145deg, #2a235a, #1a1542);
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        width: 120px;
        transition: transform 0.3s;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    }
    
    .sticker-card:hover {
        transform: translateY(-5px);
    }
    
    .sticker-image {
        width: 60px;
        height: 60px;
        display: block;
        margin: 0 auto 10px auto;
    }
    
    .sticker-text {
        color: #ff6b35;
        font-weight: bold;
        font-size: 12px;
        font-family: monospace;
    }
    
    /* Картинка в челлендже */
    .challenge-icon {
        width: 40px;
        vertical-align: middle;
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ========== ЗАГОЛОВОК ==========
st.title("СетьБезОбид")
st.markdown("*Твоя безопасная сеть без мошенников и обид*")
st.markdown("---")

# ========== БОКОВОЕ МЕНЮ ==========
menu = st.sidebar.radio(
    "**МЕНЮ**",
    ["Проверь ссылку", "Челлендж дня", "Распознай дипфейк", "Твои права в сети", "Стикер-пак #КиберПраво"]
)

# Функция для показа иконки (картинки)
def show_icon(icon_name):
    icons = {
        "shield": "https://cdn-icons-png.flaticon.com/512/754/754179.png",
        "link": "https://cdn-icons-png.flaticon.com/512/1185/1185933.png",
        "quiz": "https://cdn-icons-png.flaticon.com/512/2121/2121514.png",
        "deepfake": "https://cdn-icons-png.flaticon.com/512/5666/5666987.png",
        "law": "https://cdn-icons-png.flaticon.com/512/2826/2826774.png",
        "sticker": "https://cdn-icons-png.flaticon.com/512/3159/3159312.png",
        "warning": "https://cdn-icons-png.flaticon.com/512/709/709649.png",
        "success": "https://cdn-icons-png.flaticon.com/512/190/190411.png",
        "lock": "https://cdn-icons-png.flaticon.com/512/420/420425.png",
        "hacker": "https://cdn-icons-png.flaticon.com/512/2331/2331228.png",
        "phone": "https://cdn-icons-png.flaticon.com/512/3095/3095201.png"
    }
    return icons.get(icon_name, "https://cdn-icons-png.flaticon.com/512/754/754179.png")

# ========== 1. ПРОВЕРКА ССЫЛКИ ==========
if menu == "Проверь ссылку":
    st.header("Проверь ссылку на безопасность")
    st.markdown('<div class="info-box">Вставь ссылку — система проверит её на фишинг</div>', unsafe_allow_html=True)
    
    suspicious_words = ["login", "verify", "secure", "update", "confirm", "bank", "paypal", "password", "account", "alert", "подтвердить", "войти"]
    suspicious_domains = ["bit.ly", "tinyurl", "goo.gl", "rb.ly", "clck.ru"]
    
    link = st.text_input("Вставь подозрительную ссылку:")
    
    if link:
        link_lower = link.lower()
        found_words = [w for w in suspicious_words if w in link_lower]
        found_domains = [d for d in suspicious_domains if d in link_lower]
        
        if found_words or found_domains:
            st.error("ВНИМАНИЕ! Это похоже на ФИШИНГ!")
            if found_words:
                st.write(f"Подозрительные слова: {', '.join(found_words)}")
            if found_domains:
                st.write(f"Короткая ссылка: {', '.join(found_domains)}")
            st.info("Совет: никогда не переходи по подозрительным ссылкам!")
        else:
            st.success("Ссылка выглядит безопасно, но будь внимателен!")

# ========== 2. ЧЕЛЛЕНДЖ ДНЯ ==========
elif menu == "Челлендж дня":
    st.header("Челлендж дня")
    st.markdown('<div class="info-box">Проверь, сможешь ли ты распознать мошенника?</div>', unsafe_allow_html=True)
    
    challenges = [
        {
            "question": "Тебе звонит «сотрудник банка» и просит назвать код из SMS. Твои действия?",
            "options": ["Назову код", "Положу трубку и сам позвоню в банк", "Спрошу имя сотрудника"],
            "correct": "Положу трубку и сам позвоню в банк",
            "explanation": "Молодец! Банки никогда не просят код из SMS."
        },
        {
            "question": "В Telegram приходит сообщение от «друга» с просьбой скинуть код подтверждения. Что делать?",
            "options": ["Скину код", "Позвоню другу и спрошу, он ли это", "Проигнорирую"],
            "correct": "Позвоню другу и спрошу, он ли это",
            "explanation": "Правильно! Аккаунт друга могли взломать."
        },
        {
            "question": "Ты выиграл iPhone! Для получения нужно перейти по ссылке и ввести данные карты. Твои действия?",
            "options": ["Перейду по ссылке", "Проверю конкурс на официальном сайте", "Введу данные"],
            "correct": "Проверю конкурс на официальном сайте",
            "explanation": "Бесплатный сыр только в мышеловке! Ты молодец."
        },
        {
            "question": "На почту пришло письмо: «Ваш аккаунт будет удалён! Перейдите по ссылке». Что делать?",
            "options": ["Перейду по ссылке", "Удалю письмо и проверю отправителя", "Напишу ответ"],
            "correct": "Удалю письмо и проверю отправителя",
            "explanation": "Это классический фишинг. Ты всё сделал правильно!"
        }
    ]
    
    if "challenge_num" not in st.session_state:
        st.session_state.challenge_num = random.randint(0, 3)
    
    challenge = challenges[st.session_state.challenge_num]
    
    st.markdown(f"**{challenge['question']}**")
    answer = st.radio("Выбери ответ:", challenge["options"], key="quiz")
    
    if st.button("Проверить ответ"):
        if answer == challenge["correct"]:
            st.balloons()
            st.success(challenge["explanation"])
        else:
            st.error("Неправильно! " + challenge["explanation"])
    
    if st.button("Следующий челлендж"):
        st.session_state.challenge_num = random.randint(0, 3)
        st.rerun()

# ========== 3. ДИПФЕЙК ==========
elif menu == "Распознай дипфейк":
    st.header("Как распознать дипфейк")
    
    st.markdown("""
    <div class="info-box">
    <b>Дипфейк</b> — это фальшивое видео или голос, созданные искусственным интеллектом.
    Мошенники могут подделать голос близкого человека.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**5 признаков дипфейка:**")
        st.markdown("""
        1. Странное моргание
        2. Губы не совпадают со звуком
        3. Неправильные тени на лице
        4. Роботизированный голос
        5. Размытые края вокруг лица
        """)
    
    with col2:
        st.markdown("**Что делать:**")
        st.markdown("""
        - Попроси показать что-то в реальном времени
        - Перезвони по официальному номеру
        - Расскажи взрослым
        """)
    
    st.warning("Золотое правило: даже если видишь знакомое лицо — перепроверь другим способом!")

# ========== 4. ПРАВА В СЕТИ ==========
elif menu == "Твои права в сети":
    st.header("Твои права в интернете")
    st.caption("По законодательству Республики Беларусь")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Ты имеешь право:**")
        st.markdown("""
        - Не давать данные незнакомцам
        - Удалить свою информацию
        - Не отвечать на оскорбления
        - Сообщить в милицию (102)
        """)
    
    with col2:
        st.markdown("**Твои обязанности:**")
        st.markdown("""
        - Не распространять чужие данные
        - Не заниматься кибербуллингом
        - Не переходить по ссылкам от мошенников
        """)
    
    st.info("**Куда звонить в Беларуси:** Милиция 102 | Детский правовой сайт: mir.pravo.by")

# ========== 5. СТИКЕР-ПАК ==========
elif menu == "Стикер-пак #КиберПраво":
    st.header("Стикер-пак «СетьБезОбид»")
    st.markdown('<div class="info-box">Наши стикеры — скачивай и делись с друзьями!</div>', unsafe_allow_html=True)
    
    # Стикеры с картинками
    stickers = [
        {"img": "https://cdn-icons-png.flaticon.com/512/754/754179.png", "name": "Щит включён", "text": "Я в безопасности"},
        {"img": "https://cdn-icons-png.flaticon.com/512/709/709649.png", "name": "Фишинг пойман", "text": "Не клюй!"},
        {"img": "https://cdn-icons-png.flaticon.com/512/2331/2331228.png", "name": "Хакер плачет", "text": "Не вышло!"},
        {"img": "https://cdn-icons-png.flaticon.com/512/420/420425.png", "name": "Не делись паролем", "text": "Пароль — тайна"},
        {"img": "https://cdn-icons-png.flaticon.com/512/1185/1185933.png", "name": "Проверь источник", "text": "Доверяй, но проверяй"},
        {"img": "https://cdn-icons-png.flaticon.com/512/3095/3095201.png", "name": "Звонок из банка", "text": "Клади трубку!"},
        {"img": "https://cdn-icons-png.flaticon.com/512/5666/5666987.png", "name": "Мошенник обнаружен", "text": "Стоп, обман!"},
        {"img": "https://cdn-icons-png.flaticon.com/512/2826/2826774.png", "name": "СетьБезОбид", "text": "#КиберПраво"}
    ]
    
    # Отображаем стикеры сеткой
    cols = st.columns(4)
    for i, sticker in enumerate(stickers):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="sticker-card">
                <img src="{sticker['img']}" class="sticker-image">
                <div class="sticker-text">{sticker['name']}</div>
                <small style="color:#aaa;">{sticker['text']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("**Как скачать стикеры?**")
    st.markdown("""
    1. Нажми правой кнопкой мыши на любой стикер выше
    2. Выбери «Сохранить картинку как...»
    3. Сохрани в формате PNG
    4. Добавь в Telegram/WhatsApp/Viber
    """)
    
    st.info("**Не забудь хэштеги:** #СетьБезОбид #КиберПраво #БезопасностьДетям")

# ========== ПОДВАЛ ==========
st.markdown("---")
st.caption(f"СетьБезОбид — твоя безопасная сеть | Конкурс #КиберПраво 2026 | {datetime.now().year}")
