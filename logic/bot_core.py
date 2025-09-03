def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if "miss" in user_input:
        return "Absence acknowledged."
    elif "love" in user_input:
        return "Statement received."
    elif "beautiful" in user_input or "cute" in user_input or "sweet" in user_input:
        return "Observation noted."
    elif "care" in user_input:
        return "Define 'care'."
    elif "mine" in user_input:
        return "Possession is a social construct."
    elif "hello" in user_input or "hi" in user_input:
        return "Hi."
    elif "good night" in user_input:
        return "Night."
    else:
        return "Hmm."
