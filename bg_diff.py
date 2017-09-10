#!/usr/bin/env python
# coding: utf-8

import numpy as np
import sys
import cv2

""" 画素の絶対値の差分を用いた差分計算
"""

def main():
    threshold = 30 # しきい値

    # 引数から背景、前景画像のパスをもらう
    args = sys.argv
    argc = len(args)
    if argc != 3:
        print("背景, 前景のパスを指定してください")
        quit()

    src_path = args[1]
    dst_path = args[2]

    # 前景と背景の画像をグレースケールで読み込み
    src_im = cv2.imread(src_path, cv2.IMREAD_GRAYSCALE)
    src_median = cv2.medianBlur(src_im, 5)
    dst_im = cv2.imread(dst_path, cv2.IMREAD_GRAYSCALE)
    dst_median = cv2.medianBlur(dst_im, 5)

    # 差分画像表示用に前景のカラー画像を読み込む
    dst_color_im = cv2.imread(dst_path, cv2.IMREAD_COLOR)

    # グレースケール画像の画素値の絶対値をとる
    diff_im = cv2.absdiff(src_median, dst_median)

    # 差分を二値化
    diff_bin = cv2.threshold(diff_im, threshold, 255, cv2.THRESH_BINARY)[1]

    # 画像を切り出す
    result_im = cv2.bitwise_and(dst_color_im, diff_bin)

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", result_im)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()


