# 🎨 Background Remover

This project allows you to remove the background from an image and combine it with a new background of your choice. Using the **rembg** library for background removal and **Streamlit** for the interactive web interface, this app enables users to upload an image, remove its background, and then overlay it onto a new background image.

## Features

- Upload a foreground image (e.g., a person, object) with a background that you want to remove.
- Upload a new background image that will be used to replace the removed background.
- The app removes the background from the foreground image and resizes the background image to match the foreground's dimensions.
- The foreground and background images are then combined into a new image.
- Download the final image with the background replaced.

## Requirements

- Python 3.6+
- Streamlit
- rembg
- Pillow
- onnxruntime

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/background-remover.git
   cd background-remover

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the Streamlit app:
    ```bash
    streamlit run app.py


## How It Works

- __Upload Foreground Image:__ Upload the image from which the background will be removed.
- __Upload Background Image:__ Upload the image that you want to use as the new background.
- __Background Removal:__ The foreground image's background is automatically removed using the rembg library.
- __Image Resizing and Combination:__ The background is resized to match the size of the foreground image. The two images are then combined.
- __Download:__ After the images are combined, you can download the new image with the replaced background.


## Usage
- Visit the Streamlit app in your browser.
- Upload both the foreground and background images.
- Wait for the process to complete.
- Download the final image with the new background.

## Acknowledgements
- Streamlit for building the interactive web application ❤️‍🔥
- rembg for background removal 💙
- Pillow for image processing 🩷

