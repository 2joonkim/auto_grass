---
title: "Django 를 deep하게 feat.- 284°C(체감)"
date: 2025-02-06
url: https://velog.io/@2joon_kim/Django-%EB%A5%BC-deep%ED%95%98%EA%B2%8C-feat.-284C%EC%B2%B4%EA%B0%90
---

## 요약

오늘도 정리를 하자..
정리하자..
정리..
정.
아휴 하기싷ㅇ..
여튼 Django 좀 더 딥하게 다뤄보라고 과제를 내주셨다
열심히 적으며 복습해보자
Django가 점점 익숙해져가..진 않지만 일단 열심히 공부하자
아직 제대로 시작도 안했기에 오늘도 정진한다..⭐️
1. Django Form
Django에서의 Form은 우리가 사용하는 여러가지의 사이트 중 말 그대로 Form이다.
Form이 뭐냐? = 구글링하셈; 그냥 웹사이트에서 자주 보는 입력창을 말한다
예를 들자면 회원가입 / 로그인 / 또 뭐 있냐.. 게시판 글 작성 등 이 있다.
대충 입력해서 쓸 수 있는 양식? 정도라 생각하면 편하다

Form 생성하는 법 (model 없이)from django import forms #말 그대로 장고의 forms를 쓸거기 때문에 장고의 form 클래스를 가져온다



class 하기싫어form(forms.Form): #나는 하기싫어 form을 만들었고 form 안에 들어갈 내용들을 적었다.
    성격 = forms.CharField(max_length=100) #문자만 가능 최대 100자
    3대몇 = forms.IntegerField() #숫자만 가능 
    헬스장주소 = forms.CharField(max_length=100) #문자만 가능 최대 100자
내가 만든 하기싫어 form 에는 성격과 3대몇치는지 그리고 헬스장 주소를 입력하라고 되어 있다.
forms.들어갈 내용의 입력값(이 입력값의 범위)
요렇게 간단하게 생각하면 된다
- Form 생성하는 법 (model 사용)
```python
# 근데 만약 폼을 만들기 전 폼의 모델이 존재한다면 걍 모델을 갖다 써도 무방하다
# 훨씬 더 간단해진다
from django.forms import ModelForm #나는 모델폼을 갖다쓸꺼야
from .models import 삼대측정 # 모델에 있는 회원정보를 쓸거야
# 당연하겠지만 일단 우겨넣고 시작하는거다 그래야 얘는 알아먹는다.

class 삼대측정Form(ModelForm): #모델폼안에 있는거 써야징!
    class Meta: #얘가 이 모델 담당자다 = 한마디로 대빵
        model = 삼대측정
        fields = [&#39;성격&#39;, &#39;3대몇&#39;, &#39;헬스장주소&#39;] #모델 안에 있는 내용 중 어떤거 써 먹을지?
        fields = &#39;__all__&#39;  # 이렇게 하면 모델 안에 있는 내용들도 싹다 가져올수 있다.

         # 추가로 이것도 할 수 있는데
         # exclude = [&#39;필라테스&#39;] #예를 들어서 내가 지금 3대 측정하는곳에 
         # 필라테스 하는 사람이 오면 안되니까 &#39;필라테스&#39; 만 빼고 다 가져올 수 있다.
         # 그리고 fields / exclude 는 하나만 사용 가능하니 작성할때 나처럼 멍청한짓은 하지말자 
widgets

위젯은 말 그대로 내가 위에 생성한 폼의 입력값을 이쁘게 꾸민다고 생각하면 된다.
아래 예를 들어서 설명해보자면

class 삼대측정Form(forms.Form):
    성격 = forms.CharField(
        widget=forms.TextInput(
            attrs={&#39;class&#39;: &#39;my-input&#39;, &#39;placeholder&#39;: &#39;자네는 헬스인재인가? 성격을 서술하라&#39;}
        )
    )

# 대충 요렇게 작성했을 때 my-input은 CSS 클래스 이름이다 그냥 외우자 = 스타일 꾸밀 때 씀 ㅇㅇ
# placeholder또한 해석 그대로 공간 어캐감쌀거냐? 얘한테 알려줘야지~ 라고 생각하면 편하다
# ㄴ 우리가 아이디 입력할때 희미하게 알려주는 공간 이라고 생각하자

CreationForm

CreationForm은 그냥 생성 전용 폼이라고 생각하면 편하다
위에 modelForm안에서 파생된 폼이라고 하는데 그냥 생성하여 쓰는거랑 똑같다고 보면 된다.

# 그냥 일반적인 ModelForm의 예시
class 운동일지Form(forms.ModelForm):
    class Meta:
        model = 운동일지
        fields = &#39;__all__&#39;
    # 이 폼은 그냥 운동일지안에 있는 내용들을 다 갖다 쓸 수 있음

# CreationForm의 예시
class 운동일지생성Form(forms.ModelForm):  # Creation = 생성
    class Meta:
        model = 운동일지
        fields = [&#39;운동이름&#39;, &#39;세트수&#39;]
    # 이 폼은 오직 운동일지 안에서도 이름이랑 세트수만 셀때 쓴다고 보면 됨 왜냐?
    # 필드안에 내가 생성하고 싶은 내용들을 명확하게 적어놨기 때문에 그럼 
    # 물론 여기서 우리가 수정과 삭제 또한 추가한다면 가능하다 = 요건 views에서 구현을 해야겠지만


AuthentiactionForm

Django는 친절하게 폼도 만들어놨다 근데 만들거면 좀 더 친절하게 만들지 겁나어렵네 ㅡㅡ 여튼
AuthenticationForm은 &#39;로그인 전용&#39; 폼이다 
걍 쉽게 말해서 로그인 할 때 쓰는 폼이라고 생각하면 편하다 뭐 그거말고 설명이 없다 이건..
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth import login

# django.contrib.auth.forms 요기서 AuthenticationForm 가져오고
# django.contrib.auth 요기서는 login을 가져왔다.
# 간략하게 설명하자면 첫번째 라이브러리는 걍 로그인 회원가입폼이 들어있는 장고 라이브러리다
# 두번째는 .forms만 빠졌고 인증관련 라이브러리라고 생각하자

# 요 아래 패턴은 django 공식문서에서 쓰이는 공식 로그인view 패턴이다
# 공식문서를 생활화 하자 ^&amp;^ yeah
# 아래는 로그인 기준 그냥 이해하기 쉽게 헬스장에 들어가는 과정을 예로 든 것이다.

def 헬스장_들어가기(request):
    if request.method == &#39;POST&#39;: # POST요청을 받고 폼이 제출이 뙇 됐다
    # 그럼 AuthenticationForm얘는 request를 꼭 받은상태로 들어가야된다
    # 아니면 출입불가 request = 헬스장 회원번호

        form = AuthenticationForm(request, request.POST) 
        # Django가 헬스장 인포여서 알아서 username/password을 봄
        # 검증된 헬창들 정보를 가져옴

        if form.is_valid():  # 아 이건 밑에서 설명할라햇는데.. 걍 맞는지 확인작업
            login(request, form.get_user())
            # form.get_user()는 AuthenticationForm에만 있는 특별한 메서드라고 한다. = 헬스장에 있는 사람인지 진위 확인중

            return redirect(&#39;나가임마&#39;) #만약 아니라면 나가라고 욕을 하는 상황
    else:
        form = AuthenticationForm()  # 헬스장 들어오실? 가입하셈 ㅇㅇ
    return render(request, &#39;헬스장.html&#39;, {&#39;form&#39;: form})
    # 그럼 우리는 회원가입 폼을 주는거다 그제서야


is_valid()

위에서 설명이 간략하게 되어 있지만 진위여부 확인 즉 이게 맞는 데이터값인지 보는거다
내가 3대가 몇인지 물어봤더니 엙으앍욽넱르ㅔㅇㄱ 이렇게 적으면 안되니까 ^^
# 예를 들어 헬스장 가입폼이 이렇다면

class 헬스장가입Form(forms.Form):
    이름 = forms.CharField(max_length=10)  # 꼭 채워야 하고, 10자 이하
    3대 = forms.IntegerField()           # 꼭 채워야 하고, 숫자만
    이메일 = forms.EmailField()           # 꼭 채워야 하고, 이메일 형식만

# is_valid()는 위에 나와 있는 내용 중 그런것들을 본다.
# 너 이름 썼냐? 10자 넘지 않는지
# 너 3대 썼지? 진짜 숫자맞지?
# 이메일도 쓴거 맞지? 안쓴거 아니지? 골뱅이는 붙여야 이메일이지 임마 이런느낌
2. Django ORM
ORM(Object-Relational Mapping)은 쉽게 말해서 
파이썬 코드로 데이터베이스를 다룰 수 있게 해주는 도구다
flask에서도 ORM을 썼었는데 여기서도 Python과 친한 우리는
데이터를 Python으로 다룰 수 있게 도와준다 👍🏻
쉽게 얘기해서 SQL문을 쓸때에는 계속 손아프게 대소문자 구별해가며 써야되는데(맥os 짜증;)
SELECT * FROM 어쩌구 이거 찾아라를
어쩌구.objects.filter(요런요런 값 찾아줭)을 할수가 있다.

Django ORM 의 특징

일단 장고는 model 기반이다 우리가 기가막히게 작성한 models.py를 바탕으로
python코드로 데이터를 다룰 수 있게 된다.
인터넷에서 퍼온 official 특징들을 일단 먼저 보자면
SQL을 몰라도 데이터베이스 조작 가능 = 맞음
파이썬 문법으로 데이터베이스 조작 = 맞음
자동으로 SQL로 변환해줌 = 맞음
SQLite, PostgreSQL, MySQL 등 어떤 DB를 써도 같은 코드 사용 가능 = 맞음
내가 생각하는 실제 경험에서 우러러나오는 특징으로는
두가지가 가장 크게 와닿았던 것 같다.
1. SQL문 몰라도 된다 = ORM 방식 호출만 쓰면 댐 (물론 SQL문을 알고있어야 이해가 빠름)
2. 보기 좀 쉬움

예를 들어서
# SQL 버전
&quot;INSERT INTO 헬스장회원 (이름, 나이) VALUES (&#39;근육맨&#39;, 25);&quot;

# Django ORM 버전
헬스장회원.objects.create(이름=&#39;근육맨&#39;, 나이=25)
장고 버전이 훨씬 보기 쉬운거 같다 ^^

Django ORM 의 기본적인 사용방법

장고 ORM의 기본적인 사용법은 너무 예시가 많아 그냥 코드로 대체하겠다.
사용법이 직접 치는거 말고 뭐가 더 필요할까 😎
# 그냥 지금부터 하나의 헬스장이라 생각하면 편하다
# 나는 언제나 그랬듯이 내가 편한대로 예를 드는게 좋기 때문에 또 헬스장으로 예를 들겠다.

# objects
모든_회원 = 헬스장회원.objects.all() 
# objects는 매니저의 개념이다 얘가 다 불러와서 문제를 해결한다.
# 그래서 밑의 명령어를 보면 
# 헬스장회원.objects.어떻게찾을건데(조건) 이렇게 되어있다. 참고하자

# filter
성인_회원 = 헬스장회원.objects.filter(나이__gte=20) 
#필터는 말 그대로 필터! 저건 회원들 중 20살만!

# get
회원 = 헬스장회원.objects.get(id=1)
# 근데 get은 unique한 고유값이 아니고 결과가 없거나 여러개일때 에러가 난다고 한다.
# 이미 존재하는게 확실하고 중요한 정보를 찾을 때 쓰도록 하자

# order_by
회원목록 = 헬스장회원.objects.order_by(&#39;나이&#39;, &#39;-가입일&#39;)  
# 나이 오름차순, 가입일 내림차순 / -요게 붙으면 내림차순으로 보여준다

# create
새회원 = 헬스장회원.objects.create(
    이름=&#39;김근육&#39;,
    나이=25
)
#뭐 이건 설명이 필요할까.. create다.. 크리에이트 만들다라는 뜻이다 ^^^

# delete
회원 = 헬스장회원.objects.get(id=1)
회원.delete()
#이것도 뭐..삭제임.. 어려울게 없어서..

# update
# 업데이트는 방법이 두가지일거 같은데 특정아이디를 알거나 이름을 알면 그걸 조회 후 변경
# 특정 나이대 혹은 특정 정보를 가진 사람들을 한꺼번에 변경할 때
회원 = 헬스장회원.objects.get(id=1)
회원.나이 = 26
회원.save()
get_object_or_404
# 👆 요건 쉽다
# 👇 요게 어렵지
헬스장회원.objects.filter(나이__lt=20).update(회원등급=&#39;뉴비헬창&#39;)
# 예를 들어서 나이 20살인 애들은 모두 뉴비헬창으로 바꾸고싶을 때
# 필터를 통해 나이가 20살인 애들을 추려서 update를 사용해 회원등급을 뉴비헬창으로 바꾼다.

# get_object_or_404
# 이건 뭐 페이지 내에서 보여주는 에러형식으로 404에러 많이 봤잖아요 우리 다 ^^
# 게임 좋아하면 한번씩 보지 않나....
from django.shortcuts import get_object_or_404
# 일단 shortcuts에서 get_object_or_404을 넣고
회원 = get_object_or_404(헬스장회원, id=회원_id)
# 요렇게 해주면 내가 적은 멘트와 함께 404가 출력된다 뭐 이건 걍 오류 출력이라
# 없는값 입력 안하면 된다 = 꼭 하지말라면 하는 한국인들이 많다.
이렇게 보면 참 쉬운거 같지만 이게 다 합쳐지고 이것저것 조건들이 붙기 시작하면서
머리가 터진다. 진짜임
이제 슬슬 Auth까지 나오는데 여기서부터 또 터짐
지금 내가 그럼
3. Django Auth
Auth.. 인증이다.. 인증관련 모델은 accounts가 나온다..
여기서 부터 조금씩 복잡해지기 시작한다..
(아니 사실 복잡한게 아니라 기능이 많아지면서 점점 늘어나니까 짜증나는거 뿐이다..)
사실 개념은 너무 쉽다.
Django에서는 보통 회원 관리할 때 accounts라는 이름의 앱을 만든다고 한다.
(다른 이름을 써도 되긴 한데.. Django의 관례라고 한다. 뭐 기업에 따라 다른 이름도 쓰겠지?)

Custom UserModel

일단 Custom UserModel부터 보자면 Django에서 제공하는 모델이 아니라
Custom 우리가 직접 만드는 UserModel 이라 생각하면 쉽다.
걍 말 그대로 = 장고꺼 안쓰고 내가 만들래 아오 🔫
# AbstractUser
from django.contrib.auth.models import AbstractUser
# 장고의 순 기능 여기에 걍 넣기만 하면 된다 :)
class User(AbstractUser):
    근육량 = models.IntegerField()
    기초대사량 = models.IntegerField()
# 이런식으로 User에 (AbstractUser) 요렇게 넣어주고
# 장고의 기본 User 모델을 거의 그대로 가져다 쓰는 방식이다
# username, password, email 등이 이미 다 들어있음
# 여기에 내가 원하는 필드만 걍 추가하면 됨
# 제일 쉬움;;
# AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser
# 아까와 동일하게 auth.models에서 AbstractBaseUser를 넣어준다.
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    이름 = models.CharField(max_length=50)
    가입일 = models.DateTimeField(auto_now_add=True)
# 이게 그냥 완전 백지상태에서 시작하는 방식
# 기본 필드가 password 빼고는 아무것도 없음
# 모든 걸 직접 다 만들어야 함 = 난 못함
# 어렵지만 자유도가 높음 = 이것도 그러네
이제 여기에 붙어야 할 도구들을 알아보자
이렇게 만들었다면 여기에 또 부가적으로 붙여야 하는 도구들이 참 많다.
# PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# AbstractBaseUser이거 쓸 때 권한 관련하여 같이 쓴다고 함
class User(AbstractBaseUser, PermissionsMixin): #옆에 같이써줌
    email = models.EmailField(unique=True)
# 요런식으로 관리자 권한을 부여하거나 다 같이 관리할 수 있게끔 만들어줌
# 얘 AbstractUser는 이미 얘를 포함하고 있어서 안써도 되는데
# 얘 AbstractBaseUser는 진짜 기본적인것만 있어서 관리자 권한도 추가해줘야 관리가 가능함
# 그래서 어렵다고 한거다 %%^^^^^^^ 


# BaseUserManager
from django.contrib.auth.models import BaseUserManager
# 이렇게 넣어주고
class MyMuscleManger(BaseUserManager):
# 하고 아래 기본적인 내용을 받고싶을 때
# 기본내용은 - create_user / create_superuser 요거 두개뿐이다;;
# BaseUserManager 요놈을 써서 진행한다.
# 이거 또한!!!! AbstractBaseUser만 해당 ㅡㅡ
# AbstractUser는 이미 이 기능이 있음


# UserManager
from django.contrib.auth.models import UserManager
# 이렇게 넣으면 되고
# 예시로 또 작성해 보자면
class CustomMuscleManager(UserManager):
    def muscle_user(self, email, password=None, muscle_mass):
        return super().create_user(email, password=password)
# 위와 같이 편하게 작성을 할 수가 있다.
# BaseUserManager얘 보다 더 좋고 많은 기능을 가지고 있으며
# 애초에 AbstractUser쓸 때 따라온다.
# 보통 따로 건드릴 일은 없음

Authenticate() / Login() / Logout() / login_required 데코레이터 함수# Authenticate() = 검증하는거다
user = authenticate(username=&quot;근육맨&quot;, password=&quot;1234&quot;)
# 얘는 그냥 인증담당이다 헬스장 들어오는지 보는 역할이다. 
# 아디랑 비번이 맞는지 틀린건지 아닌지 검증한다.
# 예를 들어 헬스장 회원권 찍는지 안찍는지 검사하는 역할



Login() = 걍 로그인..
login(request, user)
위에 Authenticate() 검증을 거친 user를 세션에 넣어주는 것
이것도 딱히.. 로그인은 다 알기에..
Logout() = 걍 로그아웃..
logout(request)
뭐 딱히 설명할 게 없다..
@login_required = 이제 이건 로그인을 해서 헬스장 출결하게끔 만드는 역할
@login_required # 👈🏻 진짜 이제 로그인 도장? 뭐라해야되나 페이스 아이디같은 역할이다
def 운동기구_예약(request):
   return render(request, &#39;예약.html&#39;)
그니까 운동기구 예약을 할라면 로그인이 되야 할 수 있으니 @login_required 설정해준다
이게 없으면 비회원도 url 타고들어와서 운동예약해버리면 답이없으니
로그인 안하고 들어오면? 바로 차단해야지
![](https://velog.velcdn.com/images/2joon_kim/post/89863e25-fac9-4a20-830b-15275def259b/image.jpeg)
거의다 끝났다. 이제 진짜 얼마 안남았다.
오늘거 진짜 쓸 거 많다. 그래도 아는 내용이 많아서 참 다행이다..
~~ㅠ 아오하기싫ㅇㅇㅎ~~
잠깐 쉬어가는 시간..
빨리 쓰고 다른거 해야지..

## 4. CBV(Class Base View)

어제 한번 설명했지만 FBV를 할때 짧게 한번 적어놨었다.
둘의 차이라고 한다면 함수를 쓰냐 클래스를 쓰냐 그 차이이다.
그래도 좀 더 깊게 들어가서 정의를 내리자면 이건 그냥 개념은 알고 있으나
쉽게 설명하자면 
FBV = 간단 + 처음부터 짜봐야 몇줄 안되는 코드 easy~
CBV = 반복작업 + 여러가지 기능들 있음 + 복잡하여 코드를 재사용해야할 때 easy~

아래 내용정리를 통해 다시한번 외워버리자 걍
(Claude가 열일해서 알려준다 정확하다 아주 i love Claude)
```bash
💡 FBV는 간단하고 직관적이에요 (초보자한테 좋음)
💡 CBV는 코드 재사용이 쉽고 깔끔해요 (복잡한 기능 만들 때 좋음)
어떤 걸 써야 할까요?

📌 FBV 쓰기 좋을 때
간단한 로직
특별한 처리가 많이 필요할 때
CBV 커스텀하는 것보다 처음부터 짜는게 더 쉬울 때

📌 CBV 쓰기 좋을 때
CRUD 같은 반복적인 작업
비슷한 기능을 여러 곳에서 쓸 때
많은 기능이 이미 구현되어 있는 걸 쓸 때

그리고 FBV / CBV의 큰 차이점 중 하나는
FBV: 그냥 &quot;야 일로와봐&quot; 하면 오는데
CBV: &quot;야 일로와봐&quot; 하면 안 되고 &quot;야 일로와봐.as_view()&quot; 해야 옴
= .as_view()라는 메서드로 함수로 변환해야 애가 온다
View / Generic Viewsview
# 이건 적을게 하도 많아 그냥 코드로 정리하는게 나을 거 같아
# 또 베스트 예시인 헬스장으로 예를 들겠다.
# FBV와 기능구현은 비슷하나 CBV를 이용하여 기능을 구현하려고한다.
# Ai chego god claude ⭐️⭐️⭐️



view
from django.views import View
class 헬스장입장(View):
    def get(self, request):
        # GET 요청 = 회원이 그냥 헬스장 둘러볼라고 할때 와 동일
        return render(request, &#39;입장.html&#39;)
def post(self, request):
    # POST 요청 = 이제 일일권 끊어야겠다 싶어서 얼마에요? 하고 들어오려는거
    회원번호 = request.POST.get(&#39;회원번호&#39;)
    # ... 입장 처리 로직 ...
    return redirect(&#39;입장완료&#39;)#### Generic Views
```python
# 자 이제 헬스장에 입장했으니 각각의 특수한 환경에 접근을 해야되지 않겠음?
# PT 등록도 있을테고 뭐 회원권 수정도 해야하고 뭣도하고 뭣도하고 등등
# 비유 기가막히다 캬
# 그래서 아래에 정리를 하나하나 해보자면

# CreateView = 새 회원 등록 카운터
class 신규회원(CreateView):
   model = 헬스장회원
   fields = [&#39;이름&#39;, &#39;PT횟수&#39;]

# UpdateView = PT 횟수 수정 카운터
class PT수정(UpdateView):
   model = 헬스장회원
   fields = [&#39;PT횟수&#39;]

# ListView = 회원 명단 보는 모니터
class 회원목록(ListView):
   model = 헬스장회원

# DetailView = 회원 상세정보 창구
class 회원상세(DetailView):
   model = 헬스장회원

# DeleteView = 회원 탈퇴 창구
class 회원탈퇴(DeleteView):
   model = 헬스장회원

# TemplateView = 공지사항 게시판
class 공지사항(TemplateView):
   template_name = &#39;공지.html&#39;

# FormView = 운동일지 작성대
class 운동일지(FormView):
   form_class = 운동일지폼CreateView: 새로운 데이터 생성(회원가입)
UpdateView: 기존 데이터 수정
ListView: 목록 보여주기
DetailView: 상세 정보 보여주기
DeleteView: 데이터 삭제
TemplateView: 단순 페이지 표시
FormView: 폼 처리
정도로 이해하면 가장 쉽게 이해할 수 있을 거 같다.
✨!!!!!!!!라스트 정리!!!!!!!!✨
이렇게 View는 기본 입구고
Generic Views는 각각 전문적인 일을 하는 카운터.

request

헬스장 예로 계속 들고 있는데 오늘은 헬스장을 선택하길 잘한거 같다. 겁나쉽게 비유가되네;;
여튼 계속 써보자면 request는 말 그대로 요청이다 = 회원이 헬스장에 뭔가를 요청하는 것
# 어김없이 등장하는 헬스장 모습
# user 가져오기 = 지금 요청한 회원이 누구야?
현재회원 = request.user  # 지금 로그인한 회원 정보

# data 가져오기 = 회원이 뭘 달라고 했어?
작성내용 = request.POST.get(&#39;내용&#39;)  # 회원이 폼에 쓴 내용
첨부파일 = request.FILES.get(&#39;운동법&#39;)  # 회원이 올린 운동법

# URL 파라미터 (Path Parameter) = 회원번호로 찾기
path(&#39;회원/&lt;int:id&gt;/&#39;, ...)  # 예: /회원/123/ 
# 123번 회원 찾아줘!

# 쿼리 파라미터 (Query Parameter) = 검색어로 찾기
검색어 = request.GET.get(&#39;search&#39;)  # 예: /회원search=김이준
# = 김이준씨 나오세요.

response

이것조차 비유가 아주 쉽다. response도 말 그대로 응답 = 헬스장이 회원한테 답해주는 것
아니 물어봤으면 답을 해줘야 되잖아요
# HttpResponseRedirect = 다른 페이지로 안내
return redirect(&#39;메인페이지&#39;)  # 회원님 덤벨은 저쪽이요.

# HttpResponse = 직접 응답
return HttpResponse(&#39;성공!&#39;)  # 회원님 잘하셨어요. 두개만 더해볼게요.

# status code = 처리 결과
200 = 회원님 잘 하셨어요
404 = 회원님 물만 먹어도 살찌는건 없어요.
500 = 헬스장 문 닫았나? 아 오늘 쉬는날이네..
# 이건 진짜 그냥 주관적인 해석이 들어간 예고
# 아래를 보자
200 = 요청 성공
404 = 요청한 리소스 못 찾음
500 = 서버에서 처리 중 에러가 발생


# response data = 응답 데이터
return JsonResponse({
   &#39;message&#39;: &#39;어서오세요 돼지고갱님&#39;,
   &#39;pt_횟수&#39;: 100
})  # 들어갔을 때 나오는 회원 정보
5. Django Mail
말 그대로 장고에서 메일을 보낼 수 있는 서비스이다
나는 이거 라이브 강의를 들으며 딱 한번 써 봤는데..
사실 이걸 어디서 이용해야 할 진 모르겠다
무슨 이메일 보내는 대형 서비스가 아니고서야 내가 메일 서비스를 사용할 일 이 있을까..?
(아직 몰라서 혹시라도 누군가 읽는다면 어디서 쓰는지 좀..)
📌 검색해보니 어떤 서비스에서 보안이나 중요사항같은거 전달할 때 많이 쓴다고함
📌 뉴스레터도 이걸 통해서 서비스하게 된다면 사용하면 편리할 거 같다
추가 의견 받음!!!!!!!!!!

django.core.mail.send_mailfrom django.core.mail import send_mail



send_mail(
    &#39;ㅎㅇ 헬창들아&#39;,  # 이메일 제목
    &#39;니네 3대 500미만 나시입으면 죽는다;&#39;,  # 이메일 내용
    &#39;hellchang_master@example.com&#39;,  # 보내는 사람 이메일
    [&#39;newbie_hellchang@example.com&#39;],  # 받는 사람 이메일 = 많으면 리스트로 넣으셈
)
- django.core.signing
```python
from django.core import signing

# 데이터 서명하기
value = signing.dumps({&quot;user&quot;: &quot;헬창&quot;})

# 서명된 데이터 확인하기
original = signing.loads(value)  # {&#39;user&#39;: &#39;헬창&#39;} 이렇게 나와요
- django.core.signing.TimestampSigner

# 이 부분은 나도 정확하지 않아서 찾아봤는데
# 비밀번호나 아이디 재설정 링크를 보내준다거나 / 결제관련 메일을 보낸다거나 등
# 보안에 민감한 사항들을 보낼 때 사용한다고 한다.
# 데이터가 변조되지 않았음을 증명해주고 누가 데이터를 수정하면 바로 알 수 있다고 한다.
# 사용해본적이 없어서 모르게씀 ㅠ일단 두번째 장고 정리 끗!
정리하고 나니 이해가 좀 빠르긴 하다
다음번엔 디버깅을 좀 더 확실하게 잡고 가야겠다.
특히 보안 + 디버깅은 좀 더 신경써서 작성을 해두도록 해야겠다.
끗

[원본 글 읽기](https://velog.io/@2joon_kim/Django-%EB%A5%BC-deep%ED%95%98%EA%B2%8C-feat.-284C%EC%B2%B4%EA%B0%90)
