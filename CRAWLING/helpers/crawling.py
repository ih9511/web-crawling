from bs4 import BeautifulSoup
import requests
import pandas as pd


def 수집():
    # http://www.neweracapkorea.com/shop/shopbrand.html?xcode=031&mcode=002&type=Y&gf_ref=Yz1vU0FlS3M=
    base_url = "http://www.neweracapkorea.com"
    cap_total_url = "/shop/shopbrand.html?xcode=031&mcode=002&type=Y&gf_ref=Yz1vU0FlS3M="
    base_url + cap_total_url


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }

    cap_info_list = []
    price_list = []
    url_list = []

    for ii in range(0, 9):
        newurl = f"https://www.neweracapkorea.com/shop/shopbrand.html?type=Y&xcode=031&mcode=002&sort=&page={ii+1}"
        # get html
        response = requests.get(newurl, headers=headers)
        response.status_code

        # BeautifulSoup을 활용하여 데이터 파싱
        soup = BeautifulSoup(response.content, "lxml")
        soup

        id = "productClass"

        for i in range(0, 20):
            for j in range(0, 5):
                try:
                    cap_info_list.append(
                        soup.select(
                            f"#productClass > div > div.page-body > div.width1200 > div > table > tbody > tr:nth-child({i+2}) > td:nth-child({j+1}) > div > ul > li.dsc"
                        )[0].text
                    )
                except IndexError as e:
                    pass
                try:
                    price_list.append(
                        soup.select(
                            f"#productClass > div > div.page-body > div.width1200 > div > table > tbody > tr:nth-child({i+2}) > td:nth-child({j+1}) > div > ul > li.price"
                        )[0].text
                    )
                except IndexError as e:
                    pass
                try:
                    url_list.append(
                        soup.select(
                            f"#productClass > div > div.page-body > div.width1200 > div > table > tbody > tr:nth-child({i+2}) > td:nth-child({j+1}) > div > div > a"
                        )[0].attrs["href"]
                    )
                except IndexError as e:
                    pass

    df = pd.DataFrame(
        zip(cap_info_list, price_list, url_list),
        columns=["상품명", "가격", "상세페이지주소"],
    )
    # xlsxwriter
    # openpyxl
    df.to_excel(r"C:\Users\USER\Desktop\workspace01\crawling\data\모자결과물.xlsx", engine='openpyxl')