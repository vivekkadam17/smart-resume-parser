import streamlit as st
import os
import json
import pandas as pd
from parser.extract_text import extract_text_from_pdf, extract_text_from_docx
from parser.preprocess import clean_text
from parser.extractor import extract_entities

# Page config
st.set_page_config(page_title="Smart Resume Parser", layout="wide", page_icon="📄")

# Custom CSS for modern design
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #e6f2ff;
    }
    .main-container {
        padding: 20px 60px;
        background-color: #ffffff;
        border-radius: 20px;
        box-shadow: 0px 4px 16px rgba(0,0,0,0.1);
        margin-top: 30px;
    }
    .title-style {
        font-size: 42px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle-style {
        font-size: 18px;
        color: #34495e;
        text-align: center;
        margin-bottom: 30px;
    }
    .upload-section {
        text-align: center;
        margin-bottom: 40px;
    }
    .footer {
        margin-top: 40px;
        text-align: center;
        font-size: 14px;
        color: #7f8c8d;
    }
    .report-box {
        padding: 25px;
        background-color: #f4faff;
        border: 1px solid #d9ecff;
        border-radius: 12px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Main content box
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title & Description
st.markdown('<div class="title-style">📄 Smart Resume Parser</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-style">Upload your resume and extract clean structured data like Name, Email, Skills, Education, etc.</div>', unsafe_allow_html=True)

# Upload Section
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("📤 Upload Resume File (.pdf or .docx)", type=["pdf", "docx"])
st.markdown('</div>', unsafe_allow_html=True)

# Process file
if uploaded_file:
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("🔍 Extracting text and parsing your resume..."):
        if uploaded_file.name.endswith(".pdf"):
            raw_text = extract_text_from_pdf(file_path)
        else:
            raw_text = extract_text_from_docx(file_path)

    clean = clean_text(raw_text)
    data = extract_entities(clean)

    # Display extracted information
    st.markdown('<div class="report-box">', unsafe_allow_html=True)
    st.subheader("📋 Extracted Resume Information")
    st.json(data)
    st.markdown('</div>', unsafe_allow_html=True)

    # Save files
    out_json = os.path.join("outputs", uploaded_file.name + ".json")
    with open(out_json, "w") as f:
        json.dump(data, f, indent=4)

    df = pd.DataFrame([data])
    out_csv = os.path.join("outputs", uploaded_file.name + ".csv")
    df.to_csv(out_csv, index=False)

    st.success("✅ Resume data parsed and saved successfully!")

    # Download buttons
    col1, col2 = st.columns(2)
    with col1:
        with open(out_json, "rb") as f:
            st.download_button("📥 Download JSON", f, file_name=uploaded_file.name + ".json", mime="application/json", use_container_width=True)
    with col2:
        with open(out_csv, "rb") as f:
            st.download_button("📥 Download CSV", f, file_name=uploaded_file.name + ".csv", mime="text/csv", use_container_width=True)

# Footer
st.markdown('<div class="footer">Developed with ❤️ by <strong>Boss</strong></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # Close main-container

