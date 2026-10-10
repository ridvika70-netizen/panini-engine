import streamlit as st
import random

# ==========================================
# ADVANCED DATA MAPPING: HISTORICAL COGNATES
# ==========================================
COGNATE_DATABASE = {
    "bhū": {
        "pie": "*bhuH- (To grow, exist, become)",
        "latin": "fui (I have been) ➔ futurus (future)",
        "hindi": "होना (hona) / भवन (bhavan)",
        "english": "Be / Been / Build / Future"
    },
    "path": {
        "pie": "*peth₂- (To spread out / recite text)",
        "latin": "Not directly cognate (Indo-Iranian specialization)",
        "hindi": "पढ़ना (padhna - to read / study)",
        "english": "Path (semantic shift via tracking text lines)"
    },
    "gam": {
        "pie": "*gʷem- (To step, come, go)",
        "latin": "venire (to come)",
        "hindi": "गमन (gaman) / जाना (jana)",
        "english": "Come / Become / Avenue"
    },
    "ad": {
        "pie": "*hed- (To eat)",
        "latin": "edere (to eat)",
        "hindi": "अदना (adana)",
        "english": "Eat / Edible / Anorexia"
    },
    "kṛ": {
        "pie": "*kʷer- (To do, make, shape)",
        "latin": "creare (to create / bring forth)",
        "hindi": "करना (karna) / कर्म (karma)",
        "english": "Create / Ceramic / Karma"
    },
    "vid": {
        "pie": "*weid- (To see, know)",
        "latin": "videre (to see) ➔ visio (vision)",
        "hindi": "विद्या (vidya) / वेद (veda)",
        "english": "Wit / Wisdom / Vision / Video"
    },
    "as": {
        "pie": "*h₁es- (To be, exist)",
        "latin": "esse (to be) ➔ essentia (essence)",
        "hindi": "अस्ति (asti) / है (hai)",
        "english": "Is / Am / Essence / Absent"
    },
    "smar": {
        "pie": "(s)mer- (To remember, mind)",
        "latin": "memor (mindful) ➔ memoria (memory)",
        "hindi": "स्मरण (smaran) / याद रखना",
        "english": "Memory / Mourn / Martyr"
    },
    "daś": {
        "pie": "*denḱ- (To bite)",
        "latin": "Not directly cognate",
        "hindi": "डसना (dasna - snake bite)",
        "english": "Tongs / Tusk"
    },
    "jñā": {
        "pie": "*g̑neh₃- (To know)",
        "latin": "gnoscere (to know) ➔ ignorantia",
        "hindi": "ज्ञान (gyan) / जानना (jaanna)",
        "english": "Know / Knowledge / Diagnosis"
    }
}

# ==========================================
# PAGE CONFIG & TOP-NOTCH BURGUNDY STYLING
# ==========================================
st.set_page_config(
    page_title="Pāṇini's Master Manuscript Engine", 
    page_icon="📜", 
    layout="wide"
)

# High-end glassmorphism styling with burgundy-to-twilight gradient
st.markdown(
    "<style>"
    ".stApp { background: radial-gradient(circle at 50% 0%, #581c87 0%, #4c0519 45%, #180208 100%); background-attachment: fixed; color: #FDF2F8; font-family: 'Courier New', Courier, monospace; }"
    "h1, h2, h3 { font-family: 'Georgia', serif; color: #FDE047; text-shadow: 0 0 20px rgba(253, 224, 71, 0.4), 2px 2px 4px rgba(0,0,0,0.8); }"
    ".glass-card { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.15); border-top: 1px solid rgba(255, 255, 255, 0.3); padding: 20px; border-radius: 16px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5); margin-bottom: 20px; }"
    ".sanskrit-text { font-size: 2.2em; color: #FDE047; font-family: 'Georgia', serif; text-align: center; letter-spacing: 2px; text-shadow: 0 0 15px rgba(253, 224, 71, 0.5); }"
    ".stButton>button { background: linear-gradient(135deg, #E11D48 0%, #881337 100%); color: #FFFFFF; font-family: 'Georgia', serif; border: 1px solid rgba(255,255,255,0.3); border-radius: 12px; padding: 12px 24px; font-weight: bold; font-size: 1.05em; width: 100%; box-shadow: 0 8px 20px rgba(225, 29, 72, 0.4); }"
    "</style>",
    unsafe_allow_html=True
)

# ==========================================
# BULLETPROOF FLAT ENGINE (ZERO BRACES/PARENS ISSUES)
# ==========================================
def get_root_data(root):
    if root == "bhū":
        meaning = "to become / to exist"
        gana = "Action Word Group"
        family = "Ancient Indus Valley Word Tree"
        skt = "भवति"
        latin = "bhavati"
        steps = [
            "1. 🪄 **Magic Seed Word**: Picked the base seed sound 'bhū' from ancient tradition.",
            "2. 🧩 **Action Helper Tag**: Added the movement tag '-a-' so it becomes an active word.",
            "3. 📈 **Vowel Workout**: Stretched the short vowel sound 'ū' into a strong 'o'.",
            "4. ✨ **Final Magic Polish**: Blended it smoothly into **bhavati (भवति)**!"
        ]
        return meaning, gana, family, skt, latin, steps
        
    elif root == "paṭh":
        meaning = "to read / to recite"
        gana = "School & Learning Group"
        family = "Ancient Forest Academy Word"
        skt = "पठति"
        latin = "paṭhati"
        steps = [
            "1. 🪄 **Magic Seed Word**: Picked the base seed sound 'paṭh'.",
            "2. 🧩 **Action Helper Tag**: Attached the thematic tag '-a-'.",
            "3. 🛡️ **Steady Vowel**: Kept the short vowel 'a' nice and safe without changes.",
            "4. ✨ **Final Magic Polish**: Snapped on ending '-ti' to form **paṭhati (पठति)**!"
        ]
        return meaning, gana, family, skt, latin, steps
        
    elif root == "gam":
        meaning = "to go / to walk"
        gana = "Travel & Movement Group"
        family = "Old Steppe Traveler Word"
        skt = "गच्छति"
        latin = "gacchati"
        steps = [
            "1. 🪄 **Magic Seed Word**: Picked the base seed sound 'gam'.",
            "2. 🔄 **Word Swap**: Swapped 'gam' out for the walking style 'gacch'.",
            "3. 🧩 **Action Helper Tag**: Added the action marker '-a-'.",
            "4. ✨ **Final Magic Polish**: Attached ending '-ti' to form **gacchati (गच्छति)**!"
        ]
        return meaning, gana, family, skt, latin, steps
        
    elif root == "ad":
        meaning = "to eat"
        gana = "Food & Munching Group"
        family = "Primeval Hearth Word"
        skt = "अत्ति"
        latin = "atti"
        steps = [
            "1. 🪄 **Magic Seed Word**: Picked the base seed sound 'ad'.",
            "2. ⚡ **Fast-Track Skip**: Skipped extra middle steps for a quick snack word.",
            "3. 🤝 **Letter Blend**: Melted the consonant letters together tightly.",
            "4. ✨ **Final Magic Polish**: Produced the yummy final word **atti (अत्ति)**!"
        ]
        return meaning, gana, family, skt, latin, steps
        
    elif root == "kṛ":
        meaning = "to do / to make"
        gana = "Builder & Crafter Group"
        family = "Ancient Campfire Craft Word"
        skt = "करोति"
        latin = "karoti"
        steps = [
            "1. 🪄 **Magic Seed Word**: Picked the base seed sound 'kṛ'.",
            "2. 📈 **Vowel Workout**: Grew the vowel sound into a strong 'ar'.",
            "3. 🧱 **Helper Suffix**: Added the building block suffix '-u-'.",
            "4. ✨ **Final Magic Polish**: Assembled together into **karoti (करोति)**!"
        ]
        return meaning, gana, family, skt, latin, steps
        
    elif root == "vid":
        meaning = "to know / to find out"
        gana = "Smart & Brainy Group"
        family = "Rigveda Discovery Word"
        skt = "वेत्ति"
        latin = "vetti"
        steps = [
            "1. 🪄 **Magic Seed Word**: Picked the base seed sound 'vid'.",
            "2. 🚀 **Super Speed**: Bypassed regular tags for instant genius mode.",
            "3. 🔗 **Sound Merge**: Fused the consonant sounds together.",
            "4. ✨ **Final Magic Polish**: Created the smart word **vetti (वेत्ति)**!"
        ]
        return meaning, gana, family, skt, latin, steps
        
    elif root == "as":
        meaning = "to be / to exist"
        gana = "Existence & Life Group"
        family = "Old Starry Night Word"
        skt = "अस्ति"
        latin = "asti"
        steps = [
            "1. 🪄 **Magic Seed Word**: Picked the copular base 'as'.",
            "2. 🌿 **Simple Mode**: Kept things natural without heavy changes.",
            "3. 📌 **Person Tag**: Attached the third-person ending '-ti'.",
            "4. ✨ **Final Magic Polish**: Formed the living word **asti (अस्ति)**!"
        ]
        return meaning, gana, family, skt, latin, steps
        
    elif root == "smar":
        meaning = "to remember"
        gana = "Memory & Brain Group"
        family = "Oral Storyteller Word"
        skt = "स्मरति"
        latin = "smarati"
        steps = [
            "1. 🪄 **Magic Seed Word**: Picked the base seed sound 'smar'.",
            "2. 🧩 **Action Helper Tag**: Added the thematic marker '-a-'.",
            "3. ✂️ **Short Vowel**: Kept the vowel short and sweet.",
            "4. ✨ **Final Magic Polish**: Attached ending '-ti' to form **smarati (स्मरति)**!"
        ]
        return meaning, gana, family, skt, latin, steps
        
    elif root == "daś":
        meaning = "to bite"
        gana = "Animal Kingdom Group"
        family = "Jungle Trail Word"
        skt = "दशति"
        latin = "daśati"
        steps = [
            "1. 🪄 **Magic Seed Word**: Picked the base seed sound 'daś'.",
            "2. 🧩 **Action Helper Tag**: Added the thematic vowel '-a-'.",
            "3. 🐍 **Sharp Sound**: Kept the sharp sibilant sound protected.",
            "4. ✨ **Final Magic Polish**: Completed the word as **daśati (दशति)**!"
        ]
        return meaning, gana, family, skt, latin, steps
        
    elif root == "jñā":
        meaning = "to know / to learn"
        gana = "School & Wisdom Group"
        family = "Takshashila Classroom Word"
        skt = "जानाति"
        latin = "jānāti"
        steps = [
            "1. 🪄 **Magic Seed Word**: Picked the base seed sound 'jñā'.",
            "2. 🧠 **Smart Helper**: Inserted the wisdom affix '-nā-'.",
            "3. ⚖️ **Vowel Balance**: Adjusted long vowel positions just right.",
            "4. ✨ **Final Magic Polish**: Brought to life as **jānāti (जानाति)**!"
        ]
        return meaning, gana, family, skt, latin, steps
        
    return "unknown", "unknown", "unknown", "unknown", "unknown", []

# ==========================================
# 3-COLUMN LAYOUT
# ==========================================
left_col, main_col, right_col = st.columns([1.1, 2.2, 1.1])

# --- LEFT SIDEBAR (CREATOR BIO & STATS) ---
with left_col:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("🎧 About The Creator")
    st.write("Hi! I'm an 11th-grade student whose brain is fueled by a mix of Sanskrit roots, unread books, and terribly dry dad jokes.")
    st.markdown("---")
    st.subheader("🕹️ Engine Stats")
    st.write("Total Roots: 10 Active")
    st.write("Difficulty: 4th Grade Fun!")
    st.write("Grammar Engine: Pāṇinian Sūtras")
    st.markdown("</div>", unsafe_allow_html=True)

# --- MAIN CENTER COLUMN (CLEAN & FOCUSED) ---
with main_col:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.title("📜 Pāṇini's Magic Word Machine")
    st.write("Build ancient Sanskrit words like a fun puzzle!")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("🛠️ 1. Choose Your Word Root")
    r_choice = st.selectbox(
        "Select Root:", 
        ["bhū", "paṭh", "gam", "ad", "kṛ", "vid", "as", "smar", "daś", "jñā"],
        label_visibility="collapsed"
    )

    meaning, gana, family, skt, latin, steps = get_root_data(r_choice)

    st.markdown("---")

    st.subheader("🎯 2. Guess the Sanskrit Word!")
    st.write(f"Can you guess the final Sanskrit word for root **{r_choice}** (*{meaning}*?)")

    user_guess = st.text_input("Type your guess here:", placeholder="e.g. bhavati")

    if st.button("✨ CHECK MY GUESS"):
        cleaned_guess = user_guess.strip().lower()
        correct_latin = latin.lower()
        
        if cleaned_guess == correct_latin or user_guess.strip() == skt:
            st.balloons()
            st.success(f"🎉 **Spot on!** The correct word is **{skt} ({latin})**!")
        else:
            st.error(f"❌ Not quite! The correct word is **{skt} ({latin})**. Check the puzzle below!")

    st.markdown("---")

    st.subheader("⚡ 3. Build & Compile")
    if st.button("🔥 COMPILE WORD PUZZLE"):
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("✨ Generated Sanskrit Word ✨")
        st.markdown(f"<div class='sanskrit-text'>{skt}</div>", unsafe_allow_html=True)
        st.write(f"({latin})")
        st.markdown("---")
        st.write(f"**Meaning:** {meaning}  |  **Group:** {gana}")
        st.write(f"**Word Family:** {family}")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("🧩 Step-by-Step Word Puzzle")
        for s in steps:
            st.markdown(f"- {s}")
        st.markdown("</div>", unsafe_allow_html=True)
    if r_choice in COGNATE_DATABASE:
        data = COGNATE_DATABASE[r_choice]
        st.markdown("---")
        st.subheader("🌐 The Cross-Linguistic Time Machine")
        st.write("🧠 *Look how this exact root sound traveled down through history into words you use today:*")
        st.markdown(f"""
        <div class="glass-card" style="border-left: 4px solid #FDE047; padding-top: 10px; padding-bottom: 10px;">
            <p style="margin: 0 0 8px 0; font-size: 15px;">⏳ <b>4000 BCE Base (Proto-Indo-European):</b> <code style="color: #FBCFE8; background: transparent;">{data['pie']}</code></p>
            <p style="margin: 0 0 8px 0; font-size: 15px;">📜 <b>400 BCE Your Machine Form (Sanskrit):</b> <span style="color: #FDE047; font-weight: bold;">{skt}</span></p>
            <p style="margin: 0 0 8px 0; font-size: 15px;">🏛️ <b>100 CE Classical Latin Branch:</b> <span style="color: #E2E8F0;">{data['latin']}</span></p>
            <p style="margin: 0 0 4px 0; font-size: 15px;">🚀 <b>2026 CE Modern Day Equivalents:</b></p>
            <ul style="margin: 0 0 0 20px; padding: 0; font-size: 14px;">
                <li style="margin-bottom: 4px;"><b>English:</b> <span style="color: #93C5FD; font-weight: bold;">{data['english']}</span></li>
                <li><b>Hindi:</b> <span style="color: #86EFAC; font-weight: bold;">{data['hindi']}</span></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div class='glass-card' style='border: 2px solid #E11D48;'>", unsafe_allow_html=True)
        st.subheader("🏆 MASTER PUZZLE CARD")
        st.write(f"**Seed Root:** {r_choice} ({meaning})")
        st.write(f"**Final Word:** {skt} ({latin})")
        st.markdown("---")
        st.markdown("<p style='text-align:center; font-weight:bold; color:#FBCFE8; margin-bottom:0;'>100% Kid-Friendly & Dad-Joke Certified 🚀</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- RIGHT SIDEBAR ---
with right_col:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("🌟 Daily Challenge")
    st.write("Did you know root **'bhū'** is shared across dozens of languages to mean 'to be'?")
    st.markdown("---")
    st.subheader("🧠 Brain Teaser")
    st.write("Can you find which root means 'to eat' without looking at the menu? (Hint: It has 2 letters!)")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("🚀 Quick Links")
    st.caption("✨ Devanagari Active\n\n🎮 Guess Game Ready\n\n📜 Sūtra Logs Online")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #FBCFE8;'>*Developed with side widgets, kid-friendly explanations, and 100% error-free stability.* ✨</p>", unsafe_allow_html=True)
# ==========================================
# UNIVERSAL AI ETYMOLOGY SEARCH ENGINE
# ==========================================
from huggingface_hub import InferenceClient

st.markdown("---")
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.subheader("🔮 Universal Reverse Etymology Engine")
st.write("✨ *Type ANY word from ANY language to trace it back to its ancient Sanskrit or Indo-European root:*")

search_input = st.text_input("Type a modern word here:", placeholder="E.g., Madre, Vision, Mother, ज्ञान, Frère").strip()

if search_input:
    with st.spinner("🧠 AI Agent tracing linguistic footprints through time..."):
        try:
            # Initialize a free, high-speed open-source meta-llama AI client
            client = InferenceClient()  
            prompt = f"""
            You are an expert computational linguist specializing in historical linguistics, Paninian Sanskrit grammar, and Indo-European language trees.
            Analyze the word: '{search_input}'
            
            Provide a punchy, brief 3-sentence etymological trace back to its ancient Sanskrit root or Proto-Indo-European (PIE) cognate source. 
            Format the output beautifully with visual anchors like emojis. Keep it engaging, clear, and highly academic yet accessible.
            """
            
            response = ""
            for message in client.chat_completion(
                messages=[{"role": "user", "content": prompt}],
                max_tokens=250,
                stream=True,
            ):
                response += message.choices[0].delta.content
            
            st.success(f"🎯 **Linguistic Trace Complete for '{search_input}':**")
            st.markdown(f"""
            <div style="background-color: rgba(255,255,255,0.03); padding: 15px; border-radius: 6px; border-left: 3px solid #FDE047; font-size: 15px; color: #E2E8F0;">
                {response}
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error("🤖 The AI pipeline is temporarily busy updating its manuscripts. Let's try compiling again in a moment!")

st.markdown("</div>", unsafe_allow_html=True)
