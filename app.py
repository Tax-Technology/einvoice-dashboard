import streamlit as st
import requests
import tempfile
import os

# Custom CSS for responsiveness and better appearance
st.markdown(
    """
    <style>
    /* Base styles */
    body {
        margin: 0;
        padding: 0;
    }
    .title {
        font-size: 2.5rem; /* Adjusted for responsive scaling */
        color: #FFFFFF;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 1.5rem;
        color: #555555;
        text-align: center;
        margin-bottom: 20px;
    }
    .success, .error {
        font-size: 1rem;
        font-weight: bold;
        text-align: center;
    }
    .success {
        color: green;
    }
    .error {
        color: red;
    }
    .center {
        text-align: center;
    }
    /* Responsive design for smaller screens */
    @media (max-width: 768px) {
        .title {
            font-size: 2rem; /* Smaller font size for tablets and phones */
        }
        .subtitle {
            font-size: 1.2rem;
        }
        .success, .error {
            font-size: 0.9rem;
        }
    }
    @media (max-width: 480px) {
        .title {
            font-size: 1.5rem; /* Further reduced for small phones */
        }
        .subtitle {
            font-size: 1rem;
        }
        .success, .error {
            font-size: 0.8rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit app title
st.markdown('<div class="title">📄 e-Invoice XML to PDF Invoice Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Easily transform your e-Invoices into professional PDF Invoices 🚀</div>', unsafe_allow_html=True)

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