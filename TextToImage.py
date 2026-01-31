import streamlit as st
from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO
import os

# ===============================
# SECURITY: API KEY
# ===============================

# OLD (INSECURE)
# from config import api_key

# NEW (SECURE – ENV VAR)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set in environment variables")

# ===============================
# OPENAI CLIENT
# ===============================

# OLD (TOGETHER)
# client = OpenAI(
#     api_key=api_key,
#     base_url="https://api.together.xyz/v1"
# )

# NEW (OPENAI)
client = OpenAI(api_key=OPENAI_API_KEY)

# ===============================
# STREAMLIT APP
# ===============================

st.set_page_config(page_title="AI Image Generator", layout="centered")
st.title("🎨 AI Image Generator (Text → Image)")

# ===============================
# UI INPUTS
# ===============================

with st.form("image_gen_form"):
    st.markdown("### 📝 Prompt (Required)")
    base_prompt = st.text_area(
        "Describe what you want to generate *",
        placeholder="e.g. wearing an Instagram outfit in Canggu, Bali"
    )

    gender = st.selectbox("🚻 Gender (Optional)", ["Any", "Male", "Female"])
    ethnicity = st.selectbox("👩‍🎨 Model Ethnicity (Optional)", [
        "Any", "White", "Asian", "African", "Hispanic", "Middle Eastern", "Mixed"
    ])
    age = st.selectbox("🎂 Age Group (Optional)", [
        "Any", "Child", "Teenager", "Adult", "Elderly"
    ])
    style = st.selectbox("💄 Style (Optional)", [
        "Any", "Studio", "Candid", "Editorial", "Vintage", "Futuristic", "Street"
    ])
    lighting = st.selectbox("💡 Lighting (Optional)", [
        "Any", "Natural", "Studio", "Moody", "High Contrast"
    ])
    background = st.selectbox("🌅 Background (Optional)", [
        "Any", "Urban", "Nature", "Beach", "Indoor", "Studio"
    ])
    size = st.selectbox("📐 Image Size", ["512x512", "1024x1024"])

    submit = st.form_submit_button("✨ Generate Image")

# ===============================
# IMAGE GENERATION
# ===============================

if submit:
    if not base_prompt.strip():
        st.warning("❗ Prompt is required.")
    else:
        parts = [base_prompt.strip()]
        if gender != "Any":
            parts.insert(0, gender)
        if ethnicity != "Any":
            parts.append(f"{ethnicity} model")
        if age != "Any":
            parts.append(age)
        if style != "Any":
            parts.append(f"{style} style")
        if lighting != "Any":
            parts.append(f"{lighting} lighting")
        if background != "Any":
            parts.append(f"{background} background")

        detailed_prompt = ", ".join(parts)

        with st.spinner("Generating image..."):
            try:
                response = client.images.generate(
                    model="gpt-image-1",  # ✅ OpenAI Image Model
                    prompt=detailed_prompt,
                    size=size,
                    n=1
                )

                image_base64 = response.data[0].b64_json
                image_bytes = BytesIO(
                    __import__("base64").b64decode(image_base64)
                )

                image = Image.open(image_bytes)
                st.image(image, caption="🧠 AI-Generated Image", use_container_width=True)
                st.success("Done! Right-click or long-press to save.")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
