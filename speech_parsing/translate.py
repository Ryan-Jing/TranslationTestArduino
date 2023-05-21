import openai
import os
import config
import time

openai.api_key = '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'
pretranslate_file_path = 'transcriptions/transcriptions.txt'
previous_word = ''

print("Translated Text:")

while True:
    with open(pretranslate_file_path, 'r') as file:
        pretranslate_text = file.read()
        pretranslate_result = pretranslate_text.split()

    if pretranslate_result and pretranslate_result[-1] != previous_word:
        # send the new word using ser.write()
        prompt = f'Translate this into 1. French: \n\n{pretranslate_result[-1]}\n\n'

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.3,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        translated_text = response.choices[0].text.strip()

        with open(config.TRANSLATE_FILE, 'a') as f:
            f.write(translated_text.text)

        print(translated_text)
        previous_word = pretranslate_result[-1]  # update previous_word
        time.sleep(0.5)  # wait for 1 second before checking for updates again

