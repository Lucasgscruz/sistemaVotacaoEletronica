from PIL import Image
import os


arquivos = os.listdir()
for i in arquivos:
    if("jpg" in i):
        img = Image.open(i)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img.save("resize_" + i)
