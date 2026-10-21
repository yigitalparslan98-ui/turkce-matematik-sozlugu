import streamlit as st

st.set_page_config(
    page_title="6. Sınıf Matematik Sözlüğü", page_icon="📐", layout="wide"
)

# 6. Sınıf Düzeyine Uygun 28 Temel Matematik Terimi
math_dictionary = [
    {
        "term": "Açı",
        "category": "Geometri",
        "desc": "Başlangıç noktaları aynı olan iki ışının arasında oluşan açıklıktır.",
        "example": "Dar açı, dik açı ve geniş açı çeşitleri vardır.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><line x1='30' y1='150' x2='170' y2='150' stroke='green' stroke-width='3'/><line x1='30' y1='150' x2='130' y2='60' stroke='gray' stroke-width='3'/></svg>"
    },
    {
        "term": "Alan",
        "category": "Geometri",
        "desc": "Bir şeklin yüzeyinin kapladığı yerdir.",
        "example": "Karenin alanı bir kenarının karesidir.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><rect x='50' y='50' width='100' height='100' fill='#22c55e'/></svg>"
    },
    {
        "term": "Asal Sayı",
        "category": "Sayılar",
        "desc": "Sadece 1'e ve kendisine bölünebilen 1'den büyük doğal sayılardır.",
        "example": "2, 3, 5, 7, 11 gibi sayılar asal sayıdır.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><circle cx='100' cy='90' r='40' fill='#16a34a'/><text x='88' y='98' fill='white' font-size='24'>7</text></svg>"
    },
    {
        "term": "Basamak Değeri",
        "category": "Sayılar",
        "desc": "Bir rakamın bulunduğu basamağa göre aldığı değerdir.",
        "example": "345 sayısındaki 4 rakamının basamak değeri 40'tır.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><text x='30' y='100' fill='green' font-size='22'>345 → 40</text></svg>"
    },
    {
        "term": "Bileşik Kesir",
        "category": "Kesirler",
        "desc": "Payı paydasına eşit veya payından büyük olan kesirlerdir.",
        "example": "7/4 veya 5/3 birer bileşik kesirdir.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><text x='75' y='105' fill='green' font-size='32'>7/4</text></svg>"
    },
    {
        "term": "Bölme",
        "category": "İşlemler",
        "desc": "Bir bütünü eş parçalara ayırma veya gruplara bölme işlemidir.",
        "example": "12 elmanın 3 kişiye paylaştırılması 12 ÷ 3 = 4'tür.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><text x='65' y='105' fill='green' font-size='28'>12 ÷ 3</text></svg>"
    },
    {
        "term": "Çarpan",
        "category": "Sayılar",
        "desc": "Bir sayıyı kalansız bölen her bir doğal sayı o sayının çarpanıdır.",
        "example": "10'un çarpanları 1, 2, 5 ve 10'dur.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><text x='75' y='105' fill='green' font-size='28'>1, 2, 5</text></svg>"
    },
    {
        "term": "Çember",
        "category": "Geometri",
        "desc": "Merkezine eşit uzaklıktaki noktaların oluşturduğu kapalı eğridir.",
        "example": "Yüzük veya çember tahtası çembere örnektir.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><circle cx='100' cy='90' r='50' fill='none' stroke='green' stroke-width='4'/></svg>"
    },
    {
        "term": "Çevre",
        "category": "Geometri",
        "desc": "Bir geometrik şeklin dış sınırının uzunluğudur.",
        "example": "Kenar uzunlukları toplamı çevre uzunluğunu verir.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><rect x='50' y='50' width='100' height='100' fill='none' stroke='green' stroke-width='4'/></svg>"
    },
    {
        "term": "Daire",
        "category": "Geometri",
        "desc": "Çember ve iç bölgesinin birleşiminden oluşan düzlemsel bölgedir.",
        "example": "Madeni para bir daire modelidir.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><circle cx='100' cy='90' r='50' fill='#22c55e'/></svg>"
    },
    {
        "term": "Dik Açı",
        "category": "Geometri",
        "desc": "Ölçüsü tam 90 derece olan açıdır.",
        "example": "Kare ve dikdörtgenin köşe açıları dik açıdır.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><line x1='60' y1='130' x2='140' y2='130' stroke='green' stroke-width='3'/><line x1='60' y1='130' x2='60' y2='50' stroke='green' stroke-width='3'/></svg>"
    },
    {
        "term": "Doğal Sayılar",
        "category": "Sayılar",
        "desc": "0'dan başlayıp sonsuza kadar giden sayılar kümesidir.",
        "example": "0, 1, 2, 3, 4... şeklinde devam eder.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><text x='35' y='105' fill='green' font-size='20'>0, 1, 2, 3...</text></svg>"
    },
    {
        "term": "Geniş Açı",
        "category": "Geometri",
        "desc": "Ölçüsü 90 dereceden büyük, 180 dereceden küçük olan açıdır.",
        "example": "120 derecelik bir açı geniş açıdır.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><line x1='30' y1='130' x2='170' y2='130' stroke='green' stroke-width='3'/><line x1='30' y1='130' x2='150' y2='80' stroke='gray' stroke-width='3'/></svg>"
    },
    {
        "term": "Hacim",
        "category": "Ölçme",
        "desc": "Üç boyutlu cisimlerin uzayda kapladığı yer miktarıdır.",
        "example": "Dikdörtgenler prizmasının hacmi en, boy ve yüksekliğin çarpımıdır.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><rect x='50' y='70' width='70' height='70' fill='#22c55e'/></svg>"
    },
    {
        "term": "Kesir",
        "category": "Kesirler",
        "desc": "Bir bütünün eş parçalarından bir veya birkaçını gösteren ifade.",
        "example": "1/2, 3/4 birer kesirdir.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><text x='75' y='105' fill='green' font-size='32'>3/4</text></svg>"
    },
    {
        "term": "Koordinat Sistemi",
        "category": "Geometri",
        "desc": "İki sayı doğrusunun dik kesişmesiyle oluşan yer belirleme sistemidir.",
        "example": "x ve y eksenlerinden oluşur.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><line x1='30' y1='90' x2='170' y2='90' stroke='green' stroke-width='2'/><line x1='100' y1='20' x2='100' y2='160' stroke='green' stroke-width='2'/></svg>"
    },
    {
        "term": "Küme",
        "category": "Kümeler",
        "desc": "İyi tanımlanmış, birbirinden farklı nesneler topluluğudur.",
        "example": "Haftanın günleri bir küme oluşturur.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><ellipse cx='100' cy='90' rx='60' ry='40' fill='none' stroke='green' stroke-width='3'/></svg>"
    },
    {
        "term": "Mutlak Değer",
        "category": "Tam Sayılar",
        "desc": "Bir sayının sayı doğrusunda sıfıra olan uzaklığıdır.",
        "example": "|-5| = 5 ve |5| = 5'tir.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><text x='65' y='105' fill='green' font-size='28'>|-5| = 5</text></svg>"
    },
    {
        "term": "Ondalık Gösterim",
        "category": "Kesirler",
        "desc": "Paydası 10, 100, 1000 olan kesirlerin virgülle yazılış biçimidir.",
        "example": "0,5 veya 1,25 birer ondalık gösterimdir.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><text x='60' y='105' fill='green' font-size='28'>0,75</text></svg>"
    },
    {
        "term": "Oran",
        "category": "Oran ve Orantı",
        "desc": "İki çokluğun birbirine bölünerek karşılaştırılmasıdır.",
        "example": "3 elmanın 4 armuta oranı 3/4'tür.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><text x='85' y='105' fill='green' font-size='28'>a/b</text></svg>"
    },
    {
        "term": "Paralelkenar",
        "category": "Geometri",
        "desc": "Karşılıklı kenarları paralel olan dörtgendir.",
        "example": "Karşılıklı kenar uzunlukları eşittir.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><polygon points='50,130 150,130 130,50 30,50' fill='#22c55e'/></svg>"
    },
    {
        "term": "Sayı Doğrusu",
        "category": "Sayılar",
        "desc": "Sayıların belli aralıklarla sıralandığı düz çizgidir.",
        "example": "Üzerinde negatif ve pozitif sayılar yer alır.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><line x1='20' y1='90' x2='180' y2='90' stroke='green' stroke-width='3'/></svg>"
    },
    {
        "term": "Tam Sayılar",
        "category": "Tam Sayılar",
        "desc": "Negatif tam sayılar, sıfır ve pozitif tam sayıların birleşim kümesidir.",
        "example": "-3, -2, -1, 0, 1, 2, 3...",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><text x='40' y='105' fill='green' font-size='18'>-2, -1, 0, 1, 2</text></svg>"
    },
    {
        "term": "Üçgen",
        "category": "Geometri",
        "desc": "Üç kenarı ve üç köşesi olan kapalı geometrik şekildir.",
        "example": "Çeşitkenar, ikizkenar ve eşkenar çeşitleri vardır.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><polygon points='100,40 40,140 160,140' fill='#22c55e'/></svg>"
    },
    {
        "term": "Tümleyen Açı",
        "category": "Geometri",
        "desc": "Ölçüleri toplamı 90 derece olan iki açıdır.",
        "example": "30°'lik açının tümleyeni 60°'dir.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><line x1='50' y1='140' x2='150' y2='140' stroke='green' stroke-width='3'/><line x1='50' y1='140' x2='120' y2='70' stroke='green' stroke-width='3'/></svg>"
    },
    {
        "term": "Üslü İfade",
        "category": "Sayılar",
        "desc": "Bir sayının kendisiyle tekrarlı çarpımının kısa gösterimidir.",
        "example": "2 üssü 3 (2³) = 2 x 2 x 2 = 8'dir.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><text x='75' y='105' fill='green' font-size='32'>2³</text></svg>"
    },
    {
        "term": "Yarıçap",
        "category": "Geometri",
        "desc": "Çemberin merkezini üzerindeki bir noktaya birleştiren doğrudur.",
        "example": "Çapın uzunluğunun yarısına eşittir (r).",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><circle cx='100' cy='90' r='50' fill='none' stroke='green' stroke-width='3'/><line x1='100' y1='90' x2='150' y2='90' stroke='red' stroke-width='3'/></svg>"
    },
    {
        "term": "Yükseklik",
        "category": "Geometri",
        "desc": "Bir şeklin tepe noktasından tabanına inilen dik çizmedir.",
        "example": "Üçgende alan hesaplarken kullanılır.",
        "svg": "<svg width='100%' height='180' viewBox='0 0 200 200'><polygon points='100,40 40,140 160,140' fill='none' stroke='green' stroke-width='3'/><line x1='100' y1='40' x2='100' y2='140' stroke='red' stroke-width='2'/></svg>"
    }
]

# Mod Seçimi
col1, col2 = st.columns([2, 3])
with col1:
    mode = st.radio("Mod", ["Slayt Modu", "Sözlük Modu"], horizontal=True, label_visibility="collapsed")

st.divider()

if mode == "Slayt Modu":
    if "slide_idx" not in st.session_state:
        st.session_state.slide_idx = 0
        
    total = len(math_dictionary) + 1
    current = st.session_state.slide_idx + 1
    
    st.progress(current / total)
    
    if st.session_state.slide_idx == 0:
        st.subheader("6. Sınıf Türkçe Projesi")
        st.title("Türkçe Matematik Sözlüğü")
        st.write("USB olmadığından böyle bi sözlük hazırladım.")
        st.write("**Hazırlayan:** Yiğit ALPARSLAN (Ben)")
    else:
        item = math_dictionary[st.session_state.slide_idx - 1]
        c1, c2 = st.columns([3, 2])
        with c1:
            st.caption(item["category"])
            st.header(item["term"])
            st.write(item["desc"])
            st.info(f"Örnek: {item['example']}")
        with c2:
            st.markdown(item["svg"], unsafe_allow_html=True)
            
    def prev():
        if st.session_state.slide_idx > 0:
            st.session_state.slide_idx -= 1
    def next_s():
        if st.session_state.slide_idx < total - 1:
            st.session_state.slide_idx += 1
            
    b1, b2, b3 = st.columns([1, 2, 1])
    with b1:
        st.button("← Önceki", on_click=prev, use_container_width=True)
    with b2:
        st.write(f"Slayt {current} / {total}")
    with b3:
        st.button("Sonraki →", on_click=next_s, use_container_width=True)
        
else:
    st.title("Sözlük Modu")
    query = st.text_input("Terim ara:", "")
    st.divider()
    
    for item in math_dictionary:
        if query.lower() in item["term"].lower() or query.lower() in item["category"].lower():
            sc1, sc2 = st.columns([3, 1])
            with sc1:
                st.subheader(f"{item['term']} ({item['category']})")
                st.write(item['desc'])
                st.write(f"Örnek: {item['example']}")
            with sc2:
                st.markdown(item["svg"], unsafe_allow_html=True)
            st.divider()
