import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from streamThread import streamThread
# pegar frequencias de 250 - 10000

plt.style.use('fivethirtyeight')

st = streamThread()
st.start()
def contNubmTo(vet,nub):
    cont = 0
    for v in vet:
        cont+=1
        if v >= nub:
            return cont
    return -1
def getChunck(i):
    global st
    data = st.getData()
    if data == "":
        return 0
    plt.cla()
    audi_data  = np.frombuffer(data,np.int16)
    dfft = (abs(np.fft.rfft(audi_data)))
    n = len(dfft)
    t = st.chunk/st.fs
    
    k = np.arange(n)
    frq = k/t
    c = contNubmTo(frq,70)
    frq= frq[c:]
    dfft= dfft[c:]
    
    c = contNubmTo(frq,500)
    frq= frq[:c]
    dfft= dfft[:c]
    mx_ind= np.argmax(dfft)
    mxfr = frq[mx_ind]
    # label = str(mx_ind)
    label = str(mxfr)
    plt.plot(frq,dfft,label= label)
    plt.xlabel(label)
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(),getChunck, interval=50)


plt.tight_layout()
plt.show()