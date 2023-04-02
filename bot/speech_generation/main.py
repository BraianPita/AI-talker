from TTS.api import TTS
import pyaudio  
import wave

# Running a multi-speaker and multi-lingual model

# List available 🐸TTS models and choose the first one
# model_name = TTS.list_models()[0]

# # Init TTS
# tts = TTS(model_name)
# # Run TTS
# # ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
# # Text to speech to a file
# tts.tts_to_file(text="Hey guys, how are you doing today?", speaker=tts.speakers[0], language=tts.languages[0], file_path="output.wav")




# voice from sample
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)

def generate_speech(text):
    tts.tts_to_file(text, speaker_wav="vtuber_voice_short.wav", language="en", file_path="output.wav")


def play_audio(output_index):
    #define stream chunk   
    chunk = 1024  

    #open a wav format music  
    f = wave.open(r"output.wav","rb")  
    #instantiate PyAudio  
    p = pyaudio.PyAudio()  
    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True,
                    output_device_index=output_index)  
    #read data  
    data = f.readframes(chunk)  

    #play stream  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  

    #stop stream  
    stream.stop_stream()  
    stream.close()  

    #close PyAudio  
    p.terminate()  


