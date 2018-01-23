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
    return HAP * confidence, SAD * confidence, ANG * confidence, SUR * confidence

def main(img):
    HAP, SAD, ANG, SUR = analyze(img)
    return HAP*25, SAD*25, ANG*25, SUR*25

if __name__ == "__main__":
    img = raw_input("Please load an image: ")
    main(img)
