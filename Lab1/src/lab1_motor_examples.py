import utime
pinB6 = pyb.Pin (pyb.Pin.board.PB6, pyb.Pin.IN)					# set up pin B6/B7 to read encoder A/B
pinB7 = pyb.Pin (pyb.Pin.board.PB7, pyb.Pin.IN)
tim4 = pyb.Timer(4,prescaler = 0,period = 0xFFFF)				# set up timer tied to encoder
t4_ch1 = tim4.channel (1, pyb.Timer.ENC_AB, pin = pinB6)		# count up timer on each encoder pulse
t4_ch2 = tim4.channel (2, pyb.Timer.ENC_AB, pin = pinB7)

pinC6 = pyb.Pin (pyb.Pin.board.PC6, pyb.Pin.IN)					# See above but for C6/C7
pinC7 = pyb.Pin (pyb.Pin.board.PC7, pyb.Pin.IN)
tim8 = pyb.Timer (8,prescaler = 0,period = 0xFFFF)
t8_ch1 = tim8.channel (1, pyb.Timer.ENC_AB, pin = pinC6)
t8_ch2 = tim8.channel (2, pyb.Timer.ENC_AB, pin = pinC7)

pinPA10 = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP)			# Set up motor enable pin
pinPB4 = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)			# Set up pin B4/B5 to drive motor
pinPB5 = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
tim3 = pyb.Timer (3,freq = 20000)								# Set up PWM clock
IN1A = tim3.channel(1,pyb.Timer.PWM, pin = pinPB4)				# Set up channels IN1A/IN2A to drive motor with PWM signal
IN2A = tim3.channel(2,pyb.Timer.PWM, pin = pinPB5)

<<<<<<< HEAD
pinPA10.high()													# enable motor by driving enable pin high
IN1A.pulse_width_percent(0)										# set channel IN1A to always be high
IN2A.pulse_width_percent(0)										# set channel 1N2A to some duty cycle
while True:
    pass
    #print(tim8.counter())
    #utime.sleep_ms(500)
    
    #utime.sleep_ms(1000)
#tim4 = pyb.Timer(4, freq = 20000)
#ch1 = tim2.channel (2, pyb.Timer.PWM, pin = pinB6)
=======
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
>>>>>>> 93750a24896b82c6e3fdbb02219ba106425074e3
