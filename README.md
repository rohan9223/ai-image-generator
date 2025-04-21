# AI Image Generator 🎨

A **Generative AI Image Generator** that transforms text prompts into beautiful images, powered by **FLUX.1-schnell-Free model** and built with **Streamlit**. Create stunning visual artwork from simple text descriptions.

## 🚀 Live Demo
Try it out here: [Insert your live demo link here]

---

## 📚 Features
- **Text-to-Image Generation**: Converts text prompts into detailed images.
- **Customizable Prompts**: Tailor your images by specifying attributes like gender, age, ethnicity, style, lighting, and more!
- **Multiple Image Sizes**: Choose between 512x512, 768x768, and 1024x1024 image resolutions for different needs.
- **Easy-to-Use Interface**: Input your text, adjust settings, and generate high-quality images in just a few clicks.

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Framework:** Streamlit  
- **API:** Together.ai (using FLUX.1-schnell-Free model for Text-to-Image generation)  
- **Libraries:** `streamlit`, `openai`, `requests`, `pillow`

---

## 🏗️ How to Run Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rohan9223/AI-Image-Generator.git
   cd AI-Image-Generator
2. **Install Required Libraries:**
   ```bash
   pip install streamlit openai requests pillow
3. **Run the App:**
   ```bash
   streamlit run app.py
## 🎨 Usage
- **Input Base Prompt**: Type in a description of the image you'd like to generate in the provided input box. For example: "sharp and trendy model in Buenos Aires wearing a tango-inspired dress/suit, colorful houses of La Boca neighborhood in the background".
- **Adjust Settings**: Use the dropdowns to customize various parameters of the image:
  - **Gender**: Choose from "Any", "Male", or "Female" to adjust the character's gender.
  - **Model Ethnicity**: Select from various ethnicities such as "White", "Asian", "African", "Hispanic", "Middle Eastern", etc.
  - **Age Group**: Pick the desired age range, such as "Child", "Teenager", "Adult", or "Elderly".
  - **Style**: Select from different artistic styles like "Studio", "Candid", "Vintage", "Futuristic", or "Street".
  - **Lighting**: Choose the lighting style for the image, like "Natural", "Studio", "Moody", etc.
  - **Background**: Choose from various background options, such as "Urban", "Nature", "Beach", or "Studio".
  - **Image Size**: Select the desired image resolution (512x512, 768x768, 1024x1024).
- **Generate Image**: Click the "✨ Generate Image" button to generate the image based on your inputs. The generated image will appear below the form once it’s ready.

---

## ⭐ Acknowledgments
- **Together.ai** for providing the **FLUX.1-schnell-Free model**, which is used for the text-to-image generation.
- **Streamlit** for simplifying the creation of interactive web applications.
- **Pillow** and **Requests** libraries for handling image generation and HTTP requests.

