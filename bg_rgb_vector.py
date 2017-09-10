#!/usr/bin/env python
# coding: utf-8

import numpy as np
import sys
import cv2

""" RBGのベクトル間の角度を用いた差分計算
"""

def get_rgb_angle(x, y):
    """ 背景画素と前景画素のRGBのベクトルのなす角度を求める

    Args:
        x: 背景画素
        y: 前景画素
    Retrun:
        ベクトルのなす角度(θ)
    """

    rgb_max = 255
    rgb_min = 0

    temp_x = (x - rgb_min) / (rgb_max - rgb_min)
    temp_y = (y - rgb_min) / (rgb_max - rgb_min)

    dot_xy = np.dot(temp_x, temp_y)
    norm_x = np.linalg.norm(temp_x)
    norm_y = np.linalg.norm(temp_y)
    cos = dot_xy / (norm_x * norm_y)
    rad = np.arccos(cos)
    theta = rad * 180 / np.pi

    return theta

def main():
    # 引数から背景、前景画像のパスをもらう
    args = sys.argv
    argc = len(args)
    if argc != 3:
        print("背景, 前景のパスを指定してください")
        quit()

    src_path = args[1]
    dst_path = args[2]

    src_im = cv2.imread(src_path, cv2.IMREAD_COLOR)
    dst_im = cv2.imread(dst_path, cv2.IMREAD_COLOR)
    diff_im = np.zeros(dst_im.shape, dtype = np.uint8)

    width = src_im.shape[0]
    height = src_im.shape[1]
    print(width, height)

    threshold = 10

    for i in range(width):
        for j in range(height):
            theta = get_rgb_angle(src_im[i, j, :], dst_im[i, j, :])
            if theta > threshold:
                diff_im[i, j, : ] = dst_im[i, j, :]

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", diff_im)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()


