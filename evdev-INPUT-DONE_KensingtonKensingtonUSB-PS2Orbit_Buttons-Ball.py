from evdev import InputDevice
from evdev import UInput as ui, ecodes as e
from select import select
import evdev

thisdict = {  "kMouse": "000",}

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
#    print(device.path, device.name, device.phys)
    if device.name == "Kensington Kensington USB/PS2 Orbit":        thisdict["kMouse"] = device.path
#print("Output=",thisdict)

# A mapping of file descriptors (integers) to InputDevice instances.
devices = map(InputDevice, (thisdict["kMouse"]))
devices = {dev.fd: dev for dev in devices}
for dev in devices.values():
#    print(dev)
    dev.grab()

def Shut_Down():
    for dev in devices.values():
        dev.ungrab()
    ui.syn()
    ui.close()
    exit(0)

def mkbSwap():
    thisdict["wMouseL"],thisdict["wMouseR"]=thisdict["wMouseR"],thisdict["wMouseL"]
    thisdict["cdCcL"],thisdict["cdCcR"]=thisdict["cdCcR"],thisdict["cdCcL"]
    thisdict["cdKL"],thisdict["cdKR"]=thisdict["cdKR"],thisdict["cdKL"]
    print("MiniKeyboards SWAPED")

while True:
    r, w, x = select(devices, [], [])
    for fd in r:
        for event in devices[fd].read():
            deviceFD=str(devices[fd])+","
            if deviceFD.find(thisdict["kMouse"])!=-1:							#	Kensington Kensington USB/PS2 Orbit Ball
                if event.code ==11:break
                elif event.code<50 and event.value==1:break
                elif event.code<50 and event.value==0:break
                elif event.code<50 and event.value==-1:break

                elif event.code==0 and event.value>0:print("KR ", end="")
                elif event.code==0 and event.value<0:print("KL ", end="")
                elif event.code==1 and event.value>0:print("KD ", end="")
                elif event.code==1 and event.value<0:print("KU ", end="")
                elif event.code==272 and event.value==1:print("KiLeftMouseButton Pressed")
                elif event.code==272 and event.value==0:print("KiLeftMouseButton Released")
                elif event.code==273 and event.value==1:print("KiRightMouseButton Pressed")
                elif event.code==273 and event.value==0:print("KiRightMouseButton Released")
                else:print("1R",r,"EventType",event.type,"EventCode",event.code,"Event.Value",event.value)

