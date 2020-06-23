import fitz
path="D://Downloads//"
pdffile = path+"pdf1.pdf"
doc = fitz.open(pdffile)
page = doc.loadPage(0) #number of page
pix = page.getPixmap()
output = "outfile.png"
pix.writePNG(path+output)

