# MrBeast Gizli $10.000 Bulmacası — Çözüm Defteri

**Video:** `82CX6WULNA0` — "How 1 Person Solved A $1,000,000 Puzzle!" (Colin)
**Son güncelleme:** 2026-09-14 · **Tur 8** (veri düzenleme + bağımsız yeniden hesaplama: bkz. §0-Q)

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
| 9 | 4 bar + ok en küçük | **Least Stormy Petrel** | **340** | **thalassidromapelagica** | **21** | **i** | **a** | 🔒 *(düzeltildi: L=21, sondan 9. = a)* |
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
c o | e d | a f | n v | l i | n a | c L | i a | i a | ? | o t | y a | c h | e a
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
| 8 | `Youtube link watch?` | ⚠️ **TAMAMEN AÇIK** (tur 9): eski `NQX FILM → NTH FILM` notu **kaynaksız** → §0-R/2'de mezarlığa gömüldü |
| 9 | Transpozisyon → `LAST WORD THEN NINTH` | ✅ **Çözüldü + mekanizma kodla doğrulandı** (ikiye böl 8+9, 2. yarıyı ters çevir, dönüşümlü oku) — klasik rail fence değil, bkz. §0-Q/1 |
| 10 | `Book w/ old names… Alphabetize?` | 🟡 Meta/doğrulama (işlem değil) |
| 11 | `Roman numbers for Roman words?` | ✅ Latince ad kuralını doğruluyor |
| 12 | `Boo!` (kitap üstünde) + `Five of these` | 🟡 **BOO + K = BOOK** · 🆕 **"Five" = 5 ciltlik *Ornithological Biography*** (Birds of America'nın metin eşlikçisi, doğrulandı) → İpucu 10'un "old names" kitabı bu olabilir. Bizim verideki **TEK sayı-kelimesi** → `(66)` buradan kurulmalı |
| 13 | `(527)→(83544)→M̶R̶(9)` | ✅ **`BEASTSAND`** (MR̶ atılınca kalan 9 harf) — bkz. §4 |
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

1. **Kalan 13 harfin dizilişi** (`D E E E F H I M O R T T W`) — 9 dil tarandı, sonuç yok (bkz. `ucuncu_taraf_degerlendirme.md` EK A); güncel aday `(364)`=bu 13 harf → bkz. §0-P ve §0-Q.
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
- **İpucu 9 rail fence:** `LSWRTE / NNHTIN / HDOTA` → ikiye böl, 2. yarıyı ters çevir, dönüşümlü oku → `LAST WORD THEN NINTH` ✓  ⚠️ mekanizma adı "rail fence" DEĞİL — bkz. §0-Q/1

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
| `(66)` = FOURTH UPLOAD (6+6) | ❌ **tur 9'da çürüdü (§0-R/1)** — uzunluk kodu uyuyordu ama "4"ün hiçbir girdide kaynağı yok |
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
| ~~`UPLOAD`~~ | dayanağı `(66)=FOURTH UPLOAD` idi | ❌ **dayanağı tur 9'da çürüdü (§0-R/1)** |
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
listesi). → ~~**`(66) = FOURTH UPLOAD` artık senin verinle teyitli ✅**~~
> ⚠️ **[TUR 9 GERİ ALMA: bu "teyit" geçersiz.** Kullanıcının doğruladığı şey *4. videonun başlığı*,
> "FOURTH UPLOAD" ifadesi değil. "4"ün hiçbir girdimizde kaynağı yok → §0-R/1, mezarlık.]

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
| ~~`UPLOAD`~~ | ❌ dayanağı `FOURTH UPLOAD` tur 9'da çürüdü (§0-R/1) |
| başlıktan türetme | ❌ çıkmıyor |

## ❓ Kalan soru
"LAST WORD THEN NINTH" **neye** uygulanacak? Başlık değilse:
- 4. videonun **sabit yorumundaki (pinned comment)** bulmaca metni mi?
- 4. videonun **açıklaması** mı?
- Videonun **son sözleri** mi (transkript)?
→ Kullanıcıdan: 4. videonun sabit yorumu + bulmacanın cevap kelimesi.

---

# 0-G) 📼 VİDEO 4 TRANSKRİPTİ ÇEKİLDİ — ANALİZ (2026-09-13)

**Dosya:** `video4_transkript.md` (419 satır, **3.106 kelime** — tur 8'de yeniden sayıldı, tam transkript)
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
Transkriptte **`stunt` kelimesi hiç geçmiyor** (3.106 kelime tarandı).
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
| **B** | ~~FOURTH UPLOAD~~ | ✅ (6,6) yapısal olarak uyuyor | — | — | ❌ **ÇÜRÜDÜ (tur 9): "4" kaynaksız + `(364)`'ü zaten açıklamıyordu → §0-R/1** |
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
- ~~**`B` (FOURTH UPLOAD) yapıyı karşılıyor** ama ifade tahmin.~~ → ❌ **tur 9'da çürüdü (§0-R/1)**
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

## 2) ~~🚨 YENİ HİPOTEZ — `(66) = FOURTH UPLOAD` TAM BURAYA ÇIKIYOR~~
> ⚠️ **[TUR 9: ÇÜRÜDÜ. "4"ün hiçbir girdide kaynağı yok; bu bölüm tarihî kayıt olarak duruyor → §0-R/1.]**
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

### ~~🚨 SONUÇ: `(66) = FOURTH UPLOAD` ZİNCİRİ DOĞRULANDI~~
> ⚠️ **[TUR 9: İKİ KEZ ÇÜRÜDÜ — önce §0-N'de (kart $1M avına ait), sonra §0-R/1'de ("4" kaynaksız).]**
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

---
# 0-N) KANIT: ImageShack `BeastForce67` = **$1M AVINA AİT**, $10K'A DEĞİL (tur 7)

## Soru (kullanıcı): "Bu 4. videodaki yorum $1M ile alakalı mı? Zamanında
## kullanılmış mı? Biz $10K'yı çözüyoruz. Orada kullanıldıysa tekrara düşmez.
## Bana tam bir kanıtla gel — yalancık değil, tahmin değil."

## ✅ KANIT 1 — MATEMATİK (kendim hesapladım, doğrulanabilir)
```
W A T E R  (A=1..Z=26)
W=23  A=1  T=20  E=5  R=18   →  23+1+20+5+18 = 67
Hesap adı: BeastForce67                       = 67   ✅ BİREBİR
```
Karşılaştırma (hiçbiri 67 değil): BEAST=47, FORCE=47, MRBEAST=78,
WATERHEN=94, BEASTSAND=85, FRIDAY=63, FOURTH=88, UPLOAD=69, CROSSBILL=109.

## ✅ KANIT 2 — $1M AV TAKİPÇİSİNDE AÇIKÇA GEÇİYOR
Kaynak: **lightspeedup.com/mrbeast/** — "$1M Puzzle Hunt" izleme sitesi
(başlık: "PUZZLE SOLVED • $1,000,000 CLAIMED • CONGRATULATIONS COLIN • MARCH 6, 2026")
> *"Remaining: Validation: **WATER checksum = 67 = BeastForce67** Hint #3 confirms.
>   Letter counts match exactly."*

## ✅ KANIT 3 — ZAMANLAMA (üç bağımsız nokta üst üste biniyor)
| Olay | Tarih |
|---|---|
| Hesabın Wayback'e alınışı | **9 Şub 2026** ve **11 Şub 2026** |
| $1M avı İpucu 1 ("Playlist") | **9 Şub 2026** |
| $1M avı İpucu 3 ("Progress") | **11 Şub 2026** ← "Hint #3 confirms" |
| r/BeastForce67 subreddit'inin açılışı | **8 Şub 2026** |
| $1M avının çözülüşü (Colin) | **6 Mart 2026** |
| Bizim $10K bulmacamızın tartışması | **~5 Eyl 2026** (6 ay SONRA) |
→ Hesap, $1M avının **tam ortasında** arşivlenmiş. $10K'dan 6 ay önce.

## ✅ KANIT 4 — VİDEO 4 ZATEN $1M AVININ PARÇASI
Kullanıcı daha önce doğrulamıştı: 4. video = `$1 vs $500,000 Experiences!`
= **$1M avı playlist'inin 4. videosu**. (Video ~Kasım 2024, yorum ~2025'te
düzenlenmiş → ikisi de $1M avından ÖNCE var, ama av TARAFINDAN KULLANILMIŞ.)

## 🚨 SONUÇ — $10K İÇİN ELENDİ
`BeastForce67` hesabı, video 4'ün sabit yorumu ve kart **`$1M avının` bir
parçasıdır.** Kullanıcının kuralı: *"orada kullanıldıysa tekrara düşmez."*
→ **$10K çözümünde KULLANILMAZ. §8 mezarlığına gömüldü.**

## ⚠️ ÖZ ELEŞTİRİ — geçen tur "ZİNCİR KANITLANDI" demiştim, YANLIŞTI
Kartın başlığının (`$1 TO $500,000 EXPERIENCES!`) video 4'ün başlığıyla aynı
olması **sadece kartın o videonun "souvenir"ı olduğunu kanıtlar.** Bizim
$10K bulmacamızın `(66)` adımının oraya işaret ettiğini **kanıtlamaz.**
Kart $1M avının malzemesi olduğuna göre, $10K'nın onu tekrar kullanması
mantıksız. **"Kanıtlandı" ifadesi geri alındı.**

## ❓ KULLANICININ 2. SORUSU: "364'ün 4. videoyla bağlantısını anlamadım"
**CEVAP: BAĞLANTI YOK — biz de kuramadık.** Dürüst durum:
```
İpucu 15: (364) + (4445)  →  (66)  →  (6)
           ↑         ↑         ↑
           ?     LAST WORD  FOURTH UPLOAD (TAHMİN)
                 THEN NINTH
```
- `(4445)` → `LAST WORD THEN NINTH` ✅ **kendi çözümümüz (kanıtlı)**
- `(66)` = `FOURTH UPLOAD` ⚠️ **üçüncü taraf iddiası — 17 ipucumuzun hiçbirinde
  bu ifade GEÇMİYOR.** Tek "gerekçe": 6+6 uzunluk kodu + 4. videonun varlığı.
- `(364)` → `(66)` adımı **HİÇBİR ZAMAN TÜRETİLEMEDİ.** 364'ten "FOURTH UPLOAD"
  çıkan bir mekanizma bulamadık. Video 4'e giden bağ yalnızca
  "FOURTH UPLOAD" tahmininden geliyor, 364'ten DEĞİL.
→ ~~Bu yüzden "FOURTH UPLOAD" şüpheli listesinde kalır~~ → **tur 9'da MEZARLIĞA taşındı (§0-R/1). `(66)` BİLİNMİYOR, `(364)` AÇIK.**

---
# 0-O) DIŞARIDAKİ $10K TOPLULUĞU — DENETİM (tur 7, 2026-09-14)

## ✅ VİDEO TARİHİ DOĞRULANDI
`82CX6WULNA0` — **yayın tarihi: 2 Eylül 2026** (YouTube metadata).
→ $10K bulmacamız **12 günlük.** $1M avı (Şub–Mar 2026) biteli 6 ay olmuş.

## 🆕 TOPLULUĞUN DURUMU (r/MrBeast `1w78rdv`, 4 Eyl 2026)
Topluluk da bizimle AYNI noktada:
```
527  → birds of america → Roman/index → alphabetize → BEASTSAND      ✅
9    → beastsand (kırmızı havuz)                                     ✅
364  → xor superb owls                                               ⚠️
4445 → last word then ninth                                          ✅
66   → fourth upload                                                 ⚠️
6    → STUNTS (iddia)                                                ❌
join → red → blue → "beastsandstunts"
```

## ✅ BAĞIMSIZ TEYİT — BİZİM KIRMIZI TARAFIMIZ DOĞRULANDI
Topluluk **kendi başına** `BEASTSAND`'a ulaşmış (527 → Birds of America →
alfabetik → ~~MR~~ → 9 harf). Bu, bizim çözümümüzün **dışarıdan bağımsız
doğrulamasıdır.** Ayrıca onlar da "MR'nin üstünün fiziksel olarak çizili
olduğunu" teyit ediyor (bizim 1 numaralı kanıtımızla aynı).

## ❌ ONLARIN `(364)` OKUMASI — TESTTEN GEÇEMİYOR
`XOR | SUPERB | OWLS` (3,6,4 ✓ uzunluk kodu).
Test: "LAST WORD" = **OWLS (4 harf)** ✗ (6 olmalı) · **9. kelime YOK** (3 kelime).
→ Yapısal şartı karşılamıyor. `XOR` hâlâ kaynaksız → **ŞÜPHELİ kalıyor.**

## ❌ ONLARIN `(6) = STUNTS` İDDİASI — BİZDE 4 KEZ ÇÜRÜDÜ
Gerekçeleri: "fourth upload → last word → ninth extraction → stunts"
→ ** ara adım gösterilmemiş.** Bizim 4 çürütmemiz (24 harfli havuzda U yok,
4. video başlığında T/U yok, transkriptte "stunt" geçmiyor, adım kanıtsız)
GEÇERLİLİĞİNİ KORUYOR.

## 🆕 BİZDE OLMAYAN İKİ YENİ BİLGİ
| Bulgu | Kaynak | Değerlendirme |
|---|---|---|
| `(66)` = "**Oct 4th** + upload" — *gateway captions* (altyazı) okuması | HoldingAdvisory | ⚠️ doğrulanamadı; bizim kayıtlarımızda da "Oct 4th + upload" şüpheli olarak geçiyordu |
| **Path B:** $10.000 çizimindeki ada konturu → **Christmas Island** → Christmas Island Hawk-Owl → *Ninox natalis* | gg4999 | 🟡 İLGİNÇ: bizim `(6)` adayımız **`ISLAND` (6 harf)** ile örtüşüyor |
| Test edilecek sayı listesi: `VII, IX, 61, 46, 97, 121, 171, 364, 66, 6, 674, 4445, 251634` | HoldingAdvisory | `97, 121, 171` bizde de şüpheli listede; `61` yeni |

## 🎯 SONUÇ
- Kırmızı taraf: **biz + topluluk aynı sonuç** → artık tartışmasız.
- Mavi taraf: topluluk da **bilmiyor.** STUNTS iddiası onlarda da kanıtsız.
- `(364)` hâlâ **AÇIK** ve her iki tarafta da çözülmemiş.

---
# 0-P) 🔥 YENİ GÜÇLÜ ADAy: `(364)` = KALAN 13 HARF (tur 7)

## Buluş
24 harfli havuzdan `MRBEASTSAND` çıkarıldığında **13 harf** kalıyor:
```
D  E  E  E  F  H  I  M  O  R  T  T  W      = 13 harf
```
`(364)` uzunluk kodu olarak okunursa: **3 + 6 + 4 = 13 harf** ← **BİREBİR UYUMLU** ✅

## Çifte tutarlılık
Aynı 13 harf, İpucu 13'ün `(83544)` = 8,3,5,4,4 kodunun **kalan grubu**
(5+4+4 = 13) ile de örtüşüyor. Yani:
```
(83544)  = MRBEASTS(8) + AND(3) + [5] + [4] + [4]
                                    └── 13 harf ──┘
(364)    = [3] + [6] + [4]  = aynı 13 harfin FARKLI gruplanışı (?)
```
→ Bu, kalan 13 harfin **amaçsız artık değil, mavi tarafın GİRDİSİ** olduğunu
  düşündürüyor. Daha önce "büyük ihtimalle gerekli değil" demiştik — **ŞİMDİ
  ŞÜPHELİ.**

## Deneme (sözlük YOK — sandbox'ta /usr/share/dict boş, internet yok)
Elle yazılmış küçük kelime listesiyle 90 gruplama çıktı. Temiz İngilizce
olanlardan örnekler (hepsi 13 harfi BİREBİR kullanıyor):
```
FEW  + MOTHER + TIDE     (3+6+4) ✅ harf envanteri tam
WIT  + MOTHER + FEED     (3+6+4) ✅
FIT  + MOTHER + WEED     (3+6+4) ✅
```
Kontrol (FEW+MOTHER+TIDE): F,E,W,M,O,T,H,E,R,T,I,D,E =
D×1 E×3 F×1 H×1 I×1 M×1 O×1 R×1 T×2 W×1 ✅ = havuzun aynısı.

## ⚠️ DURUM: doğrulanmadı
Kelime listem küçük ve gürültülü (uydurma girdiler içeriyor). Kesin sonuç için
**harici bir anagram çözücü** gerekiyor.

## 👉 KULLANICIYA / BAŞKA BİR YZ'YA VERİLECEK PROMPT
```
Harf havuzu: D E E E F H I M O R T T W  (13 harf, hepsi tam kullanılacak)
Görev: bu 13 harfi 3 + 6 + 4 harfli ÜÇ İngilizce kelimeye böl.
Her harf tam bir kez kullanılmalı. Anlamlı/bulmaca bağlamına uygun
(kuş · kitap · plaka · konum · MrBeast) sonuçları sırala.
Bulmaca bağlamı: Audubon "Birds of America" plakaları, kırmızı havuz BEASTSAND,
mavi havuz 6 harfli bir kelime olmalı.
```

## ❓ AÇIK SORU
13 harf 3+6+4'e bölünürse → **6 harfli kelime hangisi?** (66) iki 6-harfli
kelime istiyor; 13 harfte tek 6-harfli kelime var. Bu çelişki ya gruplamanın
(3,6,4) olmadığını ya da (66)'nın buradan gelmediğini gösterir.

---
# 0-Q) 🧹 TUR 8 — VERİ DÜZENLEME + BAĞIMSIZ YENİDEN HESAPLAMA (2026-09-14)

Bu turda **yeni ipucu yok**; mevcut veri baştan doğrulandı, çelişkiler temizlendi.

## 1) ✅ İPUCU 9'UN MEKANİZMASI BULUNDU — KODLA DOĞRULANDI
Şimdiye kadar "çözüm anagram, mekanizma bilinmiyor" diyorduk. **Yanlıştı — mekanizma var:**
```
şifre : LSWRTE / NNHTIN / HDOTA   →  LSWRTENNHTINHDOTA  (17 harf)
① ikiye böl        : LSWRTENN | HTINHDOTA          (8 + 9)
② 2. yarıyı tersle : LSWRTENN | ATODHNITH
③ dönüşümlü oku    : L A S T W O R D T H E N N I N T H   ✅ BİREBİR
```
9+8 bölünüşünde de aynı sonuç çıkıyor. Yani `LAST WORD THEN NINTH` **tesadüfî bir
anagram değil, gerçek bir transpozisyon.** (Kullanıcının tarif ettiği yöntem buydu;
tur 8'de kodla teyit edildi.)

**Klasik "rail fence" ÇÜRÜK kalıyor:** 2–8 ray encode/decode + 2–17 kolonlu kolonar
transpozisyon tarandı → hiçbiri bu şifre metnini üretmiyor. "bird fence?" = espri +
"çit gibi dizme" iması, standart rail fence adı değil.

→ **Sonuç: `(4445) = LAST WORD THEN NINTH` artık hem içerik hem mekanizma olarak kanıtlı.**

## 2) ✅ BELGELERDEKİ SAYISAL İDDİALAR YENİDEN HESAPLANDI — 58/58
Bağımsız bir scriptle (Python) tüm temel iddialar yeniden üretildi. **58 kontrol, 0 uyumsuz:**

| Alan | Doğrulanan |
|---|---|
| İpucu 2 | 24 plaka + Roma → `IBRTADSSOREMHTDFNATEEMEW` · İngilizce ada göre alfabetik → `MRWBEASTSATDHEREOFNIDTEM` · havuz `A2 B1 D2 E4 F1 H1 I1 M2 N1 O1 R2 S2 T3 W1` |
| Kırmızı havuz | `BEASTSAND` yazılabiliyor · `BEASTHAND` de yazılabiliyor (ayırt edici değil) · **`CHRISTMAS` yazılamıyor (C yok)** · `MRBEASTS` kelime / `MRBEASTH` değil |
| Kalan 13 harf | `DEEEFHIMORTTW` ✓ (0-P'nin girdisi doğru) |
| Ana zincir | `214674 --251634--> 172446` · `214764 --241635--> 172446` · `17\|24\|46 → Q X 46` · 360 permütasyonun **0**'ı üç geçerli A1Z26 çifti veriyor |
| İpucu 9 | anagram ✓ · `NIGHT` varyantı uyuşmuyor ✓ · klasik rail fence üretmiyor ✓ |
| İpucu 1 | 27 harf `coedafnvlinacliaiajotyachea` ✓ · kırmızılar `ceanlnciijoyce` ✓ · maviler `odfvialaataha` ✓ · çift sırası ters → `eachyaot…` (**EACH**) ✓ · `thalassidromapelagica` = 21 harf, sondan 9. = `a` ✓ |
| Notasyon | `(527)`=5,2,7 ✓ · `8+3+5+4+4`=24 ✓ · `4+4+4+5`=17 ✓ · `6+6`=12 ✓ · `BEASTSAND`=9 ✓ |
| Yan kanıtlar | `WATER`=67 + 9 karşılaştırma değeri ✓ · $1M anahtarı `5,9,5,7,8,4,9,6,5`=58 ✓ · 1 Tem 1988 & 30 Haz 1989 **ikisi de Cuma**, araları **364 gün** ✓ · plaka 364 lejantı 18/14 kelime, LAST WORD `alder`(5) ✓ |

## 3) ⚠️ DÜZELTME: "12 okumadan yalnızca 214674 geçerli" — YANLIŞTI
`[harf][harf][sayı]` **biçimini iki okuma veriyor:**
```
214674 --251634--> 172446 --> 17|24|46 --> Q  X  46     ← İpucu 5'in QX'i  ✅
214476 --251634--> 172644 --> 17|26|44 --> Q  Z  44     ← biçim geçerli, ama QX değil
```
→ Zincir yine **tek** okumaya dayanıyor; gerekçesi "biçim geçerliliği" değil,
**İpucu 5'teki `QX` çiftinin yalnızca `214674`'ten çıkması.** (§2 ve ana belge güncellendi.)

## 4) 🔓 0-P'NİN ENGELİ KALKTI — ANAGRAM TAM TARANDI
0-P "sandbox'ta sözlük yok, internet yok" diyordu. **Artık geçerli değil:**
`pip` + internet var → `wordfreq` (200.000 kelimelik frekans listesi) kuruldu.
13 harf `D E E E F H I M O R T T W`, hedef 3+6+4:
```
havuzdan yazılabilen kelime : 3 harf = 694 · 4 harf = 529 · 6 harf = 121
(3,6,4) TAM BÖLME SAYISI    : 28.621
en yüksek frekanslı gruplar : few+editor+them · fit+method+were · fed+remote+with
                              few+mother+diet · few+mother+tide (0-P'nin elle bulduğu)
anlamlı üçlü                : two + hermit + feed
```
### 🐦 Dikkat çeken aday: `TOWHEE`
121 altı harfli adayın içinde **`TOWHEE`** var — **İpucu 2'nin ilk kuşu** *Towhe Bunting*
(plaka 029, `Fringilla erythrophthalma` → I). Aynı kitaptan bir kuş adının kalan 13 harften
çıkması tesadüf olabilir ama bağlama oturuyor. `TOWHEE` **660** farklı (3,6,4) bölmede geçiyor
(diğer bağlamlı adaylar: `hermit` 164 bölme, `feeder`, `meteor`, `wither`).

### ❌ Neden yine de kanıt değil
- **28.621** geçerli bölme var → `(83544)`'te yaşadığımız 110.028 sorununun aynısı.
- **Yapısal çelişki duruyor:** 13 harfte **tek** 6 harfli kelime var; `(66)` ise **iki** tane
  istiyor. Yani `(364)→(66)` adımı bu okumayla **kapanmıyor.**
→ `(364)` = kalan 13 harf **en güçlü aday** ama **kanıtsız**. Ayırt etmek için
`(66)`'nın gerçek kaynağı gerekiyor.

## 5) 🧹 BU TURDA DÜZELTİLEN VERİ HATALARI
| # | Dosya | Hata → Düzeltme |
|---|---|---|
| 1 | `cikti.md` §8 | Dosyaya sızmış `</content>` / `</invoke>` artığı **silindi** |
| 2 | `cikti.md` §6 | İpucu 13 hâlâ `MRBEASTHAND` diyordu → **`BEASTSAND`** (HAND §4'te çürütülmüştü) |
| 3 | `cikti.md` §7 | Kalan 13 harf `D E E E F I M O R S T T W` (HAND dönemi) → **`D E E E F H I M O R T T W`** |
| 4 | `cikti.md` §5 | #9 satırı `L=20 / mavi m` → **`L=21 / mavi a`** (düzeltme yalnızca düzmetin dosyasındaydı); 27 harf satırındaki `i m` → `i a` |
| 5 | `cikti.md` §6 + §8 | "Rail fence" etiketi → **transpozisyon** (mekanizma §0-Q/1'de kanıtlandı) |
| 6 | `BULMACA_ANA_DOKUMAN.md` §2 | Silinmiş `ikinci_gorus_promptu.md` envanterden **çıkarıldı** |
| 7 | `BULMACA_ANA_DOKUMAN.md` §12 | `(66)=FOURTH UPLOAD → Video 4` "BİLİNEN" listesinden **ŞÜPHELİ'ye** taşındı; SON SÖZ Video 4'e işaret etmekten çıkarıldı (o yol §8'de gömülü) |
| 8 | `README.md` | "3032 kelime" → **3.106** (transkript bölümü sayıldı) |

## 6) 👉 SIRADAKİ ADIM
`(66)`'nın kaynağını bulmak. Üç somut hat:
1. **`(364)` = kalan 13 harf** ise `(66)` neden **iki** 6 harfli kelime istiyor?
   (Belki `(66)` = 6 harfli kelime + onun 6 harfli bir türevi/anagramı.)
2. **FRIDAY yolu** (İpucu 17): `FRIDAY | FRIDAY` = (66), `FRIDAY` = (6) — yapıyı tek
   başına karşılayan okuma, ama 364'ün İ14'te kullanıldığı itirazı duruyor.
3. **İpucu 1'in 27 harfi** (5 tespit belirsiz) — netleşirse mavi tarafı besleyebilir.

---
# 0-R) ⚰️ TUR 9 — DÜRÜST ÇÜRÜTME + İPUCU 1 TARAMASI (2026-09-14)

**Kullanıcı kararları (bu turun çerçevesi):**
1. `FOURTH UPLOAD` için **mezarlık yolu kabul edildi.**
2. İpucu 1'den **okunacak bir cümle çıkması bekleniyor** → hatırlanan cümle kaydedilecek,
   veriye göre denenecek, ama **çalışma ona göre şekillenmeyecek**; mantıksızsa dürüstçe söylenecek.
3. Telefon ipucu **elenmedi, PARK edildi** — yalnızca tıkanınca denenecek.
4. `FOURTH UPLOAD` ve benzeri tüm kaynaksız iddialar dosyalarda **dürüstçe çürütülecek.**

## 1) ❌ `(66) = "FOURTH UPLOAD"` → MEZARLIĞA GÖMÜLDÜ
**"4"ün bu bulmacada hiçbir kaynağı yok.** Kanıt zinciri:
```
18 girdimizin tamamı tarandı → 4 / dört / fourth / IV / quadri- GEÇMİYOR
Bizim verideki TEK sayı-kelimesi: İpucu 12 "Five of these" → FIVE (dört değil, BEŞ)
Tek dayanak: altyazıda "Oct 4th + upload" geçtiği iddiası → HİÇ DOĞRULANAMADI
Kendi kaydımız zaten itiraf ediyordu (0-H/1): "NEREDEN ÇIKTI? ÇIKMADI. TAHMİN."
```
4. videonun gerçekten var olması yalnızca **"4. video var"**ı kanıtlar, **"FOURTH"**
kelimesini kanıtlamaz. Ayrıca o video $1M avının parçası (§0-N) → $10K'da kullanılmaz.
→ **`(66)` şu an BİLİNMİYOR.** Elde kalan tek yapısal bilgi: **6+6 harfli İKİ kelime.**

## 2) ❌ `NQX FILM → NTH FILM` → MEZARLIĞA GÖMÜLDÜ
Repoda `NQX` **tek bir satırda** geçiyor: `cikti.md:455` (İpucu 8 satırı, "Eski okuma"
etiketiyle). **Hiçbir ipucundan türetilmemiş.** `QX = TH` kuralı sağlam, ama üzerine
uygulandığı "NQX" diye bir veri yok → **kaynaksız not, ipucu değil.**
→ İpucu 8 (`Youtube link watch?`) yeniden **tamamen açık** durumda.

## 3) 🆕 ALPHABETIZE İLK KEZ İPUCU 1'E UYGULANDI — 192 DENEME
Kullanıcı tespiti doğruydu: "Alphabetize?"ı İpucu 2'de kullanmıştık ama İpucu 1'e
**hiç** uygulamamıştık. Tam tarama:
```
6 tespit kombinasyonu (#1: 197/217 × #10: 349/203/204)
× 8 sıralama (görsel 1→14, 14→1, plaka artan/azalan,
              İngilizce alfabetik + tersi, Latince alfabetik + tersi)
× 4 okuma (kırmızı+mavi, mavi+kırmızı, yalnız kırmızı, yalnız mavi)
= 192 deneme
```
| En iyi sonuçlar | Dizi | 4 harfli İngilizce kelime |
|---|---|---|
| İng. alfabetik, k+m | `cooteaiaafyachcliajliednanv` | 4 (`coot, edna, iaaf, lied`) |
| görsel 1→14, k+m | `coedafnvlinacliaiajotyachea` | 4 (`ache, coed, lina, nacl`) |
| Latince alfabetik ters | `iayaiaeaedeafcoclotnalinvch` | 3 |
**Hiçbiri okunmuyor → sorun SIRALAMA değil.**

## 4) 🔬 27 HARFİN TEŞHİSİ — neden hiçbir dilde cümle çıkmıyor
```
envanter: a×6 c×3 i×3 e×2 l×2 n×2 o×2 · d f h j t v y ×1   (27)
İngilizcede en sık harf 'e' olmalı → bizde a=%22, e=%7
EKSİK HARFLER: b, g, m, p, r, s, u, w   ← 8 yaygın harf hiç yok
```
**12 dilde tam bölme taraması** (en, es, pt, it, fr, de, tr, ca, ro, nl, id, sv —
wordfreq, 27 harfin TAMAMINI tüketen çözümler arandı):
```
EN: "the and all one via joy cia cia afc"     ES: "del con con hay tal viaje fia caia"
IT: "che non del vita fai ciao jay cala"      PT: "foi ele vai dia ano tal jay han ccc"
DE: "die ich von ein oft all jay acc aaa"     TR: "ile ile daha yani can joo cctv faa"
→ hepsi ÇÖP parçalarla bitiyor (cia / jay / ccc / viii / cctv). TEMİZ CÜMLE YOK.
```
**Kritik nokta:** 6 adet `a`'nın **4'ü KİLİTLİ tespitlerden** geliyor
(#3 `fuscus`, #6 `savanna`, #9 `pelagica`, #14 `nebulosa` — hepsi bağımsız kanıtlı).
Yani 5 belirsiz tespiti düzeltmek dağılımı tek başına İngilizce'ye çevirmeye yetmez.
**İki ihtimal kalıyor:** (a) kilitli sandığımız bazı tespitler de yanlış, ya da
(b) 27 harf okunacak bir cümle değil, başka bir adımın **girdisi/havuzu.**

## 5) 📝 KULLANICININ HATIRLADIĞI CÜMLE — KAYIT + DÜRÜST TEST
> **Kullanıcı (9. tur):** *"Bence okunacak bir cümle çıkacak. Eskiden denediğimde
> 'sentence is bali vacay a la' diye bir cümle çıkıyordu, tam hatırlamıyorum,
> İspanyolca sokak ağzı — 'Bali tarzı tatil tercih ederim' gibi bir şey.
> Ama kesinlikle buna göre şekillenmemeliyiz."*

**Bu ifade hiçbir dosyada yazılı değildi — ilk kez burada kaydediliyor.**
Harf envanterine göre test (dürüst sonuç):
| İfade | 27 harften yazılabiliyor mu? |
|---|---|
| `SENTENCE IS BALI VACAY A LA` | ❌ **HAYIR** — eksik: `s`×2, `e`×1, **`b`×1** |
| `BALI VACAY A LA` | ❌ **HAYIR** — `b` yok (envanterde hiç B harfi yok) |
| `SENTENCE` | ❌ HAYIR — `s` yok, `e` yalnızca 2 tane |
| `VACAY A LA` | ✅ **EVET** (v,a,c,a,y + a,l,a hepsi var) |
| `VACAY` | ✅ EVET |

**Dürüst değerlendirme:** hatırlanan cümlenin **büyük kısmı bu harf kümesinden
çıkamaz** (`BALI` için B harfi hiç yok). Yani ya o deneme **farklı bir harf
kümesiyle** yapılmıştı (eski/yanlış bir İpucu 1 okuması), ya da farklı bir ipucuna aitti.
**Çalışma bu cümleye göre şekillendirilmiyor.** Ama işe yarayan bir yan ürün var:
eğer hedef İspanyolca/sokak ağzı bir cümleyse, envanterde **`s`, `r`, `u`, `b`**
bulunmak zorunda — şu an **hiçbiri yok.** Bu, hangi tespitlerin yanlış olduğunu
elemek için kullanılabilir bir **teşhis kriteri.**

## 6) ✅ DÜZELTME: `(66)` çelişkisi sanıldığı kadar güçlü değil
Kayıtta "13 harfte tek 6 harfli kelime var, `(66)` iki tane istiyor → çelişki" yazıyordu.
Bu yalnızca (3,6,4) **gruplaması** için doğru. Serbest seçimle ölçtüm:
```
13 harf DEEEFHIMORTTW → İKİ 6 harfli kelime + 1 ARTAN harf: 20 ÇİFT VAR
formed+hewitt (artan e) · fitted+rehome (artan w) · demote+wither (artan f)
demote+whiter (artan f) · feeder+howitt (artan m) · hereof+witted (artan m) …
```
→ `(364)` = kalan 13 harf → `(66)` = 6+6 (**1 harf artarak**) yapısal olarak **mümkün.**
Çelişki kaydı yumuşatıldı. (Ama liste özel ad ağırlıklı; ikna edici çift yok.)

Ek: İpucu 1'in 27 harfinden yazılabilen **823** altı harfli kelime var;
bağlama oturanlar **`FALCON`** (`Falco` = 056 ve 081'in cinsi), `CANINE`, `FELINE`.

## 7) 🅿️ TELEFON İPUÇU — PARK EDİLDİ (elenmedi)
**Kullanıcı kuralı:** *"Kalsın ama sürekli denenmesin; tıkanınca, aklımıza gelirse denenir."*
Mekanizma doğrulandı (klasik multi-tap: `333→F`, `444→I`, `222→C`, `66→N` ✓) ama
bulmacadaki hiçbir sayı anlamlı kelime vermiyor:
```
527→JAP · 83544→TDJH · 364→DMG · 4445→IJ · 66→N · 6→M · 424→GAG · 46→GM · 674→MPG
214674→A·GMPG · 172446→·PAHM · 251634→AJ·MDG · 461427→GM·GAP   (1=ayraç, 0=operatör)
T9 ters arama (60k kelime): 83544, 4445, 214674, 172446, 461427, 251634 → EŞLEŞEN KELİME YOK
```
Tek yapısal örtüşme: **tuş takımında tam 24 harf var (Q/Z yok) = 24 plaka = `(83544)`=24.**
→ **DURUM: PARK.** Bir daha ancak tıkanırsak denenecek.

## 8) 👉 SIRADAKİ ADIM
1. **`(66)`'yı kendi verimizden kur** — tek sayı-kelimesi İpucu 12'nin **"Five"**'ı.
   `Boo!`+`Five of these` = BOOK + 5 ciltlik *Ornithological Biography* (İpucu 10'un
   "old names" kitabı) → 6+6 harfli iki kelime buradan çıkabilir mi?
2. **İpucu 1'in 5 belirsiz tespiti** — her biri için tek bir görsel detayı yeterli
   (#1 çapraz kılıç, #8 mavi/göz, #10 arka planın rengi, #12 çocuk/elf, #13 altın).
   Teşhis kriteri: doğru tespitler envantere **s / r / u / e** kazandırmalı.
3. İpucu 8 (`Youtube link watch?`) yeniden tamamen açık — "NTH FILM" notu silindi.

---
# 0-S) 🔬 TUR 10 — "`(66)`'NIN KAYNAĞI" ADIM ADIM ÇALIŞMA (2026-09-14)

Mavi zincirin tek eksik halkası `(66)`. Dört adımda, her adımı hesaplayarak gidildi.

## ADIM 1 — Zincirin aritmetiği: ne doğru olmak ZORUNDA?
```
(364)   GİRDİ      3 kelime · 3+6+4  = 13 harf
(4445)  TALİMAT    4 kelime · 4+4+4+5 = 17 harf   ✅ LAST WORD THEN NINTH
(66)    ARA ÇIKTI  2 kelime · 6+6    = 12 harf   ❓
(6)     CEVAP      1 kelime · 6      =  6 harf   ❓
```
TALİMAT iki seçim emri veriyor: **"LAST WORD"** (son kelime) + **"THEN NINTH"** (9. kelime).
→ Zorunlu koşullar: kaynak metin **en az 9 birim** içermeli; **son birim 6 harfli**;
**9. birim 6 harfli**; `(66)→(6)` = "LAST WORD" = ikinci kelime ✓ (kendi içinde tutarlı).

## ADIM 2 — Elimizdeki TÜM metinler testten geçirildi
| Metin | Kelime | Son | 9. kelime | `(66)`? |
|---|---|---|---|---|
| $1M 9 kelimelik anahtar | 9 | `WORLD`(5) | `WORLD`(5) | ❌ |
| `82CX6WULNA0` gerçek başlığı | 5 | `Puzzle`(6) | — | ❌ |
| `Xj0Jtjg3lHQ` gerçek başlığı | 2 | `Experiences`(11) | — | ❌ |
| İpucu 9 notu ("Should I call it bird fence") | 6 | `fence`(5) | — | ❌ |
| İpucu 10 ("Book with old names Alphabetize") | 5 | `Alphabetize`(11) | — | ❌ |
| İpucu 12 ("Boo Five of these") | 4 | `these`(5) | — | ❌ |
| *Ornithological Biography* tam başlığı | 17 | `America`(7) | `of`(2) | ❌ |
| 24 kuşun alfabetik adı (kelime dizisi) | 48 | `Dove`(4) | `Downy`(5) | ❌ |
| Video 4 transkripti (3.234 kelime) | 3234 | `guys`(4) | `half`(4) | ❌ |

⚠️ **Kendi hatam ve düzeltmesi:** ilk çalıştırmada "Bulmaca videosu başlığı ✅" çıktı.
Yanlıştı — başlığı kendim kelimelere çevirmiştim ("1"→"One", "$1,000,000"→"One Million
Dollar"). **Gerçek başlıkta 5 harf-kelime var**, şart sağlanmıyor. Düzeltildi.

### 🔑 ADIM 2'NİN ASIL BULGUSU — `66` neden İKİ AYNI RAKAM?
```
9 kelimelik bir metinde  9. KELİME = SON KELİME  (aynı şey!)
→ "LAST WORD THEN NINTH" 9 kelimelik metne uygulanırsa
  İKİ SEÇİM DE AYNI KELİMEYİ döndürür  →  (66) = X | X
```
**Bu, üç şeyi birden açıklıyor:**
1. `(66)`'nın neden `67` / `57` değil de **iki aynı rakam** olduğunu
2. `(66) → (6)` adımının neden "LAST WORD" olduğunu (iki kelime aynı olunca sonuncusu = kendisi)
3. Neden `(364)+(4445)` = 7 kelime → 2 kelime → 1 kelime diye küçüldüğünü

→ **TAHMİN: kaynak metin TAM 9 KELİME ve son kelimesi 6 HARF.**
Not: bu yapı `(66) = FRIDAY | FRIDAY` okumasıyla birebir aynı şey.

## ADIM 3 — Serbest anagram taraması: temiz bir cümle var mı?
Kelime-uzunluğu kısıtı OLMADAN, 80.000 kelimelik listeyle tam bölme arandı
(≥3 harf, zipf ≥ 2.5, en çok 7 kelime, ortalama frekansa göre sıralı):
```
24 HARF: 6.079 aday kelime → 189.191 tam bölme
  en iyiler: "aadmi bdo eft mrs new rest the" · "aadmi bdo eft new rss term the"  → ÇÖP
13 HARF:   560 aday kelime → 117.182 tam bölme
  en iyiler: "for met the wide" · "for the time wed" · "die from the wet"        → ÇÖP
```
**Sonuç: ne 24 harften ne 13 harften anlamlı bir cümle çıkıyor.**
→ `(364)` = kalan 13 harf hipotezinin **anlamsal desteği YOK**; 117.182 bölme
arasından seçim keyfî olur. (Tur 8'deki 28.621'in serbest hâli.)
→ 24 harf için elde kalan tek anlamlı okuma hâlâ `(83544)` kodunun verdiği
**`MRBEASTS AND …`** — o da 5 kelimelik devamı bulunamadığı için yarım.

## ADIM 4 — İki kritik yeniden değerlendirme

### 4a) ❌ $1M anahtar cümlesi `(66)`'nın kaynağı DEĞİL — kanıtlı
```
9 kelime, son kelime = 9. kelime = "WORLD" (5 harf)
"LAST WORD THEN NINTH" → WORLD | WORLD = (5,5) = (55)
Ama notta (66) yazıyor → ❌ KAYNAK DEĞİL
```
Bu, $10K ile $1M'i ayıran **bağımsız bir kanıt daha** (WATER=67 ve Şubat zamanlamasına ek).

### 4b) 🔄 FRIDAY okumasına gelen itiraz GEÇERSİZ — yeniden değerlendirildi
İtiraz şuydu: *"bu 364 İpucu 14'te kullanıldı → İpucu 15'te tekrar kullanılmaz."*
```
İpucu 14:  (364) → (66) → (6)             [mavi ped, video sonu]
İpucu 15:  (364) (4445) → (66) → (6)       [beyaz ped]
```
**İ15 = İ14 + TALİMAT.** Bunlar iki ayrı zincir değil, **aynı zincirin iki yazımı.**
`(364)`'ün ikisinde de geçmesi "tekrar" değil **zorunluluk.** Kullanıcının
*"orada kullanıldıysa tekrara düşmez"* kuralı farklı bir durum içindi: **$1M avının
malzemesi** olan kart (başka bulmacaya aitti). Burada aynı bulmacanın iki notu var.
→ **İtiraz bu biçimiyle geçersiz; FRIDAY yeniden en güçlü aday.**

## 🎯 TUR 10 SONUCU — `(6)` için güncel sıralama
| Sıra | Aday | Gerekçe | Durum |
|---|---|---|---|
| 🥇 | **`FRIDAY`** | İpucu 17 **doğrulanmış veri** (1 Tem 1988 = Cuma, 30 Haz 1989 = Cuma, 364 gün = 52 hafta) · `(66)=FRIDAY\|FRIDAY` **"iki aynı rakam"ı açıklayan tek okuma** · `(6)=FRIDAY` 6 harf ✓ | 🟡 **EN GÜÇLÜ** — ama talimatın bunu nasıl ürettiği gösterilemedi |
| 🥈 | `TOWHEE` | `(364)`=kalan 13 harf ise; İpucu 2'nin ilk kuşu (plaka 029) | ⚠️ 28.621/117.182 bölme → ayırt edici değil |
| 🥉 | `ISLAND` | $10.000 çizimindeki kontur + "LOCATION NAME" anahtarı | ⚠️ spekülatif |
| 4 | `PUZZLE` | video başlığının son kelimesi (6 harf) | ⚠️ spekülatif |
| ❌ | ~~`UPLOAD`~~ | dayanağı `FOURTH UPLOAD` çürüdü | **ÖLDÜ** |
| ❌ | ~~`STUNTS`~~ | 4 bağımsız çürütme + 27 harfte U yok | **ÖLDÜ** |

### `(66)` için elde kalan tek yapısal bilgi
**Aynı 6 harfli kelimenin iki kez yazılması.** Kaynak metin **tam 9 kelime** olmalı
(9. kelime = son kelime). Elimizdeki 9 kelimelik tek metin ($1M anahtarı) `WORLD`(5)
ile bitiyor → o değil. **6 harfli kelimeyle biten 9 kelimelik metin hâlâ bulunamadı.**

## 👉 SIRADAKİ ADIM
1. **9 kelimelik, 6 harfli kelimeyle biten metin ara.** Aday yerler: videodaki
   görünür yazılar, $10.000 çiziminin etrafındaki notlar, Colin'in sözleri.
2. FRIDAY'i doğrulayacak/çürütecek test: `(364)` → iki tarih → CUMA zincirini
   videodaki tarih notlarıyla birebir eşleştir (İpucu 17'nin kaynağı görsel mi?).
3. İpucu 1'in 5 tespiti (envantere `s/r/u/e` kazandıracak adaylar öncelikli).

---

## §0-T — TUR 11 · BİRİNCİL KAYNAKLARA ERİŞİM: KIRILMA

> **Tur 0-L/0-P'de "internet yok" diye bir engel kaydedilmişti. Bu engel YANLIŞTI.**
> PyPI'den sonra YouTube'a, resmî yarışma sayfasına ve resmî kurallara da erişildi.
> Bu turda proje tarihinde ilk kez **$10.000'in resmî tanımı** ele geçti.

### 1 · 🔴 $10.000 NEDİR? — RESMÎ KURALLARDAN BİREBİR

Kaynak: `https://puzzle-video-sweepstakes.mrbeast.app/official-rules` (Tur 11'de çekildi)

| Alan | Resmî metin |
|---|---|
| Ödül | *"One (1) Grand Prize is available consisting of **$10,000** awarded to the confirmed winner"* |
| Yarışma | *"the first person to solve a puzzle at the Contest Website (the "Puzzle")"* |
| Süre | *"begins at 12:00 p.m. ET on **September 2, 2026** and ends at 11:59 a.m. ET on **September 2, 2027** or when the winning answer has been successfully received"* |
| Video | *"watch the Contest video published on **@MrBeast2** on YouTube.com on September 2, 2026"* → **`82CX6WULNA0`** |
| İpuçları | *"**Clues to solving the Puzzle will be available in the Video.**"* |
| Cevap | *"go to https://puzzle-video-sweepstakes.mrbeast.app and follow the on-screen instructions to provide your answer **along with your email address**"* |
| Format | Site formunda tek serbest metin alanı: **"Guess the answer\*"** + e-posta. *"You can guess multiple times, but there is only 1 correct answer."* |

**Sonuç:** `$10.000` = **Colin'in video içine gizlediği bulmaca.** Cevap **tek bir metin**.
Yarışma **hâlâ açık** (bitiş 2 Eyl 2027). Türkiye ambargo listesinde **değil** → uygun.

### 2 · Videonun kendi ağzından (yeni birincil dosya: `PUZZLE_VIDEOSU_82CX6WULNA0.md`)

> *"at the end of this video, I'll tell you how you can solve the puzzle in this video and win $10,000."*
> *"there is a puzzle hidden within this video **created by Colin himself**, and the first person
> to answer correctly wins $10,000. So if you think you've solved it, **scan this QR code**
> and enter your final answer."*

Videonun tamamı (3.226 kelime, 268 cümle) repoya eklendi — repo'da hiç yoktu.
**İpucu 8'in "Youtube link watch?" sorusunun hedefi bu video.**

### 3 · 👤 Colin kim?

Video açıklaması: *"Check out Colin: `https://www.youtube.com/@doctorxor` — `https://youtu.be/XCOkRKUe3Nc`"*
→ **Colin = `@doctorxor`.** Videoda kasa başında: *"Is this Colin? / Hundreds and hundreds [hours]."*
Reddit'te `DoctorXOR` hesabıyla yorum bırakmış: *"was used last puzzle"*.

### 4 · 📕 84 SAYFALIK RESMÎ ÇÖZÜM PDF'İ — ALINAMADI

`https://mrb.gg/p/puzzle` → *"Million Dollar Puzzle Answers"*, 1 Eyl 2026, **84 sayfa**.
`https://mrb.gg/p/puzzle/file.pdf`
- `curl`/`requests` → **TLS EOF** (SSLZeroReturnError)
- `fetch_page` → **HTTP 500**
→ **Sandbox'tan indirilemiyor. Kullanıcının kendi tarayıcısından açması gerekiyor.**
⚠️ Bu PDF **$1M** bulmacasının dökümü; $10K bulmacası ayrı ve Colin'e ait. Yine de
aynı ekibin (Lone Shark Games) mekaniklerini gösterdiği için zincire ışık tutabilir.

### 5 · $1M kasa kodu — ve içindeki `66`

Transkriptten birebir: `R-62 · L-39 · R-05 · L-73` + *"The score was 6 to 0"* +
*"Foul on the play, **number 66**"* + *"Quarter two"* + *"3:09 on the clock"* + *"Ball on the 12"* + *"0-0-3, 0-0"* → 30 haneli kod.

> ⚠️ **Karıştırmayalım:** bu `66` $1M kodunun parçası. Bizim `(66)`'mız **kelime-uzunluğu
> notasyonu** (kanıt aşağıda, madde 6). İkisi ayrı şey.

### 6 · 🔑 NOTASYONUN KESİN KANITI (yeni)

İpucu 15: `(364) (4445) → (66) → (6)`

```
(4445) = LAST(4)  WORD(4)  THEN(4)  NINTH(5)     ← BİREBİR, harf harf tutuyor
```

Bu, parantezli sayıların **kelime uzunlukları** olduğunu **kesinleştirir**:

| Notasyon | Kelime sayısı | Toplam harf |
|---|---|---|
| `(364)` | 3 | 13 |
| `(4445)` | 4 | 17 = *LAST WORD THEN NINTH* ✅ |
| `(66)` | 2 | 12 |
| `(6)` | 1 | 6 |

İpucu 13'teki `MR(9)` = **"MR" + 9 harf** = `MRBEASTSAND` aynı notasyonu doğrular.
(İpucu 13'ün zinciri: `(527)` 3 kelime/14 harf → `(83544)` 5 kelime/24 harf → `MR(9)`.)

### 7 · ADIM 1 SONUCU — 9 KELİME AVI  ❌ (ve bir öz-düzeltme)

**Önceki turda yaptığım hata:** "kaynak metin **tam 9 kelime** olmalı" dedim.
Bu bir **AŞIRI GENELLEME.** Doğru şart daha zayıf:

```
(66)  ⇔  9. kelime 6 HARF   ve   SON kelime 6 HARF
        (aynı kelime olmaları ŞART DEĞİL — iki ayrı 6 harfli kelime de (66) verir)
        (metin tam 9 kelime ise son = 9. olur, yani X|X — özel hal)
```

**Test edilen 10 metin — hiçbirisi geçmiyor:**

| Metin | Kelime | 9. | Son | Sonuç |
|---|---|---|---|---|
| **`82CX6WULNA0` tam transkripti** | 3.226 | `this` (4) | `video` (5) | ❌ |
| $1M 9 kelimelik anahtar | 9 | `world` (5) | `world` (5) | ❌ → `(55)` |
| *Ornithological Biography* tam adı | 45 | `States` (6) | `localities` (10) | ❌ |
| Video-4 transkripti | 3.060 | `million` (7) | `guys` (4) | ❌ |
| İ9 / İ10 / İ12 / İ17 notları, 2 gerçek başlık, GENEL not | <9 | — | — | ❌ 9. kelime yok |

**Transkriptin cümle düzeyinde taranması:** 268 cümle → tam 9 kelimelik **8** cümle →
son kelimesi 6 harf olan **0** tane. (8'i: `vault`(5), `X's`(3), `commercial`(10), `Bolivia`(7),
`arrived`(7), `Roamy`(5), `Iceland`(7), `Territories`(11).)

⚠️ Video-4 transkriptinde şartı sağlayan 2 cümle çıktı (*"What we have coming up next is
even better."* ve *"Chandler either didn't jump or splatted on the ground."*) ama
**video 4 $1M avının parçası** → kullanıcı kuralı gereği kullanılamaz.

→ **`(66)`'nin kaynağı elimizdeki hiçbir metin değil.**

### 8 · 🌐 TOPLULUK ENVANTERİ — İpucu 1-17 ile birebir eşleşme (Reddit r/MrBeast)

| Topluluk adı | Bizim kayıttaki karşılığı | Durum |
|---|---|---|
| Blue Sticky Note `LSWRTE/NNHTIN/HDOTA` + *"Should I call it bird fence?"* | **İ9** | ✅ aynı, çözüm `LAST WORD THEN NINTH` |
| Green Sticky Note `QX = TH` | **İ5** | ✅ aynı |
| Orange Sticky Note `081 XIV / Seahawks?` (ve `021 XIV`) | **İ2/İ3** | ✅ aynı |
| Pink list → **Book Cipher** | **İ10** *"Book w/ old names… Alphabetize?"* | 🔥 **işlevi ilk kez duyuldu** |
| White paper → **T9 telephone system** | **park edilen telefon ipucu** | 🔥 **işlevi ilk kez duyuldu** |
| `PLATES` + `251634` → *"same number of characters, a transformation to apply"* | **İ6/İ7** | 🔥 yeni yorum: 251634 bir **dönüşüm** |
| Puzzle pieces → category-index with red/blue Roman numerals | **İ1** | ✅ aynı |
| White pad below TV: `(364) → (6…` | **İ14** | ✅ aynı |
| `$10,000` sketch with wavy contour lines | **İ6 konturları** | ✅ aynı |

**Yeni, henüz bizde olmayan gözlemler:** bilgisayar **5:34–5:35'te çöküyor**;
televizyonun sağındaki çıkartmada bir **YouTube linki** var; **jigsaw parçaları birleşiyor**;
0:30'daki abone ol mesajı döndürülebiliyor; 17:00 civarı altta **sarı yapışkan notta sayılar**.

### 9 · Doğrulanmamış topluluk iddiası

*"from LAST WORD THEN NINTH, i finally got **money video** … Airrack's video → Beast Games
Episode 3 → area code **+674** → **Nauru** island … i really think its a phone number that we are cracking"*

- `MONEY`(5) `VIDEO`(5) → `(55)`, **bizim `(66)` ile uyuşmuyor** → ya farklı bir metin, ya hatalı.
- Ama `+674` ilginç: İ6'nın `142674`'ünde `674` var.
- **Doğrulanmadı. Kullanılmıyor.** Kayıt amaçlı buraya yazıldı.

### 10 · Tur 11 bilançosu

| Konu | Durum |
|---|---|
| $10.000'in ne olduğu | ✅ **KAPANDI** — resmî kurallardan doğrulandı |
| Colin'in kimliği | ✅ **KAPANDI** — `@doctorxor` |
| Notasyonun anlamı | ✅ **KESİNLEŞTİ** — kelime uzunlukları |
| Bulmaca videosunun transkripti | ✅ **repoya eklendi** |
| `(66)`'nin kaynağı | ❌ hâlâ açık — 10 metin elendi |
| `(6)` = ? | ❌ hâlâ açık |
| 84 sayfalık resmî PDF | ⛔ sandbox engelli → **kullanıcı indirecek** |

**Sıradaki en verimli adım:** kullanıcının `https://mrb.gg/p/puzzle` PDF'ini indirip
repoya koyması. İkinci sırada: Colin'in `XCOkRKUe3Nc` videosu.

### 11 · 🧹 Doğrulama altyapısı repoya alındı + 1 veri hatası düzeltildi

**Sorun:** projenin tek otomatik kontrolü `/tmp/verify.py` idi (58 kontrol). `/tmp` geçici —
bu turda sandbox sıfırlanınca **kayboldu** ve aynı turda yerel git deposu da `b4ce99c`'ye
geri klonlanmıştı. Uzak `ea88e4d` sağlamdı; `git fetch` + `git reset --mixed` ile hizalandı.
**İş kaybı yok**, ama ders alındı: kontrol aracı artık repoda → **`dogrulama.py`**.

**Yeniden yazılan `dogrulama.py`: 67 kontrol, 67 doğrulandı, 0 uyuşmadı.**
Eskisinden daha güçlü — iki kontrol artık **bağımsız türetme**:

| Kontrol | Eski hali | Yeni hali |
|---|---|---|
| 24 harf havuzu | sabit dizi kendi kendine karşı | `ipucu2_24_duzmetin.txt` tablosunun son sütunundan **satır satır yeniden türetildi** → `IBRTADSSOREMHTDFNATEEMEW` ✅ |
| `MRWBEASTSATDHEREOFNIDTEM` | "alfabetik" diye etiketli | kuşların **İngilizce adlarına göre** sıralama olarak yeniden hesaplandı → ✅ (`American Bittern→M`, `Blue Jay→R`, `Brown Longspur→W`, `Crested Titmouse→B`, …) |

**❌ Bulunan ve düzeltilen veri hatası (9. hata):** üç dosyada *"üçü de 1-6 permütasyonu"*
yazıyordu (`ipuclari_ham.md`, `BULMACA_ANA_DOKUMAN.md:163`, `IPUCU_AGACI.md:109`). **Yanlış:**
```
251634 → {1,2,3,4,5,6}   ✅ tek gerçek 1-6 permütasyonu (sıralama anahtarı)
214674 → {1,2,4,4,6,7}   ❌ 7 var, 3 ve 5 yok, 4 iki kez
142674 → {1,2,4,4,6,7}   ❌ 214674 ile AYNI küme (zaten cikti.md:254'te yazıyordu)
461427 → {1,2,4,4,6,7}   ❌ aynı
```
`cikti.md` doğruyu biliyordu, diğer üç dosya bilmiyordu → çelişki giderildi.

**⚠️ Kendi hatam, son anda yakalandı:** kalan havuzu `24 − BEASTSAND(9) = 15 harf`
(`DEEEFHIMMORRTTW`) diye hesaplayıp dokümanların 13 harfini "hatalı" ilan etmek üzereydim.
**Dokümanlar doğru:** çıkarılan şey `BEASTSAND` değil, İ13'ün çıktısı olan
**`MRBEASTSAND` (11 harf)** → `24 − 11 = 13` → `DEEEFHIMORTTW` ✅.
Bu ayrım hiçbir dosyada açıkça yazmıyordu; artık `dogrulama.py`'da iki kontrol olarak var.
