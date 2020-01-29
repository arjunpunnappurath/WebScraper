import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.in/Roman-Living-Hastings-5-Seater-Fabric/dp/B07B75XKJP/ref=sxin_0?ascsubtag=amzn1.osa.4040bd84-e0d1-4092-ac05-ee7c6fed0edb.A21TJRUUN4KGV.en_IN&creativeASIN=B07B75XKJP&cv_ct_cx=furniture&cv_ct_id=amzn1.osa.4040bd84-e0d1-4092-ac05-ee7c6fed0edb.A21TJRUUN4KGV.en_IN&cv_ct_pg=search&cv_ct_wn=osp-single-source&keywords=furniture&linkCode=oas&pd_rd_i=B07B75XKJP&pd_rd_r=f1f6df1c-df9e-4409-993d-bcc58de30311&pd_rd_w=mqqOd&pd_rd_wg=QMv1g&pf_rd_p=8abf6964-7313-4310-9a0f-4858d74fcf4a&pf_rd_r=E5Y11QFCRCKZ7WFHJH1F&qid=1580317934&sr=1-1-32235bf8-c8dc-423d-b49a-58af94d8b862&tag=toimsp-21'

headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"}


def check_price():

    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()

    print(title.strip())
    print(price.strip())

check_price()

