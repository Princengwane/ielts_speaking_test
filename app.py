from flask import Flask, render_template, request, jsonify
from speech_to_text import transcribe_audio
from gpt_conversation import generate_examiner_response
from generate_pdf_report import generate_pdf_report

app = Flask(__name__)

# Route for the main page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route to process audio (convert to text, generate examiner response, and create PDF report)
@app.route('/process_audio', methods=['POST'])
def process_audio():
    file = request.files['audio']
    file_path = "user_audio.wav"
    file.save(file_path)

    # Convert speech to text
    user_input = transcribe_audio(file_path)

    # Get the AI response (examiner)
    examiner_response = generate_examiner_response(user_input)

    # Provide feedback (grammar, fluency, etc.)
    feedback = provide_feedback(user_input)

    # Generate PDF report
    pdf_filename = generate_pdf_report(user_input, examiner_response, feedback)

    return jsonify({
        'user_input': user_input,
        'examiner_response': examiner_response,
        'pdf_filename': pdf_filename
    })

# Provide simple feedback (for example purposes)
def provide_feedback(user_input):
    grammar_score = score_grammar(user_input)
    fluency_score = score_fluency(user_input)

    return {
        'grammar_score': grammar_score,
        'fluency_score': fluency_score,
    }

def score_grammar(text):
    words = text.split()
    return min(len(words) // 5, 9)  # Dummy logic: score based on word count

def score_fluency(text):
    return 8  # Placeholder for real fluency assessment

# Route to generate and download PDF report
@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    data = request.json
    filename = generate_pdf_report(data['user_input'], data['examiner_response'], data['feedback'])
    
    return jsonify({"message": f"PDF saved as {filename}"})


if __name__ == '__main__':
    app.run(debug=True)
