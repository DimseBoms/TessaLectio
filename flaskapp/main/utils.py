import os
import cv2
import secrets
import pytesseract
from PIL import Image, ImageOps
from flask import current_app, session, request


file_extentions = ['.png', '.jpg', 'jpeg']


# save image to the static/image folder
def save_image(img_file):
    f_ext = os.path.splitext(img_file.filename)[1]
    if f_ext.lower() in file_extentions:
        picture_fn = get_img_token(20, f_ext)
        picture_path = os.path.join(current_app.root_path, 'static/image', picture_fn)
        i = Image.open(img_file)
        i = ImageOps.exif_transpose(i) # fix image rotation
        i.save(picture_path)
        i.close()
        return picture_fn
    return False


# get unique img token
def get_img_token(byte, ext):
    directory = os.path.join(current_app.root_path, 'static/image')
    for _ in range(10):
        token = secrets.token_urlsafe(byte) + ext
        if token not in os.listdir(directory):
            break
    return token


# read and get text from image
def process_image(img_name, arg=None):
    img_path = os.path.join(current_app.root_path, 'static/image', img_name)
    
    image = cv2.imread(img_path)
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    if arg == 'thresh':
        gray_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif arg == 'blur':
        gray_img = cv2.medianBlur(gray_img, 3)

    processed_img_path = os.path.join(current_app.root_path, 'static/image_processed', img_name)
    cv2.imwrite(processed_img_path, gray_img)

    os.remove(img_path)

    return processed_img_path


def img_to_text(img_path):
    try:
        text = pytesseract.image_to_string(Image.open(img_path))
        os.remove(img_path)
    except:
        return False
    else:
        return text


# create form token
def create_token():
    token = secrets.token_hex(10)
    session['token'] = token
    return token


# check if form token is valid
def valid_token():
    if request.form.get('token') == session.get('token'):
        return True
    return False



# this file is for other functions that will help the routes in main.__init__.py (this makes the code cleaner)
