import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
# print(cv2.__version__)
list_of_names = []


def data_cleanup():
    file = open("input_file.txt")
    for each in file:
        list_of_names.append(each.strip())


def generate_certificates():
    i = 0
    for name in list_of_names:
        name = name.upper()
        no = len(list_of_names)
        template_read = cv2.imread("template.png")
        # font
        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        # org
        org = (405, 915)
        # fontScale
        font_scale = 5
        # Blue color in BGR
        color = (255, 0, 0)
        # Line thickness of 2 px
        thickness = 2

        font1_path = "./font.ttf"
        font1 = ImageFont.truetype(font1_path, 78)
        # org
        org1 = (800, 640)
        # fontScale
        font_scale1 = 1
        # Blue color in BGR
        color1 = (60, 48, 43)
        # Line thickness of 2 px
        thickness1 = 1
        img_pil = Image.fromarray(template_read)
        draw = ImageDraw.Draw(img_pil)
        draw.text(org1, name, font=font1, fill=color1, stroke_width=thickness1)
        img = np.array(img_pil)
        # cv2.putText(template_read, name, org, font, font_scale, color, thickness, cv2.LINE_AA)
        # cv2.putText(template_read, "NIT DURGAPUR", org1, font1, font_scale1, color1, thickness1, cv2.LINE_AA)
        cv2.imwrite(f'generated-certificates/{name}.png', img)
        i += 1
        print(f"{i}/{no} certificates done...")


data_cleanup()
generate_certificates()
