import requests
from imageai.Detection import ObjectDetection
import os

PHOTO_PATH = "/home/aydar/PycharmProjects/SocialPortraitByDigitalShadow/humandetection/downloaded.jpg"
RECOGNIZED_PHOTO_PATH = "/home/aydar/PycharmProjects/SocialPortraitByDigitalShadow/humandetection/recognized.jpg"


class HumanCounter:

    def __init__(self):
        self.execution_path = "/home/aydar/PycharmProjects/SocialPortraitByDigitalShadow/humandetection/"

        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath(
            "/home/aydar/PycharmProjects/SocialPortraitByDigitalShadow/humandetection/object_recognition_model.h5")
        self.detector.loadModel()

    def has_more_than_one_person(self, image_url: str) -> bool:
        if image_url == "https://sun9-37.userapi.com/impf/c856128/v856128282/20ba5a/9Q-4YnaYSTI.jpg?size=54x75&quality=96&sign=37cf9a0c5a04acda8434e12ac9809a5b&c_uniq_tag=Tvgn1X5yoXgBDha6wSiYxypjvgrlKtY5UjAg0q5QdW4&type=album":
            print()
        photo = requests.get(image_url).content

        file = open(PHOTO_PATH, "wb")
        file.write(photo)
        file.close()

        try:
            detections = self.detector.detectObjectsFromImage(
                input_image=PHOTO_PATH,
                output_image_path=RECOGNIZED_PHOTO_PATH)

            persons_count = 0
            for eachObject in detections:
                if eachObject['name'] == 'person':
                    persons_count += 1

            return persons_count > 1
        except Exception:
            return False
