import cv2
from cvzone.PoseModule import PoseDetector
from builders_recognition import find_builder


def get_humans(input_image_path: str, output_image_path: str) -> list:
    detector = PoseDetector(staticMode=True,
                            modelComplexity=1,
                            smoothLandmarks=True,
                            enableSegmentation=False,
                            smoothSegmentation=True,
                            detectionCon=0.5,
                            trackCon=0.5)
    original_image = cv2.imread(input_image_path)
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
    
    output_image = original_image.copy()

    for bbox in all_boxes:
        pos1 = (bbox[0], bbox[1])
        pos2 = (bbox[0] + bbox[2], bbox[1] + bbox[3])

        image = original_image[pos1[1]:pos2[1], pos1[0]:pos2[0]]
        if image.size < 10000:
            continue

        color = (0, 0, 255)
        text = 'Danger'
        if find_builder(image):
            color = (0, 255, 0)
            text = 'Safe'

        cv2.rectangle(output_image, pos1, pos2, color, 5)
        (w, _), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        output_image = cv2.rectangle(output_image, (pos1[0], pos1[1] - 40), (pos1[0] + w + 20, pos1[1]), color, -1)
        cv2.putText(output_image, text, (pos1[0], pos1[1] - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv2.imwrite(output_image_path, img=output_image)

    return all_boxes