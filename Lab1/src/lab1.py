# Lab 1 Python Code



# encoder reading code
def readEncoders():
    pinb6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN)
    pinb7 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN)
    tim4 = pyb.Timer(4, prescaler = 0, period = 0xFFFF)
    ch1 = tim4.channel(4, pyb.Timer.ENC_AB, pin=pinb6)
    ch2 = tim4.channel(4, pyb.Timer.ENC_AB, pin=pinb7)





# main
def main():
    readEncoders()






if __name__ == "__main__":
    main()