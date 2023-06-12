import streamlit as st

import PyPDF2

def lock_pdf(file, password):

    pdf = PyPDF2.PdfFileReader(file)

    pdf.encrypt(password)

    return pdf

def main():

    st.title("PDF Locker")

    # File upload

    st.header("Upload PDF")

    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    # Password input

    st.header("Set Password")

    password = st.text_input("Enter the password", type="password")

    if uploaded_file and password:

        locked_pdf = lock_pdf(uploaded_file, password)

        # Download the locked PDF file

        with st.beta_expander("Download Locked PDF"):

            st.download_button(

                label="Download",

                data=locked_pdf.stream(),

                file_name="locked_pdf.pdf",

                mime="application/pdf"

            )

if __name__ == "__main__":

    main()



      
