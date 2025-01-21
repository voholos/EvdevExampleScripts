from evdev import InputDevice
from evdev import UInput as ui, ecodes as e
from select import select
import evdev

thisdict = {  "kMouse": "000",}

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
#    print(device.path, device.name, device.phys)
    if device.name == "Kensington Kensington USB/PS2 Orbit":        thisdict["kMouse"] = device.path
    elif device.name == "2.4G Composite Devic Mouse":
        if "wMouseR" in thisdict:thisdict["wMouseL"] = device.path
        else:thisdict["wMouseR"] = device.path
    elif device.name == "2.4G Composite Devic Consumer Control":
        if "cdCcR" in thisdict:thisdict["cdCcL"] = device.path
        else:thisdict["cdCcR"] = device.path
    elif device.name == "2.4G Composite Devic":
        if "cdKR" in thisdict:thisdict["cdKL"] = device.path
        else:thisdict["cdKR"] = device.path
#    elif device.name == "2.4G Composite Devic System Control":
#        if "cdSc1" in thisdict:thisdict["cdSc2"] = device.path
#`	        else:thisdict["cdSc1"] = device.path
#print("Output=",thisdict)

# A mapping of file descriptors (integers) to InputDevice instances.
devices = map(InputDevice, (thisdict["wMouseL"],thisdict["cdCcL"],thisdict["cdKL"]))
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
            if event.type==1 and event.code== 1 and event.value==1: Shut_Down()	#										Press Esc Key on any Keyboard to Quit
            if event.type==1 and event.code==59 and event.value==1: mkbSwap()	#										press F1  Key on any Keyboard to SWAT
            if event.type==0:continue
            if event.type==4:continue
            
            
#            print("EventType",event.type,"EventCode",event.code,"Event.Value",event.value)
#            print("device", dev)
#            print("devices", devices)
#            print("0R0",r,"0W0",w,"0X0",x,"0FD0",fd)
#            print("TRY", devices[fd]," -- ", fd, "thisdict",thisdict["cdK1"])
            deviceFD=str(devices[fd])+","
            if deviceFD.find(thisdict["wMouseL"])!=-1:							#	Left-Hand 2.4G Composite Devic Mouse Pad
                print("-=wMouseL ",end="")
                if event.code ==11:break
                elif event.code<50 and event.value==1:break
                elif event.code<50 and event.value==0:break
                elif event.code<50 and event.value==-1:break
                elif event.code==0 and event.value>1:print("LR ", end="")
                elif event.code==0 and event.value<1:print("LL ", end="")
                elif event.code==1 and event.value>1:print("LD ", end="")
                elif event.code==1 and event.value<1:print("LU ", end="")
                elif event.code==8 and event.value<1:print("LsD ",end="")
                elif event.code==8 and event.value>1:print("LsU ",end="")
                elif event.code==272 and event.value==1:print("LeLeftMouseButton Pressed")
                elif event.code==272 and event.value==0:print("LeLeftMouseButton Released")
                elif event.code==273 and event.value==1:print("LeRightMouseButton Pressed")
                elif event.code==273 and event.value==0:print("LeRightMouseButton Released")
                else:print("3R",r,"EventType",event.type,"EventCode",event.code,"Event.Value",event.value)

            if deviceFD.find(thisdict["cdCcL"])!=-1:
                print("-=cdCcL ",end="")
                if   event.code==115:
                    if event.value==1:print("LeLeftDiscVolumeUp Preesed")
                    if event.value==0:print("LeLeftDiscVolumeUp Released")
                elif event.code==114:
                    if event.value==1:print("LeLeftDiscVolumeDown Preesed")
                    if event.value==0:print("LeLeftDiscVolumeDown Released")
                elif event.code==165:
                    if event.value==1:print("LeLeftDiscPrev Preesed")
                    if event.value==0:print("LeLeftDiscPrev Released")
                elif event.code==163:
                    if event.value==1:print("LeLeftDiscNext Preesed")
                    if event.value==0:print("LeLeftDiscNext Released")
                elif event.code==164:
                    if event.value==1:print("LeLeftDiscPlayPause Preesed")
                    if event.value==0:print("LeLeftDiscPlayPause Released")
                elif event.code==171:
                    if event.value==1:print("LeLeftColumPlayer Preesed")
                    if event.value==0:print("LeLeftColumPlayer Released")
                elif event.code==155:
                    if event.value==1:print("LeLeftColunEmail Preesed")
                    if event.value==0:print("LeLeftColumEmail Released")
                elif event.code==113:
                    if event.value==1:print("LeLeftColumMute Preesed")
                    if event.value==0:print("LeLeftColumMute Released")
                elif event.code==217:
                    if event.value==1:print("LeRightColumSearch Preesed")
                    if event.value==0:print("LeRightColumSearch Released")
                elif event.code==172:
                    if event.value==1:print("LeRightColumHome Preesed")
                    if event.value==0:print("LeRightColumHome Released")
                elif event.code==150:
                    if event.value==1:print("LeRightColumBrowser Preesed")
                    if event.value==0:print("LeRightColumBrowser Released")
                else:print("4R",r,"EventType",event.type,"EventCode",event.code,"Event.Value",event.value)

            if deviceFD.find(thisdict["cdKL"])!=-1:
                print("-=cdKL",end="")
                if event.code==105:
                    print(" DiscLeft ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==106:
                    print(" DiscRight ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==108:
                    print(" DiscDown ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==103:
                    print(" DiscUp ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==60:
                    print(" F2 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 61:
                    print(" F3 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 62:
                    print(" F4 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 63:
                    print(" F5 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 64:
                    print(" F6 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 65:
                    print(" F7 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 66:
                    print(" F8 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 67:
                    print(" F9 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 68:
                    print(" F10 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==111:
                    print(" Del ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==104:
                    print(" PgUp ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")

                elif event.code== 41:
                    print(" ` ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==  2:
                    print(" 1 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==  3:
                    print(" 2 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==  4:
                    print(" 3 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==  5:
                    print(" 4 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==  6:
                    print(" 5 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==  7:
                    print(" 6 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==  8:
                    print(" 7 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==  9:
                    print(" 8 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 10:
                    print(" 9 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 11:
                    print(" 0 ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 14:
                    print(" Back ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")

                elif event.code== 15:
                    print(" Tab ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 16:
                    print(" Q ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 17:
                    print(" W ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 18:
                    print(" E ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 19:
                    print(" R ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 20:
                    print(" T ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 21:
                    print(" Y ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 22:
                    print(" U ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 23:
                    print(" I ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 24:
                    print(" O ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 25:
                    print(" P ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 43:
                    print(" # ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==109:
                    print(" PgDn ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")

                elif event.code== 58:
                    print(" Caps ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 30:
                    print(" A ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 31:
                    print(" S ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 32:
                    print(" D ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 33:
                    print(" F ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 34:
                    print(" G ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 35:
                    print(" H ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 36:
                    print(" J ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 37:
                    print(" K ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 38:
                    print(" L ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 28:
                    print(" Enter ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")

                elif event.code== 42:
                    print(" Shift ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 44:
                    print(" Z ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 45:
                    print(" X ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 46:
                    print(" C ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 47:
                    print(" V ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 48:
                    print(" B ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 49:
                    print(" N ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 50:
                    print(" M ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 51:
                    print(" < ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 52:
                    print(" > ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 39:
                    print(" ; ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code== 40:
                    print(" ' ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")

                elif event.code==29:
                    print(" Ctrl ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==12:
                    print(" - ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==13:
                    print(" = ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==56:
                    print(" Alt ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==57:
                    print(" Space ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==100:
                    print(" AltGr ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==126:
                    print(" Win ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==26:
                    print(" [ ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==27:
                    print(" ] ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")
                elif event.code==53:
                    print(" / ",end="")
                    if event.value==2:print("LongPress")
                    if event.value==1:print("Released")
                    if event.value==0:print("Press")

                else:print("6R",r,"EventType",event.type,"EventCode",event.code,"Event.Value",event.value)

