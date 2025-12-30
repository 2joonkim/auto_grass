---
title: "Javascript를 더 deep 하게"
date: 2024-12-30
url: https://velog.io/@2joon_kim/Javascript%EB%A5%BC-%EB%8D%94-deep-%ED%95%98%EA%B2%8C
---

## 요약

슬슬 과부하가 오기 시작한다
여러 강의를 연속으로 들으니 앞서 배웠던 내용들도
뒤죽박죽이 되어가지만 네츄럴 말랑 brain을 단단하게
만들기 위해서 이악물고 강의를 들어본다
DOM 메소드 속성의 명령어를 알아보Java
상황에 따라 내 문서에따라 호출법을 사용하자
document.querySelector(값) /* 불러오거라 */
document.querySelectorAll(값) /* 다 불러라 */
document.getElementsByClassName(값) /* 클래스네임으로 불러라 */
document.getElementsById(값) /* 아이디로 불러와라 */
비교연산
크냐 작냐! 같냐 다르냐! 주어진 두 항을 비교할 수 있는
비교 연산자를 제공한다
boolean형 데이터를 사용해 반환을 한다
참 or 거짓
파이썬과 다른점이 있다면
&quot;===&quot; 완전히 같다 가 있다.
예를 들어 확인해보자
console.log(&#39;1&#39; == 1) // true
console.log(&#39;1&#39; === 1) // false

자로형과 데이터값이 모두 일치해야만 같다고 판단한다.
완전 엄격한(strict)비교라고 할 수 있겠다.
조건문
내가 가장 좋아하는 if문이 붙는 조건문이다
파이썬과 너무 흡사하기 때문에 쉽게 이해가 가능했다.
(아 오늘 코테 좀 풀고 자야겠다)
if(조건){
//조건이 true일 때 실행할 코드
}else{
  //조건이 false일 때 실행할 코드
  //if와 무조건 같이 써야한다.
}else if(조건){
 //조건이 하나가 아닌 다른 조건이 추가될 때 사용한다.
 //개수 제한은 없다. elif와 같은 느낌!
}
반복문
당연히 for문과 while문이고
이것도한 파이썬과 흡사하여 이해가 쉬웠다.
for(초기식; 조건식; 반복식){}
// 초기식 : 반복조건의 초기화 작업
// 조건식 : 반복조건의 마무리 조건
// 반복식 : 반복이 끝날때마다 실행 될 작업

while(조건){/*조건이 true인 동안에 반복 수행할 코드*/}
//while문은 조건이 참일 경우 계속~ 루프한다
조건안의 변수의 변화를 시켜주는것이 좋다
- 그래야 끝이 나니까!
DOM create!
지정된 이름의 html요소를 만들어서 반환이 가능하다
하지만 자바스크립트에서 만들어져 있는요소를 화면에
표시하는 작업을 추가로 해주어야 한다!!
그래서 appendChild가 들어간다!
document.createElement(&#39;div&#39;)
document.createElement(&#39;p&#39;)
document.createElement(&#39;a&#39;)

target.appendChild(자식으로_추가할_요소)
여기서 target은 &#39;div&#39; &#39;p&#39; &#39;a&#39;가 되겠다

[원본 글 읽기](https://velog.io/@2joon_kim/Javascript%EB%A5%BC-%EB%8D%94-deep-%ED%95%98%EA%B2%8C)
