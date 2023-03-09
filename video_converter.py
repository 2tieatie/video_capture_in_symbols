from PIL import Image
from os import system
import cv2
import time
vid = cv2.VideoCapture(0)
symbols = [i for i in '@$0B#NGWM8RDHPOKZ96khEPXS2wmeyjufF]}{tx1zv7lciL/\\|?*>r^;:_\"~,\'-.`'[::-1]]


def convert(tile, img):
    color_converted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(color_converted)
    img = img.rotate(90, expand=True)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    width = img.size[0] // tile
    height = img.size[1] // tile + tile * 40
    img = img.resize((width, height))
    pix = img.load()
    text = ''
    for x in range(width):
        for y in range(height):
            text += symbols[(pix[x, y][0] + pix[x, y][1] + pix[x, y][2]) // 12]
        text += '\n'
    print(text)


while True:
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    convert(6, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.07)
    system('cls')
vid.release()
cv2.destroyAllWindows()




