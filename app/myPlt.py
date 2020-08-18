import matplotlib.pyplot as plt
from afinado import afinador

class myPlt(object):
    def __init__(self):
        self.pl = plt
        self.pl.style.use('fivethirtyeight')
    def setPl(self,frq,dfft, max):
        self.pl.cla()
        af = afinador(max)
        label = af.getState()
        label = af.getState()
    
        if af.getAfinado():
            self.pl.plot(frq,dfft,label= label, color="green")
        else:
            self.pl.plot(frq,dfft,label= label, color="red")

        plt.xlabel(label)
        plt.tight_layout()
    def show(self):
        self.pl.tight_layout()
        self.pl.show()
