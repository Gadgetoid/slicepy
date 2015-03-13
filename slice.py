import time
import colorsys

"""
0                                   26
1                                   25
2                                   24
3                                   23
4                                   22
5                                   21
6                                   20
 7 8 9 10 11 12 13 14 15 16 17 18 19
"""

dev = open('/dev/ws2812','w')
leds = [(0,0,0)] * 25

def m(x):
    return ''.join(map(chr,x)) + chr(0)

def update():
    dev.write(''.join(map(m, leds)))
    dev.flush()

def clear():
    global leds
    leds = [(0,0,0)] * 25

def set_pixel_hue(index, h):
    (r, g, b) = colorsys.hsv_to_rgb(h/360.0, 1.0, 1.0)
    set_pixel(index, int(r*255.0), int(g*255.0), int(b*255.0))

def set_pixel(index, r, g, b):
    global leds
    leds[index] = (r, g, b)

scan_length = 14
scan_start = 5
scan_hue = 0

while True:
    for x in range(25):
        set_pixel_hue(x, (scan_hue+(x*10))%360)
    scan_hue += 1
    scan_hue %= 360
    update()
    time.sleep(0.01)

while True:
    for x in range(scan_length):
        clear()
        set_pixel_hue(scan_start+x,scan_hue)
        update()
        time.sleep(0.001)
        scan_hue += 1
        scan_hue %= 360
    for x in range(scan_length):
        clear()
        set_pixel_hue(scan_start+(scan_length-x),scan_hue)
        update()
        time.sleep(0.01)
        scan_hue += 1
        scan_hue %= 360
