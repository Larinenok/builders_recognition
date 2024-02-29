import cv2
from cvzone.PoseModule import PoseDetector


def get_humans() -> list:
    detector = PoseDetector()
    original_image = cv2.imread('images/people/2.jpg')
    image = original_image.copy()

    all_boxes = []

    while True:
        image = detector.findPose(img=image, draw=False)
        _, boxes = detector.findPosition(img=image, draw=False)

        if (boxes == {}):
            break

        bbox = boxes['bbox']
        all_boxes.append(bbox)

        pos1 = (bbox[0] + int(bbox[2] / 10), bbox[1])
        pos2 = (bbox[0] + bbox[2] - int(bbox[2] / 10), bbox[1] + bbox[3])

        cv2.rectangle(image, pos1, pos2, (0, 0, 0), -1)

    for bbox in all_boxes:
        pos1 = (bbox[0], bbox[1])
        pos2 = (bbox[0] + bbox[2], bbox[1] + bbox[3])

        cv2.rectangle(original_image, pos1, pos2, (0, 255, 0))

    cv2.imwrite('images/output/output.jpg', img=original_image)

    return all_boxes