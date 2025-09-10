import time
import pyautogui
import os

RED_THRESHOLD = 230
MAX_TIME = 50
ASSETS_FOLDER = "assets"
images_to_stop = [os.path.join(ASSETS_FOLDER, img) for img in os.listdir(ASSETS_FOLDER)]

def image_detected():
    """Check if any image from assets folder is on screen safely."""
    screenshot = pyautogui.screenshot()
    for image_path in images_to_stop:
        try:
            location = pyautogui.locate(image_path, screenshot, confidence=0.8)
            if location is not None:
                print(f"Image detected: {image_path}")
                return True
        except pyautogui.ImageNotFoundException:
            continue
    return False

def triggered_function(pos):
    print("Function started!")
    start_time = time.time()
    
    while True:
        im = pyautogui.screenshot()
        pxcolor = im.getpixel(pos)
        red_value = pxcolor[0]

        if red_value > RED_THRESHOLD:
            start_time = time.time()  # reset timer if red is detected

        stop_condition = False

        if red_value <= RED_THRESHOLD:
            print("Red no longer detected.")
            stop_condition = True

        if time.time() - start_time > MAX_TIME:
            print("Maximum time reached.")
            stop_condition = True

        if image_detected():
            print("Stopping due to image detection.")
            stop_condition = True

        if stop_condition:
            # Press 1, then 2, then make a single click
            time.sleep(0.2)
            pyautogui.press('1')
            pyautogui.press('4')
            pyautogui.click()
            print("Performed final sequence before stopping.")
            break

        pyautogui.click()
        time.sleep(0.1)

def auto_fish(pos):
    im = pyautogui.screenshot()
    pxcolor = im.getpixel(pos)
    red_value = pxcolor[0]
    print("Pixel color:", pxcolor)
    print("Red:", red_value)
    
    if red_value > RED_THRESHOLD:
        triggered_function(pos)
