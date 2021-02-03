#"D:\Program Files\Unity Hub\2019.4.15f1\Editor\Data\PlaybackEngines\AndroidPlayer\SDK\platform-tools"
import sys
import time
import pyautogui
import math

def postion_from_value_x(hand_coord, screen_coord):
    return 1.5*screen_coord*hand_coord+screen_coord/1.25

def postion_from_value_y(hand_coord, screen_coord):
    return 1.5*screen_coord*hand_coord+screen_coord/2

size = pyautogui.size()
pyautogui.FAILSAFE = False
pyautogui.moveTo(1600, 540)
hand_pos = 'v' #input("Would you like to use a vertical or horizontal hand position? (v/h) ")
headset_pos = 's' #input("Would you like the headset be be on the ground or sideways? (g/s) ")
joystick_mode = False
right_down = False
left_down = False
grip_modifier = False
hold_buttonone_time = 0.0
print('start')
for line in sys.stdin:
    result = line[43:]
    if result.startswith('DATA'):
        result_list = result.split(' ', 2)
        result_list[2] = result_list[2].strip()
        if result_list[1] == 'SecondaryIndexTrigger': #click
            if (float(result_list[2]) >= 0.5) and (not left_down):
                left_down = True
                pyautogui.mouseDown(_pause=False)
            elif left_down and (float(result_list[2]) <= 0.5):
                left_down = False
                pyautogui.mouseUp(_pause=False)
        elif result_list[1] == 'ButtonTwo': #right click
            if (result_list[2] == 'True') and (not right_down):
                right_down = True
                pyautogui.mouseDown(button='right', _pause=False)
            elif right_down and (result_list[2] != 'True'):
                right_down = False
                pyautogui.mouseUp(button='right', _pause=False)
        elif result_list[1] == 'SecondaryThumbstickButton': #switch to joystick mode
            if result_list[2] == 'True':
                joystick_mode = not joystick_mode
        elif (result_list[1] == 'SecondaryThumbstick'): #move joystick
            if grip_modifier:
                coordinates = result_list[2][1:][:-1].split(', ')
                print(coordinates)
                pyautogui.scroll(int(float(coordinates[1])*50), _pause=False)
            elif joystick_mode:
                coordinates = result_list[2][1:][:-1].split(', ')
                print(coordinates)
                print(round(float(coordinates[0]), -round(float(coordinates[1]))*10))
                pyautogui.move(round(float(coordinates[0])*10), -round(float(coordinates[1])*10), _pause=False) #square maybe?
        elif result_list[1] == 'SecondaryHandTrigger': #grab modifier
            if (float(result_list[2]) >= 0.5):
                grip_modifier = True
            else:
                grip_modifier = False
        elif result_list[1] == 'ButtonOne':
            if (result_list[2] == 'True'):
                if grip_modifier:
                    pass #switch mode
                else:
                    if hold_buttonone_time==0.0:
                        hold_buttonone_time = time.time()
            else:
                if hold_buttonone_time != 0.0:
                    if time.time()-hold_buttonone_time >= 2:
                        pass #reset view
                    else:
                        pyautogui.hotkey('win', 'shift', 's', _pause=False)
                    hold_buttonone_time = 0.0
        elif result_list[1] == 'RightCoords' and not joystick_mode:
            coords = [float(i) for i in result_list[2][1:][:-1].split(', ')]
            pyautogui.moveTo(postion_from_value_x((2*coords[0]), size[0]), postion_from_value_y(-1.25*coords[1], size[1]), _pause=False)


        """result_list = [float(i) for i in result.split(', ')]
        print(postion_from_value_x((result_list[0]), size[0]), tion.
        postion_from_value_y(-result_list[2], size[1]))
        if hand_pos=='h' and headset_pos == 'g':
            pyautogui.moveTo(postion_from_value_x((2*result_list[0]), size[0]), postion_from_value_y(1.25*result_list[2], size[1]), _pause=False)
        elif hand_pos=='v' and headset_pos == 's':
            pyautogui.moveTo(postion_from_value_x((2*result_list[0]), size[0]), postion_from_value_y(-1.25*result_list[1], size[1]), _pause=False)
        elif hand_pos=='h' and headset_pos == 's':
            pyautogui.moveTo(postion_from_value_x((-2*result_list[0]), size[0]), postion_from_value_y(-2*result_list[1]+0.5, size[1]), _pause=False)
        elif hand_pos=='v' and headset_pos == 'g':
            pyautogui.moveTo(postion_from_value_x((-2*result_list[0]), size[0]), postion_from_value_y(-2*result_list[1]+0.5, size[1]), _pause=False)"""
