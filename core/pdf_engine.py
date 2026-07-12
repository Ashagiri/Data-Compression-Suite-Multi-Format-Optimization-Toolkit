from pypdf import PdfReader, PdfWriter
import io

def compress_pdf(pdf_bytes):
    reader = PdfReader(io.BytesIO(pdf_bytes))
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    for page in writer.pages:
        page.compress_content_streams()

    out_buffer = io.BytesIO()
    writer.write(out_buffer)
    return out_buffer.getvalue()