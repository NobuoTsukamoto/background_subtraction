#!/usr/bin/env python
# coding: utf-8

import numpy as np
import sys
import cv2

""" MOG
"""

def main():

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

    # fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

    fgmask = fgbg.apply(src_median)
    fgmask = fgbg.apply(dst_median)

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", fgmask)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()


