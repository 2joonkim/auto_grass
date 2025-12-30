---
title: "FastApi 의 DB를 연결해보자"
date: 2025-02-17
url: https://velog.io/@2joon_kim/FastApi-%EC%9D%98-DB%EB%A5%BC-%EC%97%B0%EA%B2%B0%ED%95%B4%EB%B3%B4%EC%9E%90
---

## 요약

진짜로..
일과 공부를 병행하는 대한민국의 모든 학생 + 직장인 여러분 존경합니다
특히 나 같이 새벽에 일하고 쪽잠자며 낮에 공부하시는 분들은 진짜
지금_내_심정 = (&quot;존경&quot; * 10000000000) + &quot;합니다&quot;
진짜 죽을거 같지만 혼자만의 약속이기에 나만의 교육이해를 위해 작성시작한다..
📌 FastApi의 DB연동
FastApi와 DB를 연결하는 방법은 아주 다양하지만 그중에서도 나는
가장 대표적인 방법인 SQLAlchemy를 다뤄보려고 한다 (배우기도 이걸 배웠고;;)
일단 먼저 SQLAlchemy의 특징을 알아보자면 아래와 같다

데이터베이스를 파이썬에서 쉽게 다룰 수 있게 해주는 도구라고 생각하면 된다
파이썬 클래스로 데이터베이스 테이블을 다루는 것처럼 사용할 수 있다
SQL 쿼리를 직접 쓰지 않아도 되기 때문에 코드가 깔끔해진다

대표적인 특징들만 알아봤으나 사용하며 더 딥한 부분들이 많다
이틀째의 FastApi DB 연동 코드만 좀 적어보겠다
이 코드는 SQLite라는 데이터베이스를 사용하여 사용자를 추가하고 
그 사용자의 이름을 출력하는 간단한 코드이다
# 필요한 라이브러리 가져오기
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite 메모리 데이터베이스 연결
DATABASE_URL = &quot;sqlite:///:memory:&quot;  # 메모리에서 데이터베이스를 만든다
engine = create_engine(DATABASE_URL, echo=True)  # 데이터베이스 엔진 생성

Base = declarative_base()  # 데이터베이스 모델의 기본 클래스 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # 세션 생성

# 사용자 모델 정의
class User(Base):
    __tablename__ = &quot;users&quot;  # 테이블 이름
    id = Column(Integer, primary_key=True)  # 사용자 ID
    name = Column(String, nullable=False)  # 사용자 이름

# 데이터베이스에 테이블 생성
Base.metadata.create_all(bind=engine)

# 세션 시작
session = SessionLocal()
new_user = User(name=&quot;John Doe&quot;)  # 새로운 사용자 생성
session.add(new_user)  # 사용자 추가
session.commit()  # 변경사항 저장

# 모든 사용자 조회
users = session.query(User).all()  # 모든 사용자 가져오기
for user in users:  # 각 사용자에 대해
    print(user.name)  # 사용자 이름 출력
📌 FastApi의 Dependency injection?
FastApi의 강력한 기능 중 하나로 쉽게 나만의 방식으로 해석하자면 
&quot;필요한 것을 외부에서 넣어주는 방식&quot;이라고 생각하면 편할 것 같다
일단 Dependency injection의 대표적인 특징으로는

데이터베이스 연결을 자동으로 관리해준다
코드 반복을 줄여준다
테스트하기 쉬워진다
데이터베이스 세션을 안전하게 닫아준다

이 정도가 있을 것 같다
그래서 어떻게 쓰며 어떻게 관리를 하냐?
FastApi에서는 Depends를 사용하여 의존성 정의와 관리를 할 수 있다
주로 데이터베이스의 세션, 인증, 설정등에 많이 사용된다고 한다
📌 Dependency로 세션 관리
일단 먼저 나는 session에 대한 개념조차 정확하지 않았기에 짚고 넘어가기로 했다
데이터베이스와의 &quot;대화 창구&quot;라고 생각하면 될 거 같다
쉽게 예를 들어서 카페에서 주문할 때
카페 = 데이터베이스
주문창구 = 세션
주문하기 = 쿼리 실행
주문 완료 후 창구 닫기 = 세션 종료
이렇게 될 수 있을 것 같다.
세션 관리는 무조건 알고 있어야 하는데 [ money가 들어가는 부분이기 때문 ;;;]
아래의 문제점으로 인해 세션관리에도 꼭 신경쓰는 개발자가 되자👍🏻
자원 관리: 데이터베이스 연결은 비용이 많이 들어서 잘 관리해야 된다고 한다
안전성: 사용이 끝난 연결은 반드시 닫아야 한다 = 보안의 위험!!!
성능: 너무 많은 연결이 열려있으면 성능이 저하될 수 있다
아래 코드를 보고 Dependency를 알아보자
# ❌ 좋지 않은 방법
@app.get(&quot;/users&quot;)
def get_users():
    db = SessionLocal()  # 매번 직접 열고
    users = db.query(User).all()
    db.close()  # 매번 직접 닫고
    return users
# 이 예제는 Dependency를 사용하지 않은 코드이다
# 보면 나오듯이 모든 엔드포인트마다 db.close하여 매번 직접 닫고 호출을 하고 있다.

# ✅ 좋은 방법 (Dependency 사용)
# 이건 그냥 외우도록 하자 ^^
def get_db():
    db = SessionLocal()
    try:
        yield db  # 필요할 때 자동으로 열고
    finally:
        db.close()  # 자동으로 닫아줌
나머지는 또 차후에 업데이트 하도록 하겠드..아

[원본 글 읽기](https://velog.io/@2joon_kim/FastApi-%EC%9D%98-DB%EB%A5%BC-%EC%97%B0%EA%B2%B0%ED%95%B4%EB%B3%B4%EC%9E%90)
