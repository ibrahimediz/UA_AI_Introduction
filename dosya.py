import os
import shutil
liste = ["Mehmet","Cagatay","Omer","Ugur","Mustafa"]
fileName = "ornekPandas.ipynb"
for item in liste:
    adres = os.path.join("Egzersizler",item)
    if not os.path.exists(adres):
        os.mkdir(adres)
    # open(os.path.join("Egzersizler",item,fileName),"wb")
    shutil.copy(f"Egzersizler/SoruCevap/{fileName}",f"Egzersizler/{item}/{fileName}")
    

