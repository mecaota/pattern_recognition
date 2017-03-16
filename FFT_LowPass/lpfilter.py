# coding:utf-8

#cf. http://lp-tech.net/archives/2228
#Edited: b1014167 Tetsuro Higuchi
#改変内容についてはレポートを参照

import numpy as np
import cv2
from PIL import Image

image = cv2.imread("test.jpg",0)
fimage = np.fft.fft2(image)

fimage = np.fft.fftshift(fimage) #フーリエ変換行列を中央へシフト
size = image.shape #画像サイズを取得
filter_matrix = np.zeros(size) #ゼロを画像サイズの大きさ分行列に代入

length = size[0]
center = size[0]/2

#フィルター設計
R = 5000 #周波数指定
for i in range(0,length):
    for j in range(0,length):
        if (i-center)*(i-center) + (j-center)*(j-center) < R*R:
            filter_matrix[i][j] = 1 #指定周波数より低い周波数画素をビット反転

print(filter_matrix)
fimage = fimage*filter_matrix
fimage = np.fft.fftshift(fimage) #shiftしてわかりやすくする
fimage = fimage * filter_matrix
fimage = np.fft.fftshift(fimage) #shiftしたものを元に戻す
ifimage = np.fft.ifft2(fimage)   #逆フーリエ変換
ifimage = ifimage.real           #実数部分のみ見る
Image.fromarray(np.uint8(ifimage)).show()
Image.fromarray(np.uint8(ifimage)).save('result.jpg')