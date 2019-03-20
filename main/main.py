# --*-- coding: utf-8 --*--
import codecs

import re

import collections
import requests

from bs4 import BeautifulSoup


# 에러 리스트 생성 함수
def insert_error(blog_id, error, error_doc):
    for i in error_doc:
        error_log = str(error_doc["page"]) + "page / " + str(error_doc["post_number"]) \
                    + "th post / " + error + " / http://blog.naver.com/PostList.nhn?blogId=" + blog_id + "&currentPage=" + str(
            error_doc["page"])
    error_list.append(error_log)


total_num = 0;

error_list = []

print("블로그 ID->")
blog_id = input()

print("\n탐색 시작 페이지 수->")
start_p = int(input())

print("\n탐색 종료 페이지 수->")
end_p = int(input())

print("\nCreating File Naver_Blog_Crawling_Result.txt...\n")

# 파일 열기
file = codecs.open("Naver_Blog_Crawling_Result.txt", 'w', encoding="utf-8")

# 페이지 단위
for page in range(start_p, end_p + 1):
    print("=" * 50)
    file.write("=" * 50 + "\n")

    doc = collections.OrderedDict()

    # url = "http://blog.naver.com/PostList.nhn?blogId=" + blog_id + "&currentPage=" + str(page)
    url = "http://www.tankauction.co.kr/auction/ca_list.php?total_record=301&search_fm_off=1&search_fm_off=1&lawsup=&" \
          "lesson=&num1=&num2=&ju_price1=0&ju_price2=0&state=1%2C2%2C17%2C18&b_count1=" \
          "&b_count2=&power_flag=1&bi_price1=0&bi_price2=0&c_19=19&next_biddate1=&next_biddate2=&b_area1=&b_area2=" \
          "&e_area1=&e_area2=&sido=0&gugun=0&dong=0&ref_page=&ref_sido=0&ref_gugun=0&ref_dong=0&bunji_key=&bunji1=" \
          "&bunji2=&address=&address2=&special=0&order=&sagun_type=&page_code=1010&subcode=&ck_photo=1&favor_mode=" \
          "&favor_edit=0&from_favor=&from_my_search=&search_mode=1&favor_idx=&x=59&y=10&start=0"
    r = requests.get(url)

    
    if (not r.ok):
        print("Page" + page + "연결 실패, Skip")
        continue

    # html 파싱
    soup = BeautifulSoup(r.text.encode("utf-8"), "html.parser")

    # 페이지 당 포스트 수 (printPost_# 형식의 id를 가진 태그 수)
    post_count = len(soup.find_all("table", {"id": re.compile("printPost.")}))

    doc["page"] = page
# http://www.tankauction.co.kr/auction/ca_list.php?total_record=301&search_fm_off=1&search_fm_off=1&lawsup=&lesson=&num1=&num2=&ju_price1=0&ju_price2=0&state=1%2C2%2C17%2C18&b_count1=&b_count2=&power_flag=1&bi_price1=0&bi_price2=0&c_19=19&next_biddate1=&next_biddate2=&b_area1=&b_area2=&e_area1=&e_area2=&sido=0&gugun=0&dong=0&ref_page=&ref_sido=0&ref_gugun=0&ref_dong=0&bunji_key=&bunji1=&bunji2=&address=&address2=&special=0&order=&sagun_type=&page_code=1010&subcode=&ck_photo=1&favor_mode=&favor_edit=0&from_favor=&from_my_search=&search_mode=1&favor_idx=&x=59&y=10&start=0

# 결과 출력 (전체 글 수, 에러 수)
print("=" * 50)
file.write("=" * 50 + "\n")

print("Total : " + str(total_num))

error_num = len(error_list)
print("Error : " + str(error_num))

# 에러가 있을 경우 출력
if (error_num != 0):
    print("Error Post : ")
    for i in error_list:
        print(i)

# 파일 닫기
file.close()


# 46717170516e696537326649505250