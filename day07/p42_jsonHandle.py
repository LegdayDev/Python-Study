# file: p42_jsonHandle.py
# desc: json 읽고/쓰기

import json

## Json 읽기
# file 읽어서 쓸 객체변수 f, file, fp
with open("./day07/p40_testData.json", mode="r", encoding="utf-8") as fp:
    data = json.load(fp)

# print(data) -> 파이썬 Dict 형태로 출력
# print(json.dumps(data)) -> JSON 형태로 출력
# print(json.dumps(data, indent="\t")) -> 좀 더 보기 좋게 출력
print(json.dumps(data, indent="\t"))  #
jData = json.dumps(data)  # str 타입

# Json 데이터 접근은 파이썬 딕셔너리, 리스트와 동일
print(data["name"])
print(data["friends"])

## Json 쓰기
# Dict 생성 -> json dumps로 만듬
superCars = dict()
audi = dict()
audi["price"] = 300_000_000
audi["year"] = "2020"
audi["type"] = "electric"

jeep = dict()
jeep["price"] = 85_000_000
jeep["year"] = "2023"
jeep["type"] = "gasoline"

superCars["jeep"] = jeep
superCars["audi"] = audi

## Json 파일 저장
with open("./day07/superCars.json", mode="w", encoding="utf-8") as fp:
    # fp에 json 데이터가 써진다.(ensure_ascii : 국가가 바뀌면 알아서 바뀐다.)
    json.dump(superCars, fp, indent="\t", ensure_ascii=True)
