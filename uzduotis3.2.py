# Atspausdinti dabartinę datą ir laiką
# Atimti iš dabartinės datos ir laiko 5 dienas ir juos atspausdinti
# Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdinti
# Atspausdinti dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17


import datetime

dabar_data = datetime.datetime.now()
print(dabar_data)

print(dabar_data - datetime.timedelta(days=5))

print(dabar_data + datetime.timedelta(hours=8))

print(dabar_data.strftime("%Y %m %d, %X"))
