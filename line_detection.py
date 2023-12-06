import cv2
import argparse
import numpy as np
import math

def fill_triangle(image, vertices, color, mask_value):
    stencil = np.zeros(image.shape[:-1]).astype(np.uint8)
    cv2.fillPoly(stencil, [np.array(vertices)], mask_value)
    sel = stencil != mask_value
    image[sel] = color
    return image

def detect_lines(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    lines = cv2.HoughLinesP(edges, 1, np.pi/380, 30, maxLineGap=400)
    return lines

def draw_lines(image, lines):
    bottom_right_y = 0
    top_right_y = 10000
    bottom_right_x = top_right_x = 0

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 225), 5)
        if bottom_right_y < y2:  # Bottom right point
            bottom_right_y = y2
            bottom_right_x = x2
        if top_right_y > y2:  # Top right point
            top_right_y = y2
            top_right_x = x2

    mid_x = (bottom_right_x - top_right_x) // 2 + top_right_x
    mid_y = (top_right_y - bottom_right_y) // 2 + bottom_right_y
    return mid_x, mid_y

def main(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found.")
        return

    img_og = img.copy()
    fill_color = [173, 182, 185]
    mask_value = 255

    if image_path == "front.jpg":
        vertices = [(1540, 500), (-450, 2000), (3445, 2000)]
        img = fill_triangle(img, vertices, fill_color, mask_value)

        centroid_x = sum([pt[0] for pt in vertices]) // 3
        centroid_y = sum([pt[1] for pt in vertices]) // 3

        lines = detect_lines(img)
        if lines is not None:
            mid_x, mid_y = draw_lines(img, lines)

        up_point = centroid_y + 115
        down_point = centroid_y - 600
        img_og = cv2.arrowedLine(img_og, (centroid_x, up_point), (centroid_x, down_point), (0, 0, 0), 20)

    cv2.imshow("Processed Image", np.hstack([img, img_og]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())
    main(args["image"])
