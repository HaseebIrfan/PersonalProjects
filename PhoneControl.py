def wait(a):
    time.sleep(a/3)
    print(".")
    time.sleep(a/3)
    print(".")
    time.sleep(a/3)
    print(".")

def transmit(message,num):
    ph_as_email = #"8880001234@messaging.carrier.com"
    ezgmail.send(ph_as_email, '',message + str(num))

import ezgmail
import time
print("What would you like to do?")
print("")
print("QUIT: Quit this program")
print("")
print("DND1: Turns on Do Not Disturb")
print("DND0: Turns off Do Not Disturb")
print("")
print("WF1: Turns on WiFi")
print("WF0: Turns off WiFi")
print("")
print("FL1: Turns on Flashlight")
print("FL0: Turns off Flashlight")
print("")
print("MUSIC1: Play music")
print("MUSIC0: Pause music")
print("")
print("KICK: Restart WiFi")
print("")
print("VOL: Set volume level")
print("")
print("ENTER: Create new command")
print("")

track=0

while True:
    command=input()

    if command=="DND1":
        transmit('DND1 ', track)

    elif command=="DND0":
        transmit('DND0 ', track)
    
    elif command=="WF1":
        transmit('WF1 ', track)
    
    elif command=="WF0":
        transmit('WF0 ', track)
    
    elif command=="FL1":
        transmit('FL1 ', track)
    
    elif command=="FL0":
        transmit('FL0 ', track)
       
    elif command == "VOL":
        vol=input("What level should the volume be out of 10? ")
        transmit('VOL' + str(vol) + " ", track)

    elif command=="MUSIC1":
        transmit("MUSIC1 ", track)
    
    elif command=="MUSIC0":
        transmit("MUSIC0 ", track)
    
    elif command=="KICK":
        transmit('WF0 ', track)
        wait(2)
        transmit('WF1 ', track)

    elif command=="ENTER":
        freecmd=input("What is the commmand: ")
        transmit(freecmd +" ",track)

    elif command=="QUIT":
        break

    else:
        print("Command Not Recognized\n")
        continue

    print("Command sent\n")
    track+=1

print("Program Ended")
