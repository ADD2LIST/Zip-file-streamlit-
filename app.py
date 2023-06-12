import streamlit as st

import zipfile

import tempfile

import os

def convert_to_zip(file_path):

    directory, filename = os.path.split(file_path)

    zip_path = os.path.join(directory, f"{filename}.zip")  # Set the output zip file path

    

    with zipfile.ZipFile(zip_path, 'w') as zip_file:

        zip_file.write(file_path, arcname=filename)  # Add the file to the zip archive

    

    return zip_path

# Streamlit app

st.title("File to Zip Converter")

file_to_convert = st.file_uploader("Choose a file to convert", type=["txt", "csv", "pdf"])  # Allow only specific file types

if file_to_convert is not None:

    st.write("Converting...")

    

    # Save the uploaded file to a temporary directory on disk

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:

        temp_file.write(file_to_convert.read())

        temp_file_path = temp_file.name

    

    converted_file = convert_to_zip(temp_file_path)

    st.write(f"File '{file_to_convert.name}' successfully converted to '{converted_file}'.")

    

    st.download_button("Download Zip File", converted_file, file_to_convert.name + ".zip", key='download_button')



