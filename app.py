import streamlit as st
import requests
import tempfile
import os

# Custom CSS for better appearance
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 20px;
        color: #555555;
        text-align: center;
        margin-bottom: 20px;
    }
    .success {
        color: green;
        font-size: 18px;
        font-weight: bold;
    }
    .error {
        color: red;
        font-size: 18px;
        font-weight: bold;
    }
    .center {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit app title
st.markdown('<div class="title">📄 e-Invoice XML to PDF Invoice Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Easily validate and convert your XML files into professional PDF invoices 🚀</div>', unsafe_allow_html=True)

# Upload XML file
uploaded_file = st.file_uploader("📤 Upload your XML file", type=["xml"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xml") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    st.markdown('<p class="success center">✅ File uploaded successfully!</p>', unsafe_allow_html=True)

    # Display the file name
    st.write(f"**📁 File name:** {uploaded_file.name}")

    # Check XML validity via API
    st.write("🔍 Validating the XML file...")
    try:
        # Replace with your API endpoint for XML validation
        validation_api_url = "https://example.com/api/validate-xml"
        files = {"file": open(temp_file_path, "rb")}
        response = requests.post(validation_api_url, files=files)

        if response.status_code == 200:
            validation_result = response.json()

            if validation_result.get("is_valid"):
                st.markdown('<p class="success">✅ The XML file is valid!</p>', unsafe_allow_html=True)
                # Show a button to transform the XML into a PDF invoice
                if st.button("🧾 Generate PDF Invoice"):
                    st.write("📤 Submitting the XML for transformation...")

                    # Replace with your API endpoint for XML to PDF transformation
                    transform_api_url = "https://example.com/api/transform-xml-to-pdf"
                    pdf_response = requests.post(transform_api_url, files=files)

                    if pdf_response.status_code == 200:
                        # Assume the response contains the PDF file
                        pdf_file_name = f"{os.path.splitext(uploaded_file.name)[0]}.pdf"
                        with open(pdf_file_name, "wb") as pdf_file:
                            pdf_file.write(pdf_response.content)

                        st.markdown('<p class="success">🎉 PDF Invoice generated successfully!</p>', unsafe_allow_html=True)
                        # Provide a download link
                        st.download_button(
                            label="⬇️ Download PDF Invoice",
                            data=pdf_response.content,
                            file_name=pdf_file_name,
                            mime="application/pdf"
                        )
                    else:
                        st.markdown('<p class="error">❌ Failed to generate the PDF invoice. Please try again.</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="error">❌ The XML file is invalid. Please upload a valid XML file.</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="error">❌ Failed to validate the XML file. Please try again.</p>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<p class="error">❌ An error occurred: {e}</p>', unsafe_allow_html=True)
    finally:
        # Cleanup: Remove the temporary file
        os.remove(temp_file_path)