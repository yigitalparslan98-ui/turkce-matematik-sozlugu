import streamlit as st

st.set_page_config(
    page_title="6. Sınıf Türkçe Matematik Sözlüğü", page_icon="📐", layout="wide"
)

# Ferah, göz yormayan beyaz ve yeşil tonlarında minimalist CSS
st.markdown(
    """
    <style>
    html, body, [class*="css"], div, p, span, h1, h2, h3, h4, h5, h6, button {
        font-family: Arial, sans-serif !important;
    }
    .stApp {
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }
    .slide-card {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        border-left: 6px solid #16a34a;
        border-radius: 6px !important;
        padding: 30px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .slide-category {
        color: #16a34a;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 8px;
        font-weight: 700;
    }
    .slide-title {
        color: #0f172a;
        font-size: 36px;
        font-weight: 800;
        margin-bottom: 16px;
    }
    .slide-desc {
        color: #334155;
        font-size: 18px;
        line-height: 1.5;
        margin-bottom: 20px;
    }
    .slide-example {
        background-color: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-left: 4px solid #16a34a;
        padding: 14px 18px;
        font-size: 15px;
        color: #166534;
        border-radius: 4px;
    }
    .stButton > button {
        background-color: #ffffff !important;
        color: #166534 !important;
        border-radius: 4px !important;
        border: 1px solid #16a34a !important;
        font-weight: bold !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
    }
    .stButton > button:hover {
        background-color: #f0fdf4 !important;
        color: #14532d !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 6. Sınıf Müfredatına Uygun Matematik Sözlüğü Veritabanı ve SVG Çizimleri
math_dictionary = [
    {
        "term": "Açı",
        "category": "Geometri",
        "desc": "Başlangıç noktaları aynı olan iki ışının arasında oluşan açıklığa açı denir.",
        "example": "Dar açı, dik açı (90°) ve geniş açı çeşitleri vardır.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <line x1='30' y1='160' x2='170' y2='160' stroke='#0f172a' stroke-width='3'/>
            <line x1='30' y1='160' x2='140' y2='50' stroke='#16a34a' stroke-width='3'/>
            <path d='M 70 160 A 40 40 0 0 0 58 132' stroke='#2563eb' stroke-width='2' fill='none'/>
            <text x='75' y='145' fill='#2563eb' font-size='16' font-weight='bold'>a°</text>
        </svg>"""
    },
    {
        "term": "Asal Sayı",
        "category": "Sayılarda İşlemler",
        "desc": "Sadece 1'e ve kendisine bölünebilen, 1'den büyük doğal sayılardır.",
        "example": "2, 3, 5, 7, 11, 13... En küçük ve tek çift asal sayı 2'dir.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <circle cx='50' cy='70' r='20' fill='#f0fdf4' stroke='#16a34a' stroke-width='2'/>
            <text x='44' y='76' fill='#166534' font-size='18' font-weight='bold'>2</text>
            <circle cx='100' cy='70' r='20' fill='#f0fdf4' stroke='#16a34a' stroke-width='2'/>
            <text x='94' y='76' fill='#166534' font-size='18' font-weight='bold'>3</text>
            <circle cx='150' cy='70' r='20' fill='#f0fdf4' stroke='#16a34a' stroke-width='2'/>
            <text x='144' y='76' fill='#166534' font-size='18' font-weight='bold'>5</text>
            <circle cx='75' cy='130' r='20' fill='#f0fdf4' stroke='#16a34a' stroke-width='2'/>
            <text x='69' y='136' fill='#166534' font-size='18' font-weight='bold'>7</text>
            <circle cx='125' cy='130' r='20' fill='#f0fdf4' stroke='#16a34a' stroke-width='2'/>
            <text x='115' y='136' fill='#166534' font-size='18' font-weight='bold'>11</text>
        </svg>"""
    },
    {
        "term": "Açıklık",
        "category": "Veri İşleme",
        "desc": "Bir veri grubundaki en büyük değer ile en küçük değer arasındaki farktır.",
        "example": "5, 12, 20 sayılarında açıklık: 20 - 5 = 15'tir.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <rect x='30' y='120' width='30' height='40' fill='#bbf7d0' stroke='#16a34a' stroke-width='2'/>
            <rect x='80' y='80' width='30' height='80' fill='#bbf7d0' stroke='#16a34a' stroke-width='2'/>
            <rect x='130' y='40' width='30' height='120' fill='#16a34a'/>
            <line x1='30' y1='30' x2='160' y2='30' stroke='#dc2626' stroke-width='2' stroke-dasharray='4'/>
            <text x='60' y='25' fill='#dc2626' font-size='13' font-weight='bold'>En Büyük - En Küçük</text>
        </svg>"""
    },
    {
        "term": "Bölünebilme Kuralları",
        "category": "Sayılarda İşlemler",
        "desc": "Bir sayının başka bir sayıya kalansız bölünüp bölünmediğini anlama yöntemleridir.",
        "example": "Çift sayılar 2'ye, rakamları toplamı 3'ün katı olanlar 3'e tam bölünür.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <rect x='40' y='50' width='120' height='100' fill='#f0fdf4' stroke='#16a34a' stroke-width='2'/>
            <text x='65' y='90' fill='#0f172a' font-size='22' font-weight='bold'>240 ÷ 3</text>
            <text x='65' y='125' fill='#16a34a' font-size='16' font-weight='bold'>Kalan = 0</text>
        </svg>"""
    },
    {
        "term": "Çarpan (Bölen)",
        "category": "Sayılarda İşlemler",
        "desc": "Bir doğal sayıyı kalansız bölen sayılara o sayının çarpanları denir.",
        "example": "12'nin çarpanları: 1, 2, 3, 4, 6 ve 12'dir.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <text x='85' y='60' fill='#0f172a' font-size='24' font-weight='bold'>12</text>
            <line x1='75' y1='80' x2='45' y2='130' stroke='#16a34a' stroke-width='2'/>
            <line x1='115' y1='80' x2='145' y2='130' stroke='#16a34a' stroke-width='2'/>
            <text x='35' y='155' fill='#16a34a' font-size='20' font-weight='bold'>3</text>
            <text x='140' y='155' fill='#16a34a' font-size='20' font-weight='bold'>4</text>
        </svg>"""
    },
    {
        "term": "Çember",
        "category": "Geometri",
        "desc": "Düzlemde sabit bir noktaya eşit uzaklıktaki noktaların oluşturduğu kapalı eğri.",
        "example": "Çemberin içi boşken, dairenin içi doludur (örneğin simit bir çemberdir).",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <circle cx='100' cy='100' r='60' fill='none' stroke='#16a34a' stroke-width='3'/>
            <circle cx='100' cy='100' r='4' fill='#0f172a'/>
            <line x1='100' y1='100' x2='160' y2='100' stroke='#2563eb' stroke-width='2'/>
            <text x='125' y='95' fill='#2563eb' font-size='14' font-weight='bold'>r</text>
        </svg>"""
    },
    {
        "term": "Dik Açı",
        "category": "Geometri",
        "desc": "Ölçüsü tam 90 derece olan açıdır.",
        "example": "Kare ve dikdörtgenin her bir iç açısı dik açıdır.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <line x1='50' y1='150' x2='150' y2='150' stroke='#0f172a' stroke-width='3'/>
            <line x1='50' y1='150' x2='50' y2='50' stroke='#0f172a' stroke-width='3'/>
            <rect x='50' y='130' width='20' height='20' fill='none' stroke='#16a34a' stroke-width='2'/>
            <circle cx='60' cy='140' r='2' fill='#16a34a'/>
            <text x='85' y='110' fill='#16a34a' font-size='18' font-weight='bold'>90°</text>
        </svg>"""
    },
    {
        "term": "Hacim",
        "category": "Ölçme",
        "desc": "Üç boyutlu bir cismin uzayda kapladığı alana hacim denir.",
        "example": "Prizmanın hacmi = Taban Alanı x Yükseklik kuralı ile bulunur.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <rect x='50' y='80' width='70' height='70' fill='#f0fdf4' stroke='#16a34a' stroke-width='2'/>
            <path d='M 50 80 L 85 45 L 155 45 L 120 80' fill='#bbf7d0' stroke='#16a34a' stroke-width='2'/>
            <path d='M 120 80 L 155 45 L 155 115 L 120 150' fill='#86efac' stroke='#16a34a' stroke-width='2'/>
        </svg>"""
    },
    {
        "term": "İki Kümenin Birleşimi",
        "category": "Kümeler",
        "desc": "İki veya daha fazla kümenin bütün elemanlarının oluşturduğu yeni kümedir (∪ sembolü).",
        "example": "A = {1, 2} ve B = {2, 3} ise A ∪ B = {1, 2, 3}'tür.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <circle cx='75' cy='100' r='45' fill='#bbf7d0' fill-opacity='0.7' stroke='#16a34a' stroke-width='2'/>
            <circle cx='125' cy='100' r='45' fill='#bbf7d0' fill-opacity='0.7' stroke='#16a34a' stroke-width='2'/>
            <text x='55' y='105' fill='#0f172a' font-size='16' font-weight='bold'>A</text>
            <text x='135' y='105' fill='#0f172a' font-size='16' font-weight='bold'>B</text>
        </svg>"""
    },
    {
        "term": "İki Kümenin Kesişimi",
        "category": "Kümeler",
        "desc": "İki kümedeki ortak elemanların oluşturduğu kümedir (∩ sembolü).",
        "example": "A = {a, b} ve B = {b, c} ise A ∩ B = {b}'dir.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <circle cx='75' cy='100' r='45' fill='none' stroke='#0f172a' stroke-width='2'/>
            <circle cx='125' cy='100' r='45' fill='none' stroke='#0f172a' stroke-width='2'/>
            <path d='M 100 60 A 45 45 0 0 1 100 140 A 45 45 0 0 1 100 60' fill='#16a34a'/>
        </svg>"""
    },
    {
        "term": "Kesir",
        "category": "Kesirler",
        "desc": "Bir bütünün eş parçalarını gösteren ifadedir (Pay / Payda).",
        "example": "3/4 kesri, bir bütünün 4 eşit parçaya bölünüp 3'ünün alındığını gösterir.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <rect x='40' y='70' width='120' height='60' fill='none' stroke='#0f172a' stroke-width='2'/>
            <rect x='40' y='70' width='30' height='60' fill='#16a34a'/>
            <rect x='70' y='70' width='30' height='60' fill='#16a34a'/>
            <rect x='100' y='70' width='30' height='60' fill='#16a34a'/>
            <line x1='70' y1='70' x2='70' y2='130' stroke='#0f172a' stroke-width='2'/>
            <line x1='100' y1='70' x2='100' y2='130' stroke='#0f172a' stroke-width='2'/>
            <line x1='130' y1='70' x2='130' y2='130' stroke='#0f172a' stroke-width='2'/>
            <text x='88' y='165' fill='#16a34a' font-size='20' font-weight='bold'>3 / 4</text>
        </svg>"""
    },
    {
        "term": "Muttasıl (Komşu) Açılar",
        "category": "Geometri",
        "desc": "Başlangıç noktaları ve birer kolları ortak olan açılardır.",
        "example": "Yan yana duran ve bir ışını paylaşan iki açı komşudur.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <line x1='40' y1='150' x2='160' y2='150' stroke='#0f172a' stroke-width='3'/>
            <line x1='40' y1='150' x2='100' y2='40' stroke='#16a34a' stroke-width='3'/>
            <line x1='40' y1='150' x2='150' y2='80' stroke='#2563eb' stroke-width='3'/>
        </svg>"""
    },
    {
        "term": "Ondalık Gösterim",
        "category": "Kesirler ve Ondalık",
        "desc": "Paydası 10, 100, 1000 olan kesirlerin virgül kullanılarak yazılışıdır.",
        "example": "5/10 = 0,5 veya 25/100 = 0,25 şeklinde ifade edilir.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <rect x='40' y='60' width='120' height='80' fill='#f0fdf4' stroke='#16a34a' stroke-width='2'/>
            <text x='58' y='110' fill='#0f172a' font-size='32' font-weight='bold'>0,75</text>
        </svg>"""
    },
    {
        "term": "Oran",
        "category": "Oran ve Orantı",
        "desc": "İki çokluğun birbirine bölünerek karşılaştırılmasıdır.",
        "example": "Ali'nin yaşının Veli'nin yaşına oranı: 12 / 15 = 4 / 5'tir.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <text x='85' y='85' fill='#16a34a' font-size='28' font-weight='bold'>a</text>
            <line x1='70' y1='100' x2='130' y2='100' stroke='#0f172a' stroke-width='3'/>
            <text x='85' y='135' fill='#2563eb' font-size='28' font-weight='bold'>b</text>
        </svg>"""
    },
    {
        "term": "Paralelkenar",
        "category": "Geometri",
        "desc": "Karşılıklı kenarları birbirine paralel ve eşit uzunlukta olan dörtgendir.",
        "example": "Paralelkenarın alanı = Taban uzunluğu x O tabana ait yükseklik.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <polygon points='60,140 160,140 130,60 30,60' fill='#f0fdf4' stroke='#16a34a' stroke-width='3'/>
            <line x1='30' y1='60' x2='30' y2='140' stroke='#dc2626' stroke-width='2' stroke-dasharray='4'/>
            <text x='15' y='105' fill='#dc2626' font-size='14' font-weight='bold'>h</text>
        </svg>"""
    },
    {
        "term": "Tümleyen Açılar",
        "category": "Geometri",
        "desc": "Ölçüleri toplamı 90 derece olan iki açıya tümleyen açılar denir.",
        "example": "30°'lik açının tümleyeni 60°'dir (30 + 60 = 90).",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <path d='M 50 150 L 150 150 L 50 50 Z' fill='#f0fdf4' stroke='#0f172a' stroke-width='2'/>
            <line x1='50' y1='150' x2='120' y2='80' stroke='#16a34a' stroke-width='2.5'/>
            <text x='70' y='135' fill='#16a34a' font-size='14' font-weight='bold'>30°</text>
            <text x='60' y='100' fill='#2563eb' font-size='14' font-weight='bold'>60°</text>
        </svg>"""
    },
    {
        "term": "Üslü İfade",
        "category": "Sayılarda İşlemler",
        "desc": "Bir sayının kendisi ile tekrarlı çarpımının kısa yoldan gösterimidir.",
        "example": "5³ = 5 x 5 x 5 = 125 (5 üssü 3 okunur).",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <text x='75' y='120' fill='#0f172a' font-size='48' font-weight='bold'>a</text>
            <text x='105' y='80' fill='#16a34a' font-size='28' font-weight='bold'>n</text>
        </svg>"""
    },
    {
        "term": "Veri",
        "category": "Veri İşleme",
        "desc": "Bir konu hakkında bilgi toplamak amacıyla elde edilen değerlerdir.",
        "example": "Sınıftaki öğrencilerin boy uzunlukları birer veridir.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <rect x='40' y='110' width='25' height='50' fill='#16a34a'/>
            <rect x='85' y='70' width='25' height='90' fill='#16a34a'/>
            <rect x='130' y='40' width='25' height='120' fill='#16a34a'/>
        </svg>"""
    },
    {
        "term": "Yükseklik",
        "category": "Geometri",
        "desc": "Bir geometrik şeklin tepe noktasından tabanına indirilen dik doğru parçasıdır.",
        "example": "Üçgenin alanı = (Taban x Yükseklik) / 2 formülüyle bulunur.",
        "svg": """<svg width='100%' height='220' viewBox='0 0 200 200' style='background:#ffffff; border:1px solid #cbd5e1; border-radius:6px;'>
            <polygon points='30,150 170,150 100,50' fill='none' stroke='#0f172a' stroke-width='2'/>
            <line x1='100' y1='50' x2='100' y2='150' stroke='#dc2626' stroke-width='2.5' stroke-dasharray='4'/>
            <text x='105' y='100' fill='#dc2626' font-size='16' font-weight='bold'>h</text>
        </svg>"""
    }
]

# Mod Seçimi (Sol Üst)
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
    st.markdown(
        """
        <div class="slide-card">
            <div class="slide-category">6. Sınıf Matematik Projesi</div>
            <div class="slide-title">Türkçe Matematik Sözlüğü</div>
            <div class="slide-desc">USB olmadığından böyle bir sözlük hazırladım.</div>
            <div class="slide-example"><b>Hazırlayan:</b> Yiğit</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
  else:
    item = math_dictionary[st.session_state.slide_idx - 1]
    col_text, col_img = st.columns([3, 2])
    with col_text:
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
    with col_img:
      st.markdown(
          f"<div style='margin-top: 10px;'>{item['svg']}</div>",
          unsafe_allow_html=True,
      )

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
        f"<h3 style='text-align: center; color: #0f172a;'>Slayt"
        f" {current_slide} / {total}</h3>",
        unsafe_allow_html=True,
    )
  with col_next:
    st.button("Sonraki →", on_click=next_slide, use_container_width=True)

else:
  st.markdown("<h1>Sözlük Modu (A-Z Tüm Terimler)</h1>", unsafe_allow_html=True)
  search_term = st.text_input("Aramak istediğin terimi yaz:", "")
  st.divider()

  for item in math_dictionary:
    if (
        search_term.lower() in item["term"].lower()
        or search_term.lower() in item["category"].lower()
    ):
      col_sz1, col_sz2 = st.columns([3, 1])
      with col_sz1:
        st.markdown(f"## {item['term']} _({item['category']})_")
        st.markdown(f"### {item['desc']}")
        st.markdown(f"**Örnek:** {item['example']}")
      with col_sz2:
        st.markdown(item["svg"], unsafe_allow_html=True)
      st.divider()
