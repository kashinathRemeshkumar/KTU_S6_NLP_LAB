import re

def replace_match(match):
    return f"<NAME> {match.group()} </NAME>"


def tag_proper_name(text):
    pattern=r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*'

    matches=re.findall(pattern,text)

    tagged_text=re.sub(pattern,replace_match,text)

    return tagged_text,matches

text="Narendra Modi is the prime minister of India"

tagged_text,matches=tag_proper_name(text)
print(tagged_text)
print(matches)


