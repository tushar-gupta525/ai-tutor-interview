import json
from app.services.llm_service import InterviewLLM

llm = InterviewLLM()


def evaluate_candidate(conversation):

    answers = []

    for msg in conversation:
        if msg["role"] == "user":
            answers.append(msg["content"])

    answers_text = "\n".join(answers)

    evaluation_prompt = f"""
Evaluate this tutor candidate based on their answers.

Candidate answers:
{answers_text}

Score from 1-10 for:
- communication clarity
- warmth
- patience
- simplicity of explanation
- english fluency

Return ONLY JSON in this format:

{{
"clarity": number,
"warmth": number,
"patience": number,
"simplicity": number,
"fluency": number,
"recommendation": "Proceed to next round or Reject"
}}
"""

    messages = [
        {"role": "system", "content": "You are an expert tutor interviewer."},
        {"role": "user", "content": evaluation_prompt}
    ]

    response = llm.generate_response(messages)

    try:
        evaluation = json.loads(response)
    except:
        evaluation = {
            "clarity": "N/A",
            "warmth": "N/A",
            "patience": "N/A",
            "simplicity": "N/A",
            "fluency": "N/A",
            "recommendation": "Parsing failed"
        }

    return evaluation