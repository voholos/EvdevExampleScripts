import evdev

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    
#    print(device.path, device.name, device.phys)
#    print(device)
    if device.name=="3Dconnexion SpaceMouse Classic USB": deviceI = evdev.InputDevice(device.path)

print(deviceI)
for event in deviceI.read_loop():
#    print("Type",event.type,"Code",event.code,"Value",event.value)
    if event.type==00:continue
    elif event.type==1:
        if   event.code ==256:
            if event.value==0:print("1 Released")
            if event.value==1:print("1 Pressed")
        elif event.code ==257:
            if event.value==0:print("2 Released")
            if event.value==1:print("2 Pressed")
        elif event.code ==258:
            if event.value==0:print("3 Released")
            if event.value==1:print("3 Pressed")
        elif event.code ==259:
            if event.value==0:print("4 Released")
            if event.value==1:print("4 Pressed")
        elif event.code ==260:
            if event.value==0:print("5 Released")
            if event.value==1:print("5 Pressed")
        elif event.code ==261:
            if event.value==0:print("6 Released")
            if event.value==1:print("6 Pressed")
        elif event.code ==262:
            if event.value==0:print("7 Released")
            if event.value==1:print("7 Pressed")
        elif event.code ==263:
            if event.value==0:print("8 Released")
            if event.value==1:print("8 Pressed")
        elif event.code ==264:
            if event.value==0:print("* Released")
            if event.value==1:print("* Pressed")
        elif event.code ==267:
            if event.value==0:print("Puck Released")
            if event.value==1:print("Puck Pressed")
        else:print("Type 1","Code",event.code,"Value",event.value)
    elif event.type==3:
        if   event.code ==0:
            if event.value<-200:print("Puck 0 Left",event.value)
            #elif event.value==0:print("Puck 6 Centered")           
            elif event.value>200:print("Puck 0 Right",event.value)
            else:continue
        if   event.code ==1:
            if event.value<-200:print("Puck 1 Dwon",event.value)
            elif event.value==0:print("Puck Centered")           
            elif event.value>200:print("Puck 1 Up",event.value)
            else:continue
        if   event.code ==2:
            if event.value<-200:print("Puck 2 Forward",event.value)
            #elif event.value==0:print("Puck 2 Centered")           
            elif event.value>200:print("Puck 2 Backward",event.value)
            else:continue
        if   event.code ==3:
            if event.value<-200:print("Puck 3 Tilt Forward",event.value)
            #elif event.value==0:print("Puck 3 Centered")           
            elif event.value>200:print("Puck 3 Tilt Backward",event.value)
            else:continue
        if   event.code ==4:
            if event.value<-200:print("Puck 4 Rot Right",event.value)
            #elif event.value==0:print("Puck 4 Centered")           
            elif event.value>200:print("Puck 4 Rot Left",event.value)
            else:continue
        if   event.code ==5:
            if event.value>200:print("Puck 5 Tilt Left",event.value)
            #elif event.value==0:print("Puck 5 Centered")           
            elif event.value<-200:print("Puck 5 Tilt Right",event.value)
            else:continue
#        else:print("Type",event.type,"Code",event.code,"Value",event.value)

