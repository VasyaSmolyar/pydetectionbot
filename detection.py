from imageai.Detection import ObjectDetection

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel()

def draw_detecions(finput, foutput):
    detections = detector.detectObjectsFromImage(input_image=finput, output_image_path=foutput, minimum_percentage_probability=30)