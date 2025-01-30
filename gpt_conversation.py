import openai

openai.api_key = "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"

def generate_examiner_response(user_input):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"The following is a conversation between an IELTS examiner and a candidate. The candidate says: '{user_input}'. Respond as an examiner.",
        max_tokens=150
    )
    return response.choices[0].text.strip()
