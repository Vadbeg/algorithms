"""Draws koch snowflake fractal curve"""

from typing import Tuple

import numpy as np
from cv2 import cv2


def get_second_point(pt1: Tuple[int, int], angle: float, length: int) -> Tuple[int, int]:
    pt2_x = pt1[0] + np.sin(np.pi * (angle / 180)) * length
    pt2_y = pt1[1] + np.cos(np.pi * (angle / 180)) * length

    pt2 = (int(pt2_x), int(pt2_y))

    return pt2


def get_last_points(pt1: Tuple[int, int], angle: float, length: int) -> Tuple[Tuple[int, int],
                                                                              Tuple[int, int],
                                                                              Tuple[int, int]]:

    pt2 = get_second_point(pt1=pt1, angle=angle, length=length)

    one_third_x = (pt2[0] - pt1[0]) // 3
    one_third_y = (pt2[1] - pt1[1]) // 3

    print(f'One third x: {one_third_x}')
    print(f'One third y: {one_third_y}')

    pt_1_3 = (int(pt1[0] + one_third_x), int(pt1[1] + one_third_y))
    pt_2_3 = (int(pt1[0] + 2 * one_third_x), int(pt1[1] + 2 * one_third_y))

    pt_middle = get_second_point(pt1=pt_1_3, angle=angle + 60, length=length // 3)

    return pt_1_3, pt_2_3, pt_middle


def draw_koch(image: np.ndarray, depth: int, pt1: Tuple[int, int], angle: float, length: int):
    if depth == 0:
        pt2 = get_second_point(pt1=pt1, angle=angle, length=length)

        cv2.line(image, pt1=pt1, pt2=pt2, color=(0, 0, 0), thickness=2)

    else:
        pt_1_3, pt_2_3, pt_middle = get_last_points(pt1=pt1, angle=angle, length=length)

        RADIUS = 3

        cv2.circle(img=image, center=pt_1_3, radius=RADIUS, color=(0, 0, 255), thickness=cv2.FILLED)
        cv2.circle(img=image, center=pt_2_3, radius=RADIUS, color=(0, 255, 0), thickness=cv2.FILLED)
        cv2.circle(img=image, center=pt_middle, radius=RADIUS, color=(255, 0, 0), thickness=cv2.FILLED)
        cv2.circle(img=image, center=pt1, radius=RADIUS, color=(255, 255, 0), thickness=cv2.FILLED)

        draw_koch(image=image, depth=depth-1, pt1=pt1, angle=angle, length=length // 3)
        draw_koch(image=image, depth=depth-1, pt1=pt_1_3, angle=angle + 60, length=length // 3)
        draw_koch(image=image, depth=depth-1, pt1=pt_2_3, angle=angle, length=length // 3)
        draw_koch(image=image, depth=depth-1, pt1=pt_middle, angle=angle - 60, length=length // 3)


if __name__ == '__main__':
    image = np.ones((500, 500, 3)) * 255

    draw_koch(image=image, depth=4, pt1=(250, 30), angle=0, length=450)

    cv2.imshow('Image', image)
    cv2.waitKey(0)

