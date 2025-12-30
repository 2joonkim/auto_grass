---
title: "Fast-api을 다뤄보Ja"
date: 2025-02-12
url: https://velog.io/@2joon_kim/Fast-api%EC%9D%84-%EB%8B%A4%EB%A4%84%EB%B3%B4Ja
---

## 요약

어제 오늘 새벽에 일을 했던 거 때문에 몽롱하다 말이 안된다
거의 실신직전이다 하지만 잠 따위가 나를 막을 순 없..zZ
여튼 정리를 시작하자
FastApi란?
드디어 내가 가장 배우고 싶었던 웹 프레임워크인 Fast-api를 배우기 시작했다
언제나 그렇듯이 시작은 항상 즐겁고 배움의 열정으로 가득하다 아무튼 시작해보자
FastAPI는 파이썬으로 API를 만들 때 사용하는 현대적인 웹 프레임워크이다
쉽고 빠르게 웹 API를 만들 수 있게 해주는 도구라고 생각하면 될 것 같다
Ex. Django / flask / javaspring(Java를 사용) 등
📌 주요 특징

이름처럼 정말 빠른 성능을 자랑한다고 한다.
(Node.js나 Go와 비슷한 수준의 속도를 보여준다고 한다 = https://wikidocs.net/175092 )
특히 Django를 하고 와서 그런지 코드 작성이 더 수월하긴 하다
그리고 /docs 나 /redocs 처럼 api를 한눈으로 볼 수 있어 편하다.
오류를 잡기가 너무 편한 것 같다 아직 디테일한 작업을 시작하진 않았으나 너무 편하다!

📌중요하게 짚고 넘어갈 특징
비동기처리 (Asynchronous Processing)
비동기는 &quot;기다리지 않고 다른 일을 할 수 있게 해주는 처리 방식&quot;이다 
특히 웹에서 데이터를 가져오거나 파일을 읽고 쓸 때 많이 사용된다고 한다
이것에 관한 예시를 좀 찾아보니

Netflix의 스트리밍 서비스
카카오톡같은 메신저 서비스 등

여러개의 작업들을 한번에 처리할 수 있는 처리방법을 비동기 처리라고 생각하면 될 것 같다
아주 이해하기 쉽게 코드로도 정리해놔야겠댜
요건 동기처리과정
# 모든 작업이 순차적으로 진행됨
print(&quot;커피 주문&quot;)
make_coffee()    # 커피 만드는 3분 동안 멈춤
print(&quot;음악 재생&quot;)  # 커피 다 만들어진 후에야 실행
print(&quot;청소 시작&quot;)  # 그 다음에야 실행

플라스크의 비동기처리과정
async def cafe_tasks():
    # 모든 작업이 동시에 시작됨
    coffee_task = asyncio.create_task(make_coffee())    # 커피 만들기 시작
    music_task = asyncio.create_task(play_music())      # 동시에 음악 재생
    cleaning_task = asyncio.create_task(start_cleaning()) # 동시에 청소 시작

    # 각 작업이 완료되는대로 결과를 받음
    await coffee_task
    await music_task
    await cleaning_task
데이터 검증 및 직렬화
FastApi는 아래처럼 쉽게 Pydantic으로 데이터 검증과 직렬화가 가능하다
우리가 class에 coffeeOrder을 만들어 뒀다면?
아래 메뉴와 사이즈 수량 얼음유무 등 다양한 데이터를 미리 정하고 시작한다
그럼 FastApi는 알아서 데이터를 검증하고 본인이 맞는 데이터인지 확인하여 가져온다!
(역시 현대적이고 친절해 ㅠ)
from pydantic import BaseModel

class CoffeeOrder(BaseModel):
    menu: str       # 메뉴는 반드시 문자열
    size: str       # 사이즈도 문자열
    quantity: int   # 수량은 반드시 숫자
    ice: bool       # ICE 여부는 true/false만

# FastAPI가 자동으로 검증
@app.post(&quot;/order&quot;)
def create_order(order: CoffeeOrder):
    # quantity에 &quot;두잔&quot; 이라고 문자가 들어오면 자동으로 에러!
    # size에 없는 사이즈가 들어와도 에러!
    return order
그리고 직렬화는 우리가 받은 이 주문정보를
아래처럼 알아서 Json형식으로 변환해서 지가 가져온다
# 파이썬 객체(주문 정보)를 JSON으로 변환
order = CoffeeOrder(
    menu=&quot;아메리카노&quot;,
    size=&quot;Grande&quot;,
    quantity=2,
    ice=True
)
👇
# 자동으로 JSON으로 변환됨
{
    &quot;menu&quot;: &quot;아메리카노&quot;,
    &quot;size&quot;: &quot;Grande&quot;,
    &quot;quantity&quot;: 2,
    &quot;ice&quot;: true
}
객체나 데이터 구조를 일련의 바이트나 문자열로 변환하는 과정 쉽게 말해 
&quot;프로그램에서 사용하는 데이터를 저장하거나 전송할 수 있는 형태로 바꾸는 것&quot;이라고 생각하자
쉬운 예 

책의 내용을 PDF로 변환하는 것
편지를 이메일 형식으로 바꾸는 것

📌 FastApi의 기본 사용법
경로 매개변수(path parameters)
FastApi에서는 경로지정이 아주 쉽게 되어있다 (아주 쉽다👍🏻)
기본 라우팅을 지정하고 다양한 매개변수를(CRUD) 만들어 사용하면 된다
# GET 요청
@app.get(&quot;/hello&quot;)
def hello():
    return {&quot;message&quot;: &quot;안녕하세요!&quot;}

# POST 요청
@app.post(&quot;/items&quot;)
def create_item():
    return {&quot;message&quot;: &quot;아이템 생성됨&quot;}
#여기까지는 너무 쉬우니 패스하자

#이렇게 여러 매개변수를 이용해 사용할 수 도 있다.
@app.get(&quot;/users/{user_id}/items/{item_id}&quot;)
def get_user_item(user_id: int, item_id: int):
    return {&quot;user_id&quot;: user_id, &quot;item_id&quot;: item_id}
써놓고 보니까 HTTP 메서드(@app.get, @app.post 등)가 아주아주 직관적이다👍🏻
그리고 경로 매개변수가 함수 매개변수와 자연스럽게 연결되는걸 볼 수 있다
또 편한 건 타입 힌트(int)로 자동 데이터 검증이 된다는게 아주 좋은 거 같다
쿼리 매개변수(Query Parameters)
또한 쿼리 매개변수가 있는데 아주 쉽다 이거 또한
걍 URL뒤에 ?가 붙는다고 생각하자
아래와 같은 예시가 존재할 때
@app.get(&quot;/search&quot;)
def search_items(
    q: str,              # 검색어 (필수)
    category: str = None, # 카테고리 (선택)
    min_price: float = 0, # 최소가격 (기본값 0)
    max_price: float = float(&#39;inf&#39;)  # 최대가격 (기본값 무한)
):
    return {
        &quot;search&quot;: q,
        &quot;category&quot;: category,
        &quot;price_range&quot;: {&quot;min&quot;: min_price, &quot;max&quot;: max_price}
    }
search?q=신발
search?q=신발&amp;category=스포츠
search?q=신발&amp;min_price=50000&amp;max_price=100000
요런식으로 호출하여 우리는 쿼리 매개변수를 호출할 수 있다 정리하자면
쿼리 매개변수: search?q=신발&amp;category=스포츠 (URL 끝에 ? 후 추가)
= ? 로 쿼리 시작
= &amp; 로 여러 매개변수 구분
📌 Pydantic 사용법
아래의 예시를 보며 다시 복기하자
뭐 별 다를 건 없다 그냥 pydantic라이브러리를 불러와주고
아래처럼 클래스 객체를 만들어 타입을 정하고 시작하면 알아서 검증해준다!
💡 pydantic의 BaseModel은 한마디로 이터 검증과 설정을 위한 기본 모델 클래스이다.
💡 (쉽게 설명하면 &quot;데이터의 형태를 정의하는 설계도&quot; 라고 생각하면 된다)
from pydantic import BaseModel

# BaseModel을 상속받아 User 데이터 모델 정의 예시
class User(BaseModel):
    name: str
    age: int
    email: str
    is_active: bool = True  # 기본값 설정 가능
🔥🔥🔥🔥 Validator 사용법!!!!
FastApi에서 사용 가능한 내가 무조건 사용해야 하는 데이터 검증 모듈이다
사용법도 간단하고 코드의 에러방지를 위해 무조건 사용하자!!!!
특정 필드의 데이터를 검사하고 싶을 때 사용하며 여러 필드도 한번에 검사할 수 있다.
⚠️ 주의할 점

반드시 @classmethod와 함께 사용해야 한다.

데코레이터 순서가 중요하다 (@field_validator 다음에 @classmethod)
class Product(BaseModel):
  price1: int
  price2: int
  price3: int

  # price1, price2, price3 모두 한번에 검사
  @field_validator(&#39;price1&#39;, &#39;price2&#39;, &#39;price3&#39;)
  @classmethod
  def check_price(cls, value):
      if value &lt; 0:
          raise ValueError(&#39;가격은 음수가 될 수 없습니다!&#39;)
      return value
이렇게 사용하면 데이터가 들어올 때 자동으로 검사해주니 코드가 훨씬 안전해진다!


📌 Swagger UI / ReDoc
요건 이미지가 있기에 따른 자세하게 설명되어 있는 공식문서를 참조하겠다.
Swagger UI URL : https://fastapi.tiangolo.com/ko/how-to/configure-swagger-ui/
ReDoc URL : https://redocly.github.io/redoc/

[원본 글 읽기](https://velog.io/@2joon_kim/Fast-api%EC%9D%84-%EB%8B%A4%EB%A4%84%EB%B3%B4Ja)
