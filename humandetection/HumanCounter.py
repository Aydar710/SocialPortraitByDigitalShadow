import requests
from imageai.Detection import ObjectDetection

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
