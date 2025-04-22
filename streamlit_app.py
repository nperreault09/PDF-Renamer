
import streamlit as st
import fitz  # PyMuPDF
import re
import zipfile
from io import BytesIO

st.set_page_config(page_title="PDF Renamer", layout="centered")

st.title("📄 PDF Renamer by Date and Submitter")
st.write("Drop multiple PDF files below. The app will rename them using the **Date** and **Submitted By** info inside each file (format: `YYYY-MM-DD_Lastname,Firstname.pdf`).")

uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

if uploaded_files:
    output_zip = BytesIO()
    with zipfile.ZipFile(output_zip, "w") as zf:
        for uploaded_file in uploaded_files:
            pdf_data = uploaded_file.read()
            doc = fitz.open(stream=pdf_data, filetype="pdf")
            text = ""
            for page in doc:
                text += page.get_text()

            name_match = re.search(r"Submitted By\s+([A-Za-z]+,\s*[A-Za-z]+)", text)
            all_date_matches = re.findall(r"\bDate\s+(\d{4}-\d{2}-\d{2})", text)
            date_str = all_date_matches[1] if len(all_date_matches) > 1 else None

            if date_str and name_match:
                name_str = name_match.group(1).replace(" ", "")
                new_filename = f"{date_str}_{name_str}.pdf"
                zf.writestr(new_filename, pdf_data)
                st.success(f"✅ {uploaded_file.name} → {new_filename}")
            else:
                st.error(f"❌ Failed to extract data from: {uploaded_file.name}")

    st.download_button("📦 Download All Renamed PDFs", output_zip.getvalue(), "renamed_pdfs.zip", "application/zip")
