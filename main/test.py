# --*-- coding: utf-8 --*--
import codecs
import re
import collections
import requests
from bs4 import BeautifulSoup
import urllib
import json
import pandas as pd



def isCloseToSubway(adreess):
    df_origin = pd.DataFrame(columns=['address', 'lat', 'lng'])
    new_candidates = [adreess, "경기도 수원시 권선구 경수대로 270"]

    apikey = 'KakaoAK f87cecf961b6e352cf95260d25fbc133'  # 예시입니다. 본인의 apikey를 string 내부에 넣어아 합니다.

    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + new_candidates[0]
    headers = {"Authorization": apikey}
    result = json.loads(str(requests.get(url, headers=headers).text))
    # print(result)
    if result['meta']['total_count'] == 0:
        return 0
    match_first = result['documents'][0]['address']


    # print(url)

    apikey = 'KakaoAK f87cecf961b6e352cf95260d25fbc133'  # 예시입니다. 본인의 apikey를 string 내부에 넣어아 합니다.
    radius = '800'  # 거리
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?' + 'y=' + match_first['y'] + '&x=' + match_first[
        'x'] + '&radius=' + radius + '&category_group_code=SW8' + '&query=지하철역'
    # print(url)
    headers = {"Authorization": apikey}
    result = json.loads(str(requests.get(url, headers=headers).text))

    if result['meta']['total_count'] != 0:
        # print(result['documents'])

        print('역  이름 : ' + result['documents'][0]['place_name'])
        print('역간거리 : ' + result['documents'][0]['distance'])
        # print('******************************************************************************************************')
        return 1
    else:
        return 0


page_num = 0

for i in range(0,83):
    print('page'+ str(i))
    # url = "http://blog.naver.com/PostList.nhn?blogId=" + blog_id + "&currentPage=" + str(page)





    # 밑에는 오피스텔
    url = "http://www.tankauction.co.kr/auction/ca_list.php?total_record=301&search_fm_off=1&search_fm_off=1&lawsup=&" \
          "lesson=&num1=&num2=&ju_price1=0&ju_price2=0&state=1%2C2%2C17%2C18&b_count1=" \
          "&b_count2=&power_flag=1&bi_price1=0&bi_price2=0&c_19=19&next_biddate1=&next_biddate2=&b_area1=&b_area2=" \
          "&e_area1=&e_area2=&sido=0&gugun=0&dong=0&ref_page=&ref_sido=0&ref_gugun=0&ref_dong=0&bunji_key=&bunji1=" \
          "&bunji2=&address=&address2=&special=0&order=&sagun_type=&page_code=1010&subcode=&ck_photo=1&favor_mode=" \
          "&favor_edit=0&from_favor=&from_my_search=&search_mode=1&favor_idx=&x=59&y=10&start="+str(20*i)


    # 밑에는 아파트
    url = "http://www.tankauction.co.kr/auction/ca_list.php?total_record=2230&search_fm_off=1&search_fm_off=1&lawsup=" \
          "&lesson=&num1=&num2=&ju_price1=0&ju_price2=0&state=1%2C2%2C17%2C18&b_count1=&b_count2=&power_flag=1&bi_pric" \
          "e1=0&bi_price2=0&c_1=1&next_biddate1=&next_biddate2=&b_area1=&b_area2=&e_area1=&e_area2=&sido=0&gugun=0&dong" \
          "=0&ref_page=&ref_sido=&ref_gugun=&ref_dong=&bunji_key=&bunji1=&bunji2=&address=&address2=&special=0&order=&s" \
          "agun_type=&page_code=1010&subcode=&ck_photo=1&favor_mode=&favor_edit=0&from_favor=&from_my_search=&searc" \
          "h_mode=1&favor_idx=&x=67&y=12&start="+str(20*i)

    # 밑에는 빌라
    url = "http://www.tankauction.co.kr/auction/ca_list.php?total_record=1671&search_fm_off=1&lawsup=&lesson=&num1=&" \
          "num2=&ju_price1=0&ju_price2=0&state=1%2C2%2C17%2C18&b_count1=&b_count2=&power_flag=1&bi_price1=0&bi_price2=0" \
          "&c_8=8&next_biddate1=&next_biddate2=&b_area1=&b_area2=&e_area1=&e_area2=&sido=0&gugun=0&dong=0&ref_page=&ref_" \
          "sido=0&ref_gugun=0&ref_dong=0&bunji_key=&bunji1=&bunji2=&address=&address2=&special=0&order=&sagun_type=&page_c" \
          "ode=1010&subcode=&ck_photo=1&favor_mode=&favor_edit=0&from_favor=&from_my_search=&search_mode=1&favor_idx=&x=67&y=2" \
          "1&start=" + str(20 * i)

    r = requests.get(url)

    # html 파싱
    soup = BeautifulSoup(r.text.encode("utf-8"), "html.parser")


    # HTTP Header 가져오기
    header = soup.headers

    # HTTP Status 가져오기(200: 정상)
    status = soup.status_code

    # HTTP가 정상적으로 되었는지(true/false)
    is_ok = soup.ok



    my_titles = soup.select(
        'table'
    )





    for tr in soup.find('tbody').find_all('tr')[1:]:
        tds = tr.find_all('td')


        # 물건종류 및 주소
        category =  tds[2].text.strip().split('\n')

        if isCloseToSubway(category[1].split(',')[0]) == 1:
            print("사건번호 : " + tds[0].text.strip())
            print("물건종류 : " + category[0])
            print("물건주소 : " + category[1].split(',')[0])
            print("건물정보 : " + category[1].split(',')[1].strip())
            print("네이버 맵 주소 : " + "http://map.naver.com/?query=" + category[1].split(',')[
                0].replace(" ", "") + "&pinType=site&dlevel=20")
            location = category[1].split(',')[0]

            # 감정가 및 최저입찰액
            category =  tds[3].find_all('div')
            print("감정가   : " +category[0].text)
            print("최저입찰 : " +category[1].text)

            # 진행상태
            process =  tds[4].find_all('div')
            print("진행상태(유찰)   : " +process[0].text.replace("					", "") )
            print("감정가대비(비율) : " +process[1].text.strip())


            # 입찰일자
            dates = tds[5]
            print("입찰일자(날짜)   : " + dates.text.strip())
            print('\n')

        #
        # print("===========================================");
        # # 테스트를 uri로 바꿔주는 부분
        # inputx = 'hello 123 http://zetawiki.com 한글'
        # inputy = 'hello 123 http://zetawiki.com 한글'
        # print(urllib.parse.quote(input, ''))







#
# url = "http://swopenAPI.seoul.go.kr/api/subway/46717170516e696537326649505250/xml/nearBy/0/5/" + match_first['y'] + "/" +match_first['x']
# r = requests.get(url)
# print(url)
# print(url)
# # html 파싱
# soup = BeautifulSoup(r.text.encode("utf-8"), "html.parser")
#
# print(soup.find('statnnm'))
# print(soup.find('subwaynm'))
# print(soup.find('subwayxcnts')) #gps x
# print(soup.find('subwayycnts')) #gps y
