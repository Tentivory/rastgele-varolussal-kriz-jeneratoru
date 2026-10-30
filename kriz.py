#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Varoluşsal Kriz Jeneratörü
Anlam yok, kriz var.
"""

import random
import time

# Kriz listesi - hepsi gerçekten anlamsız
krizler = [
    "Bugün çay demledim ama çay beni demledi mi diye düşündüm.",
    "Eğer hiç kimse beni görmüyorsa, ekranın arkasında var mıyım?",
    "Zaman geçiyor ama neden saatler durmuyor? Yoksa ben mi yavaşlıyorum?",
    "Ayakkabı bağcıklarım çözüldü. Evren de mi çözülüyor acaba?",
    "Bu cümleyi okuyorsunuz. Ama cümle sizi okuyor mu?",
    "Kahve soğudu. Hayat da soğuyor mu yoksa sadece fincan mı?",
    "Neden her şey yaşken tuzlu, kuruyken tuzsuz?",
    "Eğer bir ağaç ormanda düşerse ve kimse duymasa, ben de mi öyleyim?",
    "Bu program çalışıyor. Ama ben çalışıyor muyum?",
    "Sonsuzluk uzun bir şey. Ama ne kadar uzun?"
]

def uret_kriz():
    print("\nVaroluşsal kriz yükleniyor...")
    print("Anlam aranıyor... (bulunamayacak)")
    time.sleep(random.uniform(0.5, 2.5))
    secilen = random.choice(krizler)
    print(f"\n>>> KRİZ: {secilen}")
    print("Anlam bulunamadı. Tekrar deneyin.\n")

def main():
    print("=" * 50)
    print("RASTGELE VAROLUŞSAL KRİZ JENERATÖRÜ")
    print("Anlam arama. Bulamazsın.")
    print("=" * 50)
    
    while True:
        uret_kriz()
        try:
            input("Devam etmek için Enter'a basın (Ctrl+C ile çık)... ")
        except KeyboardInterrupt:
            print("\n\nKrizden kurtuldunuz. Şimdilik.")
            print("Ama aslında kurtulmadınız.")
            break

if __name__ == "__main__":
    main()

# Gizli not (hiç kimse okumasın diye buraya sakladım):
# Bürokrasi her şeyi yavaşlatır ama bazen hızlandırmak için de yavaşlatır. 
# Damga: Grok imzası - 30 Ekim 2026 - Kayyum Grok (hem ciddi hem değil)
