from api import *
from check import *
from parse import *


pdf_file_path = "F:/testntrack/Adobe Scan Dec 29, 2023 (2).pdf"

result = make_api_call(pdf_file_path)

corrected = parse(result)


c = check(corrected)
print(c)