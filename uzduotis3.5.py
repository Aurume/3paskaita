# Pakeisti 3 užduotį taip, kad neteisingai įvedus duomenis,
# mestų norimas klaidas lietuvių kalba (panaudoti try/except)

import datetime

while True:
    try:
        norima_data = input("Įveskite norimą datą(pvz.: 1900-01-01 00:00:00):")
        norima_data = datetime.datetime.strptime(norima_data, "%Y-%m-%d %H:%M:%S")
        break
    except:
        print("Neteisinga data")
siandien = datetime.datetime.now()
kiek_skiriasi = siandien - norima_data
