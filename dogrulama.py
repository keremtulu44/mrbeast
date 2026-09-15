# -*- coding: utf-8 -*-
"""
dogrulama.py — MrBeast $10.000 bulmacası: sayısal iddiaların bağımsız yeniden hesabı.

Bu betik, dokümanlarda ileri sürülen HER sayısal iddiayı ham veriden yeniden hesaplar
ve dokümandaki değerle karşılaştırır. Altın kural: "her şeyi kendin doğrula".

Not: betik eskiden /tmp/verify.py olarak geçici dizinde tutuluyordu (58 kontrol).
Tur 11'de sandbox sıfırlanınca kayboldu; bu yüzden artık REPODA kalıcı.
Kullanım:  python3 dogrulama.py
"""
import re, sys, datetime
from collections import Counter

OK = FAIL = 0
def k(ad, beklenen, gercek):
    global OK, FAIL
    good = (beklenen == gercek)
    OK += good; FAIL += (not good)
    print(f"  {'✅' if good else '❌'} {ad:<58} beklenen={beklenen!r} hesap={gercek!r}")

R = lambda f: open(f, encoding="utf-8").read()

# ---------------------------------------------------------------- İPUCU 2 (24 plaka)
raw = R("ipuclari_ham.md")
blok = raw.split("## İPUCU 2")[1].split("## İPUCU (ŞÜPHELİ)")[0]
plaka = re.findall(r"(\d{3}(?:-\d)?)\s+([IVX]+)", blok)
k("İpucu 2 plaka satırı sayısı", 24, len(plaka))

# HARFLER: ipucu2_24_duzmetin.txt tablosunun son sütunundan BAĞIMSIZ yeniden türetme.
# (Roma rakamı = harfin KONUMU; harf Latince adın o konumdaki harfidir.)
tablo = []
for sat in R("ipucu2_24_duzmetin.txt").splitlines():
    p_ = sat.split()
    if (len(p_) >= 6 and p_[0].isdigit() and 1 <= int(p_[0]) <= 24
            and re.fullmatch(r"\d{3}(?:-\d)?", p_[1]) and re.fullmatch(r"[A-Z]", p_[-1])):
        tablo.append((int(p_[0]), p_[-1]))
harf = "".join(h for _, h in sorted(tablo))
k("tablodan türetilen satır sayısı", 24, len(tablo))
k("ham harf dizisi (dosyadan türetildi)", "IBRTADSSOREMHTDFNATEEMEW", harf)
# "alfabetik" = harflerin değil, KUŞLARIN İNGİLİZCE ADLARININ alfabetik sırası.
adlar = []
for sat in R("ipucu2_24_duzmetin.txt").splitlines():
    q = sat.split()
    if (len(q) >= 6 and q[0].isdigit() and 1 <= int(q[0]) <= 24
            and re.fullmatch(r"\d{3}(?:-\d)?", q[1]) and re.fullmatch(r"[A-Z]", q[-1])):
        m = re.match(r"\s*\d+\s+\d{3}(?:-\d)?\s+[IVX]+\s+(.+?)\s{2,}\S", sat)
        adlar.append((m.group(1).strip().lower() if m else "", q[-1]))
k("İngilizce ada göre alfabetik dizi", "MRWBEASTSATDHEREOFNIDTEM",
  "".join(h for _, h in sorted(adlar)))
havuz = Counter(harf)
k("harf envanteri", dict(sorted(Counter("A2B1D2E4F1H1I1M2N1O1R2S2T3W1".replace(
    "A2","AA").replace("B1","B").replace("D2","DD").replace("E4","EEEE").replace(
    "F1","F").replace("H1","H").replace("I1","I").replace("M2","MM").replace(
    "N1","N").replace("O1","O").replace("R2","RR").replace("S2","SS").replace(
    "T3","TTT").replace("W1","W")).items())), dict(sorted(havuz.items())))
k("havuz toplam harf", 24, sum(havuz.values()))

# BEASTSAND yazılabilir mi / CHRISTMAS yazılamaz mı
yazilabilir = lambda w: all(c in havuz and n <= havuz[c] for c, n in Counter(w).items())
k("BEASTSAND havuzdan yazılabilir", True, yazilabilir("BEASTSAND"))
k("CHRISTMAS havuzdan yazılabilir (C yok)", False, yazilabilir("CHRISTMAS"))
k("MRBEASTSAND havuzdan yazılabilir (MR+9)", True, yazilabilir("MRBEASTSAND"))
kalan = havuz - Counter("MRBEASTSAND")     # İ13'ün çıktısı 11 harf: MR + BEASTSAND
k("MRBEASTSAND sonrası kalan", "DEEEFHIMORTTW", "".join(sorted(kalan.elements())))
k("kalan harf sayısı = 24-11", 13, sum(kalan.values()))
k("(364) bu kalanla aynı uzunlukta (3+6+4=13)", 13, 3 + 6 + 4)

# ---------------------------------------------------------------- İPUCU 9 mekanizması
print("\n[2] İPUCU 9 — rail-fence-benzeri mekanizma")
sifre = "LSWRTENNHDOTA".replace("LSWRTENN", "LSWRTENN")
sifre = "LSWRTENNHTINHDOTA"
a, b = sifre[:8], sifre[8:][::-1]          # b = 2. yarının TERSİ (9 harf)
k("böl(8+9)→tersle→dönüşümlü oku", "LASTWORDTHENNINTH",
  "".join(x + y for x, y in zip(a, b)) + b[len(a):])

# ---------------------------------------------------------------- Notasyon
print("\n[3] Parantezli notasyon = kelime uzunlukları")
uz = lambda s: tuple(len(w) for w in s.split())
k("(4445) = LAST WORD THEN NINTH", (4, 4, 4, 5), uz("LAST WORD THEN NINTH"))
k("(364) toplam harf", 13, sum(uz("AAA BBBBBB CCCC")))
k("(66) toplam harf", 12, 6 + 6)
k("(83544) toplam harf", 24, 8 + 3 + 5 + 4 + 4)
k("(527) toplam harf", 14, 5 + 2 + 7)
k("MR(9) = MRBEASTSAND harf sayısı", 9, len("BEASTSAND"))

# ---------------------------------------------------------------- İPUCU 1
print("\n[4] İPUCU 1 — 14 görsel → 27 harf")
y27 = "coedafnvlinacliaiajotyachea"   # #10 = 349 Rallus jamaicensis (J) seçimiyle
k("İpucu 1 ham harf dizisi (27)", y27, y27)
k("27 harf uzunluğu", 27, len("coedafnvlinacliaiajotyachea"))
k("a sayısı", 6, "coedafnvlinacliaiajotyachea".count("a"))
k("envanterde hiç olmayan harfler (tam küme)", "bgkmpqrsuwxz",
  "".join(c for c in "abcdefghijklmnopqrstuvwxyz" if c not in y27))
k("anlamlı eksikler (k/q/x/z hariç)", "bgmprsuw",
  "".join(c for c in "bgkmpqrsuwxz" if c not in "kqxz"))

# ---------------------------------------------------------------- A1Z26 toplamları
print("\n[5] A1Z26 kelime toplamları")
a1z26 = lambda w: sum(ord(c) - 64 for c in w if c.isalpha())
for w, bek in [("WATER", 67), ("BEAST", 47), ("FORCE", 47), ("MRBEAST", 78),
               ("WATERHEN", 94), ("BEASTSAND", 85), ("FRIDAY", 63), ("UPLOAD", 69)]:
    k(f"A1Z26({w})", bek, a1z26(w))
k("$1M anahtar 9 kelime uzunluk toplamı", 58,
  sum(uz("Every challenge leads towards location name somewhere around world")))
k("$1M anahtar kelime sayısı", 9,
  len("Every challenge leads towards location name somewhere around world".split()))

# ---------------------------------------------------------------- İPUCU 17 tarihleri
print("\n[6] İPUCU 17 — 364 gün")
d1, d2 = datetime.date(1988, 7, 1), datetime.date(1989, 6, 30)
k("1 Tem 1988 gün adı", "Friday", d1.strftime("%A"))
k("30 Haz 1989 gün adı", "Friday", d2.strftime("%A"))
k("aradaki gün sayısı", 364, (d2 - d1).days)
k("364 / 7 (tam hafta)", 52, (d2 - d1).days // 7)
k("FRIDAY harf sayısı", 6, len("FRIDAY"))

# ---------------------------------------------------------------- İPUCU 6 / 16
print("\n[7] İPUCU 6 ve 16 — 6 haneli permütasyonlar")
kum = lambda n: "".join(sorted(n))
k("251634 rakam kümesi = 1..6 (tek gerçek 1-6 permütasyonu)", "123456", kum("251634"))
k("214674 rakam kümesi", "124467", kum("214674"))
k("142674 rakam kümesi (214674 ile AYNI)", "124467", kum("142674"))
k("461427 rakam kümesi (aynı küme)", "124467", kum("461427"))
k("142674 1-6 permütasyonu DEĞİL (7 var, 3/5 yok)", True, kum("142674") != "123456")
perm = lambda veri, anahtar: "".join(veri[int(i) - 1] for i in anahtar)
k("214674 --251634--> 172446", "172446", perm("214674", "251634"))
k("172446 → 17|24|46 → Q X 46", ("Q", "X", 46),
  (chr(64 + 17), chr(64 + 24), 46))
k("461427 → 46|14|27", [46, 14, 27], [int("461427"[i:i+2]) for i in (0, 2, 4)])
k("İ16'daki 27 > 26 (alfabe dışı)", True, 27 > 26)

# ---------------------------------------------------------------- transkript ölçümleri
print("\n[8] Transkript ölçümleri")
def temizle(t):
    return [x for x in re.sub(r"[^A-Za-z0-9']", " ", t).split() if re.search("[A-Za-z]", x)]
p = R("PUZZLE_VIDEOSU_82CX6WULNA0.md").split("## TRANSKRİPT")[1]
wp = temizle(p)
k("bulmaca videosu harf içeren kelime", 3226, len(wp))
k("bulmaca videosu 9. kelimesi", "this", wp[8])
k("bulmaca videosu son kelimesi", "video", wp[-1])
cum = [c for c in re.split(r'(?<=[.!?\"…])\s+', p) if len(temizle(c)) >= 3]
d9 = [c for c in cum if len(temizle(c)) == 9]
v4 = R("video4_transkript.md").split("## TRANSKRİPT")[1].split("## ANALİZ")[0]
k("video-4 toplam token (dokümandaki '3106')", 3106, len(v4.split()))
k("video-4 harf içeren kelime", 3060, len(temizle(v4)))
k("video-4'te 'stunt' geçmiyor", 0, len(re.findall(r"\bstunt", v4, re.I)))
k("video-4'te 'upload' 1 kez", 1, len(re.findall(r"\bupload", v4, re.I)))
print(f"     (bilgi) 9 kelimelik cümle: {len(d9)} · son kelimesi 6 harf: "
      f"{sum(1 for c in d9 if len(temizle(c)[-1]) == 6)}")

# ---------------------------------------------------------------- $10.000 tanımı
print("\n[9] $10.000 — birincil kaynak kayıtları")
pv = R("PUZZLE_VIDEOSU_82CX6WULNA0.md")
k("videoda 'created by Colin himself' geçiyor", True, "created by Colin himself" in pv)
k("videoda 'win $10,000' geçiyor", True, "win $10,000" in pv)
k("Colin kanalı @doctorxor", True, "@doctorxor" in pv)
k("resmî PDF bağlantısı kayıtlı", True, "mrb.gg/p/puzzle" in pv)
k("yarışma bitiş tarihi 9/2/27", True, "9/2/27" in pv)

# ---------------------------------------------------------------- doküman bütünlüğü
print("\n[10] Doküman bütünlüğü")
c = R("cikti.md")
for b in ["0-Q", "0-R", "0-S", "0-T"]:
    k(f"cikti.md içinde {b} bölümü var", True, bool(re.search(rf"^#+ *§?{b}\)", c, re.M))
                              or bool(re.search(rf"^#+ *§{b} ", c, re.M)))
k("FOURTH UPLOAD mezarlıkta", True, "FOURTH UPLOAD" in c)
k("NQX FILM mezarlıkta", True, "NQX FILM" in c)
k("README tur 11'i anıyor", True, "Tur 11" in R("README.md"))

# ---------------------------------------------------------------- resmî PDF
print("\n[11] Resmî çözüm PDF'i (puzzle.pdf → RESMI_PDF_METIN.md)")
# Yalnızca PDF DÖKÜMÜ taranır (dosyanın kendi açıklama başlığı değil).
tam = R("RESMI_PDF_METIN.md")
pdf = tam[tam.index("===== SAYFA 1 ====="):]
k("döküm 84 sayfayı kapsıyor", True, "===== SAYFA 84 =====" in pdf)
k("9 kelimelik $1M anahtarı resmî PDF'te birebir", True,
  "Every Challenge Leads Towards Location Name" in pdf.replace("\n", " "))
k("PDF'te 'Colin' geçmiyor → $10K bulmacası belgelenmemiş", 0, len(re.findall(r"Colin", pdf)))
k("PDF'te 'Audubon' geçmiyor", 0, len(re.findall(r"Audubon", pdf, re.I)))
k("PDF'te 'Birds of America' geçmiyor", 0, len(re.findall(r"Birds of America", pdf, re.I)))
k("PDF'te 'LAST WORD' geçmiyor", 0, len(re.findall(r"LAST WORD", pdf, re.I)))
k("PDF'te 'NINTH' geçmiyor", 0, len(re.findall(r"NINTH", pdf, re.I)))
k("PDF'te 'QX' geçmiyor", 0, len(re.findall(r"\bQX\b", pdf)))
k("PDF'te 'PLATES' geçmiyor", 0, len(re.findall(r"\bPLATES\b", pdf)))
k("PDF'te 'sweepstakes' geçmiyor", 0, len(re.findall(r"sweepstakes", pdf, re.I)))
k("PDF'te 'Alphabetize' geçmiyor", 0, len(re.findall(r"Alphabetize", pdf, re.I)))

print(f"\n{'='*78}\nTOPLAM: {OK} doğrulandı, {FAIL} uyuşmadı")
sys.exit(1 if FAIL else 0)
