import streamlit as st
import requests
import tempfile
import os

# Streamlit app title
st.title("e-Invoice XML to PDF Invoice Generator")

# Upload XML file
uploaded_file = st.file_uploader("Upload your XML file", type=["xml"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xml") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    st.write("File uploaded successfully!")

    # Display the file name
    st.write(f"File name: {uploaded_file.name}")

    # Check XML validity via API
    st.write("Validating the XML file...")
    try:
        # Replace with your API endpoint for XML validation
        validation_api_url = "https://example.com/api/validate-xml"
        files = {"file": open(temp_file_path, "rb")}
        response = requests.post(validation_api_url, files=files)

        if response.status_code == 200:
            validation_result = response.json()

            if validation_result.get("is_valid"):
                st.success("The XML file is valid!")
                # Show a button to transform the XML into a PDF invoice
                if st.button("Generate PDF Invoice"):
                    st.write("Submitting the XML for transformation...")

                    # Replace with your API endpoint for XML to PDF transformation
                    transform_api_url = "https://example.com/api/transform-xml-to-pdf"
                    pdf_response = requests.post(transform_api_url, files=files)

                    if pdf_response.status_code == 200:
                        # Assume the response contains the PDF file
                        pdf_file_name = f"{os.path.splitext(uploaded_file.name)[0]}.pdf"
                        with open(pdf_file_name, "wb") as pdf_file:
                            pdf_file.write(pdf_response.content)

                        st.success("PDF Invoice generated successfully!")
                        # Provide a download link
                        st.download_button(
                            label="Download PDF Invoice",
                            data=pdf_response.content,
                            file_name=pdf_file_name,
                            mime="application/pdf"
                        )
                    else:
                        st.error("Failed to generate the PDF invoice. Please try again.")
            else:
                st.error("The XML file is invalid. Please upload a valid XML file.")
        else:
            st.error("Failed to validate the XML file. Please try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        # Cleanup: Remove the temporary file
        os.remove(temp_file_path)