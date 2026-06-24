# 한글 형태소 분석기 사용 테스트 1

#  Hananum: KAIST 말뭉치를 이용해 생성된 사전 분석기
from konlpy.tag import Hannanum, Komoran

hananum = Hannanum()

# 제공 메소드: 레퍼런스.메소드명() 사용
# analyze(): 구(parse) 분석
# morphs(): 형태소 분석
# nouns(): 명사 분석
# pos(): 형태소 분석 + 태깅

# Hananum 사용
text = u'길동 마트의 흑마늘 양념 치킨이 논란이 되고 있다.'

print("Hananum 분석기 결과")
print(hananum.analyze(text))
print(hananum.morphs(text))
print(hananum.nouns(text))
print(hananum.pos(text))

# Kkma: 서울대에서 만든 세종 말뭉치를 이용해 생성된 사전 분석기
from konlpy.tag import Kkma

kkma = Kkma()

# 제공 메소드: 레퍼런스.메소드명() 사용
# sentences(): 문장 분석
# morphs(): 형태소 분석
# nouns(): 명사 분석
# pos(): 형태소 분석 + 태깅

# Kkma 사용
print("Kkma 분석기 결과")
print(kkma.sentences(text))
print(kkma.morphs(text))
print(kkma.nouns(text))
print(kkma.pos(text))

# Komoran: Java로 만든 오픈소스 한글 형태소 분석기
from konlpy.tag import Komoran

kom = Komoran()

# Komoran 사용
print("Komoran 분석기 결과")
print(kom.morphs(text))
print(kom.nouns(text))
print(kom.pos(text))

# Twitter(Okt): 오픈소스 한글 형태소 분석기
from konlpy.tag import Okt

okt = Okt()

print("Komoran 분석기 결과")
print(okt.phrases(text))
print(okt.morphs(text))
print(okt.nouns(text))
print(okt.pos(text))

# stem: 각 단어에서 어간 추출 처리 매개변수
print('Okt 메소드: stem 매개변수 사용')
print(okt.morphs(text, stem=True))
