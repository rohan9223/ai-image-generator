import streamlit as st
from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO
from config import api_key
# Together.ai API Setup
client = OpenAI(
    api_key = api_key,  
    base_url="https://api.together.xyz/v1"
)

# App Title
st.set_page_config(page_title="AI Image Generator", layout="centered")
st.title("🎨 AI Image Generator (Text → Image)")

# ——— UI Inputs ———
with st.form("image_gen_form"):
    base_prompt = st.text_area(
        "📝 Base Prompt",
        placeholder="e.g. wearing an Instagram outfit in Canggu, Bali"
    )

    gender = st.selectbox("🚻 Gender", ["Any", "Male", "Female"])
    ethnicity = st.selectbox(
        "👩‍🎨 Model Ethnicity",
        ["Any", "White", "Asian", "African", "Hispanic", "Middle Eastern", "Mixed"]
    )
    age = st.selectbox(
        "🎂 Age Group",
        ["Any", "Child", "Teenager", "Adult", "Elderly"]
    )
    style = st.selectbox(
        "💄 Style",
        ["Any", "Studio", "Candid", "Editorial", "Vintage", "Futuristic", "Street"]
    )
    lighting = st.selectbox(
        "💡 Lighting",
        ["Any", "Natural", "Studio", "Moody", "High Contrast"]
    )
    background = st.selectbox(
        "🌅 Background",
        ["Any", "Urban", "Nature", "Beach", "Indoor", "Studio"]
    )
    size = st.selectbox("📐 Image Size", ["512x512", "768x768", "1024x1024"])

    submit = st.form_submit_button("✨ Generate Image")

# ——— On Generate ———
if submit:
    if not base_prompt:
        st.warning("Please enter a base prompt.")
    else:
        # Build detailed prompt
        parts = [base_prompt.strip()]
        if gender != "Any":
            parts.insert(0, gender)
        if ethnicity != "Any":
            parts.insert(1, ethnicity + " model")
        if age != "Any":
            parts.append(age)
        if style != "Any":
            parts.append(style + " style")
        if lighting != "Any":
            parts.append(lighting + " lighting")
        if background != "Any":
            parts.append(background + " background")
        detailed_prompt = ", ".join(parts)

        with st.spinner("Generating image..."):
            try:
                resp = client.images.generate(
                    model="black-forest-labs/FLUX.1-schnell-Free",
                    prompt=detailed_prompt,
                    size=size,
                    n=1
                )
                url = resp.data[0].url
                image = Image.open(BytesIO(requests.get(url).content))
                st.image(image, caption="🧠 AI‑Generated Image", use_container_width=True)
                st.success("Done! Right‑click or long‑press to save.")
                
            except Exception as e:
                error_msg = str(e)
                if "image may contain NSFW content" in error_msg:
                    st.error("🚫 Your prompt might contain sensitive or NSFW content. Please revise and try again.")
                else:
                    st.error(f"❌ Unexpected Error: {error_msg}")
