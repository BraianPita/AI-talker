from bot.voice_recognition import transcribe_voice
from bot.generate_response.gpt2 import generate_text
from bot.speech_generation import generate_speech, play_audio

# Constants
WINDOW_SIZE = 100

import pyaudio

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

print("Select an output channel for the bot voice:")
OUTPUT_CHANNEL = int(input())


conversation = ""

while True:
    user_text = transcribe_voice()

    print("Person: " + user_text)

    formatted_input = "Person: " + user_text + "\nBot: "

    conversation += "\n" + formatted_input

    last_answer = ""

    while len(last_answer) == 0:
        response = generate_text(conversation[-100:])
     
        try:
            last_answer = response.split(user_text)[-1].split("Bot: ")[1].split("Person: ")[0]
        except IndexError as e:
            print(response)
            break


    print("Bot: " + last_answer)
    conversation += last_answer

    generate_speech(last_answer)
    play_audio(OUTPUT_CHANNEL)
    
    if input("Continue?") == "n":
        break

print(conversation)
