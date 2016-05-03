# coding=utf-8
__author__ = "gucuijuan"
from PIL import Image

"""
1 get_image_info,get image format,size,mode,eg:('JPEG', (96, 96), 'RGB')
2 convert_image_format_2_another,convert the format of image to another format,the default is jpg.
"""


def convert_image_format_2_another(img_name, convert_format="jpg"):
    """
    convert the format of image to another format,the default is jpg.
    :param img_name: the string of img_name
    :return:the string of jpg,png,tiff and etc.
    """
    im = Image.open(img_name)
    img_name = img_name.split(".")[0] + "." + convert_format
    im.save(img_name)


def get_image_info(image_path):
    """
    get image info,return list of (format,size,mode)
    :param image_path:
    :return:list
    """
    im = Image.open(image_path)
    return (im.format, im.size, im.mode)


