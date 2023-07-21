from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.withdraw()
filename = filedialog.askopenfile(initialdir='D:/posts_blog', title="Select an Image:")
print(filename.name)

def add_watermark(image, wm_text):
    opened_image = Image.open(image)
    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)
    font = ImageFont.truetype('ARIAL.TTF', 70)
    x, y = int(image_width / 2), int(image_height / 2)
    draw.text((x, y), wm_text,  font=font,fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')
    opened_image.show()


add_watermark(filename.name, '©SomePic')
