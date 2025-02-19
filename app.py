import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("🎨 Background Swap")

# Request user to upload images
uploaded_foreground = st.file_uploader("Upload the foreground image", type=["png", "jpg", "jpeg"])
uploaded_background = st.file_uploader("Upload the background image", type=["png", "jpg", "jpeg"])

if uploaded_foreground and uploaded_background:
    # Open the images
    foreground = Image.open(uploaded_foreground).convert("RGBA")
    background = Image.open(uploaded_background).convert("RGBA")

    # Remove the background
    no_bg = remove(foreground)

    # Resize the background to match the foreground
    background = background.resize(no_bg.size)

    # Combine the images
    combined = Image.alpha_composite(background, no_bg)

    # Display the result
    st.image(combined, caption="New Image", use_container_width=True)

    # Provide download option
    img_byte_arr = io.BytesIO()
    combined.save(img_byte_arr, format="PNG")
    st.download_button("📥 Download Image", data=img_byte_arr.getvalue(), file_name="combined_image.png", mime="image/png")
