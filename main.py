import random

def tahmin_oyunu():
    print("Merhaba! Sayı tahmin oyununa hoş geldiniz.")
    print("1 ile 100 arasında bir sayıyı tahmin etmeye çalışın.")

    # Rastgele bir sayı seçme
    rastgele_sayı = random.randint(1, 100)
    tahmin_hakkı = 5

    while tahmin_hakkı > 0:
        print("\nKalan tahmin hakkınız:", tahmin_hakkı)
        tahmin = int(input("Tahmininizi girin: "))

        # Tahminin kontrolü
        if tahmin == rastgele_sayı:
            print("Tebrikler! Doğru tahmin ettiniz.")
            break
        elif tahmin < rastgele_sayı:
            print("Daha büyük bir sayı girin.")
        else:
            print("Daha küçük bir sayı girin.")

        tahmin_hakkı -= 1

    if tahmin_hakkı == 0:
        print("\nTahmin hakkınız bitti. Doğru cevap:", rastgele_sayı)

# Oyunu başlat
tahmin_oyunu()