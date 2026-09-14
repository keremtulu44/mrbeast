# ÜÇÜNCÜ TARAF ÇIKTILARININ BAĞIMSIZ DEĞERLENDİRMESİ
**Tarih:** 2026-09-13 · **Kural:** hiçbir iddiaya körü körüne güvenilmedi, hepsi yeniden hesaplandı.

Yöntem: 114.028 kelimelik sözlük (gcide) + kelime sıklığı (wordfreq) + kendi permütasyon/anagram
kodum. Aşağıda her iddia için **kendi ölçümüm** var.

---

## 🔴 KULLANICI DOĞRULAMASI (13 Eyl 2026) — İKİ İDDİA BİRDEN BİTİYOR

> **"MR (9), MR üstü çizili, başka çizim vs yok"**

| Sonuç | Detay |
|---|---|
| ❌ **`AAA (9)` transkripsiyonu ÇÜRÜDÜ** | Çıktı 3'ün topluluk kaynaklı iddiası yanlış. Notta `M̶R̶(9)` var, `AAA` yok. |
| ❌ **`HAND` hipotezi düştü** | İpucu 13'te **el çizimi yok** → HAND'ın hiçbir görsel dayanağı kalmadı. |
| ✅ **`SAND` öne geçti** | `MRBEASTS(8) + AND(3)` havuzu 24/24 kullanıyor ve ilk 11 harf = **`MRBEASTSAND`** = `M̶R̶` atılınca kalan **tam 9 harf** → İpucu 13'ün yapısıyla birebir. |
| ✅ **`M̶R̶(9)` = "MR'yi AT, kalan 9 harf"** | Cevap 11 harf (`MRBEASTSAND`) değil, **9 harf: `BEASTSAND`** |

**Kalan tek açık nokta:** cümlenin son 13 harfi (`D E E E F H I M O R T T W` → 5+4+4).
`MRBEASTS AND` sabitlendiğinde **307 farklı kelime kümesi** çıkıyor ve **hiçbiri
gramatik bir İngilizce cümle değil** (`WIDTH MORE FEET` dahil — 5. sırada).
→ Ya kalıp yanlış (24 = 8+3+5+4+4 bir tesadüf), ya son 13 harf İngilizce değil,
ya da sadece ilk 11 harf kullanılıp kalanı başka bir mesaj.

---

## 0) ÖZET TABLO

| # | İddia (hangi çıktı) | Benim doğrulamam | Sonuç |
|---|---|---|---|
| 1 | "EACH tesadüf olamaz, P≈1/457.000" (Ç1) | Aynı 27 harf rastgele karıştırılınca **ortalama 17,35** farklı 4-harfli kelime çıkıyor (min 4 / max 34); `each` özel olarak **%0,6** | ❌ **YANLIŞ** (çoklu karşılaştırma hatası) |
| 2 | "14→1 okuma yönü doğrulandı" (Ç1) | yukarıdaki kanıt çökünce **doğrulanmamış** kalıyor | ⚠️ ŞÜPHELİ |
| 3 | #13'ü "EACH çıkmazsa olmaz" diye kilitlemek (Ç1) | EACH zaten #13'e bağlı → **döngüsel akıl yürütme** | ❌ GEÇERSİZ |
| 4 | #1 = Loxia curvirostra → `c o` (Ç1) | İki bağımsız gerekçe (bayrak=millet → American; çapraz kılıç → cross → Crossbill/Loxia) **aynı kuşa** çıkıyor | ✅ MAKUL |
| 5 | #1 için "EdCo hecesi daha doğal" (Ç1) | sahte gerekçe | ❌ ÇÖP |
| 6 | #8 = Sylvia aestiva → `i a` (Ç1) | harfler doğru; ama verdiği İngilizce ad YANLIŞ | ⚠️ KISMİ |
| 7 | Plaka 95 = "Blue Yellow-backed Warbler" (Ç1) | audubon.org: **"Blue-eyed yellow Warbler"** plaka 95 | ❌ YANLIŞ AD |
| 8 | #10 = 203 Rallus elegans → `E` (Ç1) | kilitli 9 örneğin **tamamı İSİM punu** (calendula/fuscus/nivalis/rustica…), hiçbiri kuşun rengi değil. "Least tekrarı" estetik tahmin | ⚠️ **ZAYIF** → 349 (J) birincil aday kalıyor |
| 9 | #12 = Sylvicola childrenii → `y a` (Ç1) | mantık sağlam (sakalsız→Noel Baba değil, cüce değil→elf değil→çocuk) | ✅ |
| 10 | #13 = Aquila chrysaetos → `c h` (Ç1) | kırmızı≠mavi + L≥9 filtreleri tutuyor; ama bkz. #3 | 🟡 (döngüsüz gerekçeyle) |
| 11 | "27 = 3³ → 3×9 matris" (Ç1) | destek yok | ⚠️ SPEKÜLASYON |
| 12 | "A'dan Z'ye akrostiş = alfabetik okumanın kanıtı" (Ç2) | liste **zaten** alfabetik sıralı → baş harflerin alfabetik olması ZORUNLU sonuç | ❌ **TAUTOLOJİ** |
| 13 | "NIDTEM → NINTH ITEM" (Ç2) | NIDTEM=6 harf, NINTHITEM=9 → harfler uyuşmuyor | ❌ **UYDURMA** |
| 14 | "SAT D HERE → SAT THERE" (Ç2) | D≠T, harfler uyuşmuyor | ❌ **UYDURMA** |
| 15 | **"MRBEASTS AND WIDTH MORE FEET"** (Ç2) | **24/24 harf birebir örtüşüyor, uzunluklar tam 8-3-5-4-4** | ✅ **MATEMATİK KUSURSUZ** |
| 16 | (aynı çözümün tek/EN doğru olduğu iması) | MRBEASTS sabitken **(3,5,4,4) için 110.028 çözüm** var; "MRBEASTS AND …" ile sınırlasan bile **292** | ⚠️ **1/110.028 → keyfi** |
| 17 | aynı cümlenin anlamı | "MRBEASTS AND WIDTH MORE FEET" **gramer dışı** | ⚠️ ŞÜPHELİ |
| 18 | mrb.gg/p/puzzle = 84 sayfa, 1 Eyl 2026 (Ç3) | sayfayı çektim: **"Million Dollar Puzzle Answers", Published September 1, 2026 · 84 pages** | ✅ **GERÇEK** |
| 19 | PDF'ten alıntılar (Rosé 73, Will Campbell 66, "Hawks up on the Pats 6-0") (Ç3) | PDF **iki kez HTTP 500** → doğrulanamadı. Ayrıca Hawks=NBA, Pats=NFL → iç tutarsızlık | ⚠️ **HALÜSİNASYON RİSKİ YÜKSEK** |
| 20 | "(8,3,5,4,4) için 0 çözüm var" (Ç3) | **YANLIŞ** — ben 110.028 çözüm buldum (biri tam 24/24 oturanı) | ❌ **YANLIŞ** |
| 21 | "MRBEASTHAND havuzdan yazılamaz (senin ❌'in yanlış)" (Ç3) | yazılabilir ✅ — AMA ben böyle bir şey yazmadım; benim argümanım **8 harfli kelime sınırı** ("MRBEASTH" kelime değil) | ⚠️ STRAW MAN |
| 22 | "214764 --241635--> 172446" (Ç3) | elle + kodla doğruladım: (o2,o4,o1,o6,o3,o5) = 1,7,2,4,4,6 | ✅ **DOĞRU** |
| 23 | "48 kombinasyonun hiçbiri 3 geçerli A1Z26 çifti vermiyor" (Ç3) | ben bağımsız taradım: **0** ✅ → 3. yuvanın SAYI olması yapısal zorunluluk | ✅ **DOĞRU (+ güçlü)** |
| 24 | "(364) = XOR\|SUPERB\|OWLS" (Ç3) | yapısal olarak tutarlı (3,6,4; harf toplamı 13 = rakam toplamı 13) ama topluluk iddiası, bağımsız doğrulayamadım | ⚠️ DOĞRULANAMADI |
| 25 | İpucu 13 transkripsiyonu "AAA (9)" (Ç3) | **kullanıcı doğruladı: M̶R̶(9), AAA yok** | ❌ **ÇÜRÜDÜ** |
| 26 | "97, 121, 171 sayıları" (Ç3) | kaynağı belirsiz, bizde yok | ⚠️ DOĞRULANAMADI |

---

## 1) ÇIKTI 1 — "EACH" iddiası çürüdü

27 harf: `eachyaoteiaiaclnalinvafedco`

**Ölçüm (aynı 27 harf, 2000 rastgele karıştırma):**
```
ortalama 25,67 farklı 3-harfli kelime  (min 8, max 42)
ortalama 17,35 farklı 4-harfli kelime  (min 4, max 34)
'each' geçen deneme: 12 / 2000  → P ≈ %0,60
```
Bizim dizide geçen 4-harfli kelimeler (11 tane):
`acln afed alin clna each edco hyao iacl inva lnal nali`

→ Yani bu harf havuzuyla **4 harfli bir kelime çıkması istisna değil, norm** (ortalama 17 tane).
Çıktı 1'in "1/26⁴ ≈ 1/457.000" hesabı, *önceden belirlenmiş* bir kelimenin *önceden belirlenmiş*
bir yuvada çıkması içindir. Biz kelimeyi **gördükten sonra** seçtik ve 2 yön × 24 yuva taradık
(klasik çoklu karşılaştırma hatası).

**Sonuç:** `EACH` ≠ kanıt. 14→1 okuma yönü **hâlâ doğrulanmamış hipotez.**
Ve #13'ü "EACH çıkmazsa olmaz" diye kilitlemek **döngüsel**: EACH zaten #13 ve #14'ün
harflerinden oluşuyor.

**#10 hakkında:** Çıktı 1'in gerekçesi "kahverengi → King Rail kızıl-kahve" ve
"#9'da Least kullanıldı, tekrar etmesin". İkincisi estetik tahmin; birincisi ise
**kilitli 9 örneğin mantığına aykırı** — onların hepsi İSİM punu:
`calendula`(takvim) · `fuscus`(koyu kahve) · `nivalis`(kar) · `rustica`(kır) ·
`chrysaetos`(altın kartal) · `Loxia`(çapraz) · `savanna` · `atricilla`(gülme) ·
`nebulosa`(parmaklıklı).
Hiçbiri "kuşun rengi şu" diye çalışmıyor. O yüzden 349 / **J** birincil aday olarak kalıyor.

---

## 2) ÇIKTI 2 — akrostiş tautoloji, ama içinde gerçek bir cevher var

**"A'dan Z'ye akrostiş kanıt" iddiası geçersiz:** 24 kuşu İngilizce adına göre alfabetik
sıraladığımız liste zaten elimizde. Baş harflerin A→Z gitmesi, alfabetik sıralamanın
**zorunlu sonucu** — kanıt değil. (Ayrıca "A'dan Z'ye" de değil: **B ve T iki kez**,
**L, Q, U, X eksik**.)

**"NIDTEM → NINTH ITEM" ve "SAT D HERE → SAT THERE" uydurma.** Harfler uyuşmuyor:
- `NIDTEM` = 6 harf, `NINTHITEM` = 9 harf → imkânsız
- `SAT D HERE` içindeki D, `THERE` için gereken T değil

**AMA — doğruladım:** `MRBEASTS AND WIDTH MORE FEET` havuzu **24/24 birebir** kullanıyor:
```
MRBEASTS(8) + AND(3) + WIDTH(5) + MORE(4) + FEET(4)
A2 B1 D2 E4 F1 H1 I1 M2 N1 O1 R2 S2 T3 W1   == HAVUZ  ✅ (sıfır artık)
```
Bu gerçekten şık: `83544` = 8,3,5,4,4 kalıbına tam oturuyor **ve** ilk 11 harfi
`MRBEASTSAND` = İpucu 13'ün **MR + (9)** yapısını birebir veriyor
(MR | BEASTS | AND → "MR"den sonraki 9 harf = `BEASTSAND`).

**Neden yine de şüpheli?** Çünkü bu kalıpta **110.028** çözüm var (MRBEASTS sabitken,
kelime sıklığı ≥2.5). "MRBEASTS AND …" ile daraltsan bile **292** tane:
```
MRBEASTS AND TEETH FROM WIDE   (ortalama frekans 5,39)
MRBEASTS AND WORTH FEED TIME   (5,37)
MRBEASTS AND THROW TIME FEED   (5,26)
MRBEASTS AND THEFT MORE WIDE   (5,15)
MRBEASTS AND WIDTH FEET MORE   (5,12)   ← aynı kelimeler, sıra farklı
MRBEASTS AND WIDTH MORE FEET   (5,12)
MRBEASTS AND WHITE MEET FORD   (5,09)
…
```
"WIDTH MORE FEET" ilk 10'da ama **gramatik bir cümle değil**; rakipleri de değil.
Frekans sıralamasında birinci bile değil. Yani bu çözüm **matematiksel olarak mükemmel,
anlamsal olarak keyfi** — tam olarak "matematik doğru ama mantıksız" kategorisi.

**Not (kendi hatam):** önceki turda "8,3,5,4,4 kalıbıyla 4.000+ aday, hepsi anlamsız"
yazmıştım. Arama sınırına (8000 sonuç) takıldığı için **yanlış ve eksikti**; gerçek sayı
110.028+. Düzeltiyorum.

---

## 3) ÇIKTI 3 — kaynak gerçek, ama iki merkezî iddiası yanlış

✅ **Doğrulandı:** `https://mrb.gg/p/puzzle` gerçekten var — *"Million Dollar Puzzle
Answers", Published September 1, 2026 · 84 pages*. Yani Lone Shark Games'in resmî cevap
kitabı iddiası doğru. (PDF'in kendisini çekemedim: iki denemede HTTP 500.)

❌ **Yanlış:** "(8,3,5,4,4) deseninde 0 çözüm var." Ben 110.028 çözüm buldum; biri
(MRBEASTS AND WIDTH MORE FEET) havuzu 24/24 kullanıyor. Bu, Ç3'ün benim SAND argümanımı
çürütmek için kurduğu ana dayanak — **çürütme geçersiz**. (Sonuç olarak SAND lehine
argümanım zayıflamadı; ama 110k alternatif olduğu için güçlenmedi de.)

⚠️ **Straw man:** "MRBEASTHAND havuzdan yazılabilir (senin ❌'in yanlış)" diyor.
Doğru, yazılabilir — ama ben hiçbir yerde "yazılamaz" demedim. Argümanım şuydu:
8 harfli ilk kelime zorunluysa `MRBEASTH` bir kelime değil, `MRBEASTS` ise kelime.
Bu argüman hâlâ ayakta.

✅ **Doğrulandı (güçlü):** `214764` --`241635`--> `172446`. Yani (214674, 251634) ve
(214764, 241635) **aynı çıktıyı** veriyor. Anahtar tartışması pratikte önemsizleşiyor.

✅ **Doğrulandı (güçlü):** 48 kombinasyonun hiçbiri üç geçerli A1Z26 çifti üretmiyor
(ben bağımsız taradım: 0). Yani çıktı **zorunlu olarak** [harf][harf][SAYI] biçiminde →
3. yuvanın plaka numarası olması tesadüf değil, **yapısal zorunluluk**. Bu, `46TH PLATE`
zincirini Ç3'ten bağımsız olarak güçlendiriyor.

⚠️ **Doğrulanamadı / halüsinasyon riski:** PDF'ten alıntıladığı "Rosé wears a 73",
"Hawks are up on the Pats 6-0", "Will Campbell's number 66", "quarter 2, 3:09, 3rd and 12".
PDF'i çekemedim (HTTP 500). Ayrıca **Hawks (NBA) vs Pats (NFL)** karışımı iç tutarsız.
Bu alıntıların `(66)`'ya uydurulmuş olma ihtimali ciddi. Kullanmadan önce PDF'ten kontrol et.

---

## 4) 🚨 ŞÜPHELİLER LİSTESİ (doğrulanmadan kullanılmayacak)

1. **`EACH` / 14→1 okuma yönü** — kanıt sayılan olasılık hesabı yanlış; hipotez hâlâ açık.
2. **`MRBEASTS AND WIDTH MORE FEET`** — matematik 24/24 ama 110.028 alternatiften biri ve
   gramatik değil. "Tek doğru çözüm" diye sunulması yanlış.
3. **#10 = 203 (E)** — gerekçe (kuşun rengi) kilitli örneklerin mantığıyla uyumsuz.
   349 (J) / 203 (E) / 204 (C) hâlâ açık.
4. **PDF alıntıları** (Rosé 73 / Will Campbell 66 / Hawks-Pats 6-0) — doğrulanamadı, iç tutarsız.
5. **`AAA (9)` transkripsiyonu** — kullanıcının M̶R̶(9) okumasıyla çelişiyor; videodan kontrol şart.
6. **`97, 121, 171`** sayıları — kaynağı belirsiz.
7. **"27 = 3³ → 3×9 matris"** — desteksiz.
8. **"(364) = XOR\|SUPERB\|OWLS"** — yapısal olarak tutarlı ama topluluk iddiası.
9. **Ç2'nin "NIDTEM→NINTH ITEM", "SAT D HERE→SAT THERE"** okumaları — harfler uyuşmuyor, uydurma.
10. **Ç3'ün "(8,3,5,4,4) = 0 çözüm"** iddiası — ölçülebilir şekilde yanlış.

---

## 4-B) HAND vs SAND — NİHAİ

| | HAND | SAND |
|---|---|---|
| havuzdan yazılabilir | ✅ | ✅ |
| görsel destek (İpucu 13) | ❌ **yok** (kullanıcı doğruladı) | — |
| `M̶R̶(9)` ile uyum | `BEASTHAND` (9) ✅ | `BEASTSAND` (9) ✅ |
| 8 harfli ilk kelime | `MRBEASTH` ❌ kelime değil | `MRBEASTS` ✅ |
| 24/24 tam örtüşme | ❌ | ✅ (`MRBEASTS AND` + 5,4,4) |
| topluluk okuması | 0 kayıt | 3 bağımsız okuma |

**→ `BEASTSAND`.** `HAND` artık sadece "havuzdan yazılabilir" ile ayakta, o da her iki
taraf için eşit.

## 5) BENİM NET YARGIM

- **Sağlam kalan:** 24 harf + havuz (%99), kural (tam Latince ad, baştan),
  `214674/214764 → 172446 → 17|24|46 → QX+46 → "46TH PLATE" = Barred Owl` (**bu tur
  yapısal olarak daha da güçlendi**: 3. yuvanın sayı olması zorunlu).
- **Bu turun tek yeni somut kazancı:** `MRBEASTS AND WIDTH MORE FEET` 24/24 örtüşüyor ve
  ilk 11 harfi `MRBEASTSAND` → İpucu 13'ün **MR+(9)**'uyla birebir uyumlu.
  Bu, `SAND` tarafını destekleyen **en iyi** (ama hâlâ kesin olmayan) delil.
- **Çürüyen:** EACH kanıtı, akrostiş kanıtı, Ç3'ün "0 çözüm" çürütmesi.
- ~~Kullanıcıdan istenen görsel kontrol~~ → **TAMAMLANDI (13 Eyl 2026):** `M̶R̶(9)`, el çizimi yok.

**Kalan tek soru:** son 13 harf (`D E E E F H I M O R T T W`) ne diyor? 307 adayın hiçbiri
gramatik değil. Sıradaki hamle: bu 13 harfi İngilizce dışında bir dilde (İspanyolca/Latince)
çözmeyi denemek, ya da 8-3-5-4-4 kalıbını bırakıp 83544'ü başka türlü okumak.

---

## EK A — ÇOK DİLLİ TARAMA (seçenek b: "İspanyolca / öz diller")

**Tarih:** 2026-09-13 · **Hedef:** `MRBEASTS AND` sonrası kalan 13 harf `D E E E F H I M O R T T W`

Yöntem: `wordfreq` paketinin **gerçek frekans verisi** (9 dil). wordfreq Latince
DESTEKLEMİYOR (en yakın eşleşme İtalyanca'ya düşüyor → Latince sonuçlar geçersiz).

| Dil | Sözlük | 13 harften oluşan kelime | (5,4,4) tam bölme | Sonuç |
|---|---|---|---|---|
| İngilizce | 287.289 | 2.372 | 107.576 | ❌ anlamsız |
| İspanyolca | 326.061 | 1.712 | 13.922 | ❌ anlamsız (`MEDIO WERE FTTH`) |
| İtalyanca | 293.923 | 1.691 | 10.398 | ❌ (`FETTE DIRE WHOM`) |
| Portekizce | 255.462 | 1.593 | 10.020 | ❌ (`THEFT MEIO DREW`) |
| Fransızca | 296.810 | 1.847 | 23.272 | ❌ (`THEFT DIRE MEOW`) |
| Katalanca | 175.758 | 1.086 | 3.232 | ❌ (`WHITE MORT FEED`) |
| Rumence | 42.591 | 325 | 68 | ❌ (`FEMEI DREW TOTH`) |
| Türkçe | 59.739 | 325 | 102 | ❌ (`FETHI ETME WORD`) |
| Almanca | — | 164 (≥7 harf) | — | ❌ (`WETTEIFER`, hepsi özel ad) |

**En uzun tek kelime denemesi (13 harfi tek kelime yutan var mı?):**
```
WHITTEMORE(10) · METEORITE(9) · WHITEFORD(9) · WITHERED(8) · WHITMORE(8) · METERWEIT(9, Alm.)
```
→ Hepsi **özel ad / soyadı** (Whittemore, Whitford, Whitmore) ya da tesadüf
(METEORITE). Anlamlı tek kelime yok.

### Latince neden imkânsız
Klasik Latincede **W harfi yoktur** (V kullanılır) ve H çok nadirdir. Kalan 13 harf
`D E E E F H I M O R T T W` hem **W** hem **H** içeriyor → Latince bir kelime grubu
olamaz. (Denenebilecek Latince parçalar: `FODERE`(kazmak), `MITTE`(gönder),
`ITER`(yol), `FORTE`(tesadüfen), `MERITO`(haklı olarak), `FORTEM`(cesur) — ama W
hiçbirine girmiyor.)

### SONUÇ — seçenek (b) ÇÜRÜDÜ
9 dilde de anlamlı bir kelime grubu çıkmadı. Kalan 13 harf büyük ihtimalle:
- **(c)** İpucu 13'ün cevabı için **gerekli değil** — `M̶R̶(9)` = `BEASTSAND`
  sadece ilk 11 harfi (`MRBEASTSAND`) kullanıyor, kalan 13 harf ya kullanılmıyor
  ya da başka bir ipucunun girdisi.

### 🚩 Takip edilebilecek bir ipucu (topluluk, düşük güven)
Topluluk İpucu 15'in mavi sonucunu `(6)` = **STUNTS** diye okuyor. Doğruysa:
```
BEASTSAND (9, kırmızı)  +  STUNTS (6, mavi)  =  BEASTSANDSTUNTS (15)
= "BEASTS AND STUNTS"  (6+3+6)
```
Çıktı 3 buna %20 güven veriyor (STUNTS türetmesi zayıf: U ve N×2 havuzda yok,
yani pembe 24 havuzdan gelmiyor). Ama `BEASTS AND STUNTS` İngilizce olarak
**düzgün bir ifade** — tek başına bu, diğer 307 adaydan daha anlamlı.
