import pyaudio

def getDevices():
    dic = {}
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                # print ("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
                dic[p.get_device_info_by_host_api_device_index(0, i).get('name')] = i
    return dic
def getIndexLike(st):
    dic = getDevices()
    key = dic.keys()
    cont = 0
    for k in key:
        if st in k:
            return dic[k]