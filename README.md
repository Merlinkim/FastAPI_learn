# FastAPI_learn
해당 레포는 저의 학습을 위한 레포입니다<br>
또한 해당 레포를 통해서 fastapi의 작동 원리와 방식을 다른 분들이 습득하고 얻어가실수 있다면 좋겠습니다.
<br>
1. 시작<br>
<br>
!explain.py 레포를 확인해주세요!

API application programming interface 
API는 어플리케이션 소포트웨어를 빌드하고 통합하기 위한 정의 및 프로토콜 세트입니다.

아직 말이 어렵습니다. 조금더 쉽게 말해보도록 하겠습니다.

프로그래밍에서 어플리케이션은 하나의 제품이라고 말할수도 있습니다.
여기서 프로그래밍을 빌드하고 통합한다는 말을 웹 어플리케이션의 관점에서 보겠습니다.
여기 프론트엔드와 백엔드 서버가 있습니다.
프론트엔드는 유저에게 사용가능한 UI를 제공하고 동적 페이지를 제공합니다.
백엔드는 프론트에서 생성되는 어떠한 데이터를 RDBMS에 옮기기도 혹은 어딘가에 저장하기도 합니다.
그렇다면 서로 어떠한 방식으로 통신할까
네 맞습니다. API방식으로 통신하는 경우가 많습니다.
물론 완전 맞다고는 하지 못하지만, API는 무언가에게 정보를 주고 정보를 받는 소프트웨어라고 말할수 있겠습니다.


API를 왜 써야하나
API를 사용하면 구현방식을 알지못하는 제품 또는 서비스와 통신할수 있습니다.
API구현체에 대한 코드 혹은 기술적 이해보다는 API가 주는 데이터의 형태 혹은 줘야하는 데이터의 타입을 알아야합니다. 기술적이해보단 더 쉬운 개념이죠.

정리
1. API는 무언가와 통신하기 위한 하나의 규칙이다.
2. API를 사용한다면 비용적인 부분에서 절감할수 있다.
3. 어플리케이션을 만드는데 있어 분업을 더 나누어 할수 있다.
4. 구현체에 대한 코드 공개를 하지 않아도 알지 못해도 데이터의 유형과 형태를 알면 사용가능하다.

API의 종류

(접근방식에 따른 분류)
1.Private API
해당 API는 어떠한 그룹 혹은 단체에서 내부 사용용으로 제작된 API를 뜻합니다.

2. PUblic API
Public API는 말 그래돌 public,개방형 API이다.
Public API중에서도 접속하는 대상에 대한 제약에 없는 경우를 OpenAPI라고 한다.

3. Partner API
특정 비지니스 파트너 간의 데이터 공유 API

(아키텍쳐 스타일에 따른 API)
1.REST API
2.GraphQL
3.SOAP,RPC
하지만 가장 많이 쓰이는 것은 REST API이고 GraphQL까지는 쓰이긴하지만 나머지 아키텍처 스타일은 사실상 잘 사용하지 않는다.

1. REST API
간단하다 REST란 아키텍쳐를 사용하는 API이다.
REST가 아키텍쳐인거 알았고 API는 통신하는 방법이라고 했다.
그러다면 REST라는 아키텍처링 되어 있는 통신 방법이다.

    1. REST API 기본
    CRUD method
    POST POST를 통해서 URL를 요청하면 리소스를 생성 -> Create
    GET GET를 통해 리소스를 조회 -> Read
    PUT PUT를 통해서 리소스 수정 -> Update
    DELETE 리소스 삭제 -> Delete

    2. GET and POST의 차이
