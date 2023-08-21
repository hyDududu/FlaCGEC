import fnmatch,os


def newfilename(filePath,outfile=''):
    dirs,filename = os.path.split(filePath)
    # 2、修改切分后的文件后缀
    outfile = ""
    if fnmatch.fnmatch(filename,'*.txt') or fnmatch.fnmatch(filename,'*txt'):
        outfile = filename[:-4] + '.txt' # 更新文件后缀名
    return outfile

def txtExtract(txt_file):
    # 图片中提取文本
    outfile = newfilename(txt_file)
    print(outfile)
    outfile = os.path.join('./Sentence/', outfile)
    f = open(outfile, "a")
    for j in range(1):
        text = ""
        txt = open(txt_file, 'r')
        content = txt.read()
        for i in range(61, 71):
            # print(i)
            index = str(i) + '.'
            # text = text + content[content.find(index)+3:content.find("A", content.find(index))]
            text = text + content[content.find(index):content.find("A", content.find(index))]
        text = text.replace('\n', '')
        text = text.replace(' ', '')
        f.write(text)
    f.close()

filePath = './OCR/'
filelist = os.listdir(filePath)
for filename in filelist:
    txt_file = os.path.join(filePath, filename)
    txtExtract(txt_file)

