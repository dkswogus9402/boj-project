# 사용자 인증 및 권한

### Authentication System (인증 시스템)



Django 인증 시스템은 이미 django-contrib.auth에 Django contrib module로 제공

필수 구성은 settings.py에 이미 포함되어 있으며 INSTALLED_APPS 설정에 나열된 아래 두 항목으로 구성됨

1. django.contrib.auth
2. django.contrib.contenttypes



Authentication (인증)

- 신원 확인
- 사용자가 자신이 누구인지 확인하는 것



Authorization(권한, 허가)

- 권한 부여
- 인증된 사용자가 수행할 수 있는 작업을 결정



두번째 앱 accounts 생성하기

python manage.py startapp accounts

( 앱이름이 반드시 accounts 일 필요는 없음 )

단 auth와  관련해서 장고 내부적으로 accounts를 사용중이므로 accounts로 하는 것을 권장 



로그인 로그아웃을 하기전에 알아야 할 정보들

```
http : HTML문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜

HTTP 특징 :
1. 비연결 지향 (서버는 용어에 대한 응답을 보낸후 연결을 끈음)
	
2. 무상태(stateless)
	- 연결을 끊는 순간 클라이언트와 서버간의 통신이 끝나며 상태 정보가 유지되지 않음
	- 만약 네이버에서 로그인을 하고 뉴스로 들어갔을 때 다시 로그인을 해야한다면 이는 굉장한 불편함을 가지게 됨. 
		하지만 특징1 비연결지향으로 인해 상태 정보가 유지되지 않음
	- 클라이언트와 서버가 주고 받는 메시지들은 서로 완전히 독립적임
	
	- 클라이언트와 서버의 지속적인 관계를 유지를 하기 위한다면?!!
	
	#  쿠키와 세션이 존재 ##
```



쿠키 (개념) (1/2)

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 **작은 기록 정보**파일
  - 브라우저는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
  - 이렇게 쿠키를 저장해놓았다가 동일한 서버에 재 요청을 할 때 저장된 쿠키를 함께 전송

​	참고 )  



<img src="04-11.assets/image-20220411092517991.png" alt="image-20220411092517991" style="zoom:80%;" />



클라이언트 -> 로그인 -> 서버

서버 -> 응답 + 쿠키 -> 클라이언트



즉 쿠키는 기존의 상태가 없는 세션에서 상태가 있는 세션을 만들어줌

쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용

- 이를 이용해서 사용자의 로그인 상태를 유지할 수 있음
- 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억 시켜주기 때문 



-> 즉 웹 페이지에 접속하면 요청한 웹 페이지를 받으며 쿠키를 저장하고, 클라이언트가 같은 서버에 재 요청 시 요청과 함께 쿠키도 함께 전송됨



## 쿠키의 사용 목적

1. 세션 관리 (Sesstion management) : 로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리

2. 개인화 (Personaliztion) : 사용자 선호, 테마 등의 설정

3. 트래킹 (Tracking) : 사용자 행동을 기록 및 분석 

   

시크릿 모드는 쿠키를 허용하지 않는 모드



쿠키를 이용한 장바구니 예시

<img src="04-11.assets/image-20220411093134070.png" alt="image-20220411093134070" style="zoom:80%;" /> 

장바구니에서 네트워크로 들어오게 된다면



<img src="04-11.assets/image-20220411093210391.png" alt="image-20220411093210391" style="zoom:60%;" /> 



header에 set_cookie라고 되어 있는 곳이 실제 쿠키정보들임 또한 Cookies 탭에 들어가게된다면

<img src="04-11.assets/image-20220411093330241.png" alt="image-20220411093330241" style="zoom:80%;" /> 

요청 받는 곳과 응답받는 쿠키를 확인할 수 있음



제일 기본 홈페이지에서 쿠키 요청하는 것을 확인한다면

<img src="04-11.assets/image-20220411093543531.png" alt="image-20220411093543531" style="zoom:80%;" /> 

매우 많은 쿠키가 요청되는 것을 확인할 수 있음



![image-20220411093753521](04-11.assets/image-20220411093753521.png)

Application에 들어와서 Storage에 들어온 뒤 쿠키를 확인해보면 해당 사이트에 보내주는 현재 저장된 쿠키들을 볼 수 있음 



해당 쿠키들을 보고 추천 용품들이 나옴 -> 만약 쿠키를 지운다면 ?!

기존 추천 용품 등이 사라지는 것을 확인 할 수 있음





쿠키는 세션을 포함하는 개념



### 세션

#### 세션 : 사이트와 특정 브라우저 사이의 상태를 유지시키는 것

클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고 클라이언트는 발급받은 session id를 쿠키에 저장

- 클라이언트가 다시 서버에 접속하면 요청과 함께 쿠키 (session id가 저장된)를 서버에 전달
- 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞은 로직을 처리

ID는 세션을 구별하기 위해 필요하며 쿠키에는 ID만 저장함



클라이언트가 사이트에 최초 접속시 세션 id를 주고 클라이언트는 발급받은 id를 저장 -> 다시 접속요청을 보낼 때 세션 id를 보고 판단가능 즉 세션이 ID이다.



쿠키는 각 유효기간을 가지고 있다. 유효기간을 가지고 있지 않은 세션은 ?!!

즉 로그아웃은 세션을 삭제하는 과정이다.



### 쿠키 lifetime (수명)

쿠키의 수명은 두 가지 방법으로 정의할 수 있음

1. Session cookies
   - 현재 세션이 종료되면 삭제됨
   - 브라우저가 "현재 세션"이 종료되는 시기를 정의
     - 참고) 일부 브라우저는 다시 시작할 때 세션 복원을 사용해 세션쿠키가 오래 지속 될 수 있다고 함
2. Persisetent cookies (or Permanent cookies )
   1. Expires 속성에 지정된 날짜 혹은 Max-age 속성에 지정된 기간이 지나면 삭제

<img src="04-11.assets/image-20220411095508252.png" alt="image-20220411095508252" style="zoom:80%;" />



숙제 ) SWEA 사이트의 로그아웃 기간에 대해서 알아보자!



Django의 세션은 미들웨어를 통해 구현됨



장고는 database-back sessions 저장방식을 기본 값으로 사용 (본인의 데이터 베이스에 저장한다.)

​	설정을 통해 cached , file-based, cookie-based 방식으로 변경 가능



장고는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아냄

세션 정보는 Django DB의 django_session 테이블에 저장됨



장고 id만 session으로 사용하지 않고 전부 session으로 전달해준다면 ?! -> 상호작용하는 데이터를 확인하는 단계가 많아지기 때문에 사용자가 많을 때 오래 걸림 



#### 장고의 세션은 미들웨어를 통해 구성된다고 했는데

## 미들웨어란 ?

HTTP 요청과 응답 처리 중간에서 작동하는 시스템(hooks)

Django는 HTTP 요청이 들어오면 미들웨어를 거쳐 해당 URL에 등록되어 있는 view로 연결해주고, HTTP 응답 역시 미들웨어를 거쳐서 내보냄

주로 데이터 관리, 애플리케이션 서비스, 메시징, 인증 및 API관리를 담당

<img src="04-11.assets/image-20220411100651532.png" alt="image-20220411100651532" style="zoom:80%;" /> 

( 장고 내부의 미들웨어로 지정된 코드 ) -> 따로 수정할 일은 없음



SessionMiddleware : 요청 전반에 걸쳐 세션을 관리

AuthenticationMiddleware : 세션을 사용하여 사용자를 요청과 연결





## 로그인 

로그인은 session을 Create하는 로직과 같음

Django는 우리가 session의 메커니즘에 생각하지 않게끔 도움을 줌

이를 위해 인증에 관한 built-in forms를 제공해줌



AuthenticationForm 

1. 사용자 로그인을 위한 form
2. request를 첫번째 인자로 취함 



<img src="04-11.assets/image-20220411102018375.png" alt="image-20220411102018375" style="zoom:80%;" /> 

장고 공식 홈페이지에서 authentication에 관련된 정보를 찾다보면 (bulit-in-forms) 로그인에 관한 정보가 존재함

이를 통해서 login form을 받아오고 구현이 가능



<img src="04-11.assets/image-20220411102350364.png" alt="image-20220411102350364" style="zoom:80%;" /> 

이렇게 구현이 가능함 (Authentication Form을 그대로 받아옴)

![image-20220411102637128](04-11.assets/image-20220411102637128.png) 

기존에 ModelForm을 넣을 때는 request.POST만 넣어줬는데

해당 경우는 아님 -> 즉 ModelForm이 아니라 Form의 상속을 받고 있음



유효성 검사를 통과 했을 때 login이 되야 하므로

login 함수를 따로 사용해야 함



#### login 함수

login (request, user, backend = None)

- 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 login() 함수가 필요
- 사용자를 로그인하며 view 함수에서 사용됨
- HttpRequest 객체와 User 객체가 필요함
- Django의 session Framework를 사용하여 세션에 user의 ID를 저장( == 로그인)



공식문서 How to log a user in 참고

![image-20220411103233186](04-11.assets/image-20220411103233186.png) 





이를 사용해서 채워놓는다면

![image-20220411103355687](04-11.assets/image-20220411103355687.png) 

이렇게 나오며, 현재 user에 들어갈 데이터가 없으므로 ??로 표시하였고, 또한 login이라는 함수명이 동일하므로

실행이 제대로 되지 않는다. 따라서 login 명을 명칭 바꾸며 실행한다.



Authentication Form에 존재하는 메서드들 중

현재 form에 인증된 사용자가 return 되는 메서드가 존재함

( 인증 : 데이터 베이스에 해당 데이터가 존재하는지 아닌지 (id와 password로 구별할 수 있음))

장고 공식 git hub에서 확인할 수 있음



![image-20220411104144509](04-11.assets/image-20220411104144509.png) 

결국 이렇게 완성본이 나오게 됨



폼이 만들어지면서 django_sesstion이 생성됨 (기존 Form은 데이터베이스가 생성되었나? )

<img src="04-11.assets/image-20220411104228200.png" alt="image-20220411104228200" style="zoom:150%;" />  

 

유효기간, 세션 키, 데이터 등이 저장될 공간이 생김

이후 create superuser를 해서 로그인을 함 -> 쿠키를 통해서 확인 가능함



![image-20220411104918599](04-11.assets/image-20220411104918599.png) 

현재 로그인 되어 있는 유저정보를 출력하기 위해서는 user라는 쓰면 됨



```
의문) 어떻게 user라는 데이터를 context에 전달해주지 않았는데 사용할 수 있는가?!

- context processors
	. 템플릿이 렌더링 될 때 자동으로 호출가능한 컨텍스트 목록
	. 작성된 프로세서는 RequestContext에서 사용가능한 변수로 포함됨
	
즉 자동으로 로드되는 변수 객체들이다.
```



![image-20220411105310961](04-11.assets/image-20220411105310961.png) 

3번째에 보면 auth라는 것 때문에 결국 user를 사용할 수 있음 ( default 값도 존재하며 바로 사용도 가능함 )

쉽게 생각하면 항상 전달되고 있는 context 값들 이다.



장고 공식홈페이지에서 django.contrib.auth에서 User model 과 AnonymousUser 클래스가 따로 존재하고

id 값이 없을 때 지정이 된다.



이외에도

<img src="04-11.assets/image-20220411105635655.png" alt="image-20220411105635655" style="zoom:47%;" /> 

다른 값들도 존재하므로 참고해봐야함





## 로그아웃

로그아웃은 sesstion을 Delete하는 로직과 같음

logout (request)

- HttpRequest 객체를 인자로 받고 반환 값이 없음
- 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음
- 현재 요청에 대한 sesstion data를 DB에서 완전히 삭제하고 클라이언트 쿠키에서도 session id가 삭제됨
- 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스 하는 것을 방지하기 위함 (세션이 남아있는 경우 보안 위험)



![image-20220411110546214](04-11.assets/image-20220411110546214.png) 

이렇게 logout 기능을 만들어 놓고 (url에도 추가)



기능을 동작시켜보면 쿠키에서 sesstion id가 지워지고 장고 session에도 id가 지워진다.





## 로그인 사용자에 대한 접근 제한 

비 로그인 상태에서 현재 Login과 Logout이 동시에 보인다.

즉 Login 상태에서는 Logout만 보여야하고, Logout 상태에서는 Login만 보여야 한다.



로그인 사용자에 대한  엑세스 제한 2가지 방법이 존재한다.

1. The raw way attribute
   - is_authenticated attribute -> T/F

2. The login_required decorator -> 데코레이터



is_authenticated 속성

```
User model의 속성 중 하나
모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
AnonymousUser에 대해서는 항상 False

사용자가 인증 되었는지 여부를 알 수 있는 방법

일반적으로 request.user에서 이 속성을 사용하여, 미들웨어의
django.contrib.auth.middleware.AythenticationMiddleware를 통과했는지 확인

단 권한과는 관련이 없으며, 사용자가 활성화 상태이거나 유효한 세션을 가지고 있는지 확인하지 않음

```

![image-20220411112132603](04-11.assets/image-20220411112132603.png) 

해당 위치에서 이렇게 확인 가능함 ( 보여지는 것만 막음 )



![image-20220411112314633](04-11.assets/image-20220411112314633.png) 

이 상황에서 url을 통해 로그인 페이지로 들어갈 수 있음

accounts/login으로 들어가면 

![image-20220411112405647](04-11.assets/image-20220411112405647.png) 

이렇게 나와서 제대로 출력되지 않음 ( 보여지는 것만 막다보면 나오는 화면 )



따라서 현재 로그인이 되어있는 상황이라면 view함수를 호출하지 못하게 만드는 것도 만들어줘야함

![image-20220411112517710](04-11.assets/image-20220411112517710.png) 

이렇게 막아줄 수 있음



![image-20220411112739242](04-11.assets/image-20220411112739242.png) 

로그인과 로그아웃 전부 막은 화면



#### is_authenticated 다른 적용 사례

#### 인증된 사용자(로그인 상태)만 게시글 작성 링크를 볼 수 있도록 하는 것

기준 1) html에서 설정

![image-20220411113532797](04-11.assets/image-20220411113532797.png) 



기준2) view에서 설정

login_required decorator

- 사용자가 로그인 되어 있지 않다면, settings.LOGIN_URL에 설정된 문자열 기반 절대 경로로 redirect 함
  - LOGIN_URL의 기본 값은 '/accouts/login'
  - 두번째 app 이름을 accounts로 했던 이유중 하나
- 사용자가 로그인 되어 있으면 정상적으로 view함수를 실행
- 인증 성공 시 사용자가 redirect 되어야 하는 경로는 "next"라는 쿼리 문자열 매개 변수에 저장됨
  - 예시 ) /accounts/login/?next=/articles/create/





<img src="04-11.assets/image-20220411114038610.png" alt="image-20220411114038610" style="zoom:83%;" /> 



import를 해오고 view함수 위에 데코레이터를 붙혀줍니다.

CRUD 과정에서 로그인되었을 때만 성공되어야 하는 값은 : C , U, D 입니다.

따라서 C, U, D 위에만 데코레이터를 붙힌다면 다음과 같습니다.



![image-20220411114409930](04-11.assets/image-20220411114409930.png) 

이런식으로 붙힐 수 있음

해당 데코레이터의 역할로는 만약 로그인 상태가 아닌 상태에서 view함수를 실행하려고 할 때

자동으로 login 함수로 가게끔 만들어줍니다. 

-> 그냥 되돌린 것이 아니라 전에 가고싶어 했던 곳을 기억하고 있다가 로그인만 되면 저기로 보내줌

( 해당 데코레이터를 통해서 로그인만 된다면 직전 페이지로 보내줌 (url를 보면 쿼리형식으로 전달됨) )

이렇게 조건을 걸어서 가능하게 합니다.



만약에 로그인 옵션에서 바로 해당하는 페이지로 넘어가고 싶다면 request.GET.get('next')를 전달해줍니다.

![image-20220411143139731](04-11.assets/image-20220411143139731.png) 

로그인에서 -> action 값을 제외해줘야지 현재 페이지로 이동한다. (요청되고 있는)

![image-20220411143206397](04-11.assets/image-20220411143206397.png) 

next값을 받아와서 해당 주소로 이동한다.

![image-20220411143242422](04-11.assets/image-20220411143242422.png) 

next값은 /articles/create/ 임을 알 수 있음



비로그인 상태에서 acticles에 게시글 삭제 시도 할 경우

![image-20220411143615332](04-11.assets/image-20220411143615332.png) 

해당 주소는 위와 같고 이후에 삭제시도를 할 때 405에러가 나오게 됨

405를 만났다는 것은 require_POST에서 걸리게 됩니다.



login_required는 조건에 맞지 않는 경우 redirect을 시켜줍니다.

하지만 redirect의 경우 GET요청만 받기 때문에 바로 POST로 넘어가는 Delete 연산의 경우

POST연산이 아닌 GET연산 요청을 받기 때문에 불가능해집니다.



따라서 Delete의 두가지 데코레이터는 호환되지 않는 궁합입니다.



이 과정은 두가지 문제가 발생합니다.

1. redirect 과정에서 POST 데이터 손실
2. redirect 요청은 POST 방식이 불가능하기 때문에 GET방식으로 요청됨

![image-20220411144123322](04-11.assets/image-20220411144123322.png) 

해당 과정 중 5번 과정에서 에러가 발생함

따라서 중에 하나를 내려야 합니다.

<img src="04-11.assets/image-20220411144435831.png" alt="image-20220411144435831" style="zoom:150%;" /> 

이렇게 해결할 수 있습니다.



## 회원가입

UserCreationForm

주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

3개의 필드를 가짐

1. username(from the user model)
2. password1 # 비밀번호
3. password2 # 비밀번호 확인

<img src="04-11.assets/image-20220411144630729.png" alt="image-20220411144630729" style="zoom:53%;" /> 

실제 장고 github에 저장되어 있는 ModelForm임



### 회원가입 기능 구현

1. urls.py에 path 설정

​	<img src="04-11.assets/image-20220411144914278.png" alt="image-20220411144914278" style="zoom:80%;" /> 

2. views.py 내부 (accounts) 일부 작성

![image-20220411145152894](04-11.assets/image-20220411145152894.png) 

3. templates 작성 signup.html

<img src="04-11.assets/image-20220411145311831.png" alt="image-20220411145311831" style="zoom:80%;" /> 

4. views.py 함수 완성시키기

<img src="04-11.assets/image-20220411151121246.png" alt="image-20220411151121246" style="zoom:67%;" /> 



데이터베이스에 어떤 테이블에 유저가 저장되었을지 확인해본다.

SQL에서 auth_user에 들어가보면 회원 정보들이 나오게 됨

들어가는 경우 is_superuser 와 last_name, is_active 등 선택 값들과 저장했던 아이디 등이 존재함

참고) 패스워드의 원본은 볼 수 없음

<img src="04-11.assets/image-20220411151732633.png" alt="image-20220411151732633" style="zoom:80%;" />



회원가입은 비로그인일때만 봐지고 적용되어야 하므로, 이를 수정해줘야 한다.

또한 회원가입 이후 -> 바로 로그인이 되게 해주는 서비스를 만들려고 한다면 해당 로그인 함수를 적어준다.

![image-20220411151832775](04-11.assets/image-20220411151832775.png) 



참고) usercreation Form의 save method

<img src="04-11.assets/image-20220411152009056.png" alt="image-20220411152009056" style="zoom:67%;" /> 



### 회원탈퇴

회원탈퇴는 DB에서 사용자를 삭제하는 것과 같음

urls.py 안에 delete 함수 작성

![image-20220411154611223](04-11.assets/image-20220411154611223.png)  



views에 기입( 핵심코드만 적음 )

![image-20220411154713052](04-11.assets/image-20220411154713052.png) 



base.html에서

 ![image-20220411161215678](04-11.assets/image-20220411161215678.png)

해당 문구를 기입해서 시각화를 시킵니다.



실제 서비스에서는 회원탈퇴의견을 묻고 왜 탈퇴하는지 기입하는 경우도 존재합니다.

![image-20220411155304002](04-11.assets/image-20220411155304002.png) 

여기서 중요한 부분은 로그아웃을 호출하고 delete를 받는경우 실패하게 됩니다.

데이터를 전달받지 못하기 때문!! 또한 세션도 지워버려야 하는 경우 delete를 사용합니다.



### 회원정보 수정

UserChangeForm (Admin 페이지에서 들어갔던 페이지 )

사용자의 정보 및 권한을 변경하기 위해 admin  인터페이스에서 사용되는 ModelForm

<img src="04-11.assets/image-20220411155545855.png" alt="image-20220411155545855" style="zoom:50%;" /> 

( Admin에서 볼 수 있는 github에 올라와 있는 Model Form  )



1. urls.py 수정 

   <img src="04-11.assets/image-20220411155807779.png" alt="image-20220411155807779" style="zoom: 80%;" />  

2. views.py 수정

<img src="04-11.assets/image-20220411155923340.png" alt="image-20220411155923340" style="zoom:67%;" /> 

3. update.html 파일 작성

<img src="04-11.assets/image-20220411160047545.png" alt="image-20220411160047545" style="zoom:67%;" /> 





문제점 : 여기서 보이는 것은 일반 사용자가 보면 안되는 형식들이 많이 존재함 (루트 권한 등)

<img src="04-11.assets/image-20220411161420449.png" alt="image-20220411161420449" style="zoom:50%;" /> 

따라서 출력될 무언가를 추려야 함



forms.py를 만들고 작성함

<img src="04-11.assets/image-20220411161550062.png" alt="image-20220411161550062" style="zoom:67%;" /> 

일차적으로 상속받는 폼

해당 Model에 작성해야 할 모델은 빌트인모델을 사용하는데, Model을 가져오지 못하는 문제점이 생김



이를 해결하기 위해 장고는 현재 프로젝트에서 사용하는 유저 클래스를 리턴해주는 함수가 존재함

![image-20220411162132828](04-11.assets/image-20220411162132828.png) 

이후에 필요한 데이터 중 3가지 (장고 홈페이지 참고)를 불러옴



커스텀된 Form을 만들었으므로 전에 Form을 전달해주는 update함수에는 CustomForm을 전달해줌

from .forms import CustomUserChangeForm 위에 기입해줌



<img src="04-11.assets/image-20220411162513738.png" alt="image-20220411162513738" style="zoom:67%;" /> 

이후 수정할 때도 유효성 검사를 한번 통과한 이후 기입해줌

이후 해당 버튼을 시각화 시키면 종료

![image-20220411163800272](04-11.assets/image-20220411163800272.png) 

 GET 함수로 요청을 보내야 함 a 태그로 바로 걸어도 됨



## 비밀번호 변경

위에서 비밀번호를 변경하려고 한다면 불가능하다. 즉 장고내부에서는 비밀번호를 바로 변경할 수 없도록  되어 있다.

따라서 장고 내부에서 제공하는 빌트인 Form을 제공받아야 한다.



PasswordChangeForm 

- 사용자가 비밀번호를 변경할 수 있도록 하는 Form
- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브클래스



비밀번호 변경

1. urls.py에서 추가 ( accounts를 앱이름으로 정한 이유 중 1개 기본 경로가 accounts/password임 )

   <img src="04-11.assets/image-20220411172743086.png" alt="image-20220411172743086" style="zoom:80%;" /> 

   

   경로랑 view랑 이름이 똑같지 않은 이유는 혹시나  하는 에러 때문

2. from django.contrib.auth.forms import PasswordChangeForm

​	

<img src="04-11.assets/image-20220411165337758.png" alt="image-20220411165337758" style="zoom:67%;" /> 

해당 형태는 request.user를 받는다 -> 왜? Form이기 때문에 Model Form이 아님 (github에서 확인 가능)

현재 상태의 문제점 -> 비밀번호를 변경했는데 logout이 되어버림



이유 : 비밀번호를 바꾸게 되면 기존에 있는 세션과 id값이 매칭이 안되게 됨 (다른 유저로 판단됨)

따라서 현재 세션도 업데이트를 해줘야 함  ( 장고에서 있는 빌트인 함수를 사용함 )

#### 암호 변경시 세션 무효화 방지

update_session_auth_hash(request, user)

- 현재 요청과 새 session hash가 파생 될 업데이트 된 사용자 객체를 가져오고 session hash를 적절하게 업데이트
- 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 로그인 상태를 유지할 수 없기 때문
- 암호가 변경되어도 로그아웃되지 않도록 새로운 password hash로 session을 업데이트 함 

<img src="04-11.assets/image-20220411165717923.png" alt="image-20220411165717923" style="zoom:100%;" /> 

이렇게 기입을 해줌

![image-20220411170730087](04-11.assets/image-20220411170730087.png) 



비밀번호 변경시 밑에 나오는 글귀를 제거하기 위해서는 아래와 같이 작성함

![image-20220411171631553](04-11.assets/image-20220411171631553.png) 
