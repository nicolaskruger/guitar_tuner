import numpy as np
from matplotlib.animation import FuncAnimation
from streamThread import streamThread
from audioData import audioData
from getDevices import getIndexLike
from myPlt import myPlt

# pegar frequencias de 250 - 10000

mPlt = myPlt()

device = "Microsoft"

st = streamThread(index_device=getIndexLike(device))
st.start()

def getChunck(i):
    global st
    global mPlt
    data = st.getData()
    if data == "":
        return 0
    auData = audioData(data,st.chunk,st.fs,np.int16,70,400)
    mPlt.setPl(auData.frq,auData.dfft,auData.getMaxF())

ani = FuncAnimation(mPlt.pl.gcf(),getChunck, interval=20)

mPlt.show()