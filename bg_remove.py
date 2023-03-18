from io import BytesIO

import streamlit as st
from PIL import Image
from rembg import remove


st.set_page_config(layout="wide", page_title="Nyoba Masbro")

st.write("## Project1")
st.write(
    ":dog: Akan menghapus background foto secara cepat dengan kualitas yang maksimal...!!!"
)
st.sidebar.write("## Upload dan download :gear:")

# Create the columns
col1, col2 = st.columns(2)

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Package the transform into a function
def fix_image(upload):
    image = Image.open(upload)
    col1.write("Gambar awal:camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Hasil :sparkles:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button(
        "Download Hasilnya...", convert_image(fixed), "fixed.png", "image/png"
    )

# Create the file uploader
my_upload = st.sidebar.file_uploader("Upload Foto", type=["png", "jpg", "jpeg"])

# Fix the image!
if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("./apel.jpg")