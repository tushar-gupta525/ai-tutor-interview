from fastapi import APIRouter
from app.services.llm_service import InterviewLLM
from app.utils.prompts import SYSTEM_PROMPT
from app.services.evaluation_service import evaluate_candidate

router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)

llm = InterviewLLM()

conversation = []


@router.get("/start")
def start_interview():

    global conversation

    conversation = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Start the tutor interview."}
    ]

    first_question = llm.generate_response(conversation)

    conversation.append({
        "role": "assistant",
        "content": first_question
    })

    return {"question": first_question}


@router.post("/answer")
def answer(user_answer: str):

    conversation.append({
        "role": "user",
        "content": user_answer
    })

    # Stop after ~5 questions
    user_answers = [m for m in conversation if m["role"] == "user"]

    if len(user_answers) >= 5:

        evaluation = evaluate_candidate(conversation)

        return {
            "message": "Interview complete",
            "evaluation": evaluation
        }

    reply = llm.generate_response(conversation)

    conversation.append({
        "role": "assistant",
        "content": reply
    })

    return {
        "next_question": reply
    }


