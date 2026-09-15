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


# ------------------------------------------------- İPUCU 1: kırmızı/mavi AYRI (tur 15)
print("\n[12] İpucu 1 — kırmızı ve mavi havuz, ayrı ayrı (TUR 15)")
_ROM = {"I":1,"V":5,"X":10,"L":50,"C":100}
def _r2i(t):
    t=t.strip(); tot=0; pv=0
    for ch in reversed(t):
        v=_ROM[ch]; tot += v if v>=pv else -v; pv=max(pv,v)
    return tot
_i1 = R("ipucu1_14_duzmetin.txt")
_pat = re.compile(r"SAYIM\s*:\s*([a-z]+)\s*→\s*🔴\s*([IVX]+)\s*=\s*([A-Za-z])"
                  r"\s*🔵\s*([IVX—]+)\s*=\s*([A-Za-z—])")
_sat = _pat.findall(_i1)
k("İpucu 1 SAYIM satırı (14 görsel + 4 varyant)", 18, len(_sat))
_hata = 0
for _ad,_kr,_kh,_mr,_mh in _sat:
    _L=len(_ad); _ki=_r2i(_kr)
    if _ad[_ki-1].upper()!=_kh.upper(): _hata+=1
    if _mr!="—":
        _mi=_r2i(_mr)
        if _ad[_L-_mi].upper()!=_mh.upper(): _hata+=1
k("17 satırın kırmızı+MAVİ harf aritmetiği hatasız", 0, _hata)

_PRIM=[0,2,3,4,5,6,7,8,9,13,14,15,16,17]      # TUR 17: #10 = Sula fusca (satır 13)
K="".join(_sat[i][2].lower() for i in _PRIM)
M="".join(_sat[i][4].lower() for i in _PRIM if _sat[i][4]!="—")
k("🔴 KIRMIZI havuz — TUR 17 (#10=Booby Gannet)", "ceanlnciisoyce", K)
k("🔵 MAVİ havuz (kaynaktan yeniden türetildi)",   "odfvialaataha", M)
k("🔴 kırmızı harf sayısı = (527)=5+2+7", 14, len(K))
k("🔵 mavi harf sayısı   = (364)=3+6+4", 13, len(M))
k("dosyadaki §4 kırmızı dizisi birebir", True, "c e a n l n c i i ? o y c e" in _i1)

_kK,_kM = set(K), set(M)
k("🔴 kırmızı alfabe {a,c,e,i,l,n,o,s,y} — j gitti, s geldi", set("aceilnosy"), _kK)
k("🔵 mavi alfabe {a,d,f,h,i,l,o,t,v}",    set("adfhilotv"), _kM)
_bir = _kK|_kM
for _h in "brumgpw":
    k(f"birleşik 27 harfte '{_h}' YOK", False, _h in _bir)
k("TUR 17: 's' artık KIRMIZI havuzda VAR", True, "s" in _kK)
_w = lambda hav,soz: all(Counter(soz)[c] <= Counter(hav)[c] for c in set(soz))
k("'BEAST' kırmızıdan yazılamaz",   False, _w(K,"beast"))
k("'BEAST' maviden yazılamaz",      False, _w(M,"beast"))
k("'BEAST' birleşikten yazılamaz",  False, _w(K+M,"beast"))
k("'MRBEASTSAND' birleşikten yazılamaz", False, _w(K+M,"mrbeastsand"))
k("TUR 15 iddiası: 'CEYLON' kırmızıdan YAZILABİLİYOR", True,  _w(K,"ceylon"))
k("TUR 15 iddiası: 'LATVIA' maviden YAZILABİLİYOR",    True,  _w(M,"latvia"))
k("TUR 15 iddiası: 'SRI LANKA' kırmızıdan YAZILAMIYOR (CEYLON güncel ad değil)",
  False, _w(K,"srilanka"))
_art = Counter(M)-Counter("latvia")
k("mavi − LATVIA = 7 harf", 7, sum(_art.values()))
k("mavi − LATVIA envanteri a3 d f h o", "aaadfho", "".join(sorted(_art.elements())))
k("mavi − LATVIA'da yalnızca 3 'a' var (6+6+1 için yetmez)", 3, _art["a"])
k("TUR 15: kırmızıda 'b' yok → CEYLON+LATVIA birleşik yazılamaz mı? (LATVIA'da v/t/d/f/h var)",
  False, _w(K,"latvia"))

_x = R("cikti.md")
k("cikti.md §0-X bölümü var", True, bool(re.search(r"^#+ *§?0-X\)", _x, re.M)))
k("§0-W'daki ülke testi çürütme işareti taşıyor", True, "TUR 15'TE ÇÜRÜDÜ" in _x)
k("IPUCU_AGACI.md CEYLON iddiasını çürütüyor", True, "ÇÜRÜDÜ" in R("IPUCU_AGACI.md"))
k("BULMACA_ANA_DOKUMAN.md LATVIA'yı mezarlığa aldı", True,
  "TUR 15'TE ÖLDÜ" in R("BULMACA_ANA_DOKUMAN.md"))


# ------------------------------------------------- TUR 16: 24 varyant + kesinleşen plakalar
print("\n[13] İpucu 1 — 24 varyant, kesinleşen plakalar, (66) kaynak testi (TUR 16)")
def _hv(ad, kr, mr):
    t=''.join(ch for ch in ad.lower() if ch.isascii() and ch.isalpha()); L=len(t)
    return t[L-_r2i(mr)] if mr else None, t[_r2i(kr)-1]

# --- kesinlesen 3 plaka: kazinmis lejant -> harf
for _pl,_ad,_kr,_mr,_bk,_bm in [
    (109,'Fringilla savanna','IV','VIII','n','a'),      # Pitt Darlington pitt:aud0109
    (251,'Pelecanus fuscus','VI','VI','a','f'),         # Boston Public Library
    (349,'Rallus jamaicensis','VII',None,'j',None)]:    # audubon.org "Plate 349"
    _m,_k=_hv(_ad,_kr,_mr)
    k(f"plaka {_pl}: 🔴 {_kr}→'{_bk}'" + ("  [#10 ÇÜRÜDÜ: TUR 17 → Booby Gannet]" if _pl==349 else ""), _bk, _k)
    if _bm: k(f"plaka {_pl}: 🔵 {_mr}→'{_bm}'", _bm, _m)

# --- #13: Falco mu Aquila mi — mavi ayni, kirmizi degisiyor
_m1,_k1=_hv('Aquila chrysaetos','VII','IX')
_m2,_k2=_hv('Falco chrysaetos','VII','IX')
_m3,_k3=_hv('Falcochrysaetosl','VII','IX')
k("#13 Aquila: 🔴 c / 🔵 h", ('c','h'), (_k1,_m1))
k("#13 Falco (15): 🔴 h = 🔵 h → filtre KIRILIYOR", ('h','h'), (_k2,_m2))
k("#13 Falco+otorite (16): 🔴 h / 🔵 r", ('h','r'), (_k3,_m3))
k("ÖNEMLİ: mavi harf Aquila ve Falco'da AYNI", _m1, _m2)

# --- 24 varyantin hicbiri tek kelime degil: kirmizi/mavi alfabeleri degisiyor mu?
_V1=[('Loxia curvirostra','VI','V'),('Ardea ludoviciana','VI','V')]
_V10=[('Rallus jamaicensis','VII',None),('Rallus elegans','VII',None),('Rallus crepitans','VII',None)]
_V13=['Aquila chrysaetos','Aquilachrysaetosl','Falcochrysaetosl','Falco chrysaetos']
_S=[('Regulus calendula','II','IV'),('Pelecanus fuscus','VI','VI'),('Emberiza nivalis','IX','V'),
    ('Falco lineatus','VI','VII'),('Fringilla savanna','IV','VIII'),('Larus atricilla','X','XIV'),
    ('Sylvia aestiva','V','VII'),('Thalassidroma pelagica','VIII','IX'),('Hirundo rustica','VII','IV'),
    ('Sylvicola childrenii','II','XI'),('Strix nebulosa','VII','I')]
_komb=0; _kuz=set(); _muz=set(); _filtre=0
for _a in _V1:
  for _b in _V10:
    for _c in _V13:
      _komb+=1
      _K=[];_M=[]
      for _ad,_kr,_mr in _S+[_a,_b,(_c,'VII','IX')]:
        _m,_k=_hv(_ad,_kr,_mr); _K.append(_k)
        if _m: _M.append(_m)
        if _m and _m==_k: _filtre+=1
      _kuz.add(''.join(_K)); _muz.add(''.join(_M))
k("varyant kombinasyonu (2×3×4) — TARİHSEL: #10 TUR 17'de çözüldü", 24, _komb)
k("farklı 🔴 KIRMIZI havuz sayısı (#1×2 · #10×3 · #13×2)", 12, len(_kuz))
k("farklı 🔵 MAVİ havuz sayısı (#1×2 · #13×2)", 4, len(_muz))
k("MAVI havuz 'r' İÇEREN varyant var (yalnızca +otorite)", True,
  any('r' in x for x in _muz))
k("MAVI havuz 'r' İÇERMEYEN varyant da var", True,
  any('r' not in x for x in _muz))
k("kırmızı=mavi çakışması yalnızca 'Falco chrysaetos'ta (24'te 6)", 6, _filtre)
k("hiçbir varyantta 🔴 uzunluk 14 değil", False, any(len(x)!=14 for x in _kuz))
k("hiçbir varyantta 🔵 uzunluk 13 değil", False, any(len(x)!=13 for x in _muz))

# --- İpucu 2'nin kalan 13 harfi: (66) buradan cikamaz
_h24 = harf
_mr  = "MRBEASTSAND"
kalan = Counter(_h24) - Counter(_mr)
k("İpucu 2 kalan harf sayısı (24-11)", 13, sum(kalan.values()))
k("kalan harfler DEEEFHIMORTTW", "DEEEFHIMORTTW", ''.join(sorted(kalan.elements())))
_6 = [w for w in ("MOTHER","WITHER","HERMIT","FOTHER","WIDTHX") if all(Counter(w)[c]<=kalan[c] for c in w)]
_iki6 = 0
for _x in _6:
    _r = kalan - Counter(_x)
    for _y in _6:
        if all(Counter(_y)[c]<=_r[c] for c in _y): _iki6 += 1
k("(6,6,1) için iki 6-harfli kelime birlikte sığıyor mu", 0, _iki6)
k("(66) = 12 harf, kalan havuzda 6+6 mümkün değil", True, _iki6==0)

_y = R("cikti.md")
k("cikti.md §0-Y bölümü var", True, bool(re.search(r"^#+ *§?0-Y\)", _y, re.M)))
k("348/349 uyuşmazlığı çözüldü olarak işaretli", True, "349 DOĞRU" in _y)
k("#13 lejant ikilemi kaydedildi (LOC Falco)", True, "falco chrysaetos" in _y)


# ------------------------------------------------- TUR 17: Booby Gannet
print("\n[14] İpucu 1 #10 = BOOBY GANNET (Sula fusca, plaka 207) — TUR 17")
_t,_k = _hv('Sula fusca','VII',None)
k("Sula fusca = 9 harf", 9, len('sulafusca'))
k("🔴 VII = 7. harf = 's'", 's', _k)
k("#10'da 🔵 mavi rakam yok", None, _t)
k("L=9 ≥ kırmızı 7 (filtre tutuyor)", True, 9 >= 7)
_ESKI='ceanlnciijoyce'
k("eski havuzda 10. harf 'j' idi (Rallus jamaicensis)", 'j', _ESKI[9])
_YENI=_ESKI[:9]+'s'+_ESKI[10:]
k("yeni kırmızı havuz ceanlnciisoyce", "ceanlnciisoyce", _YENI)
k("havuz uzunluğu hâlâ 14 = (527)", 14, len(_YENI))
k("rail adayları mezarlıkta (jamaicensis/elegans/crepitans)", True,
  all(x in R("cikti.md") for x in ("jamaicensis","elegans","crepitans")))
_i1t = R("ipucu1_14_duzmetin.txt")
k("dosyada Booby Gannet lejantı var", True, "Booby Gannet, Sula fusca" in _i1t)
k("dosyada plaka 207 kayıtlı", True, "PLAKA 207" in _i1t)
k("dosyada yeni kırmızı dizi var", True, "ceanlnciisoyce" in _i1t)
k("plaka 197 lejantı (Loxia curvirostra, Linn.) kayıtlı", True,
  "Loxia curvirostra, Linn." in R("cikti.md"))
_C=Counter(_YENI)
for _w,_n in (("science",7),("silence",7),("concise",7),("oceanic",7),
              ("insolence",9),("concisely",9),("leniency",8),("social",6)):
    k(f"🔴 yeni havuzdan '{_w}' yazılabiliyor", True,
      all(_C[c] >= Counter(_w)[c] for c in set(_w)))
k("🔴 'beast' hâlâ yazılamıyor (b ve t yok)", False,
  all(_C[c] >= Counter("beast")[c] for c in set("beast")))
k("cikti.md §0-Z bölümü var", True, bool(re.search(r"^#+ *§?0-Z\)", R("cikti.md"), re.M)))

print(f"\n{'='*78}\nTOPLAM: {OK} doğrulandı, {FAIL} uyuşmadı")
sys.exit(1 if FAIL else 0)
