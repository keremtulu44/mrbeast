# İPUÇLARI — İLK MESAJ KAYDI (ham)

> Bu dosya kullanıcının ilk mesajında verdiği tüm ipuçlarının birebir kaydıdır.
> Kullanıcı "bunları da kaydet, önemli" dedi. Çözümde referans olarak saklanıyor.

---

## İPUCU 1 (görseller) — açıklama
Benzer bölgede ama birleştirilmemiş puzzle parçaları; Birds of America kitabından en uygun
görsel eşleştirilerek yapılacak. **Kırmızı roman rakamı = kelimenin BAŞTAN say**, **mavi =
kelimenin SONDAN say**.

Sırayla görsel açıklamaları:
1. Umman Bayrağı — VI kırmızı, V mavi
2. Takvim — II kırmızı, IV mavi
3. Feastables Çikolata — VI kırmızı, VI mavi
4. Karlı Bulut — IX kırmızı, V mavi
5. Kırmızı Kare — VI kırmızı, VII mavi
6. Afrika kıtası ve Ot — IV kırmızı, VIII mavi
7. Gülen yüz emojisi 😂 — X kırmızı, XIV mavi
8. Gözlük (mavi çerçeveli) — V kırmızı, VII mavi
9. Grafik (4 bar, en küçük işaretli = "least") — VIII kırmızı, IX mavi
10. Swimsuit kadın — VII kırmızı
11. Amerika Bayrağı ve Ahır — VII kırmızı, IV mavi
12. Yılbaşı temalı çocuk (sakalsız, cüce değil) — II kırmızı, XI mavi
13. Mısır Lahiti ve Kartal/Şahin — VII kırmızı, IX mavi
14. Hapishane Kapısı ("barred owl" diğer ipucunda çıkıyordu) — VII kırmızı, I mavi

## İPUCU 2 (sayı + roman rakamları)
Birds of America kitabından. Metin hali:
```
029 III      039 VI
042 V        061 II
074 IX       076 IV
081 XIV      083 XI
101 II       102 III
112 IX       162 V
184 V        216 I
225 VI       235 VII
245 VIII     246 VIII
253 XIV      275 III
329 X        337 VI
358 IX       424-6 XVI
```

## İPUCU (ŞÜPHELİ) — telefon tuşları
Klasik döndürmeli telefon rakam/harf eşlemesi (T9/multi-tap). Metin:
```
    = 1
ABC = 2
DEF = 3
GHI = 4
JKL = 5
MNO = 6
PRS = 7
TUV = 8
WXY = 9
Operator = 0
```

## İPUCU 3
```
081 XIV
-
SeaHawks?
```
(İpucu 2'deki 081 XIV ile birebir aynı — doğrulama amaçlı, "?" var.)

## İPUCU 4
```
   ##
How Many?
```
(İki basamaklı `##` ve "kaç tane?" sorusu.)

## İPUCU 5
```
QX = TH
```
(QX → TH dönüşümü; "5th" gibi. İpucu 7'nin başına gelebilir.)

## İPUCU 6
```
142674
251634
461427
```
(6 haneli, hepsi 1-6 permütasyonu → İpucu 16'yı sıralamak için.)
> ⚠️ **Tur 11:** yukarıdaki satır YANLIŞ — ❌ **Tur 11 düzeltmesi:** üçü de 1-6 permütasyonu DEĞİL. Yalnızca `251634` {1,2,3,4,5,6}. `142674` ve `461427`'nin rakam kümesi {1,2,4,4,6,7} (7 var, 3 ve 5 yok; 4 iki kez) ve İpucu 16'nın `214674`'üyle AYNI küme. Kanıt: `dogrulama.py` [7].
> (Ham kayıt olduğu için kullanıcının orijinal satırı değiştirilmedi.)

## İPUCU 7
```
PLATES
```
("?" yok → doğrudan veri olarak kullanılacak.)

## İPUCU 8
```
Youtube link watch?
```
EK: https://youtu.be/82CX6WULNA0 (videonun linki kullanıcı tarafından eklendi.)

## İPUCU 9
```
  LSWRTE
  NNHTIN
  HDOTA
   -
Should I call
it bird fence?
```
Çözümü: **LAST WORD THEN NINTH** (rail fence cipher).
> ⚠️ **Tur 8 düzeltmesi:** mekanizma klasik rail fence DEĞİL. Doğru mekanizma: şifreyi
> ikiye böl (8+9) → 2. yarıyı ters çevir → dönüşümlü oku. Kodla doğrulandı, bkz. `cikti.md` §0-Q/1.
> (Ham kayıt olduğu için kullanıcının orijinal satırı değiştirilmedi.)

## İPUCU 10
```
Book w/
old names...
Alphetize?
```
(Alphabetize? → alfabetik sırala.)

## İPUCU 11
```
Roman
numbers for
Roman
words?
```
(Roma rakamları Roma/Latince kelimeler için.)

## İPUCU 12
```
Afiş: kitap üzerinde "Boo!"
altında: "Five of these"
```

## İPUCU 13
```
(527)
  |
(83544)
  |
MR(9)
```

## İPUCU 14
```
(364)
  |
(66)
 |
(6)
```

## İPUCU 15
```
(364) (4445)
   \    /
    (66)
     |
    (6)
```

## İPUCU 16
```
2                 6
1 4               7
                  4
```
(İpucu 6 ile birleşince 461427 → 46|14|27; 14 ve 27 özel bir sistemle alfabeye denk gelebilir.
Görselde tam konumlar var.)

## İPUCU 17
İki olay arasında tam **364 gün** var.

---

## GENEL (kullanıcı uyarısı)
- Verilere KÖRÜ KÖRÜNE UYMA; görsel mantıkla verilen verileri düşünmeden kullan.
- Diğer veriler yardımcı olabilir.
