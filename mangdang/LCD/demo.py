import os
import sys
import time
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import socket

sys.path.append("/home/ubuntu/minipupper_ros_bsp/mangdang")
sys.path.extend([os.path.join(root, name) for root, dirs, _ in os.walk("/home/ubuntu/minipupper_ros_bsp/mangdang") for name in dirs])
from LCD.ST7789 import ST7789

def main():
    """ The demo for picture show
    """
    #init st7789 device
    time.sleep(1)
    disp = ST7789()
    disp.begin()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    disp.clear()
    image=Image.open("/home/ubuntu/Pictures/logo.png")
    image.resize((320,240))
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 30)
    draw = ImageDraw.Draw(image)
    text = 'IP: '+str(ip)
    draw.text((25,95), text, font=font, fill="#000000", spacing=0, align='left')
    disp.display(image)
try:
    main()
except KeyboardInterrupt:
    pass

