import cv2
import numpy as np

def detect_circles(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detected_circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 250, param1=90, param2=100, minRadius=100, maxRadius=200)
    if detected_circles is not None:
        detected_circles = np.uint16(np.around(detected_circles))
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            # Draw the circumference of the circle.
            cv2.circle(image, (a, b), r, (255, 255, 0), 8)
            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(image, (a, b), 1, (255, 255, 255), 8)
    return image

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, img1 = cap.read()
        if not ret:
            break

        img2 = detect_circles(img1.copy())
        cv2.imshow("Circles Detection", np.hstack([img1, img2]))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = '/Users/sarah/PycharmProjects/circle_detection/mov_4.MOV'
    main(video_path)
