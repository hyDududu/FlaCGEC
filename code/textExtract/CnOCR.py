from cnocr import CnOcr
import numpy as np
import fnmatch,os
from PIL import Image
from pdf2image import convert_from_path

ocr = CnOcr()


def pdf2img(PDF_file):
    # PDF 转为图片
    pages = convert_from_path(PDF_file, 200)
    image_counter = 1
    for page in pages:
        filename = "./img/page_" + str(image_counter) + ".png"
        page.save(filename, 'png')
        image_counter += 1
    return image_counter, PDF_file

def img2txt(image_counter, PDF_file):
    # 图片中提取文本
    filelimit = image_counter-1
    outfile = newfilename(PDF_file)
    outfile = os.path.join('./OCR/', outfile)
    f = open(outfile, "a")
    for i in range(1, filelimit + 1):
        filename = "./img/page_"+str(i)+".png"
        text = ""
        for list in ocr.ocr(filename):
            text = text + list[0]
        print(text)
        # text = str((ocr.ocr(filename))[:][0]) # chi_sim 表示简体中文
        text = text.replace('\n', '')
        text = text.replace(' ', '')
        f.write(text)
    f.close()

def newfilename(filePath,outfile=''):
    dirs,filename = os.path.split(filePath)
    # 2、修改切分后的文件后缀
    outfile = ""
    if fnmatch.fnmatch(filename,'*.pdf') or fnmatch.fnmatch(filename,'*PDF'):
        outfile = filename[:-4] + '.txt' # 更新文件后缀名
    return outfile


filePath = './pdf/'
filelist = os.listdir(filePath)
for filename in filelist:
    PDF_file = os.path.join(filePath, filename)
    image_counter, PDF_file = pdf2img(PDF_file)
    img2txt(image_counter, PDF_file)


# https://gitee.com/cyahua/cnocr?_from=gitee_search