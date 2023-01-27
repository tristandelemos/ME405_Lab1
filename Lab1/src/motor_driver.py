import utime
class MotorDriver:
    """!
    This class implements a motor driver for an ME405 kit.
    """
    
    def __init__ (self,en_pin,in1pin,in2pin,timer):
        """!
        Creates a motor driver by initializing GPIO 
        pins and turning off the motor for safety.
        @param	en_pin A pin on the Nucleo corresponding 
                to the enable pin for the current motor driver 
                this should either be PA10 or PC1
        @param	in1pin The pin corresponding to channel 1 of the 
                motor driver should either be PB4 or PA0
        @param	in2pin The pin corresponding to channel 2 of the 
                motor driver should either be PB5 or PA1
        @param	timer An integer corresponding to the timer attached 
                to the motor driver should either be 3 or 5
        """
        print("Creating a motor driver")
        self.en_pin = pyb.Pin (en_pin, pyb.Pin.OUT_PP)
        self.in1pin = pyb.Pin (in1pin, pyb.Pin.OUT_PP)
        self.in2pin = pyb.Pin (in2pin, pyb.Pin.OUT_PP)
        self.timer = pyb.Timer (timer,freq = 20000)
        self.PWM_1 = self.timer.channel(1,pyb.Timer.PWM,pin = in1pin)
        self.PWM_2 = self.timer.channel(2,pyb.Timer.PWM,pin = in2pin)
        self.en_pin.high()
        self.PWM_1.pulse_width_percent(0)
        self.PWM_2.pulse_width_percent(0)
    
    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent 
        to the motor to the given level. Positive values 
        cause torque in one direction, negative values 
        in the opposite direction.
        
        @param	level A signed integer holding the duty
                cycle of the voltage sent to the motor
        """
        print("Setting duty cycle to {level}")
        if level >= 0:
            self.PWM_1.pulse_width_percent(0)
            self.PWM_2.pulse_width_percent(level)
        else:
            self.PWM_1.pulse_width_percent(abs(level))
            self.PWM_2.pulse_width_percent(0)
            
def main():
    moe = MotorDriver (pyb.Pin.board.PA10,pyb.Pin.board.PB4,pyb.Pin.board.PB5,3)
    moe.set_duty_cycle (42)
    utime.sleep(2)
    moe.set_duty_cycle (-42)
    utime.sleep(2)
    moe.set_duty_cycle (0)
        
            
if __name__ == '__main__':
    main()
    
    
