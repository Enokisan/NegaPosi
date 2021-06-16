import urllib.request as req
import bs4 import BeautifulSoup

def html2txt(filename):
    with open(filename+".html", "rt", encoding="sjis") as f:
        html = f.read()
        # HTMLをパースする
        soup = BeautifulSoup(html, 'html.parser')
        # ルビを削除
        soup.find("rp").extract()
        soup.find("rt").extract()
        # テキストだけを取り出す
        text = soup.get_text()
        print(text)
        # 保存
        with open(filename+".txt", "wt", encoding="utf-8") as w:
            w.write(text)

def download(url, filename):
    # ダウンロード
    req.urlretrieve(url, filename)
    print("[NegaPosi] {} has been downloaded!\n".format(filename))

def csv_download():
    # URLや保存ファイル名を指定
    url = 'http://www.cl.ecei.tohoku.ac.jp/resources/sent_lex/pn.csv.m3.120408.trim'
    filename = 'pn.csv'
    # ダウンロード
    download(url, filename)

def aozora_download():
    url = input("[NegaPosi] Paste url you want from 青空文庫.\n")
    filename = input("[NegaPosi] Type file name as you want.\n")
    download(url, filename+".html")
    html2txt(filename)
    