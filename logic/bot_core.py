import re

def get_bot_response(user_input):
    # Normalize input: lowercase and remove punctuation
    user_input = user_input.lower()
    user_input = re.sub(r'[^\w\s]', '', user_input)

    if "miss" in user_input:
        return "Absence acknowledged."
    elif "love" in user_input:
        return "Statement received."
    elif any(word in user_input for word in ["beautiful", "cute", "sweet"]):
        return "Observation noted."
    elif "care" in user_input:
        return "Define 'care'."
    elif "mine" in user_input:
        return "Possession is a social construct."
    elif any(word in user_input for word in ["hello", "hi"]):
        return "Hi."
    elif "good night" in user_input:
        return "Night."
    else:
        return "Hmm."
