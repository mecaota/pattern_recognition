# coding:utf-8

#respect from: http://tamanobi.hatenablog.com/entry/2015/07/18/110621
#cf. http://www.pybytes.com/pywavelets/ref/2d-dwt-and-idwt.html
#Edited: b1014167 Tetsuro Higuchi
#改変内容についてはレポートを参照

import numpy as np
import cv2, pywt
from PIL import Image
import PIL.ImageDraw
import PIL.ImageFont

#pywtを使ったウェーブレット変換関数
def PyWavelet(img,level=1, wavlet="db1", mode="sym"):
  #画像ファイルをグレースケールへ変換
  gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
  res = []
  tmp = gray.astype(np.uint16)
  res_pywt = pywt.wavedec2(gray,wavlet, level=level, mode=mode)
  print(res_pywt)
  res_kinji, (res_x, res_y, res_xy) = res_pywt
#マージ
  np.c_(tmp,res_x)
  np.r_(tmp,res_y)
  np.r_(tmp,res_xy)
  print("after merge")
  print(tmp)
  return tmp
  #多分,1階ウェーブレットで実行の返り値は「近似値,(x方向,y方向,xy方向)」と思われ

if __name__ == '__main__':
  im = cv2.imread("test.jpg")
  tr = PyWavelet(im)
  Image.fromarray(tr).show()
  Image.fromarray(tr).save('result.jpg')

  #実装失敗