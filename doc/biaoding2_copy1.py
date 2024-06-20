
#from spectral import *

'''

import cv2
import numpy as np
import math
def function(img,m,n):
    height,width,channels =img.shape
    emptyImage=np.zeros((m,n,channels),np.uint16)
    value=[0,0,0]
    sh=m/height
    sw=n/width
    for i in range(m):
        for j in range(n):
            x = i/sh
            y = j/sw
            p=(i+0.0)/sh-x
            q=(j+0.0)/sw-y
            x=int(x)-1
            y=int(y)-1
    for k in range(3):
        if x+1<m and y+1<n:
            value[k]=int(img[x,y][k]*(1-p)*(1-q)+img[x,y+1][k]*q*(1-p)+img[x+1,y][k]*(1-q)*p+img[x+1,y+1][k]*p*q)
            emptyImage[i, j] = (value[0], value[1], value[2])
    return emptyImage
img=cv2.imread("e:\\lena.bmp")
zoom=function(img,2048,2048)
cv2.imshow("Bilinear Interpolation",zoom)
cv2.imshow("image",img)
cv2.waitKey(0)
'''


#     import os
#     import cv2
#     import numpy as np
#
#
#     def Move(img, delta_x, delta_y):
#         img_info = img.shape
#         height = img_info[0]
#         width = img_info[1]
#
#         mat_translation = np.float32([[1, 0, delta_x], [0, 1, delta_y]])
#         dst = cv2.warpAffine(img, mat_translation, (width, height))
#         return dst
#
#
#     def TestOnePic():
#         test_tif_loc = r"E:\shujuji\6552nm\1.tif"
#         test_tif = cv2.imread(test_tif_loc, -1).transpose(1, 0)
#         cv2.imshow("Show Img", test_tif)
#         img1 = Move(test_tif, 30, 30)
#         cv2.imshow("Img1", img1)
#         cv2.waitKey(0)
#         print(test_tif.shape)
#         print(img1)
#
#
#     # def TestOneDir():
#     #     root_path = "E:\\shujuji\\6552nm"
#     #     save_path = root_path
#     #     for a, b, c in os.walk(root_path):
#     #         for file_i in c:
#     #             file_i_path = os.path.join(a, file_i)
#     #             print(file_i_path)
#     #             img_i = cv2.imread(file_i_path)
#     #
#     #
#     #
#     #             img_move = Move(img_i,30,30)
#     #             cv2.imwrite(os.path.join(save_path, file_i[:-4] + "_move.tif"), img_move)
#
#     if __name__ == "__main__":
#         TestOnePic()
#         # TestOneDir()
#         # root_path = "E:\\shujuji\\6552nm"
#         # AllData(root_path)
#
# [delta_x=math.floor((Z2*(r-i1)*D)/(tao*Z1)), delta_y=math.floor((Z2*(r-j1)*D)/(tao*Z1))]
# [delta_x=math.floor((Z2*(r-i2)*D)/(tao*Z1)), delta_y=math.floor((Z2*(r-j2)*D)/(tao*Z1))]
# [delta_x=math.floor((Z2*(r-i3)*D)/(tao*Z1)), delta_y=math.floor((Z2*(r-j3)*D)/(tao*Z1))]
# [delta_x=math.floor((Z2*(r-i4)*D)/(tao*Z1)), delta_y=math.floor((Z2*(r-j4)*D)/(tao*Z1))]




import cv2
import h5py
from matplotlib import pyplot
import io
import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
# with h5py.File('4cam_0411-1640-1.mat', 'r') as f:
#     print(list(f.keys()))
#     # print(list(f.items()))
#     dset = f['rad']  #####从总数据集出发旋转矩阵
#     dset = np.rot90(dset, 2)  # 旋转矩阵使图片旋转180°
#
#     print(dset.shape)
#     print(dset.dtype)
#
#     # print(dset[()])    #用空元组[()]检索所有数据/标量数据
#     # print(dset[0:2])    #获取多分切片上的数据
#     # print(dset[0:2,0:2,0:2])   #截取部分数据
#     result = dset[0:10, 0:145, 0:145]
#     print(result.shape)
#     print(result)
#     for i,item in enumerate(result[:10]):
#         plt.subplot(2,5,i+1)
#         plt.axis('off')
#         plt.imshow(item)
#     plt.show()

import os
import cv2


import os
import os.path as osp
import cv2
import numpy as np
from sklearn.preprocessing import Normalizer
from PIL import Image

b0 = []
path = r"E:\0429\up_center\speckle\shujuji_chazhi\crop_128_128\586nm"
path_list = os.listdir(path)
# print(path_list)
path_list.sort(key=lambda x: int(x.split('_')[0].split('#')[1].split(',')[1]))
path_list.sort(key=lambda x: int(x.split('_')[0].split('#')[1].split(',')[0]))
print(path_list)
for info in path_list:
    info = os.path.join(path, info)  # 将路径与文件名结合起来就是每个文件的完整路径
    # print(info)
    image = cv2.imread(info, -1)
    # print(image)
    b0 = np.append(b0, image)
print(len(b0))
b1 = b0.reshape(7921, 16384)  # 2809=53*53/图像像素点,1444=38*38/采样点数
b1 = b1.T
print(b1)
# # 存储数组数据, .npy文件
array_path=r"E:\0429\up_center\speckle\shujuji_chazhi\crop_128_128\cljz_586nm"
if not osp.exists(array_path):
    os.makedirs(array_path)

# scipy.io.savemat(array_path+"/"+'A.mat', {'A':b1})  # file_name.mat为保存的文件名。该保存的mat文件可直接在matlab打开
np.save(array_path+"/"+"array.npy", b1)  # 如果文件路径末尾没有扩展名.npy，该扩展名会被自动加上.

# # 读取数组数据, .npy文件
# b1 = np.load('array4.npy')
# print(b1.dtype)
# print(b1.shape)


# import os
# import cv2
# import numpy as np
# from PIL import Image
# import math
#
# for i,j,m,n in range():
#     image = cv2.imread("E:\\shujuji_chazhi\\6552nm\\1,1,1,1_move.tif",-1)
#     sp = image.shape  # 获取图像形状：返回【行数值，列数值】列表
#     sz1 = sp[0]  # 图像的高度（行 范围）
#     sz2 = sp[1]  # 图像的宽度（列 范围）
# # sz3 = sp[2]                #像素值由【RGB】三原色组成
# # 你想对文件的操作
#     a = int(sz1 / 2 - 72)  # y start
#     b = int(sz1 / 2 + 73)  # y end
#     c = int(sz2 / 2 - 145)  # x start
#     d = int(sz2 / 2 + 145)  # x end
#     cropImg = image[a:b, c:d]  # 裁剪图像
#     save_path = "E:\\shujuji_chazhi\\6552nm_resize"
# #im = Image.fromarray(cropImg)
#     cv2.imwrite(os.path.join(save_path, "_crop.tif"), cropImg)  # 写入图像路径

