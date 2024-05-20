import time 
import urx
import numpy as np


if __name__ == "__main__":
    rob = urx.Robot("192.168.1.112", use_rt=True, urFirm='5.11')
    try:
        desired_speed_pos = np.array([0.0, 0.0, 0.025, 0.0, 0.0, 0.0])
        desired_speed_neg = np.array([0, 0, -0.025, 0, 0, 0])
        acc = 0.025
        min_time = 0.1
        
        for i in range(500):
            time.sleep(0.002)
            rob.speedl_rt(desired_speed_pos, acc, min_time)
            # time.sleep(0.002)
            # rob.speedl_rt(desired_speed_neg, acc, min_time)
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt", e)
        rob.stop()
    except Exception as e:
        print("Exception", e)
        rob.stop()
    finally:
        print("Finally reach the desired velocity")
        
    try:
        desired_speed_pos = np.array([0.0, 0.0, 0.075, 0.0, 0.0, 0.0])
        desired_speed_neg = np.array([0, 0, -0.075, 0, 0, 0])
        acc = 0.025
        min_time = 0.1
        
        for i in range(500):
            time.sleep(0.002)
            # rob.speedl_rt(desired_speed_pos, acc, min_time)
            # time.sleep(0.002)
            rob.speedl_rt(desired_speed_neg, acc, min_time)
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt", e)
        rob.stop()
    except Exception as e:
        print("Exception", e)
        rob.stop()
    finally:
        print("Finally reach the desired velocity")
    
    rob.close()

