import evdev

ledSS=0

def ledS(ledSS):
    if ledSS==0:
        device.set_led(0,0)
        device.set_led(1,0)
        device.set_led(2,0)
    if ledSS==1:
        device.set_led(0,1)
        device.set_led(1,0)
        device.set_led(2,0)
    if ledSS==2:
        device.set_led(0,0)
        device.set_led(1,1)
        device.set_led(2,0)
    if ledSS==3:
        device.set_led(0,0)
        device.set_led(1,0)
        device.set_led(2,1)
    if ledSS==4:
        device.set_led(0,1)
        device.set_led(1,1)
        device.set_led(2,0)
    if ledSS==5:
        device.set_led(0,1)
        device.set_led(1,0)
        device.set_led(2,1)
    if ledSS==6:
        device.set_led(0,0)
        device.set_led(1,1)
        device.set_led(2,1)
    if ledSS==7:
        device.set_led(0,1)
        device.set_led(1,1)
        device.set_led(2,1)

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print (device)
    


if device.name=="HID 050d:0805": deviceI = evdev.InputDevice(device.path)
print(deviceI.leds())
print(deviceI)
for event in deviceI.read_loop():
#    print(event)
    if event.type==00:continue
    elif event.type==1:
        if   event.code ==304:
            if event.value==0:print("01 Released")
            if event.value==1:print("01 Pressed")
        elif event.code ==305:
            if event.value==0:print("02 Released")
            if event.value==1:print("02 Pressed")
        elif event.code ==306:
            if event.value==0:print("03 Released")
            if event.value==1:print("03 Pressed")
        elif event.code ==307:
            if event.value==0:print("04 Released")
            if event.value==1:print("04 Pressed")
        elif event.code ==308:
            if event.value==0:print("05 Released")
            if event.value==1:print("05 Pressed")
        elif event.code ==309:
            if event.value==0:print("06 Released")
            if event.value==1:print("06 Pressed")
        elif event.code ==310:
            if event.value==0:print("07 Released")
            if event.value==1:print("07 Pressed")
        elif event.code ==311:
            if event.value==0:print("08 Released")
            if event.value==1:print("08 Pressed")
        elif event.code ==312:
            if event.value==0:print("09 Released")
            if event.value==1:print("09 Pressed")
        elif event.code ==313:
            if event.value==0:print("10 Released")
            if event.value==1:print("10 Pressed")
    elif event.type==3:
        
        if event.code==00:
            if event.value==00:print("Left")
            if event.value==128:print("Center")
            if event.value==255:print("Right")
        if event.code== 1:
            if event.value==00:print("Forward")
            if event.value==128:print("Center")
            if event.value==255:print("Backward")
        if event.code== 6:
            print("Wheel is at=", event.value)
            if event.value==0  :ledS(0)
            if event.value==175:ledS(1)
            if event.value==183:ledS(2)
            if event.value==199:ledS(3)
            if event.value==215:ledS(4)
            if event.value==231:ledS(5)
            if event.value==239:ledS(6)
            if event.value==255:ledS(7)
            print(device.leds())
    elif event.type==4:continue
#    else:
    else:print(event)


