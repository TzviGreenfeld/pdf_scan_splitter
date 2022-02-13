from PyPDF2 import PdfFileWriter, PdfFileReader


def crop_left_page(page, width, height):
        left_page = page
        left_page.cropBox.lowerLeft = (15, 0)
        left_page.cropBox.upperRight = (width/2, height)
        return left_page
        
def crop_right_page(page, width, height):
        right_page = page
        right_page.cropBox.lowerLeft = (width/2, 0)
        right_page.cropBox.upperRight = (width-15, height)
        return right_page
def main(args):
        with open(args[1], "rb+") as in_f:
            right_input = PdfFileReader(in_f)
            left_input = PdfFileReader(in_f)
            output = PdfFileWriter()

            numPages = right_input.getNumPages()
            width, height = right_input.getPage(1).cropBox.getUpperRight()
            
            for i in range(numPages):

                right_page = crop_right_page(right_input.getPage(i), width, height)
                output.addPage(right_page)

                left_page = crop_left_page(left_input.getPage(i), width, height)
                output.addPage(left_page)

            with open(args[2], "wb") as out_f:
                output.write(out_f)

if __name__ == '__main__':
    main(sys.argv)          
