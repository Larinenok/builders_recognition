import yolov5
import supervision as sv
import numpy as np
import cv2


def find_builder(image) -> bool:
    # load pretrained model
    model = yolov5.load('best.pt')

    # set model parameters
    model.conf = 0.25  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.agnostic = False  # NMS class-agnostic
    model.multi_label = False  # NMS multiple labels per box
    model.max_det = 2  # maximum number of detections per image

    # inference with test time augmentation
    results = model(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), augment=True)

    detections = sv.Detections.from_yolov5(results)
    detections = detections[detections.confidence > 0.65]

    is_have_hat = 0 in detections.class_id
    is_have_vest = 3 in detections.class_id

    # show results
    results.show()
    return is_have_hat and is_have_vest