from PyPDF2 import PdfFileWriter, PdfFileReader
# page.cropBox.getLowerLeft()
# page.cropBox.getLowerRight()
# page.cropBox.getUpperLeft()
# page.cropBox.getUpperRight()

def crop_left_page(page, width, height):
        left_page = page
        left_page.cropBox.lowerLeft = (15, 0)
        left_page.cropBox.upperRight = (430, height)
        return left_page
        
def crop_right_page(page, width, height):
        right_page = page
        right_page.cropBox.lowerLeft = (410, 0)
        right_page.cropBox.upperRight = (width-15, height)
        return right_page

with open("/content/drive/MyDrive/prob.pdf", "rb+") as in_f:
    right_input = PdfFileReader(in_f)
    left_input = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = right_input.getNumPages()
    width, height = right_input.getPage(1).cropBox.getUpperRight()
    # print(width, height)
    for i in range(numPages):

        right_page = crop_right_page(right_input.getPage(i), width, height)
        output.addPage(right_page)

        left_page = crop_left_page(left_input.getPage(i), width, height)
        output.addPage(left_page)

    with open("/content/drive/MyDrive/out.pdf", "wb") as out_f:
        output.write(out_f)

