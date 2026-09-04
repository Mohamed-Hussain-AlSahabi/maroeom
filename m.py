import streamlit as st
import base64
import os

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="موقع خاص جداً ❤️",
    page_icon="🔒",
    layout="wide"
)

# --- ضع كلمة السر التي تريدها هنا ---
CORRECT_PASSWORD = "31012"  # يمكنك تغيير كلمة السر هنا (مثلاً: 2024 أو تاريخ مميز)

# دالة لقراءة الصور وتحويلها إلى Base64
def get_image_base64(file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_name)
    
    if os.path.exists(file_path):
        with open(file_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode('utf-8')
            ext = file_name.split('.')[-1].lower()
            mime = "image/png" if ext == "png" else "image/jpeg"
            return f"data:{mime};base64,{encoded}"
    else:
        return "https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=800"

# --- شاشة التحقق من كلمة السر ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #0b0214, #180524, #2d0a31);
                color: #fff;
                text-align: center;
            }
            .pass-box {
                background: rgba(255, 255, 255, 0.05);
                padding: 30px;
                border-radius: 20px;
                border: 1px solid rgba(255, 117, 140, 0.3);
                max-width: 400px;
                margin: 80px auto 20px auto;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            }
            h2 { color: #ff758c; font-family: 'Cairo', sans-serif; }
            p { color: #ddd; }
        </style>
        <div class="pass-box">
            <h2>🔒 مفاجأة خاصة جداً</h2>
            <p>ادخلي كلمة السر لرؤية المفاجأة ❤️</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        user_password = st.text_input("كلمة السر:", type="password", key="pass_input")
        if st.button("دخول ✨", use_container_width=True):
            if user_password == CORRECT_PASSWORD:
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("كلمة السر غير صحيحة، حاولي مرة أخرى! 🌹")
    st.stop()

# --- محتوى الموقع بعد إدخال كلمة السر الصحيحة ---

HER_IMG = get_image_base64("her.jpg")
ME_IMG = get_image_base64("me.jpg")

TOGETHER_1 = get_image_base64("together1.jpg")
TOGETHER_2 = get_image_base64("together2.jpg")
TOGETHER_3 = get_image_base64("together3.jpg")
TOGETHER_4 = get_image_base64("together4.jpg")

html_code = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@600;700&family=Reem+Kufi:wght@600&display=swap');

    * {{ box-sizing: border-box; }}
    
    body {{
        margin: 0;
        padding: 10px;
        background: linear-gradient(135deg, #0b0214, #180524, #2d0a31);
        color: #fff;
        font-family: 'Cairo', sans-serif;
        text-align: center;
    }}

    .snowflake {{
        position: fixed;
        top: -10%;
        user-select: none;
        z-index: 1000;
        pointer-events: none;
        animation: fall 8s linear infinite;
    }}

    @keyframes fall {{
        0% {{ transform: translateY(0) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(100vh) rotate(360deg); opacity: 0; }}
    }}

    .container {{
        max-width: 800px;
        margin: 0 auto;
    }}

    .fixed-header {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 117, 140, 0.3);
        border-radius: 20px;
        padding: 15px;
        margin-bottom: 25px;
        backdrop-filter: blur(5px);
    }}

    .couple-row {{
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-wrap: wrap;
        gap: 10px;
    }}

    .profile-card img {{
        width: 110px;
        height: 110px;
        object-fit: cover;
        border-radius: 50%;
        border: 3px solid #ff758c;
        box-shadow: 0 0 15px rgba(255, 117, 140, 0.5);
    }}

    .profile-card p {{
        margin: 5px 0 0 0;
        font-weight: bold;
        color: #ff7eb3;
    }}

    .center-text {{
        flex: 1;
        min-width: 180px;
        font-family: 'Reem Kufi', sans-serif;
        font-size: 1.4rem;
        color: #ffffff;
        text-shadow: 0 0 10px rgba(255, 117, 140, 0.8);
        padding: 5px;
    }}

    .slider-card {{
        position: relative;
        background: rgba(0, 0, 0, 0.4);
        border-radius: 20px;
        padding: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}

    .slide {{
        display: none;
    }}

    .slide.active {{
        display: block;
        animation: fadeIn 0.6s ease-in-out;
    }}

    .img-box {{
        width: 100%;
        height: 420px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: #000;
        border-radius: 12px;
        overflow: hidden;
    }}

    .img-box img {{
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
    }}

    .caption {{
        margin-top: 15px;
        font-size: 1.15rem;
        color: #ffe0e9;
        background: rgba(255, 117, 140, 0.12);
        padding: 12px 15px;
        border-radius: 10px;
        border-right: 4px solid #ff758c;
        line-height: 1.6;
    }}

    .btn {{
        position: absolute;
        top: 40%;
        transform: translateY(-50%);
        background: rgba(255, 117, 140, 0.4);
        color: white;
        border: none;
        font-size: 1.8rem;
        padding: 8px 15px;
        cursor: pointer;
        border-radius: 50%;
        user-select: none;
        z-index: 10;
        transition: 0.2s;
    }}

    .btn:hover {{
        background: rgba(255, 117, 140, 0.9);
    }}

    .prev {{ right: 10px; }}
    .next {{ left: 10px; }}

    .counter {{
        margin-top: 10px;
        font-size: 0.9rem;
        color: #bbb;
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; transform: scale(0.97); }}
        to {{ opacity: 1; transform: scale(1); }}
    }}
</style>
</head>
<body>

<div class="container">

    <div class="fixed-header">
        <div class="couple-row">
            <div class="profile-card">
                <img src="{HER_IMG}">
                <p>أجمل البنات ✨</p>
            </div>
            
            <div class="center-text">
                "بين كل دقة قلب والثانية... حبك بيكبر في قلبي أكتر وأكتر ❤️"
            </div>

            <div class="profile-card">
                <img src="{ME_IMG}">
                <p>حبيبك للأبد 🌹</p>
            </div>
        </div>
    </div>

    <div class="slider-card">
        <button class="btn prev" onclick="move(-1)">❮</button>
        <button class="btn next" onclick="move(1)">❯</button>

        <div class="slide active">
            <div class="img-box"><img src="{TOGETHER_1}"></div>
            <div class="caption">"كل لحظة بقضيها معاكي هي أجمل حلم بيتحقق في حياتي... وجودك جمبي بيطمني ومحلي كل أيامي ❤️"</div>
        </div>

        <div class="slide">
            <div class="img-box"><img src="{TOGETHER_2}"></div>
            <div class="caption">"ضحكتك هي مصدري الوحيد للسعادة والبهجة... ربنا يديمك في حياتي شمس مبتغيبش أبداً ✨"</div>
        </div>

        <div class="slide">
            <div class="img-box"><img src="{TOGETHER_3}"></div>
            <div class="caption">"معاكي وبس عرفت يعني إيه حب حقيقي وأمان... انتي مش بس حبيبتي، انتي كل دنيتي 🌸"</div>
        </div>

        <div class="slide">
            <div class="img-box"><img src="{TOGETHER_4}"></div>
            <div class="caption">"وعد مني ليكي، هفضل أحبك وأصونك وأدعمك في كل خطواتك، وأكون ليكي دايماً السند والظهر 💖"</div>
        </div>

        <div class="counter" id="slideNum">صورة 1 من 4</div>
    </div>

</div>

<script>
    const symbols = ['🌹', '❤️', '✨', '💖', '🌸'];
    for (let i = 0; i < 20; i++) {{
        let item = document.createElement('div');
        item.className = 'snowflake';
        item.innerText = symbols[Math.floor(Math.random() * symbols.length)];
        item.style.left = Math.random() * 100 + 'vw';
        item.style.animationDuration = (Math.random() * 5 + 5) + 's';
        item.style.fontSize = (Math.random() * 15 + 15) + 'px';
        document.body.appendChild(item);
    }}

    let index = 0;
    const slides = document.querySelectorAll('.slide');
    const slideNum = document.getElementById('slideNum');

    function show(n) {{
        slides.forEach(s => s.classList.remove('active'));
        slides[n].classList.add('active');
        slideNum.innerText = `صورة ${{n + 1}} من ${{slides.length}}`;
    }}

    function move(dir) {{
        index += dir;
        if (index < 0) index = slides.length - 1;
        if (index >= slides.length) index = 0;
        show(index);
    }}
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=750, scrolling=True)