# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
# Instantiates a client
client = vision.ImageAnnotatorClient()

import io
import os
import pandas as pd

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def detect_face(face_file, max_results=15):
    """Uses the Vision API to detect faces in the given file.

    Args:
        face_file: A file-like object containing an image with faces.

    Returns:
        An array of Face objects with information about the picture.
    """
    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image).face_annotations

def analyze(img):
    f = io.open(img, 'rb')
    content = f.read()
    image = types.Image(content=content)
    obj = client.face_detection(image=image).face_annotations
    confidence = obj[0].detection_confidence
    HAP = float(obj[0].joy_likelihood) - 1
    SAD = float(obj[0].sorrow_likelihood) - 1
    ANG = float(obj[0].anger_likelihood) - 1
    SUR = float(obj[0].surprise_likelihood) - 1
    return HAP * 25 * confidence, SAD * 25 * confidence, ANG * 25 * confidence, SUR * 25 * confidence

def check_dir(direct):
    return os.path.isdir(direct)

def check_file(direct):
    return os.path.isfile(direct)

def feed(inpt):

    HAP_lst = []
    SAD_lst = []
    ANG_lst = []
    SUR_lst = []
    name_lst = []

    if type(inpt) == list:
        for img in inpt:
            HAP_img, SAD_img, ANG_img, SUR_img = analyze(img)
            HAP_lst.append(HAP_img)
            SAD_lst.append(SAD_img)
            ANG_lst.append(ANG_img)
            SUR_lst.append(SUR_img)
            name_lst.append("-".join((img.split('/')[-1]).split('.')[:2])+('.jpg'))

    elif check_dir(inpt):
        file_names = []
        for the_file in os.listdir(inpt):
            if the_file.split('.')[-1] == 'jpg':
                file_names.append(str('./jpg/' + the_file))

        for img in file_names:
            HAP_img, SAD_img, ANG_img, SUR_img = analyze(img)
            HAP_lst.append(HAP_img)
            SAD_lst.append(SAD_img)
            ANG_lst.append(ANG_img)
            SUR_lst.append(SUR_img)
            name_lst.append("-".join((img.split('/')[-1]).split('.')[:2])+('.jpg'))

    elif check_file(inpt):
        HAP_img, SAD_img, ANG_img, SUR_img = analyze(inpt)
        HAP_lst.append(HAP_img)
        SAD_lst.append(SAD_img)
        ANG_lst.append(ANG_img)
        SUR_lst.append(SUR_img)
        name_lst.append("-".join((inpt.split('/')[-1]).split('.')[:2])+('.jpg'))

    elif (check_file(inpt) == False) & (check_dir(inpt) == False):
        print "The images need to be in '.jpg' format."

    df1 = pd.DataFrame({'PIC': name_lst, 'HAP %': HAP_lst, 'SAD %': SAD_lst, 'ANG %': ANG_lst, 'SUR %':SUR_lst})
    df = df1[['PIC', 'HAP %', 'SAD %', 'ANG %', 'SUR %']]
    return df.round(2)

def main(inpt):
    df = feed(inpt)
    print df.head(len(df))

if __name__ == "__main__":
    inpt = raw_input("Please load the path of the image or the path of the directory of images: ")
    main(inpt)
