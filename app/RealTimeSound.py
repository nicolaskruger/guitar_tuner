import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from streamThread import streamThread
from audioData import audioData
# pegar frequencias de 250 - 10000

plt.style.use('fivethirtyeight')

st = streamThread()
st.start()

def getChunck(i):
    global st
    data = st.getData()
    if data == "":
        return 0
    auData = audioData(data,st.chunk,st.fs,np.int16,70,400)
    plt.cla()
    
    label = str(auData.getMaxF())
    plt.plot(auData.frq,auData.dfft,label= label)
    plt.xlabel(label)
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(),getChunck, interval=20)


plt.tight_layout()
plt.show()