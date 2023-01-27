class encoder:
    
    def __init__ (self,en_pin1, en_pin2, timer):
        """!

        """
        self.en_pin1 = pyb.Pin (en_pin1, pyb.Pin.IN)
        self.en_pin2 = pyb.Pin (en_pin2, pyb.Pin.IN)
        self.timer = pyb.Timer(timer,prescaler=0,period=0xFFFF)
        self.ch1 = self.timer.channel (1, pyb.Timer.ENC_AB, pin = self.en_pin1)
        self.ch2 = self.timer.channel (2, pyb.Timer.ENC_AB, pin = self.en_pin2)
    
    def read():
        """!

        """
        return self.timer.counter()
    
    def zero():
        # zero out the counter
    def position():
        # calculate absolute position
              
                  
                  
                  
                  
                  
                
pinB6 = pyb.Pin (pyb.Pin.board.PB6, pyb.Pin.IN)					# set up pin B6/B7 to read encoder A/B
pinB7 = pyb.Pin (pyb.Pin.board.PB7, pyb.Pin.IN)
tim4 = pyb.Timer(4,prescaler = 0,period = 0xFFFF)				# set up timer tied to encoder
t4_ch1 = tim4.channel (1, pyb.Timer.ENC_AB, pin = pinB6)		# count up timer on each encoder pulse
t4_ch2 = tim4.channel (2, pyb.Timer.ENC_AB, pin = pinB7)
