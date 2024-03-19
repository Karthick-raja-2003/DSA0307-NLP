import re

def recognize_dialog_acts(utterance):
    if re.match(r'^[A-Z][\w\s,\'-]*[.!?]$', utterance):
        return "Statement"
    elif re.match(r'^[A-Za-z][\w\s,\'-]*\?$', utterance):
        return "Question"
    elif re.match(r'^[A-Z][\w\s,\'-]*\!$', utterance):
        return "Exclamation"
    elif re.match(r'^[A-Za-z][\w\s,\'-]*\.\.\.$', utterance):
        return "Ellipsis"
    else:
        return "Unknown"

def main():
    conversation = [
        "Hello, how are you?",
        "I'm doing well, thank you!",
        "That's good to hear.",
        "Are you ready to start?",
        "Yes, I'm ready.",
        "Let's begin..."
    ]
    
    for utterance in conversation:
        dialog_act = recognize_dialog_acts(utterance)
        print(f"'{utterance}' is a {dialog_act}")

if __name__ == "__main__":
    main()
