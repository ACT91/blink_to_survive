from pynput.keyboard import Controller, Key
import time

keyboard = Controller()
last_blink_time = 0
cooldown =  0.1  # seconds

def send_space_if_not_on_cooldown():
    global last_blink_time
    now = time.time()
    if now - last_blink_time > cooldown:
        print("👁️ Blink detected! Jumping...")
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        last_blink_time = now
