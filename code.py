from pmk import PMK
from pmk.platform.keybow2040 import Keybow2040 as Hardware

import usb_hid
from hid_gamepad import Gamepad

gp = Gamepad(usb_hid.devices)
keybow = PMK(Hardware())
keys = keybow.keys

yellow = (255, 255, 0)
purple = (75, 0, 130)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
orange = (255, 106, 0)
off = (255, 255, 255)
pressed_color = white

default_led_list = (green, yellow, yellow, yellow, blue, purple, purple, purple, off, off, off, red, orange, off , off, off)

# setup

for key in keys:
    key.set_led(*default_led_list[key.number])
    @keybow.on_press(key)
    def press_handler(key):
        gp.press_buttons(key.number+1)
        if not default_led_list[key.number] == off:
            key.set_led(*pressed_color)

    @keybow.on_release(key)
    def release_handler(key):
        gp.release_buttons(key.number+1)
        key.set_led(*default_led_list[key.number])


# run

while True:
    keybow.update()
