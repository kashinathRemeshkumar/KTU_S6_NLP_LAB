import asyncio
from googletrans import Translator

async def translate_text():
    translator = Translator()
    text = 'i am a student'
    to_lang ='ja'

    result = await translator.translate(text, src='en', dest=to_lang)
    print("Translated Text:", result.text)

    

# Run the async function
asyncio.run(translate_text())


#എന്തോ വസ്തു

