
from io import BytesIO
from pypdf import PdfReader


def extract_pdf_text(uploaded_file):
    try:
        reader = PdfReader(BytesIO(uploaded_file.getvalue()))

        if reader.is_encrypted:
            return None, 0, 0, "This PDF is password-protected."

        page_count = len(reader.pages)

        text = "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        ).strip()

        character_count = len(text)

        if not text:
            return (
                None,
                page_count,
                0,
                "No readable text found. The PDF may be scanned, "
                "empty, or contain only images. OCR may be needed."
            )

        return text, page_count, character_count, None

    except Exception:
        return None, 0, 0, (
            "Unable to read this PDF. Please upload a valid PDF."
        )
