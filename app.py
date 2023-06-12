import streamlit as st

import zipfile

def convert_to_zip(file_path):

    zip_path = file_path + ".zip"  # Set the output zip file path

    

    with zipfile.ZipFile(zip_path, 'w') as zip_file:

        zip_file.write(file_path, arcname=file_path)  # Add the file to the zip archive

    

    return zip_path

# Streamlit app

st.title("File to Zip Converter")

file_to_convert = st.file_uploader("Choose a file to convert", type=["txt", "csv", "pdf"])  # Allow only specific file types

if file_to_convert is not None:

    st.write("Converting...")

    converted_file = convert_to_zip(file_to_convert.name)

    st.write(f"File '{file_to_convert.name}' successfully converted to '{converted_file}'.")

    

    st.download_button("Download Zip File", file_to_convert.name + ".zip")

