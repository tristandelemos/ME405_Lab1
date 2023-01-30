from encoder_driver import EncoderDriver
from motor_driver import MotorDriver
import pyb
import utime

def main(program):
    """!
    @brief	A test function for the motor and encoder drivers
    @details	This function tests the ability of the motor and 
                encoder drivers to drive/read multiple encoders at 
                once
    @param	program An integer defining which test program to run
    """
    enc1 = EncoderDriver(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    enc2 = EncoderDriver(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    motor1 = MotorDriver (pyb.Pin.board.PA10,pyb.Pin.board.PB4,pyb.Pin.board.PB5,3)
    motor2 = MotorDriver (pyb.Pin.board.PC1,pyb.Pin.board.PA0,pyb.Pin.board.PA1,5)
    if program == 0:
        pos1 = 0
        pos2 = 0
        read1 = enc1.read()
        read2 = enc2.read()
        print("read1 =",read1,"read2 =",read2)
        while True:
            read1,pos1 = enc1.update(read1,pos1)
            read2,pos2 = enc2.update(read2,pos2)
            print("read1 =",read1,"read2 =",read2)
            print("pos1 =",pos1,"pos2 =",pos2)
            utime.sleep_ms(100)
            
    if program ==1:
        pos1 = 0
        pos2 = 0
        read1 = enc1.read()
        read2 = enc2.read()
        print("read1 =",read1,"read2 =",read2)
        
        motor1 = MotorDriver (pyb.Pin.board.PA10,pyb.Pin.board.PB4,pyb.Pin.board.PB5,3)
        motor1.set_duty_cycle (42)
        motor2 = MotorDriver (pyb.Pin.board.PC1,pyb.Pin.board.PA0,pyb.Pin.board.PA1,5)
        motor2.set_duty_cycle (80)
        for i in range(20):
            read1,pos1 = enc1.update(read1,pos1)
            read2,pos2 = enc2.update(read2,pos2)
            print("read1 =",read1,"read2 =",read2)
            print("pos1 =",pos1,"pos2 =",pos2)
            utime.sleep_ms(100)
        motor1.set_duty_cycle (-42)
        motor2.set_duty_cycle (-54)
        for i in range(20):
            read1,pos1 = enc1.update(read1,pos1)
            read2,pos2 = enc2.update(read2,pos2)
            print("read1 =",read1,"read2 =",read2)
            print("pos1 =",pos1,"pos2 =",pos2)
            utime.sleep_ms(100)
        motor1.set_duty_cycle (0)
        motor2.set_duty_cycle (0)
        

if __name__=='__main__':
    main(1)