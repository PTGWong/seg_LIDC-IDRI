import pydicom
import matplotlib.pyplot as plt


def dcm_to_png(dcm_file, output_file):
    # 读取 DICOM 文件
    ds = pydicom.dcmread(dcm_file)

    # 提取图像数据
    image_data = ds.pixel_array

    # 显示图像
    plt.imshow(image_data, cmap=plt.cm.gray)
    plt.axis('off')

    # 保存为 PNG 图像
    plt.savefig(output_file, bbox_inches='tight', pad_inches=0)
    plt.close()


# 调用函数将 .dcm 文件转换为 .png 图像
dcm_file = '/media/conrad/34E66CB9E66C7D4C/LIDC-IDRI/1-640/LIDC-IDRI-0169/1.3.6.1.4.1.14519.5.2.1.6279.6001.132644395812981309476663139204/01-01-2000/1.3.6.1.4.1.14519.5.2.1.6279.6001.935683764293840351008008793409/1.3.6.1.4.1.14519.5.2.1.6279.6001.103360397863149164683182660418.dcm'
output_file = '/home/conrad/PycharmProjects/LIDC-IDRI-Preprocessing/test_png/1.png'
dcm_to_png(dcm_file, output_file)