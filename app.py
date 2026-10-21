import streamlit as st

st.set_page_config(
    page_title="Türkçe Matematik Sözlüğü", page_icon=None, layout="wide"
)

# Vektörel / Minimalist Tasarım İçin Saf SVG İkon Tanımları
icon_book = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"/><path d="M6 6h12"/><path d="M6 10h12"/></svg>'
icon_search = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>'
icon_light = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>'

# A'dan Z'ye Tüm Harfleri Kapsayan Matematik Sözlüğü Veritabanı
math_dictionary = [
    {
        "term": "Açı",
        "category": "Geometri",
        "desc": (
            "Başlangıç noktaları ortak olan iki ışının oluşturduğu geometrik"
            " şekil."
        ),
        "example": "Dik açı 90 derece, dar açı 90 dereceden küçük açıdır.",
    },
    {
        "term": "Asal Sayı",
        "category": "Sayılar Kuramı",
        "desc": (
            "Sadece 1'e ve kendisine kalansız bölünebilen 1'den büyük doğal"
            " sayılar."
        ),
        "example": (
            "2, 3, 5, 7, 11, 13, 17... En küçük ve tek çift asal sayı 2'dir."
        ),
    },
    {
        "term": "Birim Çember",
        "category": "Trigonometri / Geometri",
        "desc": (
            "Merkezi analitik düzlemin orijininde (0,0) ve yarıçapı 1 birim olan"
            " çember."
        ),
        "example": (
            "Sinüs ve kosinüs değerlerinin geometrik olarak gösterildiği"
            " çemberdir."
        ),
    },
    {
        "term": "Çap",
        "category": "Geometri",
        "desc": (
            "Çemberin merkezinden geçen ve çemberi iki eşit parçaya bölen doğru"
            " parçası."
        ),
        "example": "Yarıçapı 5 cm olan bir çemberin çapı 10 cm'dir.",
    },
    {
        "term": "Derece",
        "category": "Geometri",
        "desc": (
            "Bir çember çevresinin 360'ta birine denk gelen açı ölçü birimi."
        ),
        "example": "Bir tam çember açısı 360 derecedir (360°).",
    },
    {
        "term": "Eğim",
        "category": "Analitik Geometri",
        "desc": (
            "Bir doğrunun x ekseniyle yaptığı pozitif yönlü açının tanjantı;"
            " dikey değişimin yatay değişime oranı."
        ),
        "example": "y = 3x + 2 doğrusunun eğimi m = 3'tür.",
    },
    {
        "term": "Fonksiyon",
        "category": "Analiz",
        "desc": (
            "Tanım kümesindeki her bir elemanı, değer kümesindeki yalnızca bir"
            " elemanla eşleyen bağıntı."
        ),
        "example": "f(x) = 2x + 1 girdi değerini 2 katının 1 fazlasına taşır.",
    },
    {
        "term": "Geometri",
        "category": "Temel Matematik",
        "desc": (
            "Nokta, doğru, düzlem, açı ve cisimlerin özelliklerini ve"
            " ilişkilerini inceleyen matematik dalı."
        ),
        "example": "Üçgen, kare, çember gibi şekiller geometrinin konusudur.",
    },
    {
        "term": "Geniş Açı",
        "category": "Geometri",
        "desc": "Ölçüsü 90 derece ile 180 derece arasında olan açı.",
        "example": "120 derecelik bir açı geniş açıdır.",
    },
    {
        "term": "Hipotenüs",
        "category": "Geometri",
        "desc": (
            "Bir dik üçgende 90 derecelik dik açının karşısında yer alan en"
            " uzun kenar."
        ),
        "example": "Pisagor bağıntısı: a² + b² = c² (c = hipotenüs).",
    },
    {
        "term": "Işın",
        "category": "Geometri",
        "desc": (
            "Başlangıç noktası sabit olup diğer yönde sonsuza kadar giden doğru"
            " parçası."
        ),
        "example": (
            "Güneş ışınları veya bir fenerin çıkardığı ışık hüzmesi gibi."
        ),
    },
    {
        "term": "İntegral",
        "category": "Analiz",
        "desc": (
            "Belirli bir aralıktaki eğrinin altında kalan alanı hesaplamaya"
            " yarayan işlem."
        ),
        "example": "Türevin ters işlemi olarak kabul edilir.",
    },
    {
        "term": "Kordinat Sistemi",
        "category": "Analitik Geometri",
        "desc": (
            "Bir noktanın konumunu belirlemek için dik kesişen iki sayı"
            " doğrusunun (x ve y eksenleri) oluşturduğu sistem."
        ),
        "example": "Orijin noktası (0,0) koordinatına sahiptir.",
    },
    {
        "term": "Limit",
        "category": "Analiz",
        "desc": (
            "Bir değişkenin bir değere yaklaşırken fonksiyonun ulaştığı veya"
            " yaklaştığı değer."
        ),
        "example": "x, 2'ye yaklaşırken (x + 3) fonksiyonunun limiti 5'tir.",
    },
    {
        "term": "Matris",
        "category": "Cebir",
        "desc": (
            "Sayıların satır ve sütunlar şeklinde dikdörtgen tablo halinde"
            " dizilmesi."
        ),
        "example": (
            "2x2 boyutundaki bir matris 2 satır ve 2 sütundan oluşur."
        ),
    },
    {
        "term": "Nokta",
        "category": "Geometri",
        "desc": (
            "Boyutu, uzunluğu, genişliği ve alanı olmayan, sadece konum belirten"
            " temel kavram."
        ),
        "example": "Büyük harflerle gösterilir (A noktası, B noktası).",
    },
    {
        "term": "Orijin",
        "category": "Analitik Geometri",
        "desc": "Koordinat eksenlerinin kesiştiği (0,0) başlangıç noktası.",
        "example": "Sayı doğrusunda veya dik koordinat sisteminde 0 noktasıdır.",
    },
    {
        "term": "Öklit Bağıntısı",
        "category": "Geometri",
        "desc": (
            "Dik üçgende dik açıdan hipotenüse indirilen dikmenin kenarlar"
            " arasındaki ilişkisi (h² = p · k)."
        ),
        "example": (
            "Hipotenüse ait yüksekliğin karesi, ayırdığı parçaların çarpımına"
            " eşittir."
        ),
    },
    {
        "term": "Polinom",
        "category": "Cebir",
        "desc": (
            "Katsayılar ve değişkenlerin üslerinin doğal sayı olduğu cebirsel"
            " ifadeler."
        ),
        "example": "P(x) = 3x² + 2x - 5 bir polinomdur.",
    },
    {
        "term": "Rasyonel Sayılar",
        "category": "Sayılar Kuramı",
        "desc": (
            "a ve b tam sayı (b ≠ 0) olmak üzere a/b şeklinde yazılabilen"
            " sayılar kümesi (Q)."
        ),
        "example": "1/2, 3/4, 5, -2 birer rasyonel sayıdır.",
    },
    {
        "term": "Sabit Terim",
        "category": "Cebir",
        "desc": (
            "Bir cebirsel ifadede değişken içermeyen, değeri değişmeyen sayı."
        ),
        "example": "2x + 5 ifadesinde '5' sabit terimdir.",
    },
    {
        "term": "Türev",
        "category": "Analiz",
        "desc": (
            "Bir fonksiyonun bir noktadaki anlık değişim oranını veren işlem."
        ),
        "example": "Hız, konumun zamana göre türevidir.",
    },
    {
        "term": "Uzaklık",
        "category": "Geometri",
        "desc": "İki nokta arasındaki en kısa doğru parçasının uzunluğu.",
        "example": "A ve B noktaları arasındaki mutlak mesafe.",
    },
    {
        "term": "Üs (Kuvvet)",
        "category": "Temel Matematik",
        "desc": (
            "Bir sayının kendisiyle kaç kez çarpılacağını gösteren küçük sayı."
        ),
        "example": "2³ = 2 × 2 × 2 = 8 ifadesinde '3' üştür.",
    },
    {
        "term": "Vektör",
        "category": "Geometri / Fizik",
        "desc": "Yönü, doğrultusu ve büyüklüğü olan doğru parçası.",
        "example": "Kuvvet ve hız vektörel büyüklüklerdir.",
    },
    {
        "term": "Yarıçap",
        "category": "Geometri",
        "desc": (
            "Çemberin merkezini çember üzerindeki herhangi bir noktaya birleştiren"
            " doğru parçası ('r')."
        ),
        "example": "Çapın yarısı uzunluktadır.",
    },
    {
        "term": "Zaman Sırası (Dizi)",
        "category": "Analiz",
        "desc": (
            "Sayılardan oluşan ve belirli bir kurala göre sıralanan elemanlar"
            " kümesi."
        ),
        "example": "2, 4, 6, 8... çift sayılar dizisidir.",
    },
]

# Yan Menü (Sidebar) - Gezinme
st.sidebar.markdown(
    f"<h3>{icon_book} Sözlük Menüsü</h3>", unsafe_allow_html=True
)
mode = st.sidebar.radio("Görünüm Modu:", ["Slayt Modu", "A'dan Z'ye Sözlük Arama"])

st.sidebar.divider()
st.sidebar.write("Hazırlayan: **Yiğit**")

# MOD 1: SLAYT SUNUM MODU
if mode == "Slayt Modu":
  if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0

  total = len(math_dictionary)

  col_nav1, col_nav2, col_nav3 = st.columns([1, 2, 1])
  with col_nav1:
    if st.button("Önceki Terim"):
      if st.session_state.slide_idx > 0:
        st.session_state.slide_idx -= 1
  with col_nav2:
    st.markdown(
        f"<h4 style='text-align: center;'>Terim"
        f" {st.session_state.slide_idx + 1} / {total}</h4>",
        unsafe_allow_html=True,
    )
  with col_nav3:
    if st.button("Sonraki Terim"):
      if st.session_state.slide_idx < total - 1:
        st.session_state.slide_idx += 1

  st.progress((st.session_state.slide_idx + 1) / total)

  # Aktif Terim Kartı
  item = math_dictionary[st.session_state.slide_idx]

  st.divider()
  st.markdown(f"<h2>{icon_book} {item['term']}</h2>", unsafe_allow_html=True)
  st.caption(f"Kategori: **{item['category']}**")

  st.info(f"**Tanım:** {item['desc']}")

  with st.expander("Örnek ve Kullanım", expanded=True):
    st.markdown(f"{icon_light} {item['example']}", unsafe_allow_html=True)

# MOD 2: ARAMA MODU
else:
  st.markdown(
      f"<h1>{icon_search} Türkçe Matematik Sözlüğü - Arama</h1>",
      unsafe_allow_html=True,
  )
  search = st.text_input("Aramak istediğiniz terimi veya harfi yazın:", "")

  results = [
      item
      for item in math_dictionary
      if search.lower() in item["term"].lower()
      or search.lower() in item["category"].lower()
  ]

  if results:
    for item in results:
      col_a, col_b = st.columns([1, 3])
      with col_a:
        st.metric(label="Kategori", value=item["category"])
      with col_b:
        st.subheader(item["term"])
        st.write(item["desc"])
        st.caption(f"Örnek: {item['example']}")
      st.divider()
  else:
    st.warning("Aradığınız kriterlere uygun terim bulunamadı.")
