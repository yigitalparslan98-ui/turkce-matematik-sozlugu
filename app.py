import streamlit as st

st.set_page_config(
    page_title="Türkçe Matematik Sözlüğü", page_icon=None, layout="centered"
)

# Siyah Bazlı, Keskin ve Minimalist Slayt Tasarımı (Dark Mode / Brutalist)
st.markdown(
    """
    <style>
    html, body, [class*="css"], div, p, span, h1, h2, h3, h4, h5, h6, button {
        font-family: Arial, sans-serif !important;
    }
    .stApp {
        background-color: #09090b !important;
        color: #fafafa !important;
    }
    /* Keskin köşeli koyu slayt kartı */
    .slide-card {
        background-color: #18181b;
        border: 2px solid #fafafa;
        border-radius: 0px !important;
        padding: 40px;
        box-shadow: 6px 6px 0px #fafafa;
        margin-top: 20px;
        margin-bottom: 20px;
        min-height: 380px;
    }
    .slide-category {
        color: #a1a1aa;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 12px;
        font-weight: 700;
    }
    .slide-title {
        color: #ffffff;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 24px;
        letter-spacing: -0.5px;
    }
    .slide-desc {
        color: #f4f4f5;
        font-size: 20px;
        line-height: 1.6;
        margin-bottom: 28px;
    }
    /* Keskin köşeli koyu örnek kutusu */
    .slide-example {
        background-color: #27272a;
        border: 1px solid #fafafa;
        border-left: 6px solid #fafafa;
        border-radius: 0px !important;
        padding: 16px 20px;
        font-size: 16px;
        color: #f4f4f5;
    }
    /* Butonları köşeli ve koyu tema uyumlu yapma */
    .stButton > button {
        background-color: #18181b !important;
        color: #fafafa !important;
        border-radius: 0px !important;
        border: 2px solid #fafafa !important;
        font-weight: bold !important;
        box-shadow: 3px 3px 0px #fafafa !important;
    }
    .stButton > button:hover {
        background-color: #27272a !important;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
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

# Slayt İndeksi Yönetimi (1 kapak + 27 terim = 28 toplam slayt)
if "slide_idx" not in st.session_state:
  st.session_state.slide_idx = 0

total = len(math_dictionary) + 1
current_slide = st.session_state.slide_idx + 1

# Üst Bilgi / İlerleme Barı
st.progress(current_slide / total)

# SLAYT İÇERİĞİ
if st.session_state.slide_idx == 0:
  # 1. Slayt: Kapak Slaytı
  st.markdown(
      """
    <div class="slide-card">
        <div class="slide-category">Matematik Projesi</div>
        <div class="slide-title">Türkçe Matematik Sözlüğü</div>
        <div class="slide-desc">USB olmadığından böyle bir sözlük hazırladım.</div>
        <div class="slide-example"><b>Hazırlayan:</b> Yiğit</div>
    </div>
    """,
      unsafe_allow_html=True,
  )
else:
  # Diğer Slaytlar: Terimler
  item = math_dictionary[st.session_state.slide_idx - 1]
  st.markdown(
      f"""
    <div class="slide-card">
        <div class="slide-category">{item['category']}</div>
        <div class="slide-title">{item['term']}</div>
        <div class="slide-desc">{item['desc']}</div>
        <div class="slide-example"><b>Örnek:</b> {item['example']}</div>
    </div>
    """,
      unsafe_allow_html=True,
  )


# Alt Kontrol Butonları
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
      f"<p style='text-align: center; color: #fafafa; font-weight: bold;"
      f" font-size: 14px; margin-top: 10px;'>SLAYT {current_slide} /"
      f" {total}</p>",
      unsafe_allow_html=True,
  )

with col_next:
  st.button("Sonraki →", on_click=next_slide, use_container_width=True)
