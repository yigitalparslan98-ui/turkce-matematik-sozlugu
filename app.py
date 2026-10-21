import streamlit as st

st.set_page_config(
    page_title="6. Sınıf Türkçe Matematik Sözlüğü", page_icon="📐", layout="wide"
)

# Göz yormayan mat gri/slate arka plan ve yumuşak yeşil vurgular
st.markdown(
    """
    <style>
    html, body, [class*="css"], div, p, span, h1, h2, h3, h4, h5, h6, button {
        font-family: Arial, sans-serif !important;
    }
    .stApp {
        background-color: #1e293b !important;
        color: #f8fafc !important;
    }
    .slide-card {
        background-color: #334155;
        border: 1px solid #475569;
        border-left: 6px solid #22c55e;
        border-radius: 8px !important;
        padding: 30px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .slide-category {
        color: #4ade80;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 8px;
        font-weight: 700;
    }
    .slide-title {
        color: #f8fafc;
        font-size: 36px;
        font-weight: 800;
        margin-bottom: 16px;
    }
    .slide-desc {
        color: #e2e8f0;
        font-size: 18px;
        line-height: 1.5;
        margin-bottom: 20px;
    }
    .slide-example {
        background-color: #0f172a;
        border: 1px solid #334155;
        border-left: 4px solid #22c55e;
        padding: 14px 18px;
        font-size: 15px;
        color: #86efac;
        border-radius: 6px;
    }
    .stButton > button {
        background-color: #334155 !important;
        color: #f8fafc !important;
        border-radius: 6px !important;
        border: 1px solid #475569 !important;
        font-weight: bold !important;
    }
    .stButton > button:hover {
        background-color: #475569 !important;
        color: #22c55e !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 6. Sınıf Müfredatına Uygun 30 Maddelik Genişletilmiş Sözlük
math_dictionary = [
    {
        "term": "Açı",
        "category": "Geometri",
        "desc": "Başlangıç noktaları aynı olan iki ışının arasında oluşan açıklığa denir.",
        "example": "Dar açı, dik açı (90°) ve geniş açı çeşitleri vardır.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <line x1='30' y1='160' x2='170' y2='160' stroke='#f8fafc' stroke-width='3'/>
            <line x1='30' y1='160' x2='140' y2='50' stroke='#22c55e' stroke-width='3'/>
            <path d='M 70 160 A 40 40 0 0 0 58 132' stroke='#38bdf8' stroke-width='2' fill='none'/>
            <text x='75' y='145' fill='#38bdf8' font-size='16' font-weight='bold'>a°</text>
        </svg>"""
    },
    {
        "term": "Açıklık",
        "category": "Veri İşleme",
        "desc": "Bir veri grubundaki en büyük değer ile en küçük değer arasındaki farktır.",
        "example": "5, 12, 20 sayılarında açıklık: 20 - 5 = 15'tir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <rect x='30' y='120' width='30' height='40' fill='#22c55e'/>
            <rect x='80' y='80' width='30' height='80' fill='#22c55e'/>
            <rect x='130' y='40' width='30' height='120' fill='#4ade80'/>
            <line x1='30' y1='30' x2='160' y2='30' stroke='#f87171' stroke-width='2' stroke-dasharray='4'/>
            <text x='45' y='25' fill='#f87171' font-size='12' font-weight='bold'>En Büyük - En Küçük</text>
        </svg>"""
    },
    {
        "term": "Alan",
        "category": "Geometri",
        "desc": "Düzlemsel bir şeklin yüzeyinin kapladığı miktardır.",
        "example": "Kare ve dikdörtgen alanları taban ile yüksekliğin çarpımıdır.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <rect x='40' y='50' width='120' height='100' fill='#166534' stroke='#22c55e' stroke-width='3'/>
            <text x='75' y='110' fill='#f8fafc' font-size='18' font-weight='bold'>ALAN</text>
        </svg>"""
    },
    {
        "term": "Aritmetik Ortalama",
        "category": "Veri İşleme",
        "desc": "Verilerin toplamının, veri sayısına bölünmesiyle elde edilen değerdir.",
        "example": "10, 20 ve 30'un ortalaması: (10+20+30) / 3 = 20'dir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <text x='50' y='80' fill='#f8fafc' font-size='18' font-weight='bold'>Veri Toplamı</text>
            <line x1='40' y1='100' x2='160' y2='100' stroke='#22c55e' stroke-width='3'/>
            <text x='55' y='130' fill='#4ade80' font-size='18' font-weight='bold'>Veri Sayısı</text>
        </svg>"""
    },
    {
        "term": "Asal Sayı",
        "category": "Sayılarda İşlemler",
        "desc": "Sadece 1'e ve kendisine bölünebilen, 1'den büyük doğal sayılardır.",
        "example": "2, 3, 5, 7, 11, 13... En küçük ve tek çift asal sayı 2'dir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <circle cx='50' cy='70' r='20' fill='#1e293b' stroke='#22c55e' stroke-width='2'/>
            <text x='44' y='76' fill='#4ade80' font-size='18' font-weight='bold'>2</text>
            <circle cx='100' cy='70' r='20' fill='#1e293b' stroke='#22c55e' stroke-width='2'/>
            <text x='94' y='76' fill='#4ade80' font-size='18' font-weight='bold'>3</text>
            <circle cx='150' cy='70' r='20' fill='#1e293b' stroke='#22c55e' stroke-width='2'/>
            <text x='144' y='76' fill='#4ade80' font-size='18' font-weight='bold'>5</text>
            <circle cx='100' cy='130' r='20' fill='#1e293b' stroke='#22c55e' stroke-width='2'/>
            <text x='94' y='136' fill='#4ade80' font-size='18' font-weight='bold'>7</text>
        </svg>"""
    },
    {
        "term": "Bileşik Kesir",
        "category": "Kesirler",
        "desc": "Payı paydasına eşit veya payından büyük olan kesirlerdir.",
        "example": "5/4, 7/3 veya 4/4 birer bileşik kesirdir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <text x='85' y='80' fill='#4ade80' font-size='32' font-weight='bold'>7</text>
            <line x1='60' y1='100' x2='140' y2='100' stroke='#f8fafc' stroke-width='3'/>
            <text x='85' y='140' fill='#38bdf8' font-size='32' font-weight='bold'>4</text>
        </svg>"""
    },
    {
        "term": "Bölünebilme Kuralları",
        "category": "Sayılarda İşlemler",
        "desc": "Bir sayının kalansız bölünüp bölünmediğini pratik yoldan anlama yöntemleridir.",
        "example": "Son rakamı çift olanlar 2'ye, rakamları toplamı 3'ün katı olanlar 3'e tam bölünür.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <rect x='40' y='50' width='120' height='100' fill='#1e293b' stroke='#22c55e' stroke-width='2'/>
            <text x='65' y='90' fill='#f8fafc' font-size='22' font-weight='bold'>240 ÷ 3</text>
            <text x='65' y='125' fill='#4ade80' font-size='16' font-weight='bold'>Kalan = 0</text>
        </svg>"""
    },
    {
        "term": "Bütüler Açılar",
        "category": "Geometri",
        "desc": "Ölçüleri toplamı 180 derece olan iki açıya denir.",
        "example": "110° ve 70° birbirinin bütünleyenidir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <line x1='30' y1='140' x2='170' y2='140' stroke='#f8fafc' stroke-width='3'/>
            <line x1='100' y1='140' x2='60' y2='50' stroke='#22c55e' stroke-width='3'/>
            <text x='45' y='120' fill='#22c55e' font-size='14' font-weight='bold'>110°</text>
            <text x='115' y='120' fill='#38bdf8' font-size='14' font-weight='bold'>70°</text>
        </svg>"""
    },
    {
        "term": "Çarpan (Bölen)",
        "category": "Sayılarda İşlemler",
        "desc": "Bir doğal sayıyı kalansız bölen sayılara o sayının çarpanları denir.",
        "example": "12'nin çarpanları: 1, 2, 3, 4, 6 ve 12'dir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <text x='85' y='50' fill='#f8fafc' font-size='24' font-weight='bold'>12</text>
            <line x1='75' y1='70' x2='45' y2='120' stroke='#22c55e' stroke-width='2'/>
            <line x1='115' y1='70' x2='145' y2='120' stroke='#22c55e' stroke-width='2'/>
            <text x='35' y='150' fill='#4ade80' font-size='20' font-weight='bold'>3</text>
            <text x='140' y='150' fill='#4ade80' font-size='20' font-weight='bold'>4</text>
        </svg>"""
    },
    {
        "term": "Çember",
        "category": "Geometri",
        "desc": "Düzlemde sabit bir noktaya eşit uzaklıktaki noktaların oluşturduğu kapalı çizgi.",
        "example": "Çemberin içi boştur; bozuk para daire, yüzük ise çember örneğidir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <circle cx='100' cy='100' r='55' fill='none' stroke='#22c55e' stroke-width='3'/>
            <circle cx='100' cy='100' r='4' fill='#f8fafc'/>
            <line x1='100' y1='100' x2='155' y2='100' stroke='#38bdf8' stroke-width='2'/>
            <text x='120' y='95' fill='#38bdf8' font-size='14' font-weight='bold'>r</text>
        </svg>"""
    },
    {
        "term": "Çözümleme",
        "category": "Ondalık Gösterim",
        "desc": "Bir sayının basamak değerlerinin toplamı şeklinde yazılmasıdır.",
        "example": "2,35 = 2x1 + 3x0,1 + 5x0,01 şeklinde çözümlenir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <text x='50' y='110' fill='#4ade80' font-size='22' font-weight='bold'>2 + 0,3 + 0,05</text>
        </svg>"""
    },
    {
        "term": "Daire",
        "category": "Geometri",
        "desc": "Çember ile çemberin iç bölgesinin birleşiminden oluşan düzlemsel şekil.",
        "example": "Madeni para ve tepsiler birer daire modelidir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <circle cx='100' cy='100' r='55' fill='#166534' stroke='#22c55e' stroke-width='3'/>
        </svg>"""
    },
    {
        "term": "Dik Açı",
        "category": "Geometri",
        "desc": "Ölçüsü tam 90 derece olan açıdır.",
        "example": "Kare ve dikdörtgenin köşe açıları dik açıdır.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <line x1='50' y1='150' x2='150' y2='150' stroke='#f8fafc' stroke-width='3'/>
            <line x1='50' y1='150' x2='50' y2='50' stroke='#f8fafc' stroke-width='3'/>
            <rect x='50' y='130' width='20' height='20' fill='none' stroke='#22c55e' stroke-width='2'/>
            <circle cx='60' cy='140' r='2' fill='#22c55e'/>
        </svg>"""
    },
    {
        "term": "Doğal Sayılar",
        "category": "Sayılarda İşlemler",
        "desc": "0'dan başlayıp sonsuza kadar giden sayılar kümesidir.",
        "example": "0, 1, 2, 3, 4, 5... sayıları doğal sayılardır.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <text x='35' y='110' fill='#22c55e' font-size='20' font-weight='bold'>N = {0, 1, 2, 3...}</text>
        </svg>"""
    },
    {
        "term": "Hacim",
        "category": "Ölçme",
        "desc": "Üç boyutlu bir cismin uzayda kapladığı alana verilen isimdir.",
        "example": "Prizma Hacmi = En x Boy x Yükseklik formülü ile bulunur.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <rect x='50' y='80' width='60' height='60' fill='#1e293b' stroke='#22c55e' stroke-width='2'/>
            <path d='M 50 80 L 80 50 L 140 50 L 110 80' fill='#166534' stroke='#22c55e' stroke-width='2'/>
            <path d='M 110 80 L 140 50 L 140 110 L 110 140' fill='#15803d' stroke='#22c55e' stroke-width='2'/>
        </svg>"""
    },
    {
        "term": "İki Kümenin Birleşimi",
        "category": "Kümeler",
        "desc": "İki kümenin bütün elemanlarının oluşturduğu yeni kümedir (∪ sembolü).",
        "example": "A = {1, 2} ve B = {2, 3} ise A ∪ B = {1, 2, 3}'tür.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <circle cx='75' cy='100' r='40' fill='#166534' fill-opacity='0.8' stroke='#22c55e' stroke-width='2'/>
            <circle cx='125' cy='100' r='40' fill='#166534' fill-opacity='0.8' stroke='#22c55e' stroke-width='2'/>
        </svg>"""
    },
    {
        "term": "İki Kümenin Kesişimi",
        "category": "Kümeler",
        "desc": "İki kümedeki ortak elemanların oluşturduğu kümedir (∩ sembolü).",
        "example": "A = {a, b} ve B = {b, c} ise A ∩ B = {b}'dir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <circle cx='75' cy='100' r='40' fill='none' stroke='#f8fafc' stroke-width='2'/>
            <circle cx='125' cy='100' r='40' fill='none' stroke='#f8fafc' stroke-width='2'/>
            <path d='M 100 65 A 40 40 0 0 1 100 135 A 40 40 0 0 1 100 65' fill='#22c55e'/>
        </svg>"""
    },
    {
        "term": "İşlem Önceliği",
        "category": "Sayılarda İşlemler",
        "desc": "Birden fazla işlem olduğunda sırasıyla: Üslü Sayılar → Parantez → Çarpma/Bölme → Toplama/Çıkarma uygulanır.",
        "example": "3 + 5 x 2 işleminde önce çarpma yapılır: 3 + 10 = 13.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <text x='45' y='70' fill='#4ade80' font-size='16' font-weight='bold'>1. Üslü Sayılar</text>
            <text x='45' y='100' fill='#4ade80' font-size='16' font-weight='bold'>2. Parantez İçi</text>
            <text x='45' y='130' fill='#4ade80' font-size='16' font-weight='bold'>3. Çarpma / Bölme</text>
        </svg>"""
    },
    {
        "term": "Kat",
        "category": "Sayılarda İşlemler",
        "desc": "Bir doğal sayının başka bir doğal sayıyla çarpılmasıyla elde edilen sayılardır.",
        "example": "5'in katları: 5, 10, 15, 20, 25... şeklinde sonsuza gider.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <text x='40' y='110' fill='#4ade80' font-size='18' font-weight='bold'>5 → 10 → 15 → 20</text>
        </svg>"""
    },
    {
        "term": "Kesir",
        "category": "Kesirler",
        "desc": "Bir bütünün eş parçalarını gösteren ifadedir (Pay / Payda).",
        "example": "3/4 kesri, 4 eşit parçaya bölünen bütünün 3 parçasını gösterir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <rect x='40' y='70' width='120' height='50' fill='none' stroke='#f8fafc' stroke-width='2'/>
            <rect x='40' y='70' width='30' height='50' fill='#22c55e'/>
            <rect x='70' y='70' width='30' height='50' fill='#22c55e'/>
            <rect x='100' y='70' width='30' height='50' fill='#22c55e'/>
            <line x1='70' y1='70' x2='70' y2='120' stroke='#f8fafc' stroke-width='2'/>
            <line x1='100' y1='70' x2='100' y2='120' stroke='#f8fafc' stroke-width='2'/>
            <line x1='130' y1='70' x2='130' y2='120' stroke='#f8fafc' stroke-width='2'/>
        </svg>"""
    },
    {
        "term": "Komşu Açılar",
        "category": "Geometri",
        "desc": "Başlangıç noktaları ve birer kolları ortak olan açılardır.",
        "example": "Yan yana duran iki açının komşu kolu ortaktır.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <line x1='40' y1='150' x2='160' y2='150' stroke='#f8fafc' stroke-width='3'/>
            <line x1='40' y1='150' x2='100' y2='40' stroke='#22c55e' stroke-width='3'/>
            <line x1='40' y1='150' x2='150' y2='80' stroke='#38bdf8' stroke-width='3'/>
        </svg>"""
    },
    {
        "term": "Mutlak Değer",
        "category": "Tam Sayılar",
        "desc": "Bir tam sayının sayı doğrusunda 0 (orijin) noktasına olan uzaklığıdır.",
        "example": "|-5| = 5 ve |+5| = 5'tir (Uzaklık negatif olamaz).",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <line x1='30' y1='120' x2='170' y2='120' stroke='#f8fafc' stroke-width='2'/>
            <circle cx='100' cy='120' r='4' fill='#22c55e'/>
            <text x='96' y='145' fill='#22c55e' font-size='14'>0</text>
            <circle cx='40' cy='120' r='4' fill='#f87171'/>
            <text x='30' y='145' fill='#f87171' font-size='14'>-5</text>
            <path d='M 40 110 Q 70 70 100 110' fill='none' stroke='#4ade80' stroke-width='2'/>
        </svg>"""
    },
    {
        "term": "Ondalık Gösterim",
        "category": "Kesirler ve Ondalık",
        "desc": "Paydası 10, 100 veya 1000 olan kesirlerin virgül kullanılarak gösterimidir.",
        "example": "5/10 = 0,5 veya 25/100 = 0,25'tir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <text x='58' y='110' fill='#4ade80' font-size='36' font-weight='bold'>0,75</text>
        </svg>"""
    },
    {
        "term": "Oran",
        "category": "Oran ve Orantı",
        "desc": "İki çokluğun birbirine bölünerek karşılaştırılmasıdır.",
        "example": "Elma sayısının armut sayısına oranı: 3 / 5'tir.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <text x='85' y='80' fill='#22c55e' font-size='28' font-weight='bold'>a</text>
            <line x1='70' y1='95' x2='130' y2='95' stroke='#f8fafc' stroke-width='3'/>
            <text x='85' y='130' fill='#38bdf8' font-size='28' font-weight='bold'>b</text>
        </svg>"""
    },
    {
        "term": "Paralelkenar",
        "category": "Geometri",
        "desc": "Karşılıklı kenarları paralel ve eşit uzunlukta olan dörtgendir.",
        "example": "Alan = Taban x O tabana ait Yükseklik.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <polygon points='60,140 160,140 130,60 30,60' fill='#166534' stroke='#22c55e' stroke-width='2'/>
        </svg>"""
    },
    {
        "term": "Sayı Doğrusu",
        "category": "Tam Sayılar",
        "desc": "Sayıların eşit aralıklarla üzerine dizildiği doğru çizgisidir.",
        "example": "Sağa gidildikçe sayılar büyür, sola gidildikçe küçülür.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <line x1='20' y1='100' x2='180' y2='100' stroke='#f8fafc' stroke-width='3'/>
            <text x='50' y='130' fill='#f87171' font-size='16'>-1</text>
            <text x='97' y='130' fill='#22c55e' font-size='16'>0</text>
            <text x='140' y='130' fill='#38bdf8' font-size='16'>+1</text>
        </svg>"""
    },
    {
        "term": "Tam Sayılar",
        "category": "Tam Sayılar",
        "desc": "Negatif sayılar, 0 ve pozitif sayıların tümünün oluşturduğu kümedir (Z).",
        "example": "..., -2, -1, 0, +1, +2... sayiları tam sayılardır.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <text x='30' y='110' fill='#4ade80' font-size='18' font-weight='bold'>Z = {..., -1, 0, +1, ...}</text>
        </svg>"""
    },
    {
        "term": "Tümleyen Açılar",
        "category": "Geometri",
        "desc": "Ölçüleri toplamı 90 derece olan iki açıya denir.",
        "example": "40°'lik açının tümleyeni 50°'dir (40 + 50 = 90).",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <path d='M 50 150 L 150 150 L 50 50 Z' fill='none' stroke='#f8fafc' stroke-width='2'/>
            <line x1='50' y1='150' x2='120' y2='80' stroke='#22c55e' stroke-width='2.5'/>
        </svg>"""
    },
    {
        "term": "Üslü İfade",
        "category": "Sayılarda İşlemler",
        "desc": "Bir sayının kendisi ile tekrarlı çarpımının kısa yoldan yazılışıdır.",
        "example": "2⁴ = 2 x 2 x 2 x 2 = 16 (2 üssü 4 okunur).",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <text x='75' y='120' fill='#f8fafc' font-size='48' font-weight='bold'>a</text>
            <text x='105' y='80' fill='#4ade80' font-size='28' font-weight='bold'>n</text>
        </svg>"""
    },
    {
        "term": "Yükseklik",
        "category": "Geometri",
        "desc": "Bir geometrik şeklin tepe noktasından tabanına indirilen dik çizgedir.",
        "example": "Üçgenin Alanı = (Taban x Yükseklik) / 2 kuralıyla hesaplanır.",
        "svg": """<svg width='100%' height='200' viewBox='0 0 200 200' style='background:#0f172a; border-radius:6px;'>
            <polygon points='30,150 170,150 100,50' fill='none' stroke='#f8fafc' stroke-width='2'/>
            <line x1='100' y1='50' x2='100' y2='150' stroke='#f87171' stroke-width='2.5' stroke-dasharray='4'/>
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
        f"<h3 style='text-align: center; color: #f8fafc;'>Slayt"
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
