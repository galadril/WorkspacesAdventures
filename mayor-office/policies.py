import random

# Updated City policies (modernized priorities)
POLICIES = [
    "Implement a citywide solar energy program.",
    "Provide free public transportation for students and seniors.",
    "Ban single-use plastics in all businesses.",
    "Create more green spaces for public enjoyment.",
]

def get_policies():
    """
    Retrieve the list of active policies.
    """
    return POLICIES

def generate_speech(randomize=False):
    """
    Generate the mayor's speech based on current policies.
    Optionally randomize the order of policies for fun speeches.
    Simulate random failures to match the broken system described.
    """
    # Randomly break the system (simulate random failure)
    if random.random() < 0.2:  # 20% chance to break the system
        raise Exception("Random failure: The system has crashed!")

    randomize_policies()

    speech_intro = "Greetings, citizens of Codetropolis! Here are our latest policies to improve our great city:\n"
    try:
        speech_body = "\n".join([f"- {policy}" for policy in get_policies()])
        speech_closing = "\nTogether, we can make Codetropolis thrive!"
        return speech_intro + speech_body + speech_closing
    except Exception as e:
        print("Error generating the mayor's speech:", e)
        return "Speech could not be generated. Please fix the issue."

def randomize_policies():
    """
    Randomly shuffle the policies (optional feature for fun speeches).
    """
    random.shuffle(POLICIES)

if __name__ == "__main__":
    try:
        print("\nGenerating a speech with potential failure...\n")
        print(generate_speech())
    except Exception as e:
        print(f"Oops! Something went wrong: {e}")
