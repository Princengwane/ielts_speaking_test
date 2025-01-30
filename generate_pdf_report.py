from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(user_input, examiner_response, feedback):
    filename = "ielts_speaking_test_report.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, f"IELTS Speaking Test Report")
    c.drawString(100, 730, f"User Input: {user_input}")
    c.drawString(100, 710, f"Examiner Response: {examiner_response}")
    c.drawString(100, 690, f"Grammar Score: {feedback['grammar_score']}")
    c.drawString(100, 670, f"Fluency Score: {feedback['fluency_score']}")
    c.save()
