
# 📄 PDF Renamer Web App

This Streamlit web app allows you to upload multiple PDF files and automatically renames them using the embedded **Date** and **Submitted By** information found inside each file.

---

## ✅ Features

- 🔍 Extracts the correct **Date** (not Submission Date)
- 👤 Extracts submitter name (e.g., `Anderson, Maitland`)
- 📎 Renames files in the format: `YYYY-MM-DD_Lastname,Firstname.pdf`
- 📦 Lets you download all renamed PDFs as a single ZIP file

---

## 🚀 How to Use

1. Upload one or more PDF files using the file uploader
2. The app extracts info and shows renamed results
3. Click **Download All** to get a ZIP of renamed files

---

## 📂 Output Format

Example:
```
Input:  Report - Embedded Labour Shift Report - 348036.pdf
Output:  2025-04-22_Cormier,Ryan.pdf
```

---

## 🧪 Built With

- [Streamlit](https://streamlit.io/)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
