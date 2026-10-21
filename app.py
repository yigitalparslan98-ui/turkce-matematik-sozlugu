import streamlit as st

st.set_page_config(
    page_title="Türkçe Matematik Sözlüğü", page_icon="📐", layout="wide"
)

# Ferah, göz yormayan beyaz ve yeşil tonlarında minimalist CSS stilleri
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

# Matematik Sözlüğü Veritabanı (A-Z) ve Uyumlu Vektörel Çizimler
math_dictionary = [
    {
        "term": "Açı",
        "category": "Geometri",
        "desc": (
            "Başlangıç noktaları ortak olan iki ışının oluşturduğu geometrik"
            " şekil."
        ),
        "example": "Dik açı 90 derece, dar açı 90 dereceden küçük açıdır.",
        "svg": """
            <svg width="100%" height="220" viewBox="0 0 200 200" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px;">
                <line x1="40" y1="160" x2="160" y2="160" stroke="#0f172a" stroke-width="2.5"/>
                <line x1="40" y1="160" x2="140" y2="60" stroke="#16a34a" stroke-width="2.5"/>
                <path d="M 70 160 A 30 30 0 0 0 63 133" stroke="#2563eb" stroke-width="2" fill="none"/>
                <text x="80" y="145" fill="#2563eb" font-size="14" font-weight="bold">α</text>
                <circle cx="40" cy="160" r="4" fill="#0f172a"/>
            </svg>
        """,
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
        "svg": """
            <svg width="100%" height="220" viewBox="0 0 200 200" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px;">
                <circle cx="50" cy="70" r="18" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
                <text x="44" y="75" fill="#166534" font-size="15" font-weight="bold">2</text>
                <circle cx="100" cy="70" r="18" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
                <text x="94" y="75" fill="#166534" font-size="15" font-weight="bold">3</text>
                <circle cx="150" cy="70" r="18" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
                <text x="144" y="75" fill="#166534" font-size="15" font-weight="bold">5</text>
                <circle cx="75" cy="130" r="18" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
                <text x="69" y="135" fill="#166534" font-size="15" font-weight="bold">7</text>
                <circle cx="125" cy="130" r="18" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
                <text x="113" y="135" fill="#166534" font-size="15" font-weight="bold">11</text>
            </svg>
        """,
    },
    {
        "term": "Birim Çember",
        "category": "Trigonometri",
        "desc": (
            "Merkezi analitik düzlemin orijininde (0,0) ve yarıçapı 1 birim olan"
            " çember."
        ),
        "example": (
            "Sinüs ve kosinüs değerlerinin geometrik gösteriminde kullanılır."
        ),
        "svg": """
            <svg width="100%" height="220" viewBox="0 0 200 200" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px;">
                <line x1="20" y1="100" x2="180" y2="100" stroke="#cbd5e1" stroke-width="1.5"/>
                <line x1="100" y1="20" x2="100" y2="180" stroke="#cbd5e1" stroke-width="1.5"/>
                <circle cx="100" cy="100" r="60" fill="none" stroke="#16a34a" stroke-width="2"/>
                <line x1="100" y1="100" x2="142" y2="58" stroke="#2563eb" stroke-width="2"/>
                <circle cx="142" cy="58" r="3" fill="#2563eb"/>
            </svg>
        """,
    },
    {
        "term": "Çap",
        "category": "Geometri",
        "desc": (
            "Çemberin merkezinden geçen ve çemberi iki eşit parçaya bölen doğru"
            " parçası."
        ),
        "example": "Yarıçapı 5 cm olan bir çemberin çapı 10 cm'dir.",
        "svg": """
            <svg width="100%" height="220" viewBox="0 0 200 200" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px;">
                <circle cx="100" cy="100" r="60" fill="none" stroke="#0f172a" stroke-width="2"/>
                <line x1="40" y1="100" x2="160" y2="100" stroke="#dc2626" stroke-width="2.5"/>
                <circle cx="100" cy="100" r="4" fill="#0f172a"/>
            </svg>
        """,
    },
    {
        "term": "Fonksiyon",
        "category": "Analiz",
        "desc": (
            "Tanım kümesindeki her bir elemanı, değer kümesindeki yalnızca bir"
            " elemanla eşleyen bağıntı."
        ),
        "example": "f(x) = 2x + 1 girdi değerini 2 katının 1 fazlasına taşır.",
        "svg": """
            <svg width="100%" height="220" viewBox="0 0 220 200" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px;">
                <ellipse cx="60" cy="100" rx="35" ry="60" fill="none" stroke="#16a34a" stroke-width="2"/>
                <ellipse cx="160" cy="100" rx="35" ry="60" fill="none" stroke="#2563eb" stroke-width="2"/>
                <text x="45" y="80" fill="#0f172a" font-size="14">x₁</text>
                <text x="45" y="120" fill="#0f172a" font-size="14">x₂</text>
                <text x="145" y="80" fill="#0f172a" font-size="14">y₁</text>
                <text x="145" y="120" fill="#0f172a" font-size="14">y₂</text>
                <path d="M 75 80 Q 110 50 145 80" fill="none" stroke="#d97706" stroke-width="2"/>
                <text x="105" y="60" fill="#d97706" font-size="12" font-weight="bold">f</text>
            </svg>
        """,
    },
]

# Diğer terimler için temiz ve şık varsayılan vektör şeması
default_svg = """
    <svg width="100%" height="220" viewBox="0 0 200 200" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px;">
        <rect x="40" y="40" width="120" height="120" fill="none" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4,4"/>
        <line x1="40" y1="40" x2="160" y2="160" stroke="#16a34a" stroke-width="2"/>
        <line x1="160" y1="40" x2="40" y2="160" stroke="#16a34a" stroke-width="2"/>
        <circle cx="100" cy="100" r="8" fill="#2563eb"/>
    </svg>
"""

full_terms = [
    "Açı",
    "Asal Sayı",
    "Birim Çember",
    "Çap",
    "Derece",
    "Eğim",
    "Fonksiyon",
    "Geometri",
    "Geniş Açı",
    "Hipotenüs",
    "Işın",
    "İntegral",
    "Koordinat Sistemi",
    "Limit",
    "Matris",
    "Nokta",
    "Orijin",
    "Öklit Bağıntısı",
    "Polinom",
    "Rasyonel Sayılar",
    "Sabit Terim",
    "Türev",
    "Uzaklık",
    "Üs (Kuvvet)",
    "Vektör",
    "Yarıçap",
    "Zaman Sırası (Dizi)",
]

existing_terms = {item["term"] for item in math_dictionary}
for t in full_terms:
  if t not in existing_terms:
    math_dictionary.append({
        "term": t,
        "category": "Matematik",
        "desc": f"{t} kavramı, matematiksel analiz ve hesaplamalarda temel bir rol oynar.",
        "example": f"{t} ile ilgili temel bir formül veya uygulama örneği.",
        "svg": default_svg,
    })

# Sol üst mod seçimi
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
    # Kapak Slaytı
    st.markdown(
        """
        <div class="slide-card">
            <div class="slide-category">Proje Sunumu</div>
            <div class="slide-title">Türkçe Matematik Sözlüğü</div>
            <div class="slide-desc">USB olmadığından böyle bir sözlük hazırladım.</div>
            <div class="slide-example"><b>Hazırlayan:</b> Yiğit ALPARSLAN</div>
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
  st.markdown(
      "<h1>Sözlük Modu (A-Z Tüm Terimler)</h1>", unsafe_allow_html=True
  )
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
