import requests
from bs4 import BeautifulSoup
import smtplib

# url = 'https://www.amazon.in/Apple-MacBook-Pro-9th-Generation-Intel-Core-i7/dp/B07SBK1YHJ/ref=sr_1_2_sspa?keywords=macbook+pro+13+inch&qid=1574159183&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyWURLQlpaVjg3WjZQJmVuY3J5cHRlZElkPUEwODAzMTgxMlRaRDdRVVI3NUVXNCZlbmNyeXB0ZWRBZElkPUEwMTYwNTkwMkZIOE1RVE9MSlEyNSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

url = 'https://www.amazon.in/Roman-Living-Hastings-5-Seater-Fabric/dp/B07B75XKJP/ref=sxin_0?ascsubtag=amzn1.osa.4040bd84-e0d1-4092-ac05-ee7c6fed0edb.A21TJRUUN4KGV.en_IN&creativeASIN=B07B75XKJP&cv_ct_cx=furniture&cv_ct_id=amzn1.osa.4040bd84-e0d1-4092-ac05-ee7c6fed0edb.A21TJRUUN4KGV.en_IN&cv_ct_pg=search&cv_ct_wn=osp-single-source&keywords=furniture&linkCode=oas&pd_rd_i=B07B75XKJP&pd_rd_r=f1f6df1c-df9e-4409-993d-bcc58de30311&pd_rd_w=mqqOd&pd_rd_wg=QMv1g&pf_rd_p=8abf6964-7313-4310-9a0f-4858d74fcf4a&pf_rd_r=E5Y11QFCRCKZ7WFHJH1F&qid=1580317934&sr=1-1-32235bf8-c8dc-423d-b49a-58af94d8b862&tag=toimsp-21'

headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"}


def check_price():

    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content,'html.parser')

    #print(soup.prettify())

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()

        # if(price < 10):
        #      send_mail()

    print(title.strip())
    print(price.strip())

# def send_mail():
#     server  =smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()

#     server.login('arjun.sourcecode','aniyanarjun')

#     subject = 'Price fell down'
#     body = 'check the link  https://www.amazon.in/Apple-MacBook-Pro-9th-Generation-Intel-Core-i7/dp/B07SBK1YHJ/ref=sr_1_2_sspa?keywords=macbook+pro+13+inch&qid=1574159183&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyWURLQlpaVjg3WjZQJmVuY3J5cHRlZElkPUEwODAzMTgxMlRaRDdRVVI3NUVXNCZlbmNyeXB0ZWRBZElkPUEwMTYwNTkwMkZIOE1RVE9MSlEyNSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    
#     msg  = f"Subject: {subject}\n\n{body}"

#     server.sendmail(
#         'arjun.sourcecode@gmail.com',
#         'arjun.parameswaran12@gmail.com',
#         msg
#     )

#     print('Hey email has been sent...')
#     server.quit()

check_price()

