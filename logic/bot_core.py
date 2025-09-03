def get_bot_response(user_input):
    responses = {
        "i love you": "Okay.",
        "i miss you": "Noted.",
        "are you mine?": "If you say so.",
        "good night": "Night.",
        "hello": "Hi.",
        "how are you?": "Functional.",
        "do you care?": "Unclear.",
    }

    user_input = user_input.lower().strip()
    return responses.get(user_input, "Hmm.")
