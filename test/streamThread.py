import threading
import pyaudio
import time
lock = threading.Lock()
class streamThread(threading.Thread):
        def __init__(self,chunk = 40960,# 1024
                        sample_format = pyaudio.paInt16,
                        channels = 1,
                        fs = 48000,
                        seconds = 3,
                        index_device = 5,
                        ):
                threading.Thread.__init__(self)
                self.chunk = chunk
                self.sample_format = sample_format
                self.channels = channels
                self.fs = fs
                self.seconds = seconds
                self.index_device = index_device
                self.data = ""
                self.p = pyaudio.PyAudio()
                self.stream = self.p.open(
                        format=self.sample_format,
                        channels=self.channels,
                        rate=self.fs,
                        frames_per_buffer=self.chunk,
                        input=True,
                        input_device_index=self.index_device
                        )
                print("crio classe")
                self.running = True
                self.data = ""
        def run(self):
                while self.running:
                        self.data = self.stream.read(self.chunk,exception_on_overflow=False)
        def set_running(self,val):
                self.running=val
        def setRunning(self,val):
                self.setLock(self.set_running,val)
        def get_data(self):
                return self.data
        def getData(self):
                return self.getLock(self.get_data)
        def getLock(self,func):
                lock.acquire()
                A = func()
                lock.release()
                return A
        def setLock(self,func,val):
               lock.acquire()
               func(val)
               lock.release()
        def stop(self):
                self.stream.stop_stream()
                self.stream.close() 
# cl = streamThread()
# cl.start()
# time.sleep(1)
# data= cl.getData()
# print(data)


