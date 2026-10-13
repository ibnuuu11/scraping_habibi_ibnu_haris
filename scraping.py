
import requests
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://www.bbc.com/news"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def ambil_html(url=BASE_URL):
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()
    return response.text

def demo_1_requests():
    print("\n=== DEMO 1: REQUESTS ===")
    response = requests.get(BASE_URL, headers=HEADERS, timeout=15)
    print("Status:", response.status_code)
    print(response.text[:500])

def demo_2_urlopen():
    print("\n=== DEMO 2: URLOPEN ===")
    req = Request(BASE_URL, headers=HEADERS)
    with urlopen(req, timeout=15) as response:
        html = response.read().decode("utf-8", errors="ignore")
    print(html[:500])

def demo_3_title():
    print("\n=== DEMO 3: TITLE ===")
    soup = BeautifulSoup(ambil_html(), "html.parser")
    print("Title:", soup.title.get_text(strip=True) if soup.title else "Tidak ditemukan")

def demo_4_find():
    print("\n=== DEMO 4: FIND H1 ===")
    soup = BeautifulSoup(ambil_html(), "html.parser")
    tag = soup.find("h1")
    print(tag.get_text(" ", strip=True) if tag else "H1 tidak ditemukan")

def demo_5_find_class():
    print("\n=== DEMO 5: FIND CLASS ===")
    soup = BeautifulSoup(ambil_html(), "html.parser")
    tag = soup.find(class_=True)
    print(tag.get_text(" ", strip=True) if tag else "Elemen ber-class tidak ditemukan")

def demo_6_find_all():
    print("\n=== DEMO 6: FIND ALL H2 ===")
    soup = BeautifulSoup(ambil_html(), "html.parser")
    judul = [
        tag.get_text(" ", strip=True)
        for tag in soup.find_all("h2")
        if tag.get_text(" ", strip=True)
    ]
    if judul:
        for i, teks in enumerate(judul[:20], start=1):
            print(f"{i}. {teks}")
    else:
        print("Judul H2 tidak ditemukan.")

def demo_7_csv():
    print("\n=== DEMO 7: SIMPAN KE CSV ===")
    soup = BeautifulSoup(ambil_html(), "html.parser")
    data = [
        tag.get_text(" ", strip=True)
        for tag in soup.find_all("h2")
        if tag.get_text(" ", strip=True)
    ]
    df = pd.DataFrame(data, columns=["Judul Berita"])
    df.to_csv("bbc.csv", index=False, encoding="utf-8-sig")
    print(df.head())
    print(f"Total judul tersimpan: {len(df)}")
    print("Data disimpan ke bbc.csv")

def demo_8_parser():
    print("\n=== DEMO 8: PERBANDINGAN PARSER ===")
    html = ambil_html()
    for parser in ["html.parser", "lxml"]:
        soup = BeautifulSoup(html, parser)
        title = soup.title.get_text(strip=True) if soup.title else "Title tidak ditemukan"
        print(f"{parser} -> {title}")

def demo_9_exception():
    print("\n=== DEMO 9: EXCEPTION ===")
    url_salah = "https://www.bbc.com/news/halaman-tidak-ada-123456"
    try:
        req = Request(url_salah, headers=HEADERS)
        with urlopen(req, timeout=15) as response:
            print("Status:", response.status)
    except HTTPError as e:
        print("HTTP Error:", e.code)
    except URLError as e:
        print("URL Error:", e.reason)
    except Exception as e:
        print("Error:", e)

def getTitle(url):
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=15) as response:
        html = response.read().decode("utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.get_text(strip=True) if soup.title else "Title tidak ditemukan"

def demo_10_gettitle():
    print("\n=== DEMO 10: GET TITLE ===")
    try:
        print(getTitle(BASE_URL))
    except Exception as e:
        print("Gagal mengambil title:", e)

def jalankan(nama, fungsi):
    try:
        fungsi()
    except Exception as e:
        print(f"{nama} gagal: {e}")

if __name__ == "__main__":
    demos = [
        ("Demo 1", demo_1_requests),
        ("Demo 2", demo_2_urlopen),
        ("Demo 3", demo_3_title),
        ("Demo 4", demo_4_find),
        ("Demo 5", demo_5_find_class),
        ("Demo 6", demo_6_find_all),
        ("Demo 7", demo_7_csv),
        ("Demo 8", demo_8_parser),
        ("Demo 9", demo_9_exception),
        ("Demo 10", demo_10_gettitle),
    ]

    for nama, fungsi in demos:
        jalankan(nama, fungsi)
