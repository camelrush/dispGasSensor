import datetime
import time
import board
import adafruit_ccs811
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image , ImageDraw ,ImageFont

i2c = board.I2C()
FONT_SANS_12 = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc" ,12)
FONT_SANS_18 = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc" ,18)

ccs811 = adafruit_ccs811.CCS811(i2c)
display = SSD1306_I2C(128, 64, board.I2C(), addr=0x3C)

while not ccs811.data_ready:
    pass

display.fill(0)
display.show()
eco2 = 0
tvoc = 0

while True:

    timestamp = datetime.datetime.now()
    img = Image.new("1",(display.width, display.height))
    draw = ImageDraw.Draw(img)
    if ccs811.data_ready:
        eco2 = ccs811.eco2
        tvoc = ccs811.tvoc
    draw.text((0,0),'時刻  ' + timestamp.strftime('%H:%M:%S'),font=FONT_SANS_12,fill=1)
    draw.text((0,20),'CO2  :' + '{:4}'.format(eco2) + 'PPM',font=FONT_SANS_18,fill=1)
    draw.text((0,40),'TVOC :' + '{:4}'.format(tvoc) + 'PPB' ,font=FONT_SANS_18,fill=1)
    display.image(img)
    display.show()


