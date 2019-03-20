# --*-- coding: utf-8 --*--
import codecs

import re

import collections
import requests
#
# url = "http://openAPI.seoul.go.kr:8088/46717170516e696537326649505250/xml/SearchLocationOfSTNByFRCodeService/1/5/424/"


# 
url = "http://swopenAPI.seoul.go.kr/api/subway/46717170516e696537326649505250/xml/nearBy/0/5/37.058044/127.073019"
r = requests.get(url)
print(r.text)




# 37.058044, 127.073019

#http://data.seoul.go.kr/search/newSearch.jsp 좌표를 통해서 근처 역 주소
# 46717170516e696537326649505250

#https://www.juso.go.kr/addrlink/devAddrLinkRequestSubmit.do 도로명 주소로 좌표 변환
# U01TX0FVVEgyMDE5MDMxOTE4Mjk0MDEwODU4ODI=

# 도로명 to 좌표
# https://openapi.naver.com/v1/map/geocode?encoding=utf-8&output=xml&coord=latlng&query=불정로6


#
# 안녕하세요, 네이버 지도입니다.
# 일단 geocode API는 주소 -> 좌표 변환 용도입니다.
# 그렇기 때문에 query 파라미터에 좌표 정보가 들어가면 안되고 주소 정보가 들어가야 하며,
# 좌표 -> 주소 변환을 하시려면 reversegeocode API를 사용하셔야 합니다.
#
# 지금 예시를 좌표 변환으로 수정한다면 다음과 같습니다.
# https://openapi.naver.com/v1/map/geocode?encoding=utf-8&output=xml&coord=latlng&query=불정로6
#
# 서버 API 사용 예시 - https://developers.naver.com/docs/map/overview
#
# 그리고 현재 WGS84 좌표계로의 변환은 지원하지 않습니다.
# 다만 WGS84 타원체가 GRS80 타원체와 거의 동일하며,
# 네이버 기본 좌표계가 GRS80 타원체를 기반으로 하고 있으므로 참고 바랍니다.
#
# Geocoder를 사용한 좌표 변환 예시 - https://navermaps.github.io/maps.js/docs/tutorial-Geocoder.html