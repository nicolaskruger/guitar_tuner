import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from streamThread import streamThread
from audioData import audioData
from getDevices import getIndexLike
from afinado import afinador

# pegar frequencias de 250 - 10000

plt.style.use('fivethirtyeight')

device = "Microsoft"

st = streamThread(index_device=getIndexLike(device))
st.start()

def getChunck(i):
    global st
    data = st.getData()
    if data == "":
        return 0
    auData = audioData(data,st.chunk,st.fs,np.int16,70,400)
    plt.cla()
    
    # label = str(int(round(auData.getMaxF())))+" Hz"
    af = afinador(auData.getMaxF())
    label = af.getState()
    COLOR = 'blue'
    
    if af.getAfinado():
        plt.plot(auData.frq,auData.dfft,label= label, color="green")
    else:
        plt.plot(auData.frq,auData.dfft,label= label, color="red")

    plt.xlabel(label)
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(),getChunck, interval=20)


plt.tight_layout()
plt.show()