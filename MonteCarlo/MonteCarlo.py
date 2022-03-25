import pandas as pd
import numpy as np
import seaborn as sns
import random

# excell dosyasinda ki verileri okuma islemi
data = pd.read_excel("monte_carlo.xlsx")

# 48 elemanli bir liste olusturup 48 ayin veri miktarlarini
# ekledim ve her miktarin kac defa gectini yani frekans degerini hesapladim
veri = list(range(48))
veri = data["Miktar"]

uc=0
dort=0
bes=0
alti=0
for i in veri:
    if i == 3:
        uc= uc+1
    elif i == 4:
        dort= dort+1
    elif i ==5:
        bes=bes+1
    elif i == 6:
        alti = alti+1

# frekans ve olasilik degerlerini tuple tipinde ekrana bastim

miktar = pd.DataFrame({
    "Miktar": [3,4,5,6],
    "Frekans": [uc, dort,bes,alti],
    "Olasilik": [uc/48, dort/48, bes/48, alti/48]
})
print(miktar)

# kumulatif olasilik hesaplama islemi gerceklestirdim
# round fonksiyonu olasilik degerlerinin virgulden sonraki 6 hanesini aldim
olasilik = [round(uc/48,6), round(dort/48,6), round(bes/48,6), round(alti/48,6)]
k_olasilik = [0,0,0,0,0]
k_olasilik[1]=olasilik[0]
k_olasilik[2]=olasilik[0]+olasilik[1]
k_olasilik[3]=olasilik[0]+olasilik[1]+olasilik[2]
k_olasilik[4]=olasilik[0]+olasilik[1]+olasilik[2]+olasilik[3]
mikta=[3,4,5,6,""]
print(pd.DataFrame(k_olasilik,mikta))

# 12 tane rastgele sayi urettim ve frekans degerlerini hesapladim
x=0
three=0
four=0
five=0
six=0

for j in range(1000):
    for i in range(12):
        x = round(random.random(),6)
        if(x > k_olasilik[0] and x < k_olasilik[1]):
            three += 1
        elif(x > k_olasilik[1] and x < k_olasilik[2]):
            four += 1
        elif(x > k_olasilik[2] and x < k_olasilik[3]):
            five += 1
        elif(x > k_olasilik[3] and x < k_olasilik[4]):
            six += 1

# Rastgele sayilarin Kumulatif Olasilik degerlerinden karsilik gelen Miktar degerini ekrana yazdirdim
tahmin = pd.DataFrame({
    "Miktar": [3,4,5,6],
    "Frekans": [three, four,five,six]
})
print(tahmin)






