"""! ME 405 Lab 0 """

   def led_setup ():
       """! Setup pwm function  """
       pinA1 = pyb.Pin (pyb.Pin.board.PA1, pyb.Pin.OUT_PP)
       tim2 = pyb.Timer (2, freq=20000)
       ch2 = tim2.channel (2, pyb.Timer.PWM, pin=pinA1)
       
       pyb.Timer.PWM_INVERTED

   def led_brightness (n):
       """! Change the pulse width """
        ch2.pulse_width_percent(n)

   if __name__ == "__main__":
       
       while True
           for x in range 100:
               led_brightness(x)
            for x in range 100:
                led_brightness(100-x)