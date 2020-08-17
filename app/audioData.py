import numpy as np
class audioData(object):
    def __init__(self,audio,chunk,fs,tipe,min=0,max=-1):
        ad = np.frombuffer(audio,tipe)
        self.dfft = (abs(np.fft.rfft(ad)))
        n = len(self.dfft)
        t = chunk/fs
        k = np.arange(n)
        self.frq = k/t
        if max != -1:
            self.setFaixa(min,max)
        mx_ind= np.argmax(self.dfft)
        self.mxfr = self.frq[mx_ind]
    def setMin(self,min):
        c = self.getIndexPos(min)
        self.frq= self.frq[c:]
        self.dfft= self.dfft[c:]  
    def setMax(self,max):
        c = self.getIndexPos(max)
        self.frq= self.frq[:c]
        self.dfft= self.dfft[:c]  
    def setFaixa(self,min,max):
        self.setMin(min)
        self.setMax(max)
    def getIndexPos(self,num):
        cont = 0
        for v in self.frq:
            cont+=1
            if v >= num:
                return cont
        return -1
    def getMaxF(self):
        return self.mxfr
