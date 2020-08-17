import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from streamThread import streamThread
plt.style.use('fivethirtyeight')

st = streamThread()
st.start()
def getChunck(i):
    global st
    data = st.getData()
    if data == "":
        return 0
    plt.cla()
    audi_data  = np.frombuffer(data,np.int16)
    dfft = abs(np.fft.rfft(audi_data))
    x = np.arange(len(dfft))
    plt.plot(x,dfft)
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(),getChunck, interval=100)


plt.tight_layout()
plt.show()