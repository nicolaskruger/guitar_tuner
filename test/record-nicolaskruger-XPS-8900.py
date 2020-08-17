import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
import time

def getData(in_data):
    audio_date = np.fromstring(in_data,np.int16)
    dfft = abs(np.fft.rfft(audio_date))
    x = np.arange(len(dfft))
    #x = np.arange(len(audio_date))
    plt.plot(x,dfft)
    #plt.pause(0.05)
    #print(audio_date)


chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True,
                input_device_index=5
                )

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk,exception_on_overflow=False)
    frames.append(data)
    #getData(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

getData(frames[20])
plt.show()
# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()