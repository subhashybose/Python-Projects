import random
import keyboard
#import sys

#print(f"System Version: {sys.version}")
while True:
    print("Press Key: R-Roll the Dice, X-Exit")
    print(keyboard.read_key())
    if keyboard.read_key() == 'r':
        print(f"Dice Number: {random.randint(1,6)}")
    elif  keyboard.read_key() == 'x':
        break;





