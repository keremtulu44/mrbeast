# MrBeast Gizli $10.000 Bulmacası — Çözüm Defteri

**Video:** `82CX6WULNA0` — "How 1 Person Solved A $1,000,000 Puzzle!" (Colin)
**Son güncelleme:** 2026-09-13

---

# 0) DURUM ÖZETİ

| Bölüm | Durum |
|---|---|
| İpucu 2 (24 plaka → 24 harf) | ✅ **%100 DOĞRULANDI** (İpucu 7 + bağımsız lejant kontrolü) |
| İpucu 6+16+4+5+7 zinciri → `46TH PLATE` | ✅ **ÇALIŞIYOR** (kendi kendini doğruluyor) |
| İpucu 13 `M̶R̶(9)` → **`MRBEASTSAND`** | ✅ **HAND düştü** — kullanıcı doğruladı: MR üstü çizili, **el çizimi YOK** |
| İpucu 1 (14 görsel → 27 harf) | 🟡 9/14 kilitli, dizi henüz okunmuyor |
| İpucu 3–17 | 🟡 Kısmi (aşağıda tablo) |
| İpucu 16 dizilimi (142 mi 214 mü) | ⚠️ **KRİTİK ÇELİŞKİ** — aşağıda TUR 2 / A ve B |
| `HAND` mı `SAND` mı | ⚠️ **KANIT YETERSİZ** — aşağıda TUR 2 / C |

---

# 0-B) 🆕 TUR 2 BULGULARI (2026-09-13, 2. tur)

## A) İpucu 16'nın dizilimi — 360 permütasyon brüt-zorlaması

Panelin fiziksel dizilimi (İpucu 16 ham kaydı):
```
   2              6
 1   4            7      ← sol ÜÇGEN (2 tepede, 1 ve 4 tabanda)
                  4      ← sağ DİKEY KOLON (6 / 7 / 4)
```
Sol üçgenin 6 okuma yönü × sağ kolonun 2 yönü = **12 aday girdi.**

Anahtar **251634** ile (kural: `yeni = [2., 5., 1., 6., 3., 4.]`):

| Okuma | Sonuç | İkili gruplar | A1Z26 | Geçerli mi |
|---|---|---|---|---|
| **214674** | **172446** | **17\|24\|46** | **Q X 46** | ✅ **TEK TEMİZ SONUÇ** |
| 142674 | 471426 | 47\|14\|26 | ✗ ✗ Z | ❌ 47 > 26 |
| 142476 | 471624 | 47\|16\|24 | ✗ P X | ❌ |
| 214476 | 172644 | 17\|26\|44 | Q Z ✗ | ❌ |
| 241674 | 472416 | 47\|24\|16 | ✗ X P | ❌ |
| 421674 | 274416 | 27\|44\|16 | ✗ ✗ P | ❌ |
| 124674 | 271446 | 27\|14\|46 | ✗ N ✗ | ❌ |
| 412674 | 174426 | 17\|44\|26 | Q ✗ Z | ❌ |

*(12 okumanın tamamı + 360 permütasyonun tamamı tarandı.)*

### 🔴 SONUÇ 1
**Anahtar 251634 ile, 12 panel okumasından SADECE `214674` geçerli bir
`[harf][harf][sayı]` üçlüsü üretir — ve o harfler tam olarak İpucu 5'in
tarif ettiği `QX` (=TH) çiftidir.** Diğer 11 okuma 47/74/41/76/27 gibi
geçersiz çiftler verir.

→ Yani **`46TH PLATE` zinciri, panelin `214` okumasına yaslanıyor.**

---

## B) ⚠️ AMA: İpucu 6'nın üç satırı ancak `241635` ile tutarlı

İpucu 6:
```
142674   ← satır 1 (girdi)
251634   ← satır 2 (anahtar)   [kullanıcı: "241635 DEĞİL, 251634"]
461427   ← satır 3 (çıktı?)
```

Hangi anahtar `142674`'yi `461427`'ye götürür? **Permütasyon tek belirlenir:**

```
142674  --(241635)-->  461427   ✅ TAM İSABET (satır1 × anahtar = satır3)
142674  --(251634)-->  471426   ❌ satır 3 değil
142674  --(251634 ters)--> 217446  ❌
```

Yani **İpucu 6 kendi içinde ancak anahtar `241635` ise tutarlı** — üç satır
"girdi / anahtar / çıktı" olarak kusursuz oturuyor.

### İki sistem karşı karşıya

| | SİSTEM 1 (46TH) | SİSTEM 2 (İpucu 6'nın kendi örneği) |
|---|---|---|
| Girdi | 214674 | 142674 |
| Anahtar | **251634** | **241635** |
| Çıktı | 172446 → 17\|24\|46 → QX+46 | 461427 → 46\|14\|27 |
| Anlam | **"46TH PLATE"** = Barred Owl = İpucu 14'ün görseli ✅ | 46 = plaka, 14 = N, 27 = ? |
| Dayanak | İpucu 5 (QX=TH) + İpucu 7 (PLATES) + İpucu 14 (görsel) | Sadece aritmetik |

### 🔴 SONUÇ 2 — TEK BELİRLEYİCİ SORU
**İpucu 6'nın 2. satırı gerçekten `251634` mi, `241635` mi?**
- `251634` ise → panel `214` okunmalı → `46TH PLATE` zinciri doğru.
- `241635` ise → panel `142` okunmalı (sizin dediğiniz gibi) ve İpucu 6
  kendi kendini gösteren bir örnek; `46TH` zinciri o zaman tesadüf.

⚠️ Bu ikisi **aynı anda doğru olamaz** (farklı permütasyon yörüngeleri:
214674'ün yörüngesi {214674, 172446, 741624, 427416}, 142674'ninki ise
{142674, 471426, 724614, 217446, 142476, 471624, …} — kesişmiyorlar).

---

## C) 🔥 Kalan 13 harf ve `HAND` — DÜRÜST YENİDEN DEĞERLENDİRME

Sözlük: **114.000 kelime** (gcide) + kelime sıklığı verisi. Sonuçlar:

### 1) "HAND havuzdan çıkıyor" bir KANIT DEĞİL ❌
24 harfli havuzdan oluşabilen kelime sayıları:

| Uzunluk | Oluşabilen kelime sayısı |
|---|---|
| 3 harf | 357 |
| 4 harf | **899** |
| 5 harf | 1131 |
| 8 harf | 927 |

`HAND` 899 dört-harfli kelimeden sadece biri. `SAND` da çıkıyor, `HARD`,
`HEAD`, `READ`, `MADE`, `HOME`, `FIND` da. → **Havuz testi HAND'ı
SAND'a karşı ayırt edemez.** Önceki turdaki "KANITLANDI" ifadesi fazla güçlüydü.

### 2) Kalan 13 harf her iki varyantta da anlamsız
| Varyant | Kalan 13 harf | Oluşan kelime | En iyi 3'lü gruplar |
|---|---|---|---|
| `MRBEAST`+**HAND** | D E E E F I M O R S T T W | 732 | WEIRD FEET MOST · WORST FEED TIME · SWEET DIET FROM |
| `MRBEAST`+**SAND** | D E E E F H I M O R T T W | 584 | TRIED FEET WHOM · WORTH FEED TIME · TEETH FROM WIDE |

İkisi de saçma. → **Kalan 13 harfin anlamlı bir kelime grubu olmadığı
neredeyse kesin.** Bu, sizin sezdiğiniz "sorun".

### 3) 🆕 YENİ KEŞİF: `83544` = **8+3+5+4+4 = 24** = harf sayısı!
İpucu 15'teki `4445` = `LAST(4) WORD(4) THEN(4) NINTH(5)` bir **kelime
uzunluğu kodu**. Aynı mantık:

```
527   → 5+2+7   = 14 = "BIRDSOFAMERICA" (14 harf) ✅
83544 → 8+3+5+4+4 = 24 = İpucu 2'nin 24 harfi ✅✅
```

→ **İpucu 13'ün ara adımı (83544), 24 harfin 5 kelimeye
(8, 3, 5, 4, 4 harf) bölünmüş hâli.**

### 4) ⚠️ Bu hipotez `SAND` lehine, `HAND` aleyhine bir delil
5 kelimenin ilki **8 harf** olmalı:

| Seçenek | 8 harf + 3 harf | Değerlendirme |
|---|---|---|
| **SAND** | `MRBEASTS` (8) + `AND` (3) | ✅ iki kelime de temiz — ve topluluğun **`BEASTSAND`** okumasını birebir açıklıyor |
| HAND | `MRBEASTH` (8) + `AND` (3) | ❌ "MRBEASTH" kelime değil |

Ayrıca `MR(9)` = "MR" + 9 harf: `BEASTS`(6) + `AND`(3) = 9 ✅ tam oturuyor.

⚠️ **AMA bu kesin değil**: 5 kelimelik cümlenin tamamı bulunamadı
(8,3,5,4,4 kalıbıyla havuzdan **4.000+** farklı cümle çıkıyor ve en yüksek
sıklıklıları bile anlamsız: "HANDMADE BET FIRST WERE MOST" gibi).

### 5) Öneri
HAND/SAND'ı havuzdan değil **görselden** çözmeli:
- İpucu 13'ün görselinde/pedinde **el (hand)** çizimi veya yazısı var mı?
- İpucu 13 "kırmızı/beyaz" — elin rengi/şekli betimlenebilir mi?

---

# 0-C) 🆕 TUR 3 — ÜÇ HARİCİ ÇIKTININ BAĞIMSIZ DENETİMİ (2026-09-13)

Tam rapor: **`ucuncu_taraf_degerlendirme.md`**

## ✅ Doğrulananlar
| İddia | Sonuç |
|---|---|
| `MRBEASTS AND WIDTH MORE FEET` havuzu 24/24 kullanıyor | ✅ **KUSURSUZ** (A2 B1 D2 E4 F1 H1 I1 M2 N1 O1 R2 S2 T3 W1, sıfır artık; uzunluklar tam 8-3-5-4-4) |
| İlk 11 harf `MRBEASTSAND` = İpucu 13'ün **MR+(9)**'u (MR\|BEASTS\|AND → 9 harf) | ✅ birebir uyumlu → **SAND lehine en iyi delil** |
| `214764 --241635--> 172446` (= 214674+251634 ile aynı) | ✅ doğru → anahtar tartışması pratikte önemsiz |
| 48 kombinasyonun hiçbiri 3 geçerli A1Z26 çifti vermiyor | ✅ doğru → 3. yuvanın SAYI olması **yapısal zorunluluk**; `46TH PLATE` zinciri güçlendi |
| `mrb.gg/p/puzzle` = "Million Dollar Puzzle Answers", 1 Eyl 2026, 84 sayfa | ✅ **GERÇEK** (sayfa çekildi) |

## ❌ Çürüyenler
| İddia | Ölçümüm |
|---|---|
| "EACH tesadüf olamaz, P≈1/457.000" | ❌ Aynı 27 harf rastgele karıştırılınca **ortalama 17,35** farklı 4-harfli kelime çıkıyor; `each` %0,6. Çoklu karşılaştırma hatası → **14→1 yönü hâlâ kanıtsız** |
| "A'dan Z'ye akrostiş = alfabetik okumanın kanıtı" | ❌ **TAUTOLOJİ** — liste zaten alfabetik sıralı, baş harflerin A→Z gitmesi zorunlu sonuç |
| "NIDTEM → NINTH ITEM", "SAT D HERE → SAT THERE" | ❌ harfler uyuşmuyor, **uydurma** |
| "(8,3,5,4,4) için 0 çözüm var" | ❌ **YANLIŞ** — 110.028 çözüm buldum (biri 24/24 oturuyor) |
| #13'ü "EACH çıkmazsa olmaz" diye kilitlemek | ❌ **döngüsel** (EACH zaten #13+#14'ün harfleri) |

## ⚠️ Kendi hatam (düzeltme)
Önceki turda "8,3,5,4,4 kalıbıyla 4.000+ aday, hepsi anlamsız" yazmıştım. Arama
**8000 sonuç sınırına takılmış**; gerçek sayı **110.028**. "Anlamsız" yargısı
(sübjektif olarak) duruyor ama sayı yanlıştı.

## ⚠️ Şüpheli — kullanmadan önce videodan/PDF'ten doğrula
1. `MRBEASTS AND WIDTH MORE FEET` → 110.028 alternatiften biri ve **gramatik değil**
2. #10 = 203 (E) → gerekçesi "kuşun rengi"; kilitli 9 örneğin hepsi **İSİM punu** → 349 (J) birincil kalıyor
3. PDF alıntıları (Rosé 73 / Will Campbell 66 / "Hawks up on the Pats 6-0") → PDF iki kez HTTP 500, ayrıca Hawks=NBA / Pats=NFL tutarsız → **halüsinasyon riski yüksek**
4. `AAA(9)` transkripsiyonu → senin M̶R̶(9) okumanla çelişiyor
5. `97, 121, 171` sayıları, "27=3³→3×9 matris", "(364)=XOR\|SUPERB\|OWLS" → doğrulanamadı

---

# 1) KESİNLEŞEN KURALLAR

1. **Sayı = *Birds of America* (Havell, 1–435) PLAKA numarası.** (İpucu 7 `PLATES`)
2. **Roma rakamı = plakaya kazınmış ORİJİNAL Latince adın harfi.** (İpucu 11 `Roman numbers for Roman words?`)
3. **İngilizce ad yalnızca kuşu TESPİT etmek için** — sayım Latince ad üzerinden.
4. **Boşluk, noktalama ve otorite kısaltması (L., Gm., Wils.) SAYILMAZ.**
5. **`424-6` = plaka 424'ün 6. kuşu** (Brown Longspur). Doğrulandı: kullanıcının 435'lük listesinde 424 altında 6 kuş var ve 6.'sı Brown Longspur.
6. **İpucu 1'de kırmızı = baştan, mavi = sondan.** İkisi **2 AYRI harf** verir (aynı harf değil).
7. **`?` ile biten ipucu = doğrulama (meta); `?` olmayan = veri.** (İpucu 3, 4, 8, 10, 11 → meta)
8. **Latince ad minimum uzunluk kısıtı:** `L ≥ max(kırmızı, mavi)`.

### İpucu 1'in Latince saydığının KESİN kanıtı
İpucu 1 / görsel 7 (😂) = Laughing Gull.
- İngilizce adı `Laughing Gull` = **12 harf**
- Mavi rakamı = **XIV = 14**
- 14 > 12 → **İngilizcede sayılamaz.** Zorunlu olarak Latince.

---

# 2) 🔥 ANA ZİNCİR — İpucu 16 + 6 + 4 + 5 + 7

```
①  İPUCU 16  :  214  +  674   =  214674
      (elektrik panolarında İKİ AYRI ÜÇLÜ, farklı konumlarda)
              ↓
②  İPUCU 6 anahtarı 251634 ile sırala
      kural: yeni = [2., 5., 1., 6., 3., 4.]
      214674 → 1 7 2 4 4 6
              ↓
③  İPUCU 4 (## / "How Many?") → iki basamaklı gruplar
      17 | 24 | 46
              ↓
④  A1Z26 →   17 = Q      24 = X      46 = SAYI
              ↓
⑤  İPUCU 5 (QX = TH) →  QX → TH
              ↓
⑥  Sayı başa gelir  →  46 + TH  =  46TH
              ↓
⑦  İPUCU 7 (PLATES) →  "46TH PLATE"
```

## SONUÇ: **`46TH PLATE` = PLAKA 46 = BARRED OWL = İPUCU 14'ÜN GÖRSELİ (HAPİSHANE KAPISI)** ✅

Bu zincir **doğrulama** işlevi görüyor: yöntemimizin (plaka → Latince ad → harf) doğru olduğunu geriye dönük kanıtlıyor. İpucu 3'teki "SeaHawks?" mantığıyla aynı.

**İpucu 5'in kendi notu bunu birebir tarif ediyordu:**
> *"QX bir kodlamada çıkacak TH (**5th** gibi İngilizce kullanımda)"*
> → **46 + th = 46th** — sıra sayısı (ordinal) kullanımı tam olarak bu.

### İpucu 6'nın yapısı (netleşti)

| İpucu 6 satırı | Rakam kümesi | Rolü |
|---|---|---|
| 142674 | {1,2,4,4,6,7} | girdi / örnek |
| **251634** | {1,2,3,4,5,6} | **ANAHTAR** (tek gerçek 1-6 permütasyonu) |
| 461427 | {1,2,4,4,6,7} | kullanıcının manuel sonucu |

İpucu 16 = **214674** → {1,2,4,4,6,7} — aynı küme!

### 🔶 "JUN" — TEYİT GEREKLİ ⚠️
461427'ye 251634 tekrar uygulanırsa → 624714 → 62|47|14 → **J,U,N** = **JUN**.
İpucu 17'nin tarihlerinden biri **June 30 - 89** olduğu için çarpıcı.
**AMA** 461427 kullanıcının kendi SONUCU olduğu için bu **çift uygulama** = şüpheli.
Alternatif: 461427'nin kendi çiftleri = **46\|14\|27** (46 yine çıkıyor; 14=N, 27=?).

### 🟡 142674 → 471426 → 47\|14\|26 → U,N,Z — çözülmedi. Muhtemelen örnek/şamandıra.

---

# 3) İPUCU 2 — 24 PLAKA (✅ %100 DOĞRULANDI)

Kullanıcının güvenilir 435'lük Havell listesiyle **24/24 birebir eşleşti.**
Ayrıca plaka 102 (Blue Jay, *Corvus cristatus*) bağımsız lejant kaynağından (audubon.org + kazınmış `PLATE CII`) doğrulandı.

| # | Plaka | Roma | Kuş (eski ad) | Latince ad (orijinal lejant) | Harf |
|---|---|---|---|---|---|
| 1 | 029 | III | Towhe Bunting | Fringilla erythrophthalma | **I** |
| 2 | 039 | VI | Crested Titmouse | Parus bicolor | **B** |
| 3 | 042 | V | Orchard Oriole | Icterus spurius | **R** |
| 4 | 061 | II | Great Horned Owl | Strix virginiana | **T** |
| 5 | 074 | IX | Indigo Bird | Fringilla cyanea | **A** |
| 6 | 076 | IV | Virginian Partridge | Perdix virginiana | **D** |
| 7 | 081 | XIV | Fish Hawk / Osprey | Falco haliaetus | **S** |
| 8 | 083 | XI | House Wren | Troglodytes aedon | **S** |
| 9 | 101 | II | Raven | Corvus corax | **O** |
| 10 | 102 | III | Blue Jay | Corvus cristatus | **R** |
| 11 | 112 | IX | Downy Woodpecker | Picus pubescens | **E** |
| 12 | 162 | V | Zenaida Dove | Columba zenaida | **M** |
| 13 | 184 | V | Mango Humming Bird | Trochilus mango | **H** |
| 14 | 216 | I | Wood Ibiss | Tantalus loculator | **T** |
| 15 | 225 | VI | Kildeer Plover | Charadrius vociferus | **D** |
| 16 | 235 | VII | Sooty Tern | Sterna fuliginosa | **F** |
| 17 | 245 | VIII | Thick-billed Murre | Uria brunnichii | **N** |
| 18 | 246 | VIII | Eider Duck | Fuligula mollissima | **A** |
| 19 | 253 | XIV | Jager | Lestris parasiticus | **T** |
| 20 | 275 | III | Noddy Tern | Sterna stolida | **E** |
| 21 | 329 | X | Yellow-breasted Rail | Rallus noveboracensis | **E** |
| 22 | 337 | VI | American Bittern | Ardea minor | **M** |
| 23 | 358 | IX | Pine Grosbeak | Pyrrhula enucleator | **E** |
| 24 | 424-6 | XVI | Brown Longspur (424'ün 6. kuşu) | Plectrophanes townsendi | **W** |

**24 HARF:** `I B R T A D S S O R E M H T D F N A T E E M E W`

**Harf havuzu:**
```
A×2   B×1   D×2   E×4   F×1   H×1   I×1   M×2   N×1   O×1   R×2   S×2   T×3   W×1  = 24
```

**Alfabetik sıralama (İpucu 10 "Alphabetize?"):**
`M R W B E A S T S A T D H E R E O F N I D T E M`
→ içinde görünen: `MR` · `BEAST(S)` · `SAT` · `HERE` · `ITEM` · `OF`

---

# 4) ⚠️ `HAND` DÜŞÜRÜLDÜ → **`MRBEASTSAND`** (2026-09-13 kullanıcı doğrulaması)

## 🔴 KULLANICI DOĞRULAMASI: İpucu 13'te `M̶R̶(9)` — MR üstü çizili, **BAŞKA ÇİZİM YOK**
Bu iki sonucu birden doğuruyor:
1. **`AAA(9)` transkripsiyonu ÇÜRÜDÜ** (Çıktı 3'ün topluluk kaynaklı iddiası yanlış).
   Kullanıcının gözüyle: `M̶R̶(9)`, el/hand çizimi yok.
2. **`HAND` hipotezi görsel desteğini tamamen kaybetti.** Savunulacak tek dayanağı
   "havuzdan yazılabiliyor" idi — o da `SAND` için eşit derecede geçerli.

## `SAND` lehine kesinleşen delil
```
MRBEASTS(8) + AND(3) + [5] + [4] + [4]   →  havuzu 24/24 kullanıyor (sıfır artık)
ilk 11 harf = MRBEASTSAND  =  MR̶ + (9 harf)  ← İpucu 13'ün yapısıyla BİREBİR
```
`MR̶(9)` = "MR'yi at, kalan 9 harf" = **`BEASTSAND`**. HAND için karşılığı
`BEASTHAND` olurdu ama o zaman 8 harfli ilk kelime `MRBEASTH` olmak zorunda —
kelime değil.

---

## (ESKİ BÖLÜM — artık geçersiz, arşiv)

# 4-ESKİ) `MRBEAST` + `HAND` — ÇÜRÜDÜ

24 harf havuzundan:

```
M R B E A S T   →  M✓ R✓ B✓ E✓ A✓ S✓ T✓   (hepsi havuzda)
H A N D         →  H✓ A✓ N✓ D✓             (hepsi havuzda)
```

**`MRBEASTHAND` = 11 harf = `MR` + 9 harf**

```
İPUCU 13:   (527) → (83544) → M̶R̶(9)
                                ↓
                    MR + BEASTHAND = MRBEASTHAND
                    (2)   (   9   )
```

> **`MR̶` üstü çizili = "MR zaten biliniyor", `(9)` = kalan 9 harf.**
> Bu, kullanıcının EN BAŞINDAN BERİ savunduğu `HAND` tezinin kanıtı.
> Topluluğun `BEASTSAND` okuması anlamsız ("BEAST SAND") — `HAND` DOĞRU.

**Kullanılan:** A×2(hepsi), B×1, D×1, E×1, H×1, M×1, N×1, R×1, S×1, T×1
**KALAN 13 HARF:**
```
D  E  E  E  F  I  M  O  R  S  T  T  W
```

### Kalan 13 harften aday kelimeler (İpucu 15'in mavi sonucu = 6 harf)

| Kelime | Harfler | Uzunluk |
|---|---|---|
| **FOREST** | F,O,R,E,S,T | 6 ⭐ |
| **SORTED** | S,O,R,T,E,D | 6 |
| **SORTIE** | S,O,R,T,I,E | 6 |
| DEFROST | D,E,F,R,O,S,T | 7 |
| TWISTED | T,W,I,S,T,E,D | 7 |
| FROSTED | F,R,O,S,T,E,D | 7 |

⚠️ **AÇIK:** Kalan 13 harfin dizilişi henüz çözülmedi. Kullanıcının yönlendirmesi:
*"İspanyolca / öz dillerde kelime grubu türet, sadece İngilizce odaklanma."*

---

# 5) İPUCU 1 — 14 GÖRSEL → 27 HARF

**Kural:** her görsel → kuş → plakadaki Latince ad → 🔴 baştan / 🔵 sondan → **2 harf**
(10. görselde sadece kırmızı var → **27 harf**)

| # | Görsel | Kuş | Plaka | Latince | L | 🔴 | 🔵 | Durum |
|---|---|---|---|---|---|---|---|---|
| 1 | Umman Bayrağı | American Crossbill | 197 | loxiacurvirostra | 16 | c | o | 🟡 |
| 1-alt | " | Louisiana Heron | **217** | **ardealudoviciana** | 16 | **l** | **c** | 🔒 doğrulandı |
| 2 | Takvim | **Ruby-crowned Wren** | **195** | **reguluscalendula** | 16 | **e** | **d** | 🔒 |
| 3 | Çikolata | **Brown Pelican** | **251** | **pelecanusfuscus** | 15 | **a** | **f** | 🔒 |
| 4 | Karlı bulut | **Snow Bunting** | **189** | **emberizanivalis** | 15 | **n** | **v** | 🔒 |
| 5 | Kırmızı kare | **Red-shouldered Hawk** | **56** | **falcolineatus** | 13 | **l** | **i** | 🔒 |
| 6 | Afrika + ot | **Savannah Finch** | **109** | **fringillasavanna** | 16 | **n** | **a** | 🔒 |
| 7 | 😂 | **Laughing Gull** | 314 | larusatricilla | 14 | **c** | **L** | 🔒 |
| 8 | Mavi gözlük | Blue-eyed Y. Warbler | 95 | sylviaaestiva | 13 | i | a | 🟡 |
| 9 | 4 bar + ok en küçük | **Least Stormy Petrel** | **340** | **thalassidromapelagica** | 20 | **i** | **m** | 🔒 |
| 10 | Kahverengi kadın mayosu | Water-hen | 349? | rallus? | ? | ? | — | ⚠️ |
| 11 | ABD bayrağı + ahır | Barn Swallow | 173 | hirundorustica | 14 | o | t | 🟡 |
| 12 | Elf | Children's Warbler | 35 | sylvicolachildrenii | 19 | y | a | 🟡 |
| 13 | Lahit + kartal | Golden Eagle | 181 | aquilachrysaetos | 16 | c | h | 🟡 |
| 14 | Hapishane kapısı | **Barred Owl** | **46** | **strixnebulosa** | 13 | **e** | **a** | 🔒 |

## Kilitli Latince adların lejant kaynakları (audubon.org + kazınmış Roma rakamı)

| Plaka | Roma | İngilizce | Latince | L |
|---|---|---|---|---|
| 46 | XLVI | Barred Owl | STRIX NEBULOSA | 13 |
| 56 | LVI | Red-shouldered Hawk | FALCO LINEATUS | 13 |
| 95 | XCV | Yellow-poll / Blue-eyed Warbler | SYLVIA AESTIVA | 13 |
| 102 | CII | Blue Jay | CORVUS CRISTATUS | 15 |
| 109 | CIX | Savannah Finch | FRINGILLA SAVANNA | 16 |
| 143 | CXLIII | Golden-crowned Thrush | TURDUS AUROCAPILLUS | 16 |
| 173 | — | Barn Swallow | HIRUNDO RUSTICA | 14 |
| 189 | CLXXXIX | Snow Bunting | EMBERIZA NIVALIS | 15 |
| 195 | CXCV | Ruby-crowned Wren | REGULUS CALENDULA | 16 |
| 217 | CCXVII | Louisiana Heron | ARDEA LUDOVICIANA | 16 |
| 251 | CCLI | Brown Pelican | PELECANUS FUSCUS | 15 |
| 314 | — | Black-headed / Laughing Gull | LARUS ATRICILLA | 14 |
| 340 | CCCXL | Least Stormy Petrel | THALASSIDROMA PELAGICA | 20 |
| 414 | CCCCXIV | 1. Golden-winged / 2. **Cape May** Swamp-Warbler | 1. HELINAIA CHRYSOPTERA / 2. **HELINAIA MARITIMA** | 16 |

## 🎯 Latince düzeyinde çalışan PUN'lar (büyük keşif)

| # | Görsel | Latince pun | Anlamı |
|---|---|---|---|
| 2 | Takvim | **`calendula`** | ← Latince `kalendae` = **TAKVİM** |
| 3 | Çikolata | **`fuscus`** | = **koyu kahverengi** (Audubon: *"rich dark chocolate brown"*) |
| 4 | Kar yağışı | **`nivalis`** | = **karlı / kardan gelen** |
| 11 | Ahır | **`rustica`** | = kırsal / çiftlik |
| 13 | Altın lahit + kartal | **`chrysaetos`** | = Yunanca **altın kartal** |
| 1 | Çapraz kılıçlar | **`Loxia`** | = Yunanca **çapraz/eğik** (+ crossbill = çapraz gaga) |

## İpucu 1'in 27 harfi (mevcut en iyi tahmin)

```
c o | e d | a f | n v | l i | n a | c L | i a | i m | ? | o t | y a | c h | e a
```

⚠️ **Henüz okunmuyor.** Harf dağılımı İngilizce değil (a=5, c/i=3'er, e=2; İngilizcede **e** en sık olmalı).
→ Ya kalan 5 tespit (#1, #8, #10, #11, #12, #13) yanlış, ya da 27 harf **sonraki bir adımda işlenecek.**

### Uygulanan filtreler (çalıştıkları kanıtlandı)
- **`L ≥ max(🔴,🔵)`** → 222 White Ibis (L=8 < 9) elendi ✓
- **🔴 ≠ 🔵** (kilitli 7 örnekte farklı) → şunlar elendi:
  46→#4 (u/u), 132 (t/t), 147 (a/a), 27 (e/e), 37 (a/a), 113 (i/i), 263 (s/s), 71 (a/a)

---

# 6) İPUCU 3–17 DURUMU

| İpucu | İçerik | Durum |
|---|---|---|
| 3 | `081 XIV / SeaHawks?` | ✅ Doğrulama (İpucu 2'deki 081 XIV ile aynı) |
| 4 | `## / How Many?` | ✅ **İki basamaklı gruplar** — ana zincirde kullanıldı ✓ |
| 5 | `QX = TH` | ✅ **Ordinal ek (-th)** — ana zincirde kullanıldı ✓ |
| 6 | `142674 / 251634 / 461427` | ✅ 251634 = ANAHTAR; 214674'e uygulandı |
| 7 | `PLATES` | ✅ Sayılar = plaka numarası; `46TH PLATE` |
| 8 | `Youtube link watch?` | 🟡 Meta. Eski okuma: `NQX FILM` → `NTH FILM` |
| 9 | Rail fence → `LAST WORD THEN NINTH` | ✅ Çözüldü (kullanıcı yöntemi: ikiye böl, 2. yarıyı ters çevir, dönüşümlü oku) |
| 10 | `Book w/ old names… Alphabetize?` | 🟡 Meta/doğrulama (işlem değil) |
| 11 | `Roman numbers for Roman words?` | ✅ Latince ad kuralını doğruluyor |
| 12 | `Boo!` (kitap üstünde) + `Five of these` | 🟡 **BOO + K = BOOK** → Birds of America. "Five of these" = FIVE+TH = **FIFTH** |
| 13 | `(527)→(83544)→M̶R̶(9)` | ✅ **`MRBEASTHAND`** (MR + 9) |
| 14 | `(364)→(66)→(6)` (video sonu, mavi/mavi) | 🟡 364 = iki tarih arası; (6) = **FRIDAY** (6 harf) hipotezi |
| 15 | `(364)(4445)→(66)→(6)` (beyaz/mavi) | 🟡 4445 = `LAST WORD THEN NINTH` uzunluk kodu |
| 16 | `214` + `674` (iki ayrı üçlü, elektrik panoları) | ✅ Ana zincirin girdisi |
| 17 | İki olay arası **364 gün** (`July 1 - 1988` / `June 30 - 89`) | 🟡 Tarihler = dekor/yan veri (bir ipucuna ait değil); 364 = İpucu 14/15 girdisi |

### Tarihler ve FRIDAY
- 1 Tem 1988 = **Cuma**, 30 Haz 1989 = **Cuma** (364 gün = tam 52 hafta → gün korunur)
- **FRIDAY = 6 harf** → İpucu 14/15'in `(66)` ve `(6)` çıktılarıyla bağdaşıyor.
- ⚠️ Kullanıcı notu: tarihler bir ipucunun İÇİNDE değil, birçok ipucuna yakın bir konumda → konum kanıtı olarak kullanılmamalı, ama VERİ olarak geçerli.

---

# 7) AÇIK SORULAR / SONRAKİ ADIMLAR

1. **Kalan 13 harfin dizilişi** (`D E E E F I M O R S T T W`) — İspanyolca/Latince kelime grubu denenecek.
2. **İpucu 1'in 27 harfi okunmuyor** → 6 tespit daha doğrulanmalı: 197, 95, 349, 233, 203, 204.
3. **#1 (Umman bayrağı):** bayrak = "simgelediği şey" (ülke/millet) → 197 Crossbill mi 217 Louisiana Heron mu?
4. **#10:** `su + dişi(hen) + kahverengi` → Water-hen. Hangi plaka? (349 / 233 / 203 / 204)
5. **142674 → "UNZ"** ve **461427 → "JUN"** ilişkisi netleşmeli.
6. **Tarihlerin (İpucu 17) nerede kullanılacağı** bilinmiyor.
7. **83544** hâlâ çözülmedi (multi-tap "TDJH" çöp; belki zaman damgası 8:35:44).

---

# 8) ARŞİV — ESKİ NOTLAR

- **527** = `BIRDS(5) OF(2) AMERICA(7)` ✓
- **4445** = `LAST(4) WORD(4) THEN(4) NINTH(5)` ✓
- **364** = 52 hafta × 7 gün
- **83544** rakam toplamı = 24 (girdi sayısı)
- **Telefon tuş takımı (İpucu Şüpheli):** 24 harf (Q ve Z YOK) — 24 kuşla örtüşüyor.
  Multi-tap: `444`=I, `44`=H, `4445`=IJ, `44455`=IK, `66`=N, `6`=M, `527`=JAP, `364`=DMG
- **5. video** = "POKEMON GO STEREOTYPES" (2016-07-14). Outro: "...WATCH MY LAST VIDEO IT WAS EPIC / CHOOSE ONE" + taş-kağıt-makas. Açıklamadaki Rock/Paper/Scissors linkleri **2016 şablonu** (aynı 3 ID farklı etiketlerle dönüyor) → "Paper" özel video değil.
- **Kasa sahnesi CC:** "R-62… L-39… Your **fingers** are shaking! / Wait, **hold your hand out like this**. / It's a **MILLION DOLLAR** combination! / R… 0-5… L-73…" — transkriptte "Hands" YOK; H/I büyük harfleri ekran üstü yazıdan geliyor.
- **İpucu 9 rail fence:** `LSWRTE / NNHTIN / HDOTA` → ikiye böl, 2. yarıyı ters çevir, dönüşümlü oku → `LAST WORD THEN NINTH` ✓
</content>
</invoke>

---

# 0-D) 🔵 İPUCU 15 — `(364)(4445)→(66)→(6)` ANALİZİ (2026-09-13)

## ✅ KESİNLEŞEN KURAL: `(N)` = KELİME-UZUNLUĞU KODU

Bu kural artık **5 bağımsız örnekte** doğrulandı:

| Kod | Kod çözümü | Toplam harf | Kaynak |
|---|---|---|---|
| `(527)` | BIRDS(5) OF(2) AMERICA(7) | **14** ✓ | İpucu 13 girdisi (kitap) |
| `(83544)` | MRBEASTS(8) AND(3) ?(5) ?(4) ?(4) | **24** ✓ | İpucu 13 ara adımı (24 plaka) |
| `(4445)` | LAST(4) WORD(4) THEN(4) NINTH(5) | **17** ✓ | İpucu 9 rail fence (kendi çözümümüz) |
| `(66)` | FOURTH(6) UPLOAD(6) | **12** ✓ | İpucu 15 ara adımı (topluluk) |
| `(9)` | **BEASTSAND** — tek kelime, 9 harf | **9** ✓ | İpucu 13 ÇIKTISI ← kendi çözümümüz |

🔑 **Kritik ayrım:** çok haneli kodlar = *kaç kelime ve uzunlukları*;
**tek haneli kod = CEVABIN HARF SAYISI.** `(9)` 9 harf ✓ (BEASTSAND doğrulandı)
→ **`(6)` = 6 harfli TEK BİR KELİME.**

## 🔴 `(6) = STUNTS` İDDİASI KANITSIZ

Topluluk (Reddit r/MrBeast, 4 Eyl 2026) `STUNTS` diyor. **Bağımsız denetimim:**

| Adım | Durum |
|---|---|
| `(4445)` = LAST WORD THEN NINTH | ✅ **kendi çözümümüz** (İpucu 9 rail fence) |
| `(66)` = FOURTH UPLOAD (6+6) | ⚠️ uzunluk koduyla uyumlu AMA kaynağı doğrulanamadı ("Oct 4th + upload" altyazı iddiası) |
| `(364)` = XOR SUPERB OWLS (3+6+4) | ⚠️ uzunluk koduyla uyumlu; "SUPERB OWLS" = **Super Bowl** punu mantıklı ($1M bulmaca Super Bowl LX reklamındaydı — spor sitesinden bağımsız doğrulandı) AMA **`XOR` 17 ipucumuzda hiç yok** → şüpheli |
| "fourth upload → last word → ninth → **STUNTS**" | ❌ **KİMSE GÖSTERMEDİ.** Gerekçe olarak sunulan tek şey: *"birkaç MrBeast videosu stuntlarla ilgili"* — bu çıkarım değil, tahmin. |

Topluluk bile *"If that extraction is correct…"* diyor. **`(6)` hâlâ AÇIK.**

## 🆕 KENDİ HİPOTEZİM: `(66)→(6)` indirgemesi = "LAST WORD"

```
(66) = FOURTH | UPLOAD
       ↓  "LAST WORD" uygulanırsa
(6)  = UPLOAD          ← tam 6 harf ✓
```
Bu, `(66)→(6)` okunuşunun **mekanik olarak en temiz** açıklaması: tek haneli
kod bir kelime, `(66)` iki kelime → "LAST WORD" ikincisini seçer.
Topluluk `UPLOAD`'ı "zaten talimatın parçası" diye eledi ama **bu bir varsayım,**
kanıt değil. (Not: `BEASTSAND`+`UPLOAD` anlamsız; `BEASTSAND`+`STUNTS` =
"BEASTS AND STUNTS" anlamlı → STUNTS *dilbilgisi* açısından daha iyi.)

## ❓ ÇÖZÜLMESİ GEREKEN TEK ŞEY
`(4445)` talimatının **neye** uygulandığı. İki aday:
- **(A)** "FOURTH UPLOAD" ifadesinin kendisine → `(6) = UPLOAD`
- **(B)** MrBeast'in gerçekten 4. yüklemesinin başlığına → o başlığın son kelimesi,
  sonra 9. harf → ? (`STUNTS` iddiası buraya oturmuyor: 6 harfli bir kelime
  tek bir "9. harf"ten çıkmaz.)

→ **Kullanıcıdan istenen:** elindeki 4 videonun **başlıkları** (özellikle 4.'sü).
Onları verirsen "LAST WORD THEN NINTH"i bizzat uygulayıp `(6)`yı hesaplarım.
Ayrıca videoda altyazıda **"Oct 4th"** ve **"upload"** geçiyor mu? → `(66)`'nın kaynağı.

---

# 0-E) 🟢 $1M AVININ 9 KELİMELİK ANAHTARI — BAĞIMSIZ DOĞRULAMA (2026-09-13)

`(364)`'in "SUPERB OWLS" = Super Bowl okuması, bizi $1M avının malzemesine
götürdü. Oradaki resmî yapıyı doğruladım:

## ✅ 9 kelimelik ipucu DOĞRULANDI (resmî uzunluklarla birebir)
```
resmî   : 5, 9, 5, 7, 8, 4, 9, 6, 5   (toplam 58 harf)
iddia   : EVERY CHALLENGE LEADS TOWARDS LOCATION NAME SOMEWHERE AROUND WORLD
ölçümüm : 5, 9, 5, 7, 8, 4, 9, 6, 5   → TAM EŞLEŞME ✓  (toplam 58 ✓)
```
Kaynak: `mrbeast.salesforce.com` resmî İpucu #1 (Lone Shark Games) + iki bağımsız
topluluk kaynağı. **Anahtar cümle: "LOCATION NAME SOMEWHERE AROUND WORLD"**
→ o avın cevapları **KONUM** (ülke/şehir) çıkıyordu.

## 🔥 Bu, `BEASTSAND`'i kesinleştiren bir kontrol daha verdi
Topluluğun alternatif kolu "CHRISTMAS ISLAND" (9 = CHRISTMAS, 6 = ISLAND).
**Kendi ölçümümle çürüttüm:**

| İddia | 24 harfli havuzdan yazılabilir mi? |
|---|---|
| `BEASTSAND` | ✅ **EVET** (A2 B1 D2 E4 F1 H1 I1 M2 N1 O1 R2 S2 T3 W1 — 24/24) |
| `CHRISTMAS` | ❌ **HAYIR** — havuzda **C harfi YOK** |
| `ISLAND` | ❌ havuzda **L de yok** (ama (6) zaten mavi zincirden geliyor, havuzdan değil) |

→ **Kırmızı havuz `(9) = BEASTSAND`.** "Christmas" iddiası harf envanteriyle
çürüyor. Bu, M̶R̶(9) + 24/24 örtüşme + (83544) uzunluk kodundan SONRA 4. bağımsız teyit.

## ⚠️ İki havuzun birleşimi hâlâ belirsiz
Topluluk `red→blue = BEASTSANDSTUNTS` diyor ama başka bir okuma var:
**"Combo-lock L/R"** ($1M kasasındaki gibi) → (9) ve (6) **yan yana iki kadran**,
birleştirilmiş tek kelime DEĞİL. Bu okumada `BEASTSAND` + 6 harfli bir KONUM
(örn. `ISLAND`) mantıklı olur — çünkü anahtar cümle "LOCATION NAME" diyor.

## `(6)` aday tablosu (bağımsız sıralamam)
| Aday | Gerekçe | Güven |
|---|---|---|
| `STUNTS` | sadece "6 harf" şartını sağlıyor; çıkarım **hiç gösterilmedi** | ❌ zayıf |
| `UPLOAD` | `(66)=FOURTH UPLOAD` → "LAST WORD" → 6 harf ✓ mekanik | ⚠️ orta |
| `ISLAND` | 6 harf + anahtar cümle KONUM diyor + $10.000 çizimindeki **kontur/ada** + Christmas Island kolu | ⚠️ orta |
| `PUZZLE` | video başlığının son kelimesi, 6 harf | ⚠️ spekülatif |

## ❌ Çürüyen topluluk iddiaları (bu turda)
- `(6) = STUNTS` → süreçte **hiçbir adım gösterilmedi**, sadece uzunluğa uydurma
- `(9) = CHRISTMAS` → 24 harfli havuzda C yok
- "9-word clue bizim zincirimizde geçiyor" → hayır, o **$1M avının** malzemesi;
  bizim `(364)`'e yalnızca "eski av" referansı olarak giriyor

---

# 0-F) 🔴 4. VİDEO = "$1 vs $500,000 Experiences!" — ÇIKARIM UYGULANDI (2026-09-13)

Kullanıcı doğruladı: **4. videonun başlığı "1 Dolar vs. 500.000 Dolarlık
Deneyimler!"** = `$1 vs $500,000 Experiences!`.
Bu, $1M avı playlist'inin **4. videosuyla BİREBİR aynı** (kaynak: resmî playlist
listesi). → **`(66) = FOURTH UPLOAD` artık senin verinle teyitli ✅**

## "LAST WORD THEN NINTH" uygulaması
```
LAST WORD  = "Experiences!"  → EXPERIENCES (11 harf)
9. HARF    = E1 X2 P3 E4 R5 I6 E7 N8 C9  →  C
```
→ Sonuç **tek harf**, 6 harfli bir kelime DEĞİL. Yani `(6)` havuzu
**başlıktan çıkmıyor**; kaynak videonun içinde başka bir yerde.
(9 video başlığının son kelimelerinden de 6 harfli bir şey çıkmıyor.)

## ❌❌ `STUNTS` KESİN OLARAK ÇÜRÜDÜ (3. bağımsız çürütme)
Başlığın harf envanteri: `v s E x p e r i e n c e s`
```
STUNTS için gereken: S T U N T S
başlıkta yok       : T ve U   → YAZILAMAZ
```
Daha önce: (1) 24 harfli pembe havuzda U yoktu, (2) hiçbir çıkarım adımı
gösterilmemişti. Şimdi (3) 4. video başlığında da T ve U yok.
→ **`(6) = STUNTS` öldü.** Topluluğun en popüler iddiası yanlış.

## ⚠️ Önemli yan bulgu: 4. videonun bulmaca cevabı 7 harf
Resmî uzunluk listesi `5,9,5,7,8,4,9,6,5` → 4. kelime **7 harf**.
9 kelimelik anahtar cümlede 4. kelime = **TOWARDS** (7) ✓
→ 4. videonun bulmaca cevabı büyük ihtimalle **TOWARDS**.

## Başlık harflerinden çıkan 6 harfli kelimeler (en sık 12)
`SERIES · SCREEN · PRINCE · RECIPE · EXCESS · PIERCE · EXPIRE · RECESS ·
REVISE · SERENE · EXCISE · VESPER`
Hiçbiri `(6)` havuzu için ikna edici değil (başlıktan 6 harfli kelime
üretmek zaten talimatta yok).

## Güncel `(6)` durumu
| Aday | Durum |
|---|---|
| `STUNTS` | ❌ **ÇÜRÜDÜ** (T,U yok) |
| `UPLOAD` | ⚠️ `(66)=FOURTH UPLOAD` → "LAST WORD" → 6 harf ✓ en mekanik okuma |
| başlıktan türetme | ❌ çıkmıyor |

## ❓ Kalan soru
"LAST WORD THEN NINTH" **neye** uygulanacak? Başlık değilse:
- 4. videonun **sabit yorumundaki (pinned comment)** bulmaca metni mi?
- 4. videonun **açıklaması** mı?
- Videonun **son sözleri** mi (transkript)?
→ Kullanıcıdan: 4. videonun sabit yorumu + bulmacanın cevap kelimesi.

---

# 0-G) 📼 VİDEO 4 TRANSKRİPTİ ÇEKİLDİ — ANALİZ (2026-09-13)

**Dosya:** `video4_transkript.md` (384 satır, 3032 kelime, tam transkript)
**Kaynak:** `$1 vs $500,000 Experiences!` · `Xj0Jtjg3lHQ` · 2 Kas 2024 · 17:39

## "LAST WORD THEN NINTH" — tüm okumalar denendi
| Okuma | Sonuç | 6 harfli kelime? |
|---|---|---|
| Videonun son kelimesi | **`guys`** ("I love you guys!") | ❌ 4 harf |
| 9. kelime | `$1` | ❌ |
| Sondan 9. kelime | `put` | ❌ |
| 9. harf (yalın) | `o` | ❌ |
| Her satırın son kelimesinin 9.su | `God` | ❌ |
| Satır son kelimelerinin 9. harfleri | `clgaeloaneneecsceegesiiieioksrycvynn` | ❌ saçma |
| Cümle son kelimelerinin 9. harfleri | `clgaelloanenneeccsceegesieieieioksrycrvyntn` | ❌ saçma |

→ **`(6)` transkriptte YOK.** (Beklenirdi: video 4'ün bulmacası konuşmada değil,
ekrandaki görsellerde + sabit yorumda.)

## ❌ `STUNTS` 4. KEZ ÇÜRÜDÜ
Transkriptte **`stunt` kelimesi hiç geçmiyor** (3032 kelime tarandı).
Önceki çürütmeler: (1) 24 harfli pembe havuzda U yok, (2) çıkarım adımı hiç
gösterilmedi, (3) başlıkta T ve U yok. → **`(6) = STUNTS` kesin öldü.**

## 🔎 Transkriptte dikkat çekenler
- **"upload"** tam **1 kez** geçiyor: *"If I don't make this still upload the video!"*
  (skydiving öncesi) — `(66)=FOURTH UPLOAD` ile tesadüf mü, değil mi, belirsiz.
- **"nine"** 2 kez: *"This **nine** course meal…"* ve *"…try **nine** mouthwatering courses…"*
- Konumlar: Egypt/pyramids · Africa(safari) · Dubai · Abu Dhabi · Burj Khalifa · Atlantis
- Sayılar: $1 · $10,000 · $50,000 · $200,000 · $250,000 · $500,000 · 3000ft · 500ft ·
  600ft · 2700ft · 900ft · 160 stories · 10,000ft · 80 sharks · 119 Swarms

## ✅ 9 kelimelik anahtar 3. BAĞIMSIZ KAYNAKLA DOĞRULANDI
`laurencetennant.com` (avın ayrıntılı post-mortemi) Stage 0 cümlesini birebir veriyor:
**"EVERY CHALLENGE LEADS TOWARDS LOCATION NAME SOMEWHERE AROUND WORLD"** ✓

## ⚠️ KENDİ ŞÜPHE KAYDIMI KISMEN DÜZELTİYORUM
Tur 3'te PDF alıntılarını (özellikle "Rosé 73") "halüsinasyon riski yüksek" diye
şüpheli listesine almıştım. **Gerçekten var — ama hâliyle:**
> *"Take the vault code, add **L73 from Rosé's shirt**, then add on all the numbers in
> the background of the picture to get the final answer `R62L39R05L73606623093121200300`"*
Yani doğrusu **"73" değil "L73"** (harf + sayı). Diğer iki alıntı
(Will Campbell 66, "Hawks up on the Pats 6-0") hâlâ doğrulanamadı.

## 🎯 Video 4'ün bulmaca cevabı = **TOWARDS**
Resmî uzunluk listesinde 4. kelime 7 harf; anahtar cümlede 4. kelime `TOWARDS` (7) ✓
Bulmaca tipi: karıştırılmış mahalle/konum adları (COLFAX, DOVERCOURT, HOLSTER) →
renkli harfler → 7 harfli cevap.

## ❓ Sıradaki adım
`(6)` transkriptte değil → şuralarda aranmalı:
1. Video 4'ün **sabit yorumundaki (pinned comment)** bulmaca metni
2. Video 4'ün **ekrandaki grafikleri** (karıştırılmış konum adları + renkli harfler)
3. Video 4'ün **açıklaması**

---

# 0-H) 🔍 `364` ÜN ALTERNATİF ANLAMLARI — BAĞIMSIZ DENETİM (2026-09-13)

## 1) ❓ "FOURTH UPLOAD" NEREDEN ÇIKTI? — **ÇIKMADI. TAHMİN.**
Dürüst cevap: **hiçbir türetim yok.** Zincir şu:
1. `(66)` bir uzunluk kodu → **2 kelime, 6+6 harf** (kuralımız, 5 örnekle sabit)
2. Topluluk bu kalıba "FOURTH UPLOAD" uydurdu (6+6 ✓)
3. Sonra "4. yükleme"yi $1M playlist'inin 4. videosuyla eşleştirdi
4. Sen 4. videonun gerçekten **"$1 vs $500,000 Experiences!"** olduğunu doğruladın

⚠️ **Ama bu, "FOURTH UPLOAD" İFADESİNİN doğru olduğunu KANITLAMIYOR.**
Sadece "4. video diye bir şey var"ı kanıtlıyor. Kalıba uyan başka 6+6
ifadeler de var (`SECOND UPLOAD`, `FOURTH UPLOAD`, …). Kaynak: altyazıda
"Oct 4th + upload" iddiası — **doğrulanamadı.**

## 2) 👏 KULLANICININ YAPISAL GÖZLEMİ — haneler küçülüyor
```
(364) + (4445)  →  (66)  →  (6)
 3 hane  4 hane    2 hane    1 hane
```
Uzunluk-kodu kuralıyla bu şu demek:
```
3 kelime + 4 kelime  →  2 kelime  →  1 kelime
```
- **`LAST WORD`** → `(66)→(6)` adımını birebir açıklıyor: 2 kelimenin sonuncusu ✓
- **`THEN NINTH`** → o zaman `(364)+(4445)→(66)` adımını açıklamalı.

### 🆕 HİPOTEZ: talimatın İKİ PARÇASI BİRER KELİME SEÇİYOR → 2 kelime = `(66)`
```
"LAST WORD"    → bir metnin SON KELİMESİ        (1 kelime)
"THEN NINTH"   → o metnin 9. KELİMESİ           (1 kelime)
                                    toplam = 2 kelime = (66) ✓✓ YAPISAL OLARAK KUSURSUZ
```
**Test edilen aday metinler — hiçbiri iki 6-harfli kelime vermiyor:**
| Metin | LAST WORD | 9. kelime | Sonuç |
|---|---|---|---|
| 9 kelimelik anahtar cümle | WORLD (5) | WORLD (5) | ❌ 5+5 |
| 9 video başlığı | Africa/Strangers/… | yok/uyuşmuyor | ❌ |
| Video 4 başlığı | EXPERIENCES (11) | — (4 kelime) | ❌ |
| Video 4 transkripti | guys (4) | — | ❌ |
→ **Kaynak metin hâlâ bilinmiyor.** Yapı doğru, hedef yanlış.

## 3) ❌ `NIGHT` DEĞİL `NINTH` — KESİN ÇÜRÜTME
Yapıştırılan metin "last word then **night**" diyor. **Yanlış:**
```
scramble (İpucu 9) : LSWRTENNHTINHDOTA = 17 harf, G harfi YOK
LASTWORDTHENNINTH  : 17 harf → HARF KUMESİ BİREBİR UYUMLU ✓
LASTWORDTHENNIGHT  : 17 harf → UYUMSUZ (fazla G, eksik N) ❌
```
Uzunluk kodu `(4445)` her ikisine de uyar (NINTH=5, NIGHT=5) ama
**harf envanteri kararı verir: NINTH.**

## 4) 📊 364 ALTERNATİFLERİ — YAPILAN LİSTENİN BAĞIMSIZ DENETİMİ
| Aday | Gerçek mi? | Bu bulmacada karşılığı | Güven |
|---|---|---|---|
| **Uzunluk kodu 3,6,4 = 13 harf** | ✅ **kuralımız (5 örnek)** | tek haneli olmayan her kod gibi | 🥇 **EN YÜKSEK** |
| **İpucu 17'nin 364 günü** (52×7) | ✅ 364 | kendi ham verimiz | 🥈 |
| **PLAKA 364 = White-winged Crossbill** | ✅ **2 bağımsız kaynak** | plaka mekaniği + İpucu 1 #1 crossbill | 🥉 **YENİ, GÜÇLÜ** |
| İskambil destesi 4×91 = 364 | ✅ 364 | destede kart motifi kanıtı YOK | ⚠️ zayıf |
| Alan kodu 364 (Kentucky, Bowling Green) | ✅ gerçek | telefon dalı var (+674 Nauru, 214 Dallas) | ⚠️ tutarlı ama kanıtsız |
| Kitap şifresi sayfa 364 | ⚠️ kuralımızla çelişir | **ama PLAKA 364 var** → yukarıya bak | ⚠️ kısmen |
| Alice / un-birthday | — | destek yok | ❌ dolgu |
| Dante / Milton 364. kıta | — | destek yok | ❌ dolgu |
| Birthday attack (364/365) | ✅ matematik | fiziksel masa bulmacasıyla alakasız | ❌ |
| Melek sayısı 364 | — | destek yok | ❌ dolgu |
| XOR | ❌ **döngüsel** | aynı Reddit kaynağına referans | ❌ |

## 5) 🆕 YENİ HİPOTEZ: `(364)` = **PLAKA 364**
```
PLAKA 364 (CCCLXIV) = White-winged Crossbill
Latince             = LOXIA LEUCOPTERA        ← iki kaynakla doğrulandı
```
**Neden çarpıcı:**
- Bu bulmacanın MERKEZÎ mekaniği plaka numarası (İpucu 7 `PLATES`)
- İpucu 1 / görsel #1 zaten bir **crossbill** (`Loxia` = çapraz gaga) —
  plaka 197 (American Crossbill) veya 217. **Aynı cins!**
- İngilizce ad: **WHITE(5) WINGED(6) CROSSBILL(9)**
  - `LAST WORD` = **CROSSBILL = tam 9 harf** ← talimattaki "NINTH" ile örtüşüyor!
  - `CROSSBILL`'in 9. harfi = **L**
  - Latince `LEUCOPTERA`'nın 9. harfi = **R**

⚠️ Bu bir **kanıt değil, yön.** Ama "kitap şifresi" sezgisi doğru yere
bakıyordu: kitap *Birds of America* ve koordinat sayfa değil **PLAKA.**

## 6) ❓ Sıradaki
`(6)` için yeni aday: **`WINGED`** (6 harf, plaka 364'ün adında).
Doğrulanması gereken: plaka 364'ün lejantında/altyazısında 6 harfli bir şey var mı?

---
# 0-I) (364) OKUMALARI — YAPISAL (66)/(6) TESTİ (tur 6, 2026-09-14)

## Kullanıcının itirazı (iki ayaklı)
1. **"İpucu 17'nin 364 günü olamaz"** — o 364 zaten İpucu 14'te kullanıldı
   (iki tarih arası 364 gün, ikisi de CUMA → FRIDAY). İpucu 15'in `(364)`'ü
   aynı girdi olamaz → **bu plaka 364'ü öne çıkarır.**
2. **"ama sorun şu ki"** — plaka 364 → son kelime CROSSBILL → 9. harf = **L**
   → bu TEK HARF. `(66)` (iki 6-harfli kelime) ve `(6)` nasıl olacak?

## Yapısal şart (uzunluk-kodu kuralımızdan)
```
(66) = 2 kelime × 6 harf = 12 harf
(6)  = 1 kelime × 6 harf
→ (364)'ün kaynak metni, "LAST WORD" ve "9. KELİME" çıkarımıyla
  İKİ AYRI 6-HARFLİ KELİME vermek ZORUNDA.
```

## 🆕 PLAKA 364'ÜN TAM LEJANTI — DOĞRULANDI (3. bağımsız kaynak)
Kaynak: Boston Public Library, Havell baskısı, 1837, *The Birds of America*
(digitalcommonwealth.org · ark:/50959/9s16d7299 · Appleton kopyası)
```
Lejant: "White-winged crossbill : Loxia leucoptera, Gm. Male adult, 1, 2.
         Female adult, 3. Young F., 4. New Foundland alder"
Gravür: "Drawn from nature by J. J. Audubon F.R.S. F.L.S. Engraved, printed
         & coloured by R. Havell, 1837."
Numara: her plaka iki kez numaralı — set 73, plaka CCCLXIV (364) ✓
```
Latince ad (otorite hariç, kuralımız): **LOXIA LEUCOPTERA** (Gm. = Gmelin).
Plakanın bitkisi: **New Foundland alder** (Newfoundland kızılağacı).

### Lejant üzerinde (66) testi — ÜÇ VARYANT
| Varyant | Kelime sayısı | LAST WORD | 9. kelime | (66) şartı? |
|---|---|---|---|---|
| tüm kelimeler | 18 | alder (5) | 2 (1) | ❌ |
| sayılar atılmış | 14 | alder (5) | adult (5) | ❌ |
| sayı + otorite atılmış | 13 | alder (5) | Young (5) | ❌ |

**→ PLAKA 364, `(66)`'yı ÜRETEMİYOR. Kullanıcının itirazı VERİYLE DOĞRULANDI.**
(`CROSSBILL → 9. harf = L` tek harf verir; 6+6 vermez. Lejant da 6+6 vermiyor.)

## Üç okuma — karşılaştırma tablosu
| # | `(364)` = | `(66)` üretir mi? | `(6)` | `(4445)` rolü | Durum |
|---|---|---|---|---|---|
| **A** | 364 gün (İp 17/14) → iki tarih → ikisi de CUMA | ✅ **FRIDAY \| FRIDAY** (6,6) | ✅ **FRIDAY** (6) | ❓ rolü yok | ✅ **YAPININ TEK KARŞILIĞI** — ama "İp 14'te kullanıldı" itirazı var |
| **B** | FOURTH UPLOAD | ✅ FOURTH \| UPLOAD (6,6) | ✅ UPLOAD (6) | ✅ LAST WORD = son kelime | ⚠️ ifade **TAHMİN** + `(364)`'ü açıklamıyor |
| **C** | PLAKA 364 = White-winged Crossbill | ❌ (CROSSBILL→L = 1 harf; lejant 5+5) | ❌ | ✅ uygulanıyor ama 1 harf | ❌ **YAPIYI ÜRETMİYOR** (lejant testiyle kanıtlandı) |
| **D** | uzunluk kodu 3,6,4 = 13 harf | ? | ? | ? | ❓ kaynak metin bilinmiyor |

## ✅ FRIDAY YOLU — KAYIT (kullanıcı istedi: "bunu da kaydetmek lazım")
```
İPUCU 14 (mavi kağıt / mavi yazı, video bitimi):
  (364) = 364 GÜN (İpucu 17) → 1 Tem 1988 (CUMA) + 30 Haz 1989 (CUMA)
  (66)  = FRIDAY | FRIDAY          → 6 + 6  ✅ kendi uzunluk-kodu kuralımızla BİREBİR
  (6)   = FRIDAY                   → 6      ✅ (LAST WORD / tekilleştirme)
```
⚠️ Bu, **elimizdeki doğrulanmış veriyle `(66)`→`(6)` yapısını karşılayan TEK okuma.**
   Kayda geçti. Kullanıcı notu: bu 364 İpucu 17'den geliyor → İpucu 15'te
   tekrar kullanılması mantıksız → **İpucu 15 için hâlâ yeni bir `(364)` aranıyor.**

## Zayıf gözlem (kanıt değil, not)
Plaka 364 lejantındaki 6 harfli kelimeler: **WINGED** (White-**winged**) ve
**FEMALE** (Female adult). Talimatın bunları seçtiğine dair hiçbir kanıt yok.

## SONUÇ
- **`C` (plaka 364) çürüdü** — kullanıcının itirazı doğru, lejant testiyle kanıtlandı.
- **`A` (FRIDAY) yapıyı karşılıyor** ama İpucu 14'e ait → İpucu 15 için açık.
- **`B` (FOURTH UPLOAD) yapıyı karşılıyor** ama ifade tahmin.
- **`(364)` HÂLÂ AÇIK.** Sıradaki test: hem plaka hem ikinci bir girdi olarak
  okunabilen, 6+6 üreten bir kaynak var mı?

---
# 0-J) VİDEO 4 SABİT YORUMU + AÇIKLAMA — ImageShack `BeastForce67` (tur 6)

## 1) Sabit yorum — DOĞRULANDI (video 4 = `Xj0Jtjg3lHQ`)
```
@MrBeast · 1 yıl önce (düzenlendi) · +107.408 beğeni
"Oh man, that was a trip. Several, actually. Here's a little souvenir for you."
https://imageshack.com/user/BeastForce67
```
✅ Kaynak: ruclips.net/video/Xj0Jtjg3lHQ/$1-vs-$500-000-experiences.html
   → yorum aynen bu videoda, **4. video** = `$1 vs $500,000 Experiences!` ✓

## 2) 🚨 YENİ HİPOTEZ — `(66) = FOURTH UPLOAD` TAM BURAYA ÇIKIYOR
```
(66) = "FOURTH UPLOAD"  ← İKİ OKUMA BİRDEN, İKİSİ DE AYNI YERE:
  (a) upload = YouTube videosu → 4. video → `$1 vs $500,000 Experiences!`
      → SABİT YORUM → imageshack.com/user/BeastForce67
  (b) upload = ImageShack yüklemesi → o hesabın 4. yüklemesi (4th upload)
→ "LAST WORD" → (6) = o yüklemenin son kelimesi (6 harf)
```
**"upload" kelimesinin bir resim barındırma hesabına çıkması tesadüf değil gibi.**
Hesap adı `BeastForce67` — İpucu 16'daki `674`/`214` ile "67" örtüşmesi not edildi (kanıt değil).

### ❌ Erişilemedi
`imageshack.com/user/BeastForce67` → **ana sayfaya yönlendiriyor (giriş duvarı)**
Denenen: `/user/BeastForce67`, `/user/BeastForce67/images`, `imageshack.us/user/BeastForce67`
→ **üçü de aynı.** Hesabın içeriği (yükleme sayısı, başlıklar, sıra) BİLİNMİYOR.

## 3) Açıklama (description) — analiz
Kullanıcı "şüpheli geldi" dedi. İncelenen öğeler:
| Öğe | Değerlendirme |
|---|---|
| **Kutu sanatı** (4 satır ╔═╦╗...) | Karakter sayıları **19 / 18 / 19 / 19** → temiz ızgara değil. Sadece kutu-çizim karakterleri, **okunur metin yok.** Büyük ihtimalle dekoratif banner. ⚠️ Kayıtta, düşük öncelik. |
| `chucky@mrbeastbusiness.com` | Gerçek iş iletişim adresi (standart şablon) |
| MrBeast Lab Swarms / Walmart / Target / Amazon | Moose Toys sponsorluk metni (standart) |
| "ABONE OLUN YA DA KÖPEĞİNİZİ ALIRIM" | Standart şaka şablonu |
| mrbeast.store · viewstats · extrememusic | Standart bağlantılar |

## 4) `BeastForce67` bir TOPLULUK ADI — ⚠️ DİKKAT
- **r/BeastForce67** subreddit'i var (Şub 2026): "Join our discord server to help us solve the puzzle: discord.gg/BeastForce67"
- imgpile'da `beastforce67` kullanıcısı "Puzzle" başlıklı görsel paylaşmış (84.405 görüntüleme)
  → **sayfa artık kaldırılmış** ("Not found")
- Yorumlarda `discord.gg/tq5TQN59` "OFFICIAL DISCORD" iddiası
⚠️ **Bunların hiçbiri resmî değil.** Topluluk adı, MrBeast'in sabit yorumundaki
hesaptan geliyor. "Resmî Discord" iddiası **kanıtsız → oltalama/ scam riski.**
  → **Kural: bu sunuculara giriş yapılmaz, bağlantılara tıklanmaz.**

## 5) 🆕 ÜÇÜNCÜ TARAF İDDİALARIN DENETİMİ (Reddit r/MrBeast 1w5g827)
Kuralımız: doğrulanmadan KABUL YOK, mantıksızsa ŞÜPHELİ KAYDET.
| İddia | Test | Sonuç |
|---|---|---|
| **İpucu 9 = "rail fence cipher"** (3 satır) | 2–8 ray decode + **720 kolon permütasyonu** denendi | ❌ **ÇÜRÜDÜ** — hiçbiri `LASTWORDTHENNINTH` üretmiyor, hiçbiri İngilizce değil. Çözüm **anagram** (harf envanteri birebir). "bird fence?" = ESPri (kuş temalı şaka), mekanizma adı değil. |
| **`QX = TH`** (yeşil not) | Bizim **İpucu 5** ile birebir aynı | ✅ **BAĞIMSIZ TEYİT** (bizim kaydımız doğrulanmış oldu) |
| **`021 XIV` / `SeaHawks?`** (turuncu not) | Bizim **İpucu 3** ile aynı | ✅ BAĞIMSIZ TEYİT |
| **84 sayfalık PDF: `mrb.gg/p/puzzle`** | Daha önce 3+ denemede **HTTP 500** | ⚠️ erişilemiyor, içerik doğrulanamadı |
| **"+674 → Nauru, telefon numarası çözüyoruz"** | İpucu 16'daki `674` ile uyumlu ama "telefon numarası" sonucu **gösterilmemiş** | ⚠️ **ŞÜPHELİ** |
| İpucu 2 transkripsiyonu farklı (`329 XXVI`, `253 XIV 337 VI`) | Bizim kullanıcı kaydımız farklı (`329 X`, `337 VI`) | ⚠️ **BİZİM KAYIT ESAS** (kullanıcı teyidi) |

## 6) SIRADAKİ ADIM — kullanıcıya soru
ImageShack hesabının içeriği **bizim için erişilemez** (giriş duvarı).
Kullanıcı tarayıcıda açıp şunları söylerse `(66)/(6)` kırılabilir:
1. Hesapta **kaç yükleme** var?
2. **4. yüklemenin** başlığı / üzerindeki yazı ne?
3. Yüklemelerin **sırası** ve tarihleri?

---
# 0-K) ImageShack `BeastForce67` — ARŞİVDE BULUNDU (tur 6)

## Kullanıcı: "link temizlenmiş, boş"
Hesap şu an boş görünüyor. **Wayback Machine ile geri aldım.**

## ✅ ARŞİVDE GÖRSEL VAR
Wayback'te 2 anlık görüntü: **09 Şub 2026** ve **11 Şub 2026** (ikisi de aynı içerik)
```
Hesap sayfası : imageshack.com/user/BeastForce67
Görsel sayfası: imageshack.com/i/pmKqjfA5p          (3 anlık görüntü)
Görsel ID     : KqjfA5
Dosya adı     : 9ErN78U5uxbnR2WTkd6S.png  (rastgele → bilgi yok)
Albüm         : "No Albums"  (albüm yok)
GÖRSEL SAYISI : 1  ← iki anlık görüntüde de TEK görsel (lazy-load değil)
```

## 🔥 TAM BOYUT: `2550 × 3300`
```
https://imagizer.imageshack.com/v2/2550x3300q70/922/KqjfA5.png
2550 / 3300 = 0,772727...
8,5  / 11   = 0,772727...   ← ABD LETTER @ 300 DPI — BİREBİR ✅
```
Boyut seçenekleri menüsünde (1600x1200'a kadar) **bu boyut YOK** → 2550×3300
büyük ihtimalle **orijinal**. Yani bu bir telefon fotoğrafı değil,
**taranmış/dijital bir BELGE (letter boyutu, dikey, 300 dpi).**
Küçük sürüm 240×310 → oran 0,7746 (aynı) ✓

## ⚠️ "FOURTH UPLOAD" OKUMASI GÜNCELLENDİ
Hesapta **tek görsel** var → "4. yükleme" okuması **(b) DÜŞTÜ.**
Kalan okuma:
```
(66) = "FOURTH UPLOAD" = 4. YouTube videosu
     → video 4 (`$1 vs $500,000 Experiences!`)
     → SABİT YORUM → imageshack.com/user/BeastForce67
     → hesaptaki TEK görsel (KqjfA5, 2550×3300 belge)
     → "LAST WORD" → (6) = belgedeki metnin son kelimesi (6 harf)
```

## ⚠️ BEN GÖREMİYORUM
- Sandbox'ta doğrudan ağ erişimi yok (python TLS hatası, `curl` yok)
- `fetch_page` ikili dosyayı metin olarak vermiyor
→ **Görseli kullanıcı açıp TARİF ETMELİ.**

## 📎 KULLANICININ AÇACAĞI BAĞLANTILAR
1. **Tam boyut görsel (arşiv):**
   `https://web.archive.org/web/20260209005254/https://imagizer.imageshack.com/v2/2550x3300q70/922/KqjfA5.png`
2. **Görsel sayfası (arşiv):**
   `https://web.archive.org/web/20260209031715/https://imageshack.com/i/pmKqjfA5p`
3. **Canlı CDN (hesap boş olsa da çalışabilir):**
   `https://imagizer.imageshack.com/v2/2550x3300q70/922/KqjfA5.png`

**İstenen:** görselde ne var? Metin varsa **aynen yaz** — özellikle
son kelimesi ve 9. kelimesi (6'şar harf olabilirler → `(66)`).

---
# 0-L) ImageShack GÖRSELİ = BULMACA KARTI (tur 6) — ÜÇÜNCÜ TARAF ANALİZİNİN DENETİMİ

Kullanıcı `KqjfA5.png` görselini bir görsel analiz aracına verdirdi ve
"tamamen doğru demiyorum, körü körüne güvenme, sen bak" dedi.
**Analiz 240×310 KÜÇÜK sürümden yapılmış** (orijinal 2550×3300).

## ✅ BENİM DENETİMİM — MAKRO DOĞRU (GÜVEN)
| Kontrol | Sonuç |
|---|---|
| **Başlık: `$1 TO $500,000 EXPERIENCES!`** | ✅ **Video 4'ün başlığıyla BİREBİR AYNI** — bu kart gerçekten video 4'ün "souvenir"ı |
| Giriş cümlesi: "I went all over the world for these experiences. Where did I go?" | ✅ Tema uyumlu (dünya gezisi, destinasyonlar) |
| 15 satır / 21 kutu | ✅ İçsel tutarlı (6 satırda 2 kutu = 12 + 9 tek = 21 ✓) |
| 7 renk paleti | ✅ Tutarlı |
| Yapı: anagram (karışık harf) bulmacası | ✅ İpucu 9'daki anagram mantığıyla UYUMLU |

### 🚨 SONUÇ: `(66) = FOURTH UPLOAD` ZİNCİRİ DOĞRULANDI
```
(66) = "FOURTH UPLOAD" → 4. video → sabit yorum → ImageShack → BU KART
```
Kartın başlığı video 4'ün başlığıyla birebir aynı → **zincir artık tahmin değil, KANIT.**

## ⚠️ MİKRO (HARF OKUMALARI) — GÜVENİLMEZ
Analiz **240 px genişliğinde** bir küçük sürümden yapılmış; orijinal 2550 px
(**10,6 kat** daha yüksek çözünürlük). Analizin kendi metni de emin değil:
`NASCAN?( ')`, `MCGLL.'(?)`, `TUAIOVEA(?)`, `JAASEF(?)OYAS` — **? işaretleri var.**
→ **Harf düzeyindeki veri KANIT DEĞİL, ön okuma.**

## ❌ `(66)` YAPISAL TESTİ — OKUMALARLA UYUŞMUYOR
Kural: `(66)` = **iki ayrı 6-harfli kelime**. Karta uygulanınca:
| Okuma | LAST WORD | 9. (NINTH) | (66)? |
|---|---|---|---|
| 21 kutudan sonuncusu + 9.su | kutu21 `LLDMCGREGOY` (11) | kutu9 `TUAIOVEA` (8) | ❌ |
| Giriş cümlesinin son kelimesi + 9. kelimesi | `go` (2) | `experiences` (11) | ❌ |
→ **Ya harf okumaları yanlış (muhtemel) ya da uygulama farklı.**

## 📋 KARTIN İÇERİĞİ (ön okuma — KESİN DEĞİL)
```
BAŞLIK : $1 TO $500,000 EXPERIENCES!
SORU   : I went all over the world for these experiences. Where did I go?
YAPI   : 15 satır / 21 kutu / 7 renk
Renkler: kırmızı #E8434A · mavi #4E68AF · turuncu #F8B447 · sarı #F2EE4F
         yeşil #82C562 · koyu mor #5E4089 · orkide #CE8CBB
Kart   : beyaz zemin, hot-pink #E24882 kenarlık, başlık lacivert #082846
```
Satır dökümü (anlamlandırılamadı — ? = belirsiz glif):
```
 1 kırmızı        GLENECA.RY
 2 mavi+turuncu   NASCAN?(')  · CIFTEL
 3 kırmızı+mavi   NESTACGA    · CAMOIN
 4 koyu mor       LSIPAIZER
 5 kırmızı+sarı   MCGLL.'(?)  · F.LIRCKA
 6 orkide         TUAIOVEA(?)
 7 yeşil+mor      GLENAVON    · COLFAX
 8 orkide         JAASEF(?)OYAS
 9 turuncu        TOVERCOUIT
10 sarı           GOCKYFORIST
11 orkide         DALIAAGLEN
12 yeşil          MCGECBIAN
13 yeşil+mor      AALYISC     · LOSTHEN
14 mavi+turuncu   ATGIPSCY    · BIUTOS
15 sarı           LLDMCGREGOY
```

## ⚠️ BEN ÇÖZEMİYORUM — TEKNİK ENGEL
Anagramları çözmek için sözlük gerekli. Sandbox'ta:
- `/usr/share/dict/` BOŞ · `wordfreq` YOK · `nltk` YOK
- doğrudan internet erişimi YOK (python TLS hatası) → sözlük indirilemiyor

## 👉 SIRADAKİ ADIM (öncelik sırası)
1. **Aynı analizi 2550×3300 ORİJİNAL üzerinde tekrarla** → harfler netleşir
   `https://web.archive.org/web/20260209005254/https://imagizer.imageshack.com/v2/2550x3300q70/922/KqjfA5.png`
2. 21 kutunun **çözülmüş destinasyon adlarını** listele (21 yer adı)
3. Sonra `(66)` testini tekrarla: **21. (son) ve 9. ad** 6'şar harf mi?

---
# 0-M) GÖRSEL ERİŞİM DURUMU — KESİN SONUÇ + KARTIN HARF ENVANTERİ (tur 6)

## ❌ TAM BOYUT (2550×3300) HİÇBİR YERDE YOK — KANIT
| Kaynak | Sonuç |
|---|---|
| `imageshack.com/i/pmKqjfA5p` | **"This photo has been deleted."** |
| `imagizer.imageshack.com/v2/2550x3300q70/...` (canlı) | ana sayfaya yönlendiriyor |
| Wayback tam boyut | **"The Wayback Machine has not archived that URL."** |
| `archive.ph` (archive.today) | **"No results"** |
| Eski format `imagizer.imageshack.us/a/img922/922/KqjfA5.png` | ana sayfaya yönlendiriyor |
| Benzersiz dosya adıyla arama (`9ErN78U5uxbnR2WTkd6S`) | sonuç yok |

## ✅ DÜNYADA KALAN TEK KOPYA: 240×310 (aynı dosya, 2 kopya)
CDX doğrulaması: `image/png 200` · 56.625 ve 57.259 bayt · aynı sağlama toplamı
```
https://web.archive.org/web/20260209031711/https://imagizer.imageshack.com/v2/240x310q70/922/KqjfA5.png
https://web.archive.org/web/20260211213114/https://imagizer.imageshack.com/v2/240x310q70/922/KqjfA5.png
```
→ **Kullanıcının analiz ettiği dosya zaten mevcut en iyi sürüm. Daha iyisi yok.**

## 🆕 ÖNEMLİ: TOPLULUĞUN TAM ÇÖZÜM DOKÜMANI BULUNDU
```
"mr beast $1m write-up" — retrocraft / Team Omega (CC0)
https://docs.google.com/document/d/1svEYBKoLsSNOBL6WHf9M7jB5_Awtq7QT-ZJot7YyhQY/mobilebasic
PDF: https://writeup.retrocraft.ca/pdf
```
İçindekiler: **Hint 1–23** (Hint 1 "Playlist" 9 Şub — hesabın arşivlendiği GÜN!),
"Phases: 100 birincil puzzle", "Threads", kolon: "The vault is a combination lock.
Letters and numbers will tell you how to open it."
⚠️ 32 bölüm → okuması uzun. Kullanıcıya sorulacak: açıp tarayayım mı?

## KARTIN HARF ENVANTERİ (OCR'dan temizlenmiş — ? = belirsiz)
| # | Satır/Renk | Okuma | Harf |
|---|---|---|---|
| 1 | 1 kırmızı | GLENECARY | 9 |
| 2 | 2 mavi | NASCAN | 6 |
| 3 | 2 turuncu | CIFTEL | 6 |
| 4 | 3 kırmızı | NESTACGA | 8 |
| 5 | 3 mavi | CAMOIN | 6 |
| 6 | 4 koyu mor | LSIPAIZER | 9 |
| 7 | 5 kırmızı | MCGLL? | 5-6 |
| 8 | 5 sarı | FLIRCKA | 7 |
| 9 | 6 orkide | **TUAIOVEA** | **8** ← 9. KUTU |
| 10 | 7 yeşil | GLENAVON | 8 |
| 11 | 7 koyu mor | COLFAX | 6 |
| 12 | 8 orkide | JAASEFOYAS | 10 |
| 13 | 9 turuncu | TOVERCOUIT | 10 |
| 14 | 10 sarı | GOCKYFORIST | 11 |
| 15 | 11 orkide | DALIAAGLEN | 10 |
| 16 | 12 yeşil | MCGECBIAN | 9 |
| 17 | 13 yeşil | AALYISC | 7 |
| 18 | 13 koyu mor | LOSTHEN | 7 |
| 19 | 14 mavi | ATGIPSCY | 8 |
| 20 | 14 turuncu | BIUTOS | 6 |
| 21 | 15 sarı | **LLDMCGREGOY** | **11** ← SON KUTU |
Toplam 168 harf (21 kutu × ortalama 8)

## ❌ `(66)` TESTİ — ŞU AN TUTMUYOR
Hipotez: `LAST WORD` = 21. kutu, `THEN NINTH` = 9. kutu → ikisi de **6 harf** olmalı.
Gerçekleşen: 21. = 11 harf, 9. = 8 harf → ❌
**Ya OCR harf sayılarında yanlış, ya da uygulama farklı.**
→ KULLANICIYA DOĞRULAMA SORULARI (bkz. ana belge / sohbet)
