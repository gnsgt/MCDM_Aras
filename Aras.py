import pandas as pd
import numpy as np

    #Excel dosyasını oku ve DataFrame'e dönustur
df_excel = pd.read_excel("C:/Users/gokha/OneDrive/Masaüstü/Tez/5.1-Aras.xlsx")
maliyet = df_excel.iloc[1:2].copy()
agirlik = df_excel.iloc[:1].copy()
df = df_excel.iloc[2:]  

    #Kac satır kaç sutun?
satir_sayisi = df.shape[0] 
sutun_sayisi = df.shape[1]

    #Donusturulmus Karar Matrisi
df_donusturulmus = df.copy()
for j in range(0,sutun_sayisi):
    for i in range(0,satir_sayisi):
        if maliyet.iloc[0,i] == "fayda":
            df_donusturulmus.iloc[j,i] = df.iloc[j,i]
        else:
            df_donusturulmus.iloc[j,i] = 1 / df.iloc[j,i]

df_donusturulmus_toplamlar = []
for j in range(sutun_sayisi):
    toplam = 0
    for i in range(satir_sayisi):
        toplam = toplam + df_donusturulmus.iloc[i,j]
    df_donusturulmus_toplamlar.append(toplam)
    

    #Normalize
normalize_df = df_donusturulmus.copy()
for j in range(sutun_sayisi):
    toplam = 0
    for i in range(satir_sayisi):
        normalize_df.iloc[i,j] =  df_donusturulmus.iloc[i,j] / df_donusturulmus_toplamlar[j]

# Agirlikli Normalize İslemi
anormalize_df = normalize_df.copy()  # normalize_df verilerini kopyala
for i in range(sutun_sayisi):
    anormalize_df.iloc[:, i] = normalize_df.iloc[:, i] * agirlik.iloc[0, i]
    
    #Si
si= []
for j in range(0,sutun_sayisi):
    si_toplam = 0
    for i in range(0,satir_sayisi):
        si_toplam = anormalize_df.iloc[j,i] + si_toplam
    si.append(si_toplam)

sia0_ref = si.pop(0)

    #Ki
ki = []
for i in range(len(si)):
    ki.append(si[i] / sia0_ref)

print("\n")
for i in range(satir_sayisi-1):
    max_deger = max(si)
    max_index = si.index(max_deger)
    print(f"Aras Si: {max_deger}, İndex: {max_index + 1}")
    si[max_index] = -99999

print("\n")
for i in range(satir_sayisi-1):
    max_deger = max(ki)
    max_index = ki.index(max_deger)
    print(f"Aras Ki: {max_deger}, İndex: {max_index + 1}")
    ki[max_index] = -99999




    
