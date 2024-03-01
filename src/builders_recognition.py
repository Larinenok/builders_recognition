import yolov5
import supervision as sv


def find_builder():
    # load pretrained model
    model = yolov5.load('best.pt')

    # set model parameters
    model.conf = 0.25  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.agnostic = False  # NMS class-agnostic
    model.multi_label = False  # NMS multiple labels per box
    model.max_det = 1000  # maximum number of detections per image

    # set image
    img = 'images/people/2.jpg'

    # inference with test time augmentation
    results = model(img, augment=True)

    detections = sv.Detections.from_yolov5(results)
    detections = detections[detections.confidence > 0.5]

    for class_id in detections.class_id:
        if class_id in (0, 2):
            print(class_id)

    # show detection bounding boxes on image
    results.show()