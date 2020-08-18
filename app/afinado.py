class afinador(object):
    def __init__(self,maxF):
        self.invalido = "..."
        self.fr ={
            self.invalido: 0,
            "mi_": 330,
            "si": 247,
            "sol": 196,
            "re": 146,
            "la": 110,
            "mi":  82
        }
        self.ofset ={
            self.invalido: 0,
            "mi_": 1,
            "si": 0,
            "sol": 0,
            "re": 0,
            "la": 0,
            "mi": 0
        }
        self.maxF = maxF
        self.curState = list(self.fr.keys())[0]
        self.setCurrNota()
    def setCurrNota(self):
        for f in self.fr:
            if ((self.fr[f]+10) > self.maxF )and ((self.fr[f]-10) < self.maxF ):
                self.curState = f
                return
        self.curState = list(self.fr.keys())[0]
    def getAfinado(self):
        return self.fr[self.curState] == self.getMax()
    def getMax(self):
        return int(round(self.maxF))+self.ofset[self.curState]
    def getState(self):
        st = self.curState
        st += " " +str(self.getMax())+"Hz"
        if self.invalido == self.curState:
            return st
        if self.getAfinado():
            st += " afinado"
        else:
            st +=" desafinado"
            if self.getMax() >  self.fr[self.curState]:
                st += "<<"
            else:
                st += ">>"
       
        st += " "+str(self.fr[self.curState])+"Hz"
        return st
        