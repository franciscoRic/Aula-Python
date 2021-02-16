"""

Modulos Externos

https://pypi.org

from colorama import init, Fore, Back, Style

init()

print(Fore.BLACK + Back.CYAN + 'Francisco Ricardo')

"""

import pydf

pdf = pydf.generate_pdf('<h1>Francisco Ricardo</h1>')

with open(r'c:\test_doc.pdf', 'wb') as f:
    f.write(pdf)
