import PyPDF2


def read_pdf(file):
    
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text.strip()

def read_txt(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    return text.strip()



