from pdf2image import convert_from_path
import glob
#images = convert_from_path("TeracimiAhval.pdf", 500,poppler_path=r'C:\\Users\\serhat\\Downloads\\poppler-0.68.0_x86')
files=glob.glob("E:\\Custom Documents\\TahSAM\\*.pdf")
for i, filename in enumerate(files):
    fname = 'E:\\Custom Documents\\Tah\sayfa'+str(i)+'.jpg'
    images= convert_from_path(filename, 500,poppler_path=r'C:\\Users\\serhat\\Downloads\\poppler-0.68.0_x86')
    images[0].save(fname, "JPEG")