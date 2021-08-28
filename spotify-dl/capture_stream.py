import wave
import pyaudio
import numpy as np
from pydub import AudioSegment, silence

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"
MP3_OUTPUT_FILENAME = "output.mp3"

p = pyaudio.PyAudio()

print("Press any key to begin")
input()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("* Recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    raw_data = stream.read(CHUNK)
    data = np.frombuffer(raw_data, dtype=np.int16)
    frames.append(data)

# while 1:
#     data = stream.read(CHUNK)
#     frames.append(data)


print("* Done recording")

stream.stop_stream()
stream.close()


p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

music = AudioSegment.from_wav("output.wav")
music_nonsilent = silence.detect_nonsilent(music)
music_nonsilent.export(MP3_OUTPUT_FILENAME, format="mp3")
