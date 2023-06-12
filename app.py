import streamlit as st

import zipfile

def convert_file_to_zip(file_path):

  """Converts a file to a zip file.

  Args:

    file_path: The path to the file to convert.

  Returns:

    A zip file object.

  """

  with zipfile.ZipFile(file_path + ".zip", "w") as zip_file:

    zip_file.write(file_path)

def main():

  """The main function of the Streamlit application."""

  # Get the file to convert.

  file_path = st.file_uploader("Upload a file", type=["*"])

  # If a file was uploaded, convert it to a zip file and provide a download option.

  if file_path is not None:

    with open(file_path, "rb") as f:

      zip_file = convert_file_to_zip(f.name)

    st.download_button(

      label="Download Zip File",

      data=zip_file,

      file_name=file_path.name + ".zip"

    )

if __name__ == "__main__":

  main()


    
