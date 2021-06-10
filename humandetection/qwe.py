from imageai.Detection import ObjectDetection

execution_path = "/home/aydar/PycharmProjects/SocialPortraitByDigitalShadow/humandetection/"

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("/home/aydar/PycharmProjects/SocialPortraitByDigitalShadow/humandetection/object_recognition_model.h5")
detector.loadModel()

detections = detector.detectObjectsFromImage(
                input_image="smile.jpg",
                output_image_path="another.jpg")