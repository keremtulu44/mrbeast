# 🧩 MrBeast GİZLİ $10.000 BULMACASI — TAM ANALİZ ve YÖNLENDİRME DOKÜMANI

**Video:** `82CX6WULNA0` — "How 1 Person Solved A $1,000,000 Puzzle!"
**Bulmacayı yapan:** Colin ($1M'lik Salesforce avını çözen kişi)
**Son güncelleme:** 2026-09-13 · **Durum:** 🟡 Kısmen çözüldü — kırmızı taraf TAMAM, mavi taraf AÇIK

---

# 0) BU BELGE NASIL KULLANILIR

Bu, bulmacanın **tek ve eksiksiz kaydıdır.** Sıfırdan gelen biri (insan veya yapay zekâ)
bu belgeyi baştan sona okuduğunda şunları bilir: ne çözüldü, nasıl çözüldü, ne
çürüdü, ne kaldı, sıradaki adım ne.

## Okuma sırası
1. **§1** Bulmacanın tanımı ve hedefi
2. **§3** Kesinleşen kurallar *(bunlar değiştirilemez; geri kalan her şey bunlara dayanır)*
3. **§4** 17 ipucunun tek tek durumu
4. **§5** Ana zincir (`46TH PLATE`) — yöntemin doğruluğunun kanıtı
5. **§6** KIRMIZI TARAF — **ÇÖZÜLDÜ: `BEASTSAND`**
6. **§7** MAVİ TARAF — **AÇIK: `(6)` = ?**
7. **§8** Çürüyenler mezarlığı *(aynı hataya ikinci kez düşmemek için)*
8. **§10** Açık sorular — **öncelik sırasıyla sıradaki adımlar**

## Altın kurallar (çalışma disiplini)
- ✅ **Her şeyi kendin doğrula.** Harici/topluluk çıktılarına körü körüne güvenilmez.
- ⚠️ **Matematiksel olarak doğru olsa bile mantıksızsa ŞÜPHELİ olarak kaydet.**
- 📝 **Sonuçlar mutlaka workspace'e yazılır ve pushlanır.** Sohbette kalmaz.
- ❌ **Çürüyen iddia silinmez** — §8'e gömülür, ki bir daha denenmesin.

---

# 1) BULMACA NEDİR?

MrBeast'in "1 kişi $1.000.000'lık bulmacayı nasıl çözdü" videosunda, Colin adlı
çözücü kendi gizli **$10.000** bulmacasını saklamıştır. Sahne: bir masa/çalışma
odası. Masanın üzerinde:

| Nesne | İşlevi |
|---|---|
| Pembe notlar (24 plaka + Roma rakamları) | **Kırmızı tarafın** girdisi |
| Mavi not (`LSWRTE / NNHTIN / HDOTA`) | Rail fence → talimat |
| Beyaz kağıt (`(527) > (83544) > M̶R̶(9)`) | Kırmızı tarafın akış şeması |
| Mavi ped (`(364) (4445) → (66) → (6)`) | Mavi tarafın akış şeması |
| Yeşil not (`QX = TH`) | Sübstitüsyon anahtarı |
| Turuncu not (`SeaHawks?`) | Doğrulama |
| Sarı telefon (T9) | Muhtemelen başka bir dal (Nauru) |
| Elektrik panoları (`214` / `674`) | Ana zincirin girdisi |
| `$10,000` çizimi + dalgalı kontur | Coğrafi konum ipucu (ada?) |

**HEDEF:** İki "havuz" (sink) üretmek:
- 🔴 **Kırmızı havuz = `(9)`** → 9 harfli bir kelime → **`BEASTSAND`** ✅
- 🔵 **Mavi havuz = `(6)`** → 6 harfli bir kelime → **HENÜZ BİLİNMİYOR** ❌

---

# 2) DOSYA ENVANTERİ

| Dosya | İçerik |
|---|---|
| **`BULMACA_ANA_DOKUMAN.md`** | ← **BU BELGE.** Baştan sona yönlendirme |
| `cikti.md` | Ana çalışma defteri (tarihçe, tüm turlar) |
| `ucuncu_taraf_degerlendirme.md` | 26 harici iddianın bağımsız denetimi + şüphe listesi |
| `ipuclari_ham.md` | 17 ipucunun ham kaydı (değişmemiş birincil veri) |
| `ipucu2_24_duzmetin.txt` | İpucu 2: 24 plaka → 24 harf (satır satır gerekçe) |
| `ipucu1_14_duzmetin.txt` | İpucu 1: 14 görsel → 27 harf (görsel tanımı + lejant) |
| `video4_transkript.md` | Video 4'ün tam transkripti (3032 kelime) |
| `ikinci_gorus_promptu.md` | Başka bir yapay zekâya verilmek üzere hazır prompt |

---

# 3) KESİNLEŞEN KURALLAR

Bunlar **kanıtlanmış** kurallardır; tartışmaya kapalıdır.

### 3.1 Harf çıkarma
1. **Sayı = *Birds of America* (Havell, 1–435) PLAKA numarası.** (İpucu 7 `PLATES`)
2. **Roma rakamı = plakaya kazınmış ORİJİNAL Latince adın harf pozisyonu.** (İpucu 11)
3. Harf çıkarma **yalnızca Latince ad** üzerinden yapılır. İngilizce ad sadece kuşu
   tespit + alfabetik sıralama içindir. *(Modern bilimsel ad DEĞİL — Audubon'un kendi
   dönemindeki lejant.)*
4. Boşluk, noktalama, otorite kısaltması (L., Gm., Wils.) **sayılmaz.**
5. `424-6` = plaka 424'ün **6. kuşu** (Brown Longspur) — doğrulandı.
6. **İpucu 1'de kırmızı = baştan, mavi = sondan** → görsel başına **2 AYRI harf**
   (toplam 27, çünkü #10'da mavi yok).
7. `?` ile biten ipucu = **doğrulama/meta**; `?` olmayan = **veri**.
8. Filtreler: `L ≥ max(🔴,🔵)` ve **🔴 ≠ 🔵** (kilitli 7 örnekte doğrulandı).

**Latince saydığının KESİN kanıtı:** #7 Laughing Gull — İngilizce adı 12 harf,
mavi rakamı **XIV = 14** → 14 > 12 → İngilizcede sayılamaz.

### 3.2 🔑 NOTASYON: `(N)` = KELİME-UZUNLUĞU KODU — 5 ÖRNEKLE KESİN

| Kod | Açılım | Harf | Kaynak |
|---|---|---|---|
| `(527)` | BIRDS(5) OF(2) AMERICA(7) | **14** ✓ | İpucu 13 girdisi |
| `(83544)` | MRBEASTS(8) AND(3) ?(5) ?(4) ?(4) | **24** ✓ | 24 plakanın harfi |
| `(4445)` | LAST(4) WORD(4) THEN(4) NINTH(5) | **17** ✓ | İpucu 9 rail fence |
| `(66)` | FOURTH(6) UPLOAD(6) | **12** ✓ | İpucu 15 ara adımı |
| `(9)` | **BEASTSAND** — tek kelime | **9** ✓ | İpucu 13 ÇIKTISI |

**Kritik ayrım:** çok haneli kod = *kaç kelime ve uzunlukları*;
**tek haneli kod = CEVABIN HARF SAYISI.**
→ **`(6)` = 6 harfli TEK BİR KELİME.**

---

# 4) İPUÇLARI — TEK TEK DURUM

| # | İçerik | Durum |
|---|---|---|
| 1 | 14 görsel (emoji/bayrak) → 27 harf | 🟡 **9/14 kilitli**, dizi okunmuyor |
| 2 | 24 plaka → 24 harf | ✅ **%100 DOĞRULANDI** |
| 3 | `081 XIV / SeaHawks?` | ✅ Doğrulama (İpucu 2 ile aynı veri) |
| 4 | `## / How Many?` | ✅ **İki basamaklı gruplar** — ana zincirde kullanıldı |
| 5 | `QX = TH` | ✅ **Ordinal ek (-th)** — ana zincirde kullanıldı |
| 6 | `142674 / 251634 / 461427` | ✅ 251634 = ANAHTAR |
| 7 | `PLATES` | ✅ Sayılar = plaka numarası |
| 8 | `Youtube link watch?` | 🟡 Meta |
| 9 | Rail fence → `LAST WORD THEN NINTH` | ✅ **ÇÖZÜLDÜ** |
| 10 | `Book w/ old names… Alphabetize?` | 🟡 Meta (işlem değil, yönlendirme) |
| 11 | `Roman numbers for Roman words?` | ✅ Latince kuralını doğruluyor |
| 12 | `Boo!` + `Five of these` | 🟡 BOO+K = BOOK |
| 13 | `(527)→(83544)→M̶R̶(9)` | ✅ **ÇÖZÜLDÜ: `BEASTSAND`** |
| 14 | `(364)→(66)→(6)` (video sonu) | 🟡 Mavi tarafın aynı zinciri |
| 15 | `(364)(4445)→(66)→(6)` | 🟡 **(6) AÇIK** |
| 16 | `214` + `674` (iki ayrı üçlü) | ✅ Ana zincirin girdisi |
| 17 | İki olay arası **364 gün** | 🟡 Yan veri (konum kanıtı değil, VERİ olarak geçerli) |

---

# 5) ANA ZİNCİR — `46TH PLATE` (yöntemin doğruluğunun kanıtı)

```
①  İPUCU 16  :  214 + 674 = 214674        (iki ayrı elektrik panosu)
                    ↓
②  İPUCU 6 anahtarı 251634 ile sırala
      kural: yeni = [2., 5., 1., 6., 3., 4.]
      214674 → 1 7 2 4 4 6
                    ↓
③  İPUCU 4 (## / "How Many?") → iki basamaklı gruplar
      17 | 24 | 46
                    ↓
④  A1Z26 →  17 = Q    24 = X    46 = SAYI
                    ↓
⑤  İPUCU 5 (QX = TH) →  QX → TH
                    ↓
⑥  Sayı başa →  46 + TH = 46TH
                    ↓
⑦  İPUCU 7 (PLATES) →  "46TH PLATE"
```

**SONUÇ: `46TH PLATE` = PLAKA 46 = BARRED OWL = İPUCU 14'ÜN GÖRSELİ (HAPİSHANE KAPISI)** ✅

Bu zincir, yöntemin (plaka → Latince ad → harf) doğru olduğunu **geriye dönük kanıtlar.**

**Bağımsız doğrulama (tur 3):** 48 olası kombinasyonun **hiçbiri** üç geçerli A1Z26
çifti vermiyor → 3. yuvanın SAYI olması tesadüf değil, **yapısal zorunluluk.**
Ayrıca: 12 panel okumasından **yalnızca `214674`** geçerli sonuç verir; 360
permütasyonun tamamı taranmıştır.

---

# 6) 🔴 KIRMIZI TARAF — ÇÖZÜLDÜ: `BEASTSAND`

## Akış
```
(527) BIRDS OF AMERICA  →  (83544) 24 harf  →  M̶R̶(9)  →  BEASTSAND
```

## 24 harf (İpucu 2, plaka sırası)
```
I B R T A D S S O R E M H T D F N A T E E M E W
```
Havuz: `A×2 B×1 D×2 E×4 F×1 H×1 I×1 M×2 N×1 O×1 R×2 S×2 T×3 W×1`

**Alfabetik sıralayınca:**
```
M R W B E A S T S A T D H E R E O F N I D T E M
```
→ içinde **`MRBEASTSATDHERE…`** okunuyor.

## Çözüm
```
MRBEASTS(8) + AND(3) + [5] + [4] + [4]   ← (83544) uzunluk kodu, havuzu 24/24 kullanır
ilk 11 harf = MRBEASTSAND
M̶R̶ üstü çizili → "MR'yi AT" → kalan 9 harf = BEASTSAND  ✅ tam (9)
```

## 🔥 4 BAĞIMSIZ KANIT
| # | Kanıt |
|---|---|
| 1 | **Kullanıcı doğrulaması:** İpucu 13'te `M̶R̶(9)` — MR üstü çizili, **el çizimi YOK** |
| 2 | Havuz 24/24 birebir örtüşüyor (sıfır artık) |
| 3 | `(83544)` = 8,3,5,4,4 ve `(9)` = cevap uzunluğu — notasyon kuralıyla uyumlu |
| 4 | Alternatif `CHRISTMAS` **çürüdü**: havuzda **C harfi yok** |

## ⚠️ Kalan 13 harf
`D E E E F H I M O R T T W` → 5+4+4. **307 İngilizce adayın hiçbiri gramatik değil**
(`WIDTH MORE FEET` dâhil — 5. sırada). 9 dilde (İspanyolca, İtalyanca, Portekizce,
Fransızca, Katalanca, Rumence, Türkçe, Almanca, İngilizce) tarandı, hiçbirinde
anlamlı grup çıkmadı. **Latince imkânsız** (klasik Latincede W yok).
→ **Büyük ihtimalle İpucu 13'ün cevabı için gerekli DEĞİL.**

---

# 7) 🔵 MAVİ TARAF — AÇIK: `(6)` = ?

## Akış
```
(364) + (4445)  →  (66)  →  (6)
```

## ✅ Çözülen adımlar
| Adım | Sonuç | Kanıt |
|---|---|---|
| `(4445)` | **LAST WORD THEN NINTH** | ✅ İpucu 9 rail fence — **kendi çözümümüz** |
| `(66)` | **FOURTH UPLOAD** | ✅ 6+6 uzunluk kodu + **kullanıcı doğruladı: 4. video = "$1 vs $500,000 Experiences!"** (= $1M avı playlist'inin 4. videosu) |

## ⚠️ `(364)` — ŞÜPHELİ / ÇOK ADAYLİ
Topluluk: `XOR | SUPERB | OWLS` (3+6+4 ✓ uzunluk koduyla uyumlu).
- **"SUPERB OWLS" = Super Bowl punu gerçek ve mantıklı** ($1M bulmaca Super Bowl LX
  reklamındaydı — bağımsız kaynaklarla doğrulandı).
- **AMA `XOR` 17 ipucumuzun hiçbirinde yok** → kaynağı belirsiz, şüpheli.

### 📊 364'ün alternatif anlamları — bağımsız denetim (2026-09-13)
| Aday | Gerçek mi? | Bu bulmacada karşılığı | Güven |
|---|---|---|---|
| **Uzunluk kodu 3,6,4 = 13 harf** | ✅ **kuralımız (5 örnek)** | her çok haneli kod gibi | 🥇 **EN YÜKSEK** |
| **İpucu 17'nin 364 günü** (52×7) | ✅ | kendi ham verimiz | 🥈 |
| **PLAKA 364 = White-winged Crossbill** | ✅ **3 bağımsız kaynak** | plaka mekaniği + İpucu 1 #1 crossbill | ❌ **ÇÜRÜDÜ — `(66)` üretemiyor** (lejant testi, aşağıda) |
| İskambil destesi 4×91 = 364 | ✅ | kart motifi kanıtı yok | ⚠️ zayıf |
| Alan kodu 364 (Kentucky) | ✅ gerçek | telefon dalı var (+674 Nauru) | ⚠️ kanıtsız |
| Kitap şifresi *sayfa* 364 | ⚠️ kuralımızla çelişir | **ama PLAKA 364 var** ↑ | ⚠️ kısmen |
| Alice/un-birthday · Dante · birthday attack · melek sayısı | — | destek yok | ❌ dolgu |
| XOR | ❌ **döngüsel** (aynı Reddit kaynağı) | — | ❌ |

### ❌ `(364)` = PLAKA 364 — ÇÜRÜDÜ (kullanıcı itirazı + lejant testiyle)
Hipotez çarpıcıydı: plaka numarası bu bulmacanın merkezî mekaniği (İpucu 7 `PLATES`)
ve İpucu 1 / görsel #1 **zaten bir crossbill** (`Loxia`) — aynı cins:
```
PLAKA 364 (CCCLXIV) = White-winged Crossbill · Latince LOXIA LEUCOPTERA
İngilizce: WHITE(5) WINGED(6) CROSSBILL(9)
  → LAST WORD = CROSSBILL = 9 harf → 9. harf = L  ← tek harf!
```
**Kullanıcı itirazı:** `CROSSBILL → L` **tek harf** verir; `(66)` iki 6-harfli
kelime (12 harf) ister. → **İtiraz doğru, lejantla kanıtlandı.**

**Plaka 364'ün TAM lejantı (doğrulandı, Boston Public Library / Havell 1837):**
```
"White-winged crossbill : Loxia leucoptera, Gm. Male adult, 1, 2.
 Female adult, 3. Young F., 4. New Foundland alder"
Gravür: "...Engraved, printed & coloured by R. Havell, 1837."
Numara: set 73, plaka CCCLXIV (364) ✓
```
| Varyant | Kelime | LAST WORD | 9. kelime | `(66)`? |
|---|---|---|---|---|
| tüm kelimeler | 18 | alder (5) | 2 (1) | ❌ |
| sayılar atılmış | 14 | alder (5) | adult (5) | ❌ |
| sayı + otorite atılmış | 13 | alder (5) | Young (5) | ❌ |

→ **Plaka 364 ne `CROSSBILL→L` ile ne de lejantıyla `(66)` üretiyor.**
§8 mezarlığına gömüldü (bir daha bu yönden denenmeyecek).

### ✅ FRIDAY YOLU — KAYITTA (İpucu 14 + 17)
```
(364) = 364 GÜN (İpucu 17) → 1 Tem 1988 (CUMA) + 30 Haz 1989 (CUMA)
(66)  = FRIDAY | FRIDAY   → 6 + 6  ✅ uzunluk-kodu kuralımızla BİREBİR
(6)   = FRIDAY            → 6      ✅
```
⚠️ **Doğrulanmış veriyle `(66)`→`(6)` yapısını karşılayan TEK okuma.**
Ama kullanıcı notu: bu 364 İpucu 17'den geliyor ve İpucu 14'te kullanıldı →
İpucu 15'in `(364)`'ü aynı girdi olamaz. **Açık soru olarak duruyor.**

### ❌ `NIGHT` değil `NINTH` — kesin
```
scramble (İpucu 9): LSWRTENNHTINHDOTA = 17 harf, G YOK
LASTWORDTHENNINTH : 17 harf → harf kümesi birebir uyumlu ✓
LASTWORDTHENNIGHT : 17 harf → UYUMSUZ (fazla G, eksik N) ❌
```

### 👏 Yapısal gözlem: haneler küçülüyor
`(364)+(4445) → (66) → (6)` = **3+4 kelime → 2 kelime → 1 kelime.**
`LAST WORD` son adımı (2→1) açıklıyor. `THEN NINTH` ilk adımı açıklamalı →
**hipotez: talimatın iki parçası birer kelime seçer** (son kelime + 9. kelime =
2 kelime = `(66)` ✓ yapısal olarak kusursuz). Test edilen metinlerin hiçbiri
iki 6-harfli kelime vermedi (9 kelimelik cümle, 9 video başlığı, video 4
başlığı/transkripti, plaka 364 lejantı) → **kaynak metin hâlâ bilinmiyor.**

### `(364)` okumaları — yapısal karşılaştırma
| # | `(364)` = | `(66)` üretir mi? | `(6)` | `(4445)` rolü | Durum |
|---|---|---|---|---|---|
| **A** | 364 gün → iki tarih → ikisi de CUMA | ✅ FRIDAY \| FRIDAY (6,6) | ✅ FRIDAY | ❓ yok | ✅ yapının tek karşılığı, ama İp 14'e ait |
| **B** | FOURTH UPLOAD | ✅ FOURTH \| UPLOAD (6,6) | ✅ UPLOAD | ✅ LAST WORD | ⚠️ ifade tahmin |
| **C** | PLAKA 364 | ❌ CROSSBILL→L (1 harf) | ❌ | ✅ ama 1 harf | ❌ çürüdü |
| **D** | uzunluk kodu 3,6,4 (13 harf) | ? | ? | ? | ❓ kaynak metin yok |

## 🚨 VİDEO 4 SABİT YORUMU — `(66) = FOURTH UPLOAD` TAM BURAYA ÇIKIYOR
Video 4 (`Xj0Jtjg3lHQ` = `$1 vs $500,000 Experiences!`) sabit yorumu, +107.408 beğeni:
```
@MrBeast · 1 yıl önce (düzenlendi)
"Oh man, that was a trip. Several, actually. Here's a little souvenir for you."
https://imageshack.com/user/BeastForce67
```
**(66) = "FOURTH UPLOAD" — İKİ OKUMA, İKİSİ DE AYNI YERE ÇIKIYOR:**
```
(a) upload = YouTube videosu  → 4. video → SABİT YORUM → ImageShack hesabı
(b) upload = ImageShack yüklemesi → o hesabın 4. yüklemesi
→ "LAST WORD" → (6) = o yüklemenin son kelimesi (6 harf)
```
`"upload"` kelimesinin bir **resim barındırma hesabına** çıkması dikkat çekici.
Hesap adı `BeastForce67` — İpucu 16'daki `674` ile "67" örtüşmesi not edildi (kanıt değil).

### ✅ ARŞİVDE BULUNDU — Wayback Machine (09 + 11 Şub 2026)
Hesap **şu an boş** (kullanıcı teyidi) ama Wayback'te **2 anlık görüntü** var:
```
Görsel ID : KqjfA5 · Dosya adı: 9ErN78U5uxbnR2WTkd6S.png (rastgele)
Görsel sayısı: 1  ← iki anlık görüntüde de TEK görsel
Albüm: "No Albums"
TAM BOYUT: 2550 × 3300 px
   2550/3300 = 0,772727…   8,5/11 = 0,772727…  → ABD LETTER @ 300 DPI (BİREBİR)
   Boyut menüsünde bu seçenek yok (1600x1200'a kadar) → ORİJİNAL BOYUT
   → telefon fotoğrafı DEĞİL, taranmış/dijital bir BELGE
```
⚠️ **"4. yükleme" okuması (b) DÜŞTÜ** (hesapta tek görsel var).
Kalan zincir: `FOURTH UPLOAD` = **4. video** → sabit yorum → hesap → TEK görsel
→ `LAST WORD` → `(6)` = belgedeki metnin son kelimesi.

**📎 Kullanıcının açacağı bağlantılar** (benz göremiyor: ağ erişimi + vision yok):
1. Tam boyut: `https://web.archive.org/web/20260209005254/https://imagizer.imageshack.com/v2/2550x3300q70/922/KqjfA5.png`
2. Görsel sayfası: `https://web.archive.org/web/20260209031715/https://imageshack.com/i/pmKqjfA5p`
3. Canlı CDN: `https://imagizer.imageshack.com/v2/2550x3300q70/922/KqjfA5.png`

👉 **İstenen:** görselde ne var? Metni **aynen yaz** — özellikle **son kelime** ve
**9. kelime** (ikisi 6'şar harfse `(66)` kırılır).

### ⚠️ `BeastForce67` aynı zamanda bir TOPLULUK ADI — DİKKAT
- **r/BeastForce67** (Şub 2026) + `discord.gg/BeastForce67` + `discord.gg/tq5TQN59` ("OFFICIAL" iddiası)
- imgpile'da `beastforce67` "Puzzle" görseli (84.405 görüntüleme) → **sayfa kaldırılmış**
- ⚠️ **Hiçbiri resmî değil.** Topluluk adını MrBeast'in sabit yorumundan almış.
  "Resmî Discord" iddiası **kanıtsız → oltalama riski. Bu sunuculara girilmez.**

## ❌ `(6)` — HENÜZ YOK. `STUNTS` 4 KEZ ÇÜRÜDÜ
Topluluğun en popüler iddiası `STUNTS`. Bağımsız denetim:

| # | Çürütme |
|---|---|
| 1 | 24 harfli pembe havuzda **U yok** |
| 2 | "fourth upload → last word → ninth → STUNTS" adımı **kimse tarafından gösterilmedi** |
| 3 | 4. video başlığında **T ve U yok** |
| 4 | Video 4 transkriptinde (3032 kelime) **`stunt` kelimesi hiç geçmiyor** |

## `(6)` aday tablosu
| Aday | Gerekçe | Güven |
|---|---|---|
| `STUNTS` | sadece "6 harf" şartını sağlıyor | ❌ **ÖLDÜ** |
| `UPLOAD` | `(66)=FOURTH UPLOAD` → "LAST WORD" → 6 harf ✓ **en mekanik okuma** | ⚠️ orta |
| `ISLAND` | 6 harf + $10.000 çizimindeki kontur/ada + anahtar cümle KONUM diyor | ⚠️ orta |
| `PUZZLE` | video başlığının son kelimesi | ⚠️ spekülatif |

## Uygulanan ama sonuç vermeyen denemeler (Video 4, `Xj0Jtjg3lHQ`)
| Okuma | Sonuç |
|---|---|
| Videonun son kelimesi | `guys` ("I love you guys!") |
| 9. kelime / sondan 9. / 9. harf | `$1` / `put` / `o` |
| Satır son-kelimelerinin 9. harfleri | `clgaeloaneneecsceegesiiieioksrycvynn` ❌ |
| Cümle son-kelimelerinin 9. harfleri | `clgaelloanenneeccsceegesieieieioksrycrvyntn` ❌ |

→ **`(6)` transkriptte değil.** Video 4'ün bulmacası konuşmada değil, **ekrandaki
grafiklerde ve sabit yorumda** (karıştırılmış konum adları: COLFAX, DOVERCOURT,
HOLSTER + renkli harfler → 7 harfli cevap = **TOWARDS**).

---

# 8) ÇÜRÜYENLER MEZARLIĞI (bir daha denenmeyecek)

| İddia | Neden çürüdü |
|---|---|
| `MRBEASTHAND` | İpucu 13'te **el çizimi yok** (kullanıcı doğruladı); `MRBEASTH` kelime değil |
| `(6) = STUNTS` | 4 bağımsız çürütme (§7) |
| `(9) = CHRISTMAS` | 24 harfli havuzda **C yok** |
| "EACH tesadüf olamaz, P≈1/457.000" | Aynı 27 harf rastgele karıştırılınca **ortalama 17,35** dört-harfli kelime çıkıyor; `each` %0,6 → çoklu karşılaştırma hatası |
| "A'dan Z'ye akrostiş = alfabetik okuma kanıtı" | **TAUTOLOJİ** — liste zaten alfabetik sıralı |
| "NIDTEM → NINTH ITEM", "SAT D HERE → SAT THERE" | Harfler uyuşmuyor — **uydurma** |
| "(8,3,5,4,4) için 0 çözüm var" | **YANLIŞ** — 110.028 çözüm bulundu |
| #13'ü "EACH çıkmazsa olmaz" diye kilitlemek | **Döngüsel** (EACH zaten #13+#14'ün harfleri) |
| `AAA(9)` transkripsiyonu | **Kullanıcı doğruladı: `M̶R̶(9)`, AAA yok** |
| Latince ada göre alfabetik sıralama | Anlamsız çıktı |
| İpucu 2 için sondan-sayma | Anlamsız çıktı |
| "HAND havuzdan yazılabiliyor" kanıtı | Havuzdan 899 dört-harfli kelime çıkıyor → kanıt değil |
| Kalan 13 harften İspanyolca/Latince grup | 9 dil tarandı, hiçbiri anlamlı değil; Latincede W yok |
| `(364)` = PLAKA 364 (White-winged Crossbill) | Kuş doğru (3 kaynak) ama `CROSSBILL→L` **tek harf**; lejantın LAST WORD=<br>`alder`(5), 9. kelime=`Young`(5) → **`(66)` üretilemiyor** (§7) |

---

# 9) ŞÜPHELİLER LİSTESİ (doğrulanmadan kullanma)

1. `(364) = XOR SUPERB OWLS` — `XOR` kaynağı yok
2. `(66) = FOURTH UPLOAD` — uzunluk kodu uyumlu ama "Oct 4th + upload" altyazı
   iddiası doğrulanamadı (kullanıcı teyidi hariç)
3. Resmî cevap PDF'i (`mrb.gg/p/puzzle/file.pdf`) — **2 kez HTTP 500**, JS viewer
   arkasında. İçeriği doğrulanamadı.
4. "Will Campbell 66" ve "Hawks up on the Pats 6-0" alıntıları — doğrulanamadı
   (Hawks=NBA / Pats=NFL tutarsız)
5. `97, 121, 171` sayıları · "27=3³→3×9 matris" · "beastsandstunts" birleşimi
6. #10 = 203 (E) — gerekçesi "kuşun rengi"; kilitli 9 örneğin hepsi **İSİM punu**
   → **349 (J) birincil kalıyor**
7. **"İpucu 9 = rail fence cipher"** (topluluk + bizim ham kaydımızdaki not)
   → ❌ **ÇÜRÜDÜ:** 2–8 ray decode + 720 kolon permütasyonu denendi, hiçbiri
   `LASTWORDTHENNINTH` üretmiyor. Çözüm **anagram** (harf envanteri birebir uyumlu).
   "bird fence?" notu **ESPri** (kuş temalı), mekanizma adı değil.
8. **"+674 → Nauru → telefon numarası"** (topluluk) — İpucu 16'daki `674` ile uyumlu
   ama sonuç **gösterilmemiş** → şüpheli
9. **"OFFICIAL DISCORD"** (`discord.gg/tq5TQN59`, `discord.gg/beastforce67`) —
   **kanıtsız, resmî değil → oltalama riski. Girilmez.**
10. **84 sayfalık resmî cevap PDF'i** (`mrb.gg/p/puzzle`) — topluluk da doğruluyor
    ama **HTTP 500**, erişilemiyor

### ✅ Üçüncü taraf kaynaklardan BAĞIMSIZ TEYİT ALANLARIMIZ
- **`QX = TH`** → bizim **İpucu 5** ile birebir aynı ✓
- **`021 XIV` / `SeaHawks?`** → bizim **İpucu 3** ile aynı ✓
- **`(364) → (66) → (6)`** beyaz pad → bizim **İpucu 15** ile aynı ✓

### ⚠️ Kısmi düzeltme (kendi şüphe kaydım)
"Rosé 73" alıntısını halüsinasyon diye işaretlemiştim. **Gerçekten var — ama hâliyle:**
> *"Take the vault code, add **L73 from Rosé's shirt**, then add on all the numbers in
> the background"* → `R62L39R05L73606623093121200300`

Doğrusu **"73" değil "L73"**.

---

# 10) AÇIK SORULAR — ÖNCELİK SIRASIYLA

### 🥇 1. `(6)` — mavi havuz (bulmacanın kalan tek büyük parçası)
**EN SICAK İP: `imageshack.com/user/BeastForce67`** — video 4'ün sabit yorumundaki
"souvenir" bağlantısı. `(66) = FOURTH UPLOAD` buraya çıkıyor (iki okuma birden).
**Engel:** ImageShack giriş duvarı — içerik bizim için erişilemez.
👉 **Kullanıcı açıp 3 şeyi söylemeli: kaç yükleme var · 4. yüklemenin başlığı/yazısı · sıra+tarih.**
Ardından: video 4'teki **ekrandaki grafikler** (karıştırılmış konum adları + renkli harfler).
*Transkriptte değil — 7 farklı okuma denendi, hiçbiri 6 harf vermedi.*
*Sabit yorumun kendi metni de 6+6 vermiyor (LAST=you(3), 9.=Here(4)) — cevap HESAPTA.*

### 🥈 2. `$10.000` çiziminin altındaki dalgalı kontur
Ada haritası mı (Christmas Island kolu), dağ konturu mu?
Anahtar cümle **"LOCATION NAME SOMEWHERE AROUND WORLD"** diyor → cevap bir KONUM olabilir.

### 🥉 3. İpucu 1'in kalan 6 tespiti
#1 (Umman bayrağı), #8, #10 (Water-hen), #11, #12, #13. 27 harf hâlâ okunmuyor.
⚠️ Düzeltme: #9'da `thalassidromapelagica` = **21 harf**, mavi IX → sondan 9. = **a**
(eski "m" yanlıştı).

### 4. `142674` → "UNZ" ve `461427` → "JUN" ilişkisi
İpucu 17'nin tarihlerinden biri June 30 - 89 → "JUN" ilgi çekici ama çift uygulama şüpheli.

### 5. Tarihlerin (İpucu 17) nerede kullanılacağı
1 Tem 1988 ve 30 Haz 1989 **ikisi de Cuma**; 364 gün = tam 52 hafta.
`FRIDAY` = 6 harf → `(66)`/`(6)` ile bağdaşıyor ama henüz kanıtlanmadı.

### 6. İpucu 8 (`Youtube link watch?`) ve İpucu 12 (`Boo! Five of these`)
Henüz kullanılmadı.

---

# 11) DOĞRULANMIŞ YAN BİLGİLER

- **$1M avının 9 kelimelik anahtar cümlesi — 3 bağımsız kaynakla doğrulandı:**
  `EVERY CHALLENGE LEADS TOWARDS LOCATION NAME SOMEWHERE AROUND WORLD`
  Uzunluklar `5,9,5,7,8,4,9,6,5` = 58 harf ✓ (resmî Lone Shark Games İpucu #1 ile birebir)
- **Video 4'ün bulmaca cevabı = `TOWARDS`** (7 harf — resmî listeyle uyumlu)
- **`+674` = Nauru ülke kodu** (telefon/T9 dalı)
- **İpucu 1'in Latince punları:** `calendula`(takvim) · `fuscus`(çikolata) ·
  `nivalis`(kar) · `rustica`(ahır) · `chrysaetos`(altın kartal) · `Loxia`(çapraz)

---

# 12) ÖZET: NE BİLİYORUZ / NE BİLMİYORUZ

| | |
|---|---|
| ✅ **BİLİNEN** | Yöntem (plaka → Latince ad → harf) · `46TH PLATE` zinciri · 24 plaka/24 harf · Notasyon kuralı `(N)` · **Kırmızı havuz = `BEASTSAND`** · `(4445) = LAST WORD THEN NINTH` · `(66) = FOURTH UPLOAD` → Video 4 |
| ❌ **BİLİNMEYEN** | **`(6)` = mavi havuz** · `(364)`'ün anlamı · İpucu 1'in 27 harfi · kalan 13 harf · 142674/461427 · tarihlerin yeri |
| ⚠️ **ŞÜPHELİ** | `XOR` kaynağı · PDF alıntıları · `#10 = 203` |

## SON SÖZ
Kırmızı taraf kapanmıştır. **Bulmacanın tamamlanması tek bir şeye bağlı: Video 4'ün
sabit yorumundaki / ekranındaki bulmacadan `(6)` havuzunu (6 harf) çıkarmak.**
O bulunduğunda birleşim `BEASTSAND` + `(6)` olacaktır.
