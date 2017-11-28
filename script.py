from PyPDF2 import PdfFileWriter, PdfFileReader
import PyPDF2
import sys
import copy

def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 50):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '💃' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

output = PdfFileWriter()
inputFile = "input.pdf"
if len(sys.argv) > 1:
	inputFile = sys.argv[1]


input_pdf = PdfFileReader(open(inputFile, "rb"))
skip_pages = [0];
input_length = input_pdf.getNumPages()
print("file " + inputFile + " is read successfully with " + str(input_length) + " pages")

for i in range(input_length):
	if i in skip_pages:
		output.addPage(input_pdf.getPage(i))
	else:
		# page_left = PyPDF2.pdf.PageObject.createBlankPage()
		# page_right = PyPDF2.pdf.PageObject.createBlankPage()
		# page_left.mergePage(input_pdf.getPage(i))
		# page_right.mergePage(input_pdf.getPage(i))
		page_left = input_pdf.getPage(i)
		page_right = copy.copy(page_left)
		
		page_right.mediaBox.upperRight = (
			page_right.mediaBox.getUpperRight_x()/2,
			page_right.mediaBox.getUpperRight_y()
		)
		page_left.mediaBox.upperLeft = (
			page_left.mediaBox.getUpperRight_x()/2,
			page_left.mediaBox.getUpperRight_y()
		)
		output.addPage(page_left)
		output.addPage(page_right)
	printProgress(i, input_length)
outputFile = "output.pdf"
print("finished successfully! writing file")
if len(sys.argv) > 2:
	outputFile = sys.argv[2]
output.write(open(outputFile, "wb"))
print("file written successfully")

