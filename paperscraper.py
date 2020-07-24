import requests
from datetime import date
from PyPDF2 import PdfFileMerger, PdfFileReader
import glob
import os

mergedObject = PdfFileMerger()


get_date = date.today()
today = get_date.strftime("%d%m%y%y")

pageno = '01'

while True:
    URL = 'https://epaper.livehindustan.com/epaperimages/' + \
        today + '/' + today + '-NGR-PAT-' + pageno + '.PDF'

    r = requests.get(url=URL, allow_redirects=False)

    # End of page logic
    if (r.status_code != 200):
        break

    with open('./' + pageno + '.pdf', 'wb') as f:
        f.write(r.content)

    # Incrementing page numbers
    if (int(pageno[0]) == 0):
        pageno = str(int(pageno[1]) + 1).zfill(2)
    else:
        pageno = str(int(pageno) + 1)


endpage = int(pageno) - 1

# Merging PDF's
pdf_list = (glob.glob("*.pdf"))
pdf_list.sort()
i = 0
while (i < len(pdf_list)):
    mergedObject.append(PdfFileReader(pdf_list[i], 'rb'))
    i = i + 1

mergedObject.write("Todays Newspaper - " + today + ".pdf")

# Deleting individual files
j = 0
while (j < len(pdf_list)):
    os.remove(pdf_list[j])
    j = j + 1
