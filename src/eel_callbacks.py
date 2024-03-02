import eel
import cv2
from tkinter import filedialog

from human_detetor import get_humans


image_types = (('Изображения', ['*.png', '*.jpg', '*.jpeg']),)
input_image_path = 'src/web/images/input_image.png'
output_image_path = 'src/web/images/output_image.png'


@eel.expose
def get_input_image():
    file_path = filedialog.askopenfilename(filetypes=image_types)

    if (file_path):
        cv2.imwrite(input_image_path, cv2.imread(file_path))

        print('input:', file_path)
        eel.set_input_image(file_path)


@eel.expose
def save_output_image():
    file_path = filedialog.asksaveasfilename(defaultextension='*.png', filetypes=image_types)

    if (file_path):
        cv2.imwrite(file_path, cv2.imread(output_image_path))

        print('output:', file_path)


@eel.expose
def find_human():
    get_humans(input_image_path, output_image_path)
    eel.find_human_success()