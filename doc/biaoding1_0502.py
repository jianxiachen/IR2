import cv2
import numpy as np
from PIL import Image
import math
import os
import os.path as osp

s = 2  # 2
k = 33  # 33


# # # # 定义一个空字典
# shujuji_6552nm = {}
# # 以下写成一个循环读存图像数据到字典中
# # 设置目录路径
# # directory = r"E:\exp1\test"
# directory = r"E:\0429\on_center\speckle\speckle_qubj_0_pingyi_33\586nm"
# count=1
# for m in range(1,134,33):  #1-53,增量为2
#     for n in range(1,134,33):   #1-53,增量为2
#         m_n = str(m) + ',' + str(n)
#         # print(m_n)
#         image_path = os.path.join(directory, str(count)+'.tiff')
#         # print('...........', image_path)
#         if not os.path.exists(image_path):
#             print("The image is not exists:",image_path)
#             continue
#         else:
#             count+=1
#             shujuji_6552nm[m_n] = cv2.imread(image_path, -1)
#             # print(shujuji_6552nm[m_n])
# # cv2.imshow("tif1",shujuji_6552nm['1,1'])
# # cv2.waitKey(0)
# # print(shujuji_6552nm['1,1'])
#
# def Move(img, delta_x, delta_y):
#     img_info = img.shape
#     height = img_info[0]
#     width = img_info[1]
#
#     mat_translation = np.float32([[1, 0, -delta_x], [0, 1, -delta_y]])
#     dst = cv2.warpAffine(img, mat_translation, (width, height))
#     return dst
#
# # dest = "E:/0429/on_center/speckle/shujuji_chazhi/128_128/596nm_crop"   # 需要变动
# # if not osp.exists(dest):
# #     os.makedirs(dest)
#
# save_path = "E:/0429/on_center/speckle/shujuji_chazhi/move_33/586nm"
# if not osp.exists(save_path):
#     os.makedirs(save_path)
#
# for q in range(3,4):     #(25)/(25)(25,26)/(25,26) 27*27  38*38
#     for p in range(3,4):  #(25)/(25,26)(25)/(25,26)
#         i1 = 1 + k * q
#         j1 = 1 + k * p
#         i2 = 1 + k * q
#         j2 = 1 + k * (p+1)
#         i3 = 1 + k * (q+1)
#         j3 = 1 + k * p
#         i4 = 1 + k * (q+1)
#         j4 = 1 + k * (p + 1)
#         a = str(i1)+','+str(j1)
#         b = str(i2)+','+str(j2)
#         c = str(i3)+','+str(j3)
#         d = str(i4)+','+str(j4)
#         print(a, b, c, d)
#         print(shujuji_6552nm[a])
#         for r in range(i1, i1+k+1):       # 这里需要+1 when?与上面p,q对应
#             for z in range(j1, j1+k+1):   # 这里需要+1 when?
#                 img1 = Move(shujuji_6552nm[a], math.floor((r-i1)*s), math.floor((z-j1)*s))
#                 img2 = Move(shujuji_6552nm[b], math.floor((r-i2)*s), math.floor((z-j2)*s))
#                 img3 = Move(shujuji_6552nm[c], math.floor((r-i3)*s), math.floor((z-j3)*s))
#                 img4 = Move(shujuji_6552nm[d], math.floor((r-i4)*s), math.floor((z-j4)*s))
#                 C_rz = ((k-abs(r-i1))/k)*((k-abs(z-j1))/k)*img1+((k-abs(r-i2))/k)*((k-abs(z-j2))/k)*img2+((k-abs(r-i3))/k)*((k-abs(z-j3))/k)*img3+((k-abs(r-i4))/k*(k-abs(z-j4))/k)*img4
#                 C_rz = C_rz.astype(np.uint16)  # uint8没必要吧？
#                 # # im = Image.fromarray(C_rz)
#                 cv2.imwrite(os.path.join(save_path, str(i1)+ ',' + str(j1) + '#' +str(r) + ',' + str(z) + "_move.tiff"), C_rz)
#                 sp = C_rz.shape  # 获取图像形状：返回【行数值，列数值】列表
#                 sz1 = sp[0]  # 图像的高度（行 范围）
#                 sz2 = sp[1]  # 图像的宽度（列 范围）
#                 # # 对图像裁剪
#                 # e = int(sz1 / 2 - 64)  # y start
#                 # f = int(sz1 / 2 + 64)  # y end
#                 # g = int(sz2 / 2 - 64)  # x start
#                 # h = int(sz2 / 2 + 64)  # x end
#                 # cropImg = C_rz[e:f, g:h]  # 裁剪图像
#
#                 # ##以亮斑为中心取散斑区域(亮斑区域相对整个图像区域是在变动的！！按照平移之后25张散斑的位置变动，需要写一个循环。)
#                 # 中心亮斑的位置按照p,q的变化来写循环，确定抠值区域
#                 # 好像不需要变动，只需要确定中心位置就可以了。   这样的话把插值和抠图分开会更简单一些！！
#                 # 先根据y来确定中心亮斑以上的区域。再来抠取CCD中相同位置的散斑。
#
#
#                 # cropImg = C_rz[y_center-int(speckle_sz_y/2):y_center+int(speckle_sz_y/2), x_center-int(speckle_sz_x/2):x_center+int(speckle_sz_x/2)]
#                 # ##以亮斑为中心取散斑区域(亮斑在动，中心的位置在变化)
#
#                 # # cropImg = cropImg.astype(np.uint16)
#                 # # print(cropImg)
#                 # # dest = "E:/cjx/shujuji_chazhi20/6557nm_crop"   # 需要变动
#                 # # im = Image.fromarray(cropImg)
#
#                 # cv2.imwrite(os.path.join(dest, str(i1) + ',' + str(j1) + '#' + str(r) + ',' + str(z) + "_crop.tiff"),
#                 #             cropImg)  # 写入图像路径


##第二步
# 读取插值后的散斑，并裁剪。保存裁剪后的散斑
root_path = r"E:/0429/on_center/speckle/shujuji_chazhi/move"
save_path = r"E:/0429/up_center/speckle/shujuji_chazhi/crop_128_128"
# root_path = r"E:/0429/on_center/speckle/shujuji_chazhi/move_33"
# save_path = r"E:/0429/on_center/speckle/shujuji_chazhi/crop_33_260_460"
# image_path = os.path.join(directory, str(count)+'.tiff')
if not osp.exists(save_path):
    os.makedirs(save_path)

for wl_file in os.listdir(root_path):
    print(wl_file)  # 586nm
    wl_path = os.path.join(root_path, wl_file)
    print(wl_path)  # E:/0429/on_center/speckle/shujuji_chazhi/move\586nm
    # save_file = os.path.join(save_path, wl_path[:-4])
    for image_file in os.listdir(wl_path):
        print(image_file)  # 1,1,1,13_move.tiff

        save_file = os.path.join(save_path,wl_file)
        # save_file = os.path.join(save_path + wl_file, image_file[:-4]+'.tiff')
        print(save_file)
        if not osp.exists(save_file):
            os.makedirs(save_file)

        image_path = os.path.join(wl_path,image_file)
        print(image_path)
        C_rz = cv2.imread(image_path, -1)
    # save_file = "F:/scene_pic" + scene_path[:-4]

        sp = C_rz.shape  # 获取图像形状：返回【行数值，列数值】列表
        sz1 = sp[0]  # 图像的高度（行 范围）
        sz2 = sp[1]  # 图像的宽度（列 范围）

# # #裁剪按照这个来,取亮斑上方区域
        n_y = 8 #y方向亮斑长度的一半
        y_center_crop = 358 #y方向亮斑的中心；
        x_center_crop = 485 #x方向按照亮斑的中心

        N_roi_y = 128 # 4 * 22 + 1 = 89 % 实际单幅散斑每行的像元数：初始像元数减去全视场单行的像元数
        N_roi_x = 128 #同上 % 列方向同上

        cropImg = C_rz[y_center_crop - n_y - N_roi_y:y_center_crop - n_y, x_center_crop - int(
            N_roi_x / 2): x_center_crop + int(N_roi_x / 2)]

        cv2.imwrite(os.path.join(save_file, image_file[:-9]+'crop.tiff'), cropImg)

        # # #裁剪按照这个来,取亮斑上区域（包含亮斑）以平移之后的中间处散斑（第13张散斑）的零频亮斑的中心为中心
        # y_center_crop = 424  # y方向亮斑的中心；
        # x_center_crop = 550  # x方向按照亮斑的中心
        #
        # N_roi_y = 260  # 4 * 22 + 1 = 89 % 实际单幅散斑每行的像元数：初始像元数减去全视场单行的像元数
        # N_roi_x = 460  # 同上 % 列方向同上
        #
        # cropImg = C_rz[y_center_crop - int(N_roi_y / 2):y_center_crop + int(N_roi_y / 2), x_center_crop - int(
        #     N_roi_x / 2): x_center_crop + int(N_roi_x / 2)]
        # # cropImg = C_rz[201:460+1, 201: 660+1]
        # # cropImg = C_rz[y_center - int(speckle_sz_y / 2):y_center + int(speckle_sz_y / 2),
        # #           x_center - int(speckle_sz_x / 2):x_center + int(speckle_sz_x / 2)]
        #
        # cv2.imwrite(os.path.join(save_file, image_file[:-9]+'crop.tiff'), cropImg)











