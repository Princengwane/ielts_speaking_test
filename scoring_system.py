# scoring_system.py

def score_grammar(text):
    # Simple grammar scoring based on word count
    words = text.split()
    return min(len(words) // 5, 9)  # Simple formula for grammar score

def score_fluency(text):
    # Dummy fluency score (can be expanded)
    return 8  # Placeholder for fluency assessment

def provide_feedback(user_input):
    # Get feedback based on user input
    grammar_score = score_grammar(user_input)
    fluency_score = score_fluency(user_input)

    return {
        'grammar_score': grammar_score,
        'fluency_score': fluency_score,
    }
