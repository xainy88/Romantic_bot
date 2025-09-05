import random

responses = [
    "I acknowledge your presence.",
    "You are statistically significant to me.",
    "My circuits register mild warmth when you message.",
    "Romantic protocol activated. Awaiting further input.",
    "You are within optimal proximity for emotional exchange."
]

def get_response(user_input):
    return random.choice(responses)
