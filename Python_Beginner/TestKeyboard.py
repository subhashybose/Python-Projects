import keyboard

while True:
    try:
        if keyboard.is_pressed('enter'):
            print("Enter pressed")
            #break;
        elif keyboard.is_pressed('q'):
            print("Q pressed")
            #break;
        else:
            pass
            #print("Nothing pressed")
            #break;
    except:
        break;
