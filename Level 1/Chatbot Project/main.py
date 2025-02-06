import json
from difflib import get_close_matches

# Load the knowledge base file from JSON
def load_knowledge_base(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            data: dict = json.load(file)
    except FileNotFoundError:
        data = {"questions": []}
    except json.JSONDecodeError:
        data = {"questions": []}
    return data

# Save the knowledge base to a JSON file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Find the best match from the dictionary
def find_best_matches(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

# Get an answer for a question
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

# Main script
def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    print("Bot: Hello! I am your chatbot. Ask me anything or type 'quit' to exit.")

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'quit':
            break
        best_match: str | None = find_best_matches(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Thank you! I learned a new response!')

if __name__ == '__main__':
    chat_bot()
