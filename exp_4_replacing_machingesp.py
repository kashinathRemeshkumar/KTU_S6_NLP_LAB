import re

text="this is a sample sentence with 123 and !@#"

def replace(pattern,replacement,text):
    return re.sub(pattern,replacement,text)

pattern=r'\d+'
replacement='NUMBERS'
print(f'original text \n{text}')
new_text=replace(pattern,replacement,text)
print(new_text)

pattern=r'([!@#])+'
replacement='SYMBOLS'
print(replace(pattern,replacement,new_text))