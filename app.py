import streamlit as st
from utils import classify_image
from PIL import Image


# Apllication

st.set_page_config(
    page_title="MedNet",
    page_icon="⚕️",
    layout="wide"
)
#MainMenu {visibility: hidden;}
hide_streamlit_style = """
            <style>
            
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: #363677 ; margin-bottom: 35px'>Brief MedNet</h1>",
            unsafe_allow_html=True)

container1 = st.container()

with container1:
    st.markdown("<p style='text-align: left; color: #a4a7b3; margin-bottom: 150px; font-size: 1.5rem;'> Cette application permet de sélectionner un fichier image et de le télécharger :Puis elle permet d’obtenir sa classification. Les informations affichées sont « ID » qui correspond au numéro allant de 1 à 6 de la classe et « Class » qui correspond au nom de la classe. </p>",
            unsafe_allow_html=True)



container2 = st.container()



with container2:
    st.markdown("<h1 style='text-align: center; color: #a4a7b3; margin-bottom: px'>Upload image(s)</h1>",
            unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        "", accept_multiple_files=True, type=['jpg', 'jpeg', 'png'])

    if st.button('Upload'):
        if uploaded_files is not None:
            # Create a list to hold the images
            image_list = []
            image_names = []

            # Loop through the uploaded files and add them to the list
            for uploaded_file in uploaded_files:

                image_list.append(uploaded_file)
                image_names.append(uploaded_file.name)

            # Create a grid to display the images
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.subheader('')
                

            with col2:
                st.subheader('Images')
                for image in image_list:
                    #st.image(image, width=400)
                    st.image(image, use_column_width=True)

            with col3:
                st.subheader('Images names')
                st.markdown(f"<h3 style='color: #a4a7b3; padding-top:100px'></h3>",
                            unsafe_allow_html=True)
                for name in image_names:
                    st.markdown(f"*<h3 style='color: #a4a7b3;text-align: center; margin-bottom:200px'>{name}</h3>*",
                                unsafe_allow_html=True)

            with col4:
                st.subheader('Detected Xray Class')
                st.markdown(f"<h3 style='color: #a4a7b3; padding-top:150px'></h3>",
                            unsafe_allow_html=True)
                for image in image_list:
                     st.markdown(f"<h3 style='color: #a4a7b3;text-align: center; margin-bottom:200px'>{classify_image(image)}</h3>",
                                unsafe_allow_html=True)

            with col5:
                st.subheader('')