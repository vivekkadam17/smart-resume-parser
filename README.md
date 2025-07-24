#  Smart Resume Parser

Smart Resume Parser is a simple and elegant web app built using **Streamlit** that allows users to upload resumes in PDF or DOCX format and extracts key information such as name, email, education, skills, and more using a custom natural language processing (NLP) pipeline.


##  Features

- Upload resumes in `.pdf` or `.docx` format.
- Automatically extracts structured information:
  - 👤 Name
  - 📧 Email
  - 💼 Skills
  - 🎓 Education
- Clean and modern UI with responsive layout.
- Download the extracted data as `.json` or `.csv`.
- Custom styling and theme using embedded CSS.

---

##  Tech Stack

- **Python**
- **Streamlit** for frontend interface
- **Pandas** for data formatting
- **JSON** for structured output
- **Custom NLP methods** (can be extended with spaCy, NLTK, etc.)

---

## 📁 Folder Structure

Smart-Resume-Parser/
├── app.py # Main Streamlit application
├── parser/
│ ├── extract_text.py # Handles text extraction from PDF/DOCX
│ ├── preprocess.py # Cleans raw text
│ └── extractor.py # Extracts structured info like Name, Email, etc.
├── uploads/ # Folder to store uploaded resumes
├── outputs/ # Folder to save parsed JSON and CSV outputs
├── images/ # (Optional) Screenshots or logos
├── requirements.txt # Python dependencies
└── README.md # Project documentation 

