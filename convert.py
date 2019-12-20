from PIL import Image
import os.path
import glob
path = "D:\\workspace\\python\\convert\\"
def convertpng(pngfile,outdir,width=512,height=512):
    img=Image.open(pngfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(pngfile)))
    except Exception as e:
        print(e)
        
for pngfile in glob.glob(path+"*.png"):
    convertpng(pngfile,path+"done")
