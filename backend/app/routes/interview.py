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


# from fastapi import APIRouter
# from app.services.llm_service import InterviewLLM
# from app.services.evaluation_service import evaluate_candidate
# from app.utils.prompts import SYSTEM_PROMPT

# router = APIRouter(
#     prefix="/interview",
#     tags=["Interview"]
# )

# # Initialize LLM
# llm = InterviewLLM()

# # Interview Questions
# questions = [
#     "Explain fractions to a 9-year-old.",
#     "A student says they don't understand a problem after trying for 5 minutes. What would you do?",
#     "How do you keep children engaged during online learning?",
#     "A student gives a wrong answer confidently. How would you respond?",
#     "How do you make math fun for kids?"
# ]

# # Conversation memory
# conversation = []

# # Question tracker
# question_index = 0


# @router.get("/start")
# def start_interview():
#     global conversation
#     global question_index

#     # Reset interview
#     conversation = [
#         {"role": "system", "content": SYSTEM_PROMPT}
#     ]

#     question_index = 0

#     first_question = questions[question_index]

#     conversation.append({
#         "role": "assistant",
#         "content": first_question
#     })

#     return {"question": first_question}


# @router.post("/answer")
# def answer(user_answer: str):
#     global question_index

#     # Save user answer
#     conversation.append({
#         "role": "user",
#         "content": user_answer
#     })

#     question_index += 1

#     # If interview finished → evaluate
#     if question_index >= len(questions):

#         evaluation = evaluate_candidate(conversation)

#         return {
#             "message": "Interview complete",
#             "evaluation": evaluation
#         }

#     # Otherwise generate follow-up
#     reply = llm.generate_response(conversation)

#     conversation.append({
#         "role": "assistant",
#         "content": reply
#     })

#     next_question = questions[question_index]

#     conversation.append({
#         "role": "assistant",
#         "content": next_question
#     })

#     return {
#         "follow_up": reply,
#         "next_question": next_question
#     }