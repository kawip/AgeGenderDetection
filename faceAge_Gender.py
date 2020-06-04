# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:10:56 2020

@author: kawisara.n
"""
import streamlit as st
import cv2
from PIL import Image, ImageOps
import numpy as np
from detect import detect_all

LANG = {
    "TH": [
        "**อัพโหลดรูปหน้าของคนที่คุณต้องการเช็คอายุและเพศ**",  # 0
        "อัพโหลดรูปภาพที่หนึ่ง...",  # 1
        "รูปภาพที่อัพโหลด",  # 2
        "**ผลลัพธ์คือ**",  # 3
    ],
    "EN": [
        "**Upload face image that you would like to check for age and gender.**",  # 0
        "Upload the 1st image...",  # 1
        "Uploaded Image.",  # 2
        "**The result is**",  # 3
    ],
}

def load_image_and_preprocess(image_filepath, resize_wh=(720, 720)):
    image = Image.open(image_filepath).convert('RGB')
    image = ImageOps.exif_transpose(image)
    image.thumbnail(resize_wh, Image.ANTIALIAS)
    return image    

language = st.checkbox("Thai Language")
st.title("*Face Gender & Age* :dart:")
if language:
    t = LANG["TH"]
else:
    t = LANG["EN"]

st.write(t[0])
uploaded_file = st.file_uploader('', type=("png", "jpg", "jpeg"))

if uploaded_file is not None:
    try:
        image = load_image_and_preprocess(uploaded_file)
        st.image(image, caption=t[2], use_column_width=True)
    except Exception as e:
        st.text("loading/processing img1 failed")
    if image:
        opencvImage = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        resultImg = detect_all(opencvImage)
        st.write(t[3])
        resultImg = cv2.cvtColor(resultImg, cv2.COLOR_BGR2RGB)
        st.image(resultImg, use_column_width=True)
