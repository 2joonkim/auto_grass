---
title: "FastApi를 더 알아보Ja"
date: 2025-02-18
url: https://velog.io/@2joon_kim/FastApi%EB%A5%BC-%EB%8D%94-%EC%95%8C%EC%95%84%EB%B3%B4Ja
---

## 요약

요즘 그래도 슬슬 다시 재미가 붙어서 다행이다
할게 너무나도 많아서 잠깐 뇌가 망가져 있었는데
주말동안 푸욱쉬고 나니까 다시 일하라고 뇌에서 명령을 내리는 것 같다
아무튼 요즘은 FastApi에 미쳐 살고 있는중이다
내가 가장 배우고싶었던 웹프레임워크이기도 했고
가장 좋은점은 난이도가 타 웹프레임워크에 비해 쉽다는 점이다 ^.^
아 근데 뭔가 이해가 더 빠르게 가는건 Django인거 같은데..
아무튼 오늘도 예쁘게 정리를 시작해본다
지금까지 배운건 막힘없이 뇌 속에 넣었기 때문에
아주 기초적인 부분들은 따로 이제 정리를 안하려고 한다
(물론 나중에 또 복습한답시고 이것저것 적을게 뻔하다)

  



📌 FastApi - Background Task?
FastApi에서의 Background Task란 무엇인지 정의부터 내리고 가자
Background Task는 HTTP 응답을 반환한 후에 실행되는 작업을 의미한다
예를 들어 내가 이메일을 보내고 싶어서 이것저것 타이핑한 후
이메일 보내기를 누른다면? 우리는 바로 전송되는 걸 확인할 수 있다
이메일을 보냈다면? 우리가 이메일이 전달 될 때 까지 기다릴 필요가 있느냐?
아니다 우리는 이메일을 성공적으로 전달이 되었다는 창만 보고나서는 
다른 작업들을 진행할 수 있다!
다만 컴퓨터는 Background Task를 통해 이것저것 복잡한 여러가지 과정들을 거치고
내가 보내고싶은 사람에게 메일을 안전하게 전송한다!
이 과정속에서 Background Task를 통해 우리는 특정 작업을 위해
대기를 하는 번거로움을 줄여줄 수 있다!!

정적으로 정리를 해보자면🔥
HTTP 요청에 대한 응답은 즉시 클라이언트에게 반환
Background Task는 응답이 전송된 후 비동기적으로 실행
클라이언트는 응답을 기다리지 않고도 다음 작업을 진행 가능
이제 주의사항도 알아보자❗️
Background Task는 응답이 전송된 후에만 실행
너무 긴 작업은 Celery나 다른 작업 큐 시스템을 고려 필요
서버가 재시작되면 실행 중이던 Background Task는 손실 가능성 존재

아래 코드 예시를 보고 내용을 좀 더 디테일하게 다듬어보자
오늘 학습한 따끈따끈한 예제이다
@app.post(&quot;/upload-file/&quot;)
async def upload_file(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks(), db: Session = Depends(get_db)):
    file_content = await file.read()  # 파일을 미리 읽어서 백그라운드 작업으로 전달
    background_tasks.add_task(save_file, file.filename, file_content)
    background_tasks.add_task(log_file_upload, file.filename, db)
    return {&quot;message&quot;: &quot;파일 업로드 중...&quot;}
💡 실제 동작
file.read(): 업로드된 파일의 내용을 읽는다
background_tasks.add_task(): 두 가지 작업을 백그라운드에서 실행한다
데이터베이스에 로그 기록하고
사용자에게는 즉시 &quot;파일 업로드 중...&quot; 메시지를 보여준다
💡 동작 순서
사용자가 파일 업로드 ➡️
파일 내용 읽기 ➡️
백그라운드 작업 예약 ➡️
사용자에게 응답 전송 ➡️
백그라운드에서 파일 저장 및 로그 기록 ✅
이렇게 하면 대용량 파일을 업로드해도 서버가 멈추지 않고 
사용자도 오래 기다리지 않아도 되는 장점이 있다
그래서 포스트맨으로 쏴보면 아래와 같이 나오는걸 볼 수 있다 ^&gt;^

  
    
    
  



📌 FastApi - WebSocket?
오늘 학습한 내용중에서 가장 재미있었다
왠지 모르게 와 이거 하면서 내가 뭔가 어이없게 뿌듯하면서 신기했는데
사실 실시간으로 테스트할 수 있다는게 너무 갑자기 흥미가 생겨서
미친듯이 재밌게 알아본 것 같다
WebSocket이란 쉽게 얘기해서 실시간 통화라고 생각하면 편하다
일반적인 HTTP 통신은 마치 편지를 주고받는 것과 똑같다고 치면
➡️ 클라이언트가 요청(편지)을 보낸다
➡️ 서버가 응답(답장)을 보낸다
➡️ 쓸말 없으면 통신을 종료해버림
⬆️ 새로운 정보가 필요하면 다시 요청을 보내야 된다 (위로 반복)
반면 WebSocket은 실시간 통화인데
➡️ 한 번 연결이 되면 양방향으로 실시간 대화가 가능
➡️ 서버도 클라이언트에게 먼저 메시지를 보내는 것이 가능
➡️ 연결이 끊어질 때까지 계속 통신 유지
아주 좋은 예를 들고 와서 개념 자체는 이해가 쉬울 것 같다

다시 정적으로도 정리를 해보자면🔥
WebSocket은 실시간으로 지속적인 양방향 통신이 필요한 경우에 사용되는 프로토콜❗️

아래의 예시코드를 보고 더 디테일하게 다듬자
이것도 오늘 학습한 따끈따끈한 코드이다
class ConnectionManager:
    &quot;&quot;&quot; WebSocket 연결 관리 &quot;&quot;&quot;
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        &quot;&quot;&quot; 클라이언트가 WebSocket 연결을 요청하면 리스트에 추가 &quot;&quot;&quot;
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        &quot;&quot;&quot; 클라이언트 연결 종료 시 리스트에서 제거 &quot;&quot;&quot;
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        &quot;&quot;&quot; 모든 연결된 클라이언트에게 메시지 전송 &quot;&quot;&quot;
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket(&quot;/ws&quot;)
async def websocket_endpoint(websocket: WebSocket):
    &quot;&quot;&quot; 클라이언트가 /ws 경로로 WebSocket 연결 요청 &quot;&quot;&quot;
    await manager.connect(websocket)
    try:
        print(f&quot;접속된 인원: {len(manager.active_connections)}&quot;)
        while True:
            data = await websocket.receive_text()  # 클라이언트에서 데이터 수신
            await manager.broadcast(f&quot;📢 새로운 알림: {data}&quot;)  # 모든 연결된 클라이언트에 전송
            print(f&quot;클라이언트로부터 받은 메시지: {data}&quot;)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print(&quot;클라이언트가 연결을 종료했습니다.&quot;)
💡 실제 동작
➡️ 새로운 클라이언트 연결 수락 = 요건 로컬환경이니 내가 되겠다
➡️ 실시간 메시지 수신 및 브로드캐스트 = 실시간 메세지 수신/발신(포스트맨) 가능
✅ 연결 종료 처리 = 연결 종료
💡 작동 방식
➡️ 클라이언트가 /ws 엔드포인트로 WebSocket 연결을 요청
➡️ 서버는 연결을 수락하고 active_connections 리스트에 추가
➡️ 무한 루프에서 클라이언트로부터 메시지 대기 = data = await websocket.receive_text()
➡️ 메시지를 받으면 &quot;📢 새로운 알림: [data]&quot; 형식으로 모든 연결된 클라이언트에게 브로드캐스트
➡️ 클라이언트가 연결을 종료 시 WebSocketDisconnect 예외가 발생하고 해당 연결을 리스트에서 제거!

 
   
     
   
   
     
   
   
     
   
 


고러면 이렇게 아주 예쁘게 출력되는걸 볼 수 있다
오늘의 FastApi 끗~

[원본 글 읽기](https://velog.io/@2joon_kim/FastApi%EB%A5%BC-%EB%8D%94-%EC%95%8C%EC%95%84%EB%B3%B4Ja)
