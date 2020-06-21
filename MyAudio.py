import pyaudio
import wave, os
import speech_recognition as speech_recog
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"
audio = pyaudio.PyAudio()
recog = speech_recog.Recognizer()
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print("recording...")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    print("finished recording")
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
os.system("afplay file.wav")
sample_audio = speech_recog.AudioFile('file.wav')
with sample_audio as audio_file:
    audio_content = recog.record(audio_file)
command = recog.recognize_google(audio_content, language="ru-RU")
print('You said: ' + command)
