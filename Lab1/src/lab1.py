# Lab 1 Python Code



# encoder reading code
def readEncoders():
    pinb6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN)
    pinb7 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN)
    tim2 = pyb.Timer(2, freq = 20000)
    ch1 = tim2.channel(2, pyb.Timer.ENC_AB, pin=pinb6)
    ch2 = tim2.channel(2, pyb.Timer.ENC_AB, pin=pinb7)

    



# main
def main():
    readEncoders()






if __name__ == "__main__":
    main()