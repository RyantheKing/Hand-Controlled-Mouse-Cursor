#cd "D:\Program Files\Unity Hub\2019.4.15f1\Editor\Data\PlaybackEngines\AndroidPlayer\SDK\platform-tools"
#adb logcat -s Unity | py "D:\Documents\VRMouse\Assets\Scripts\logcat.py"
import sys, os
import time
import pyautogui

# work on hand gestures, rotational mode

def postion_from_value_x(hand_coord, screen_coord):
    return 1.5*screen_coord*hand_coord+screen_coord/1.25

def postion_from_value_y(hand_coord, screen_coord):
    return 1.5*screen_coord*hand_coord+screen_coord/1.5

size = pyautogui.size()
pyautogui.FAILSAFE = False
offset = [0.0000, 0.0000]
pyautogui.moveTo(960, 540)
hand_pos = 'v' #input("Would you like to use a vertical or horizontal hand position? (v/h) ")
headset_pos = 's' #input("Would you like the headset be be on the ground or sideways? (g/s) ")
joystick_mode = False
right_down = False
left_down = False
grip_modifier = False
right_click_modifier = False
left_click_modifier = False
hold_buttonone_time = 0.0
pinch_time = 0.0
keyboard_wait = 0.0
keyboard_open = False
ring_pinch = False
old_y_coords = 0
print('start')
for line in sys.stdin:
    result = line[43:]
    if result.startswith('DATA'):
        result_list = result.split(' ', 2)
        result_list[2] = result_list[2].strip()
        #if result_list[1] == 'RightPolCoords':
         #   print(result_list[2])
        if result_list[1] == 'SecondaryIndexTrigger': #click
            if (float(result_list[2]) >= 0.5) and (not left_down):
                left_down = True
                pyautogui.mouseDown(_pause=False)
            elif left_down and (float(result_list[2]) <= 0.5):
                left_down = False
                pyautogui.mouseUp(_pause=False)
        elif result_list[1] == 'MiddlePinch': #right click
            if result_list[2] == 'True': right_click_modifier = True
            else: right_click_modifier = False
            if (result_list[2] == 'True') and (not right_down) and (not left_click_modifier):
                right_down = True
                pyautogui.mouseDown(button='right', _pause=False)
            elif right_down and (result_list[2] != 'True'):
                right_down = False
                pyautogui.mouseUp(button='right', _pause=False)
        elif result_list[1] == 'IndexPinch': #click
            if result_list[2] == 'True': left_click_modifier = True
            else: left_click_modifier = False
            if (result_list[2] == 'True') and (not left_down) and (not right_click_modifier):
                left_down = True
                pyautogui.mouseDown(_pause=False)
            elif (left_down and (result_list[2] == 'False')) or right_click_modifier:
                left_down = False
                pyautogui.mouseUp(_pause=False)
        elif result_list[1] == 'ButtonTwo': #right click
            if (result_list[2] == 'True') and (not right_down):
                right_down = True
                pyautogui.mouseDown(button='right', _pause=False)
            elif right_down and (result_list[2] != 'True'):
                right_down = False
                pyautogui.mouseUp(button='right', _pause=False)
        elif result_list[1] == 'RingPinch': # keyboard
            if (result_list[2] == 'True') and (not ring_pinch) and (time.time()-keyboard_wait > 1):
                if keyboard_open:
                    os.system("TASKKILL /F /IM Click-N-Type.exe")
                    keyboard_wait = time.time()
                else:
                    os.startfile('"C:\Program Files (x86)\Click-N-Type\Click-N-Type.exe"')
                    keyboard_wait = time.time()
                keyboard_open = not keyboard_open
                ring_pinch = True
            if result_list[2] == 'False':
                ring_pinch = False
        elif result_list[1] == 'PinkyPinch': # idk yet
            if result_list[2] == 'True':
                if pinch_time==0.0:
                    pinch_time = time.time()
                elif time.time()-pinch_time >= 1:
                    offset = coords
            else:
                pinch_time = 0.0
        elif result_list[1] == 'SecondaryThumbstickButton': #switch to joystick mode
            if result_list[2] == 'True':
                joystick_mode = not joystick_mode
        elif (result_list[1] == 'SecondaryThumbstick'): #move joystick
            if grip_modifier:
                coordinates = result_list[2][1:][:-1].split(', ')
                pyautogui.scroll(int(float(coordinates[1])*50), _pause=False)
            elif joystick_mode:
                coordinates = result_list[2][1:][:-1].split(', ')
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
                    elif time.time()-hold_buttonone_time >= 1:
                        offset = coords
            else:
                if hold_buttonone_time != 0.0:
                    if time.time()-hold_buttonone_time < 1:
                        if keyboard_open:
                            os.system("TASKKILL /F /IM Click-N-Type.exe")
                        else:
                            os.startfile('"C:\Program Files (x86)\Click-N-Type\Click-N-Type.exe"')
                        keyboard_open = not keyboard_open
                        #pyautogui.hotkey('win', 'shift', 's', _pause=False)
                    hold_buttonone_time = 0.0
        elif result_list[1] == 'RightCoords' and (not joystick_mode):
            coords = [float(i) for i in result_list[2][1:][:-1].split(', ')]
            final_coords = [coords[0]-offset[0], coords[1]-offset[1]]
            y_coords = postion_from_value_y(-1.25*final_coords[1], size[1])
            if right_click_modifier and left_click_modifier:
                pyautogui.scroll(-int(y_coords-old_y_coords)*5, _pause=False)
            else:
                pyautogui.moveTo(postion_from_value_x((2*final_coords[0]), size[0]), y_coords, _pause=False)
            old_y_coords = y_coords

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
