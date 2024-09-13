from ultralytics import YOLO

model = YOLO('best(Flag_detector).pt') # yolov3-v7
print(model.names[0])