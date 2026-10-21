import streamlit as st

st.set_page_config(
    page_title="Türkçe Matematik Sözlüğü", page_icon="📐", layout="centered"
)

# Matematik Sözlüğü Veritabanı (A-Z)
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
            "2, 3, 5, 7, 11, 13... En küçük ve tek çift asal sayı 2'dir."
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
            "Sinüs ve kosinüs değerlerinin geometrik gösteriminde kullanılır."
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
        "term": "Koordinat Sistemi",
        "category": "Analitik Geometri",
        "desc": (
            "Bir noktanın konumunu belirlemek için dik kesişen iki sayı"
            " doğrusunun oluşturduğu sistem."
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
        "example": "Yüksekliğin karesi, ayırdığı parçaların çarpımına eşittir.",
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

# Sol üst köşede mod seçimi
col_mode1, col_mode2 = st.columns([2, 3])
with col_mode1:
  mode = st.radio(
      "Mod Seçimi",
      ["Slayt Modu", "Sözlük Modu"],
      horizontal=True,
      label_visibility="collapsed",
  )

st.divider()

if mode == "Slayt Modu":
  if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0

  total = len(math_dictionary) + 1
  current_slide = st.session_state.slide_idx + 1

  st.progress(current_slide / total)

  if st.session_state.slide_idx == 0:
    st.markdown("# Türkçe Matematik Sözlüğü")
    st.markdown("## USB olmadığından böyle bir sözlük hazırladım.")
    st.markdown("### Hazırlayan: Yiğit")
  else:
    item = math_dictionary[st.session_state.slide_idx - 1]
    st.markdown(f"### Kategori: {item['category']}")
    st.markdown(f"# {item['term']}")
    st.markdown(f"## {item['desc']}")
    st.markdown(f"### **Örnek:** {item['example']}")

  def prev_slide():
    if st.session_state.slide_idx > 0:
      st.session_state.slide_idx -= 1

  def next_slide():
    if st.session_state.slide_idx < total - 1:
      st.session_state.slide_idx += 1

  col_prev, col_counter, col_next = st.columns([1, 2, 1])
  with col_prev:
    st.button("← Önceki", on_click=prev_slide, use_container_width=True)
  with col_counter:
    st.markdown(
        f"<h3 style='text-align: center;'>Slayt {current_slide} / {total}</h3>",
        unsafe_allow_html=True,
    )
  with col_next:
    st.button("Sonraki →", on_click=next_slide, use_container_width=True)

else:
  st.markdown("# Sözlük Modu (A-Z Tüm Terimler)")
  search_term = st.text_input("Aramak istediğin terimi yaz:", "")

  st.divider()

  for item in math_dictionary:
    if (
        search_term.lower() in item["term"].lower()
        or search_term.lower() in item["category"].lower()
    ):
      st.markdown(f"## {item['term']} _({item['category']})_")
      st.markdown(f"### {item['desc']}")
      st.markdown(f"**Örnek:** {item['example']}")
      st.divider()
