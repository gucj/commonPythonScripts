# coding=utf-8
__author__ = "gucuijuan"
import qrcode
import os
import Image


def gen_qrcode(string, path, logo=""):
    """
    生成二维码，可带中间图片或者不带
    需要安装qrcode, PIL库
    :param string: 二维码字符串
    :param path: 生成的二维码保存路径
    :param logo: 二维码中间图片的路径
    :return:
    """
    qr = qrcode.QRCode(
        version=3,  # 生成的二维码大小,从1 到 40依次变大
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=4,  # 二维码每个小个子包含的像素数
        border=1  # 二维码外围的边框大小
    )
    qr.add_data(string)
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGBA")

    if logo and os.path.exists(logo):
        icon = Image.open(logo)
        img_w, img_h = img.size
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)
    img.save(path)