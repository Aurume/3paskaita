# Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
# Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
# Metų
# Mėnesių
# Dienų
# Valandų
# Minučių
# Sekundžių


import datetime

norima_data = input("Įveskite norimą datą(pvz.: 1900-01-01 00:00:00):")
norima_data = datetime.datetime.strptime(norima_data, "%Y-%m-%d %H:%M:%S")  # nedet kabutese kablelio tarp datos ir laiko!!!
siandien = datetime.datetime.now()
print(siandien)
print(norima_data)

kiek_skiriasi = (siandien - norima_data)
print("Data skiriasi dienų: ", kiek_skiriasi.days)

print("Kiek  metų: ", kiek_skiriasi.days // 365)
print("Kiek  mėnesių: ", round(kiek_skiriasi.days / 365 * 12))
print("Kiek savaičių: ", kiek_skiriasi.days // 7)
print("Kiek dienų: ", kiek_skiriasi.days)
print("Kiek valandų: ", round(kiek_skiriasi.total_seconds() // 3600))
print("Kiek minučių: ", round(kiek_skiriasi.total_seconds() / 60))
print("Kiek sekundžių: ", round(kiek_skiriasi.total_seconds()))
