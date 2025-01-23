# policies.py

import random

# City policies (intentionally outdated)
POLICIES = [
    "Increase parking fines for hovercars.",
    "Ban robots from using public parks.",
    "Subsidize anti-gravity bikes for citizens.",
    "Introduce a curfew for drones after 10 PM.",
]

def get_policies():
    """
    Retrieve the list of active policies.
    """
    return POLICIES


def generate_speech():
    """
    Generate the mayor's speech based on current policies.
    """
    speech_intro = "Greetings, citizens of Codetropolis! Here are our latest policies to improve our great city:\n"
    try:
        speech_body = "\n".join([f"- {policy}" for policy in get_policies()])
        speech_closing = "\nTogether, we can make Codetropolis thrive!"
        return speech_intro + speech_body + speech_closing
    except Exception as e:
        print("Error generating the mayor's speech:", e)
        return "Speech could not be generated. Please fix the issue."


# Intentional bug: randomizing policies for speech (messing up order)
def randomize_policies():
    """
    Randomly shuffle the policies (currently unused).
    """
    random.shuffle(POLICIES)


if __name__ == "__main__":
    print(generate_speech())
