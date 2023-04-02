import speech_recognition as sr
import tempfile
import os

temp_dir = tempfile.mkdtemp()
save_path = os.path.join(temp_dir, "temp.wav")
r = sr.Recognizer()


def transcribe_voice():
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Done")

    try:
        return r.recognize_whisper(audio, language="english")
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Whisper")


# def check_stop_word(predicted_text: str, stop_word: str) -> bool:
#     import re
#     pattern = re.compile('[\W_]+', re.UNICODE)
#     return pattern.sub('', predicted_text).lower() == stop_word


# def transcribe_voice(model, language, stop_word):
#     # there are no english models for large
#     if model != "large" and language == 'english':
#         model = model + ".en"

#     audio_model = whisper.load_model(model)

#     with sr.Microphone(sample_rate=16000) as source:
#         print("Listening:")
#         while True:
#             # record audio stream into wav
#             audio = r.listen(source)
#             data = io.BytesIO(audio.get_wav_data())
#             audio_clip = AudioSegment.from_file(data)
#             audio_clip.export(save_path, format="wav")

#             if language == 'english':
#                 result = audio_model.transcribe(save_path, language='english')
#             else:
#                 result = audio_model.transcribe(save_path)

#             predicted_text = result["text"]

#             return predicted_text
#             # print("Text: " + predicted_text)

#             # if check_stop_word(predicted_text, stop_word):
#             #     break


# print(transcribe_voice("base", "english", stop_word=""))