from helpers.db import MySQLDatabase
from helpers.db2 import *

# from helpers.ui import Ms
from helpers.crawling import 수집
from helpers.crawling_sele import User

import time


if __name__ == "__main__":
    # 버전 125.0.6422.113(공식 빌드) (64비트)
    # https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.113/win64/chromedriver-win64.zip
    # user = User("n")
    user = User()
    user.move_page("https://www.danawa.com/")

    # 특정 area (검색창) 따오기.
    # 브라우저 -> F12 -> Selector
    # AKCSearch
    # //*[@id="AKCSearch"]
    # user.select_obj('//*[@id="AKCSearch"]', "맥북")
    user.cover_obj('//*[@id="AKCSearch"]', "맥북")

    user.delay_normal(3)

    user.press_key(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "search__submit", " " ))]'
    )  # 돋보기 누르기

    user.delay_normal(3)

    # //*[@id="saveDESC"]/a # 인기상품순 XPATH
    # //*[@id="opinionDESC"]/a # 상품평 많은 순 XPATH
    # //*[@id="dataDESC"]/a # 신상품순 XPATH
    # 상품평 많은 순 누르기
    user.press_key(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "click_log_product_standard_title_", " " ))]'
    )

    user.delay_normal(3)

    user.press_key('//*[@id="thumbLink_12660491"]')

    user.delay_normal(3)

    user.new_window(1)

    # 리뷰 크롤링
    item = []
    review_title = []
    review_text = []
    review_star = []
    page_num = []

    for j in range(0, 100):
        user.delay_normal(2)
        for i in range(0, 9):
            try:
                item = "맥북"
                # 리뷰 제목
                review_title.append(
                    user.crawl_text(
                        f'//*[@id="danawa-prodBlog-companyReview-content-wrap-0"]/div/div[{i + 1}]/p'
                    )
                )

                # 리뷰 내용
                review_text.append(
                    user.crawl_text(
                        f'//*[@id="danawa-prodBlog-companyReview-content-wrap-0"]/div/div[{i + 2}]'
                    )
                )

                # 리뷰 별점
                review_star.append(
                    user.crawl_text(
                        f'//*[@id="danawa-prodBlog-companyReview-content-list"]/ul/li[1]/div[1]/span[{i + 1}]'
                    )
                )

                # 페이지 번호
                page_num.append(j + 1)

                # 다음 페이지 클릭
                user.paging(
                    f"/html/body/div[2]/div[5]/div[2]/div[4]/div[4]/div/div[3]/div[2]/div[3]/div[2]/div[5]/div/div/div/a[{j + 1}]"
                )

            except Exception as e:
                print(f"문제 있는 {i}, {j}")

    time.sleep(10)
    # 작업 종료
    # user.close_connection()
