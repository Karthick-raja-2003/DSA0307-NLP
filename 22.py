import re

def resolve_references(text):
    references = {
        "he": "John",
        "she": "Mary",
        "it": "the book",
        # Add more reference mappings as needed
    }
    
    resolved_text = text
    for pronoun, reference in references.items():
        resolved_text = re.sub(r'\b' + pronoun + r'\b', reference, resolved_text, flags=re.IGNORECASE)
    
    return resolved_text

def main():
    text = """
    He went to the store. She bought a new dress. It was blue.
    """
    resolved_text = resolve_references(text)
    print(resolved_text)

if __name__ == "__main__":
    main()
