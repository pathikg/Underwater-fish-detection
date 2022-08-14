import os
import glob
from PIL import Image
import streamlit as st
from subprocess import call


def main():
    new_title = '<p style="font-size: 42px;">Welcome to Fish Detection App!</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)

    read_me = st.markdown("""
    This project was built using Streamlit to demonstrate YoloV7 model 
    """
                          )
    st.sidebar.title("Select Activity")
    choice = st.sidebar.selectbox(
        "MODE", ("About", "Fish Detection(Image)", "Fish Detection(Video)"))
    # ["Show Instruction","Landmark identification","Show the #source code", "About"]

    if choice == "Fish Detection(Image)":
        read_me_0.empty()
        read_me.empty()

        upload_image()

    elif choice == "Fish Detection(Video)":
        st.title('To be added soon...')

    elif choice == "About":
        print()


def upload_image():

    st.title('Fish Detection in Images')
    st.subheader("""
    Upload an image having fishes and let YoloV7 detect fishes....
    """)
    file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
    if file != None:
        placeholder = st.empty()
        img1 = Image.open(file)
        img1.save("source.jpg")
        placeholder.image(img1, caption="Uploaded Image")
        st.button("Detect Fish", on_click=detect_image(placeholder))


def detect_image(placeholder):
    """detects, stores and loads stored fish from the source image 

    Args:
        placeholder (_type_): st.empty()
    """

    with st.spinner('Detecting 🐟 🐠 🦈 🐡...'):
        call(["python", "./yolov7/detect.py", "--weights", "./weights/best.pt",
              "--conf-thres", "0.1", "--source", "source.jpg", "--no-trace" ,"--exist-ok", "--project", "detection", "--name", "output"])

        detected_img = glob.glob("./detection/output/**.jpg")[0]

        placeholder.empty()
        img = Image.open(detected_img)
        placeholder.image(img, caption="Fish Detection")


if __name__ == '__main__':
    main()
