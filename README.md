# 14기 FE 7주차 Form-Tag 실습
# 실습 환경 세팅

---

### 1. 레포지토리 클론

프로젝트를 클론받습니다.

```
git clone https://github.com/LikeLion-at-DGU/14th-fe-form-tag-practice.git
```

클론이 완료되면 폴더로 이동해주세요.

```
cd 14th-fe-form-tag-practice
```

### 2. 가상환경 세팅

```
[Mac]
source venv/bin/activate

[Windows Git Bash
source venv/Scripts/activate

[Windows PowerShell]
.\venv\Scripts\activate
```

## 3. 필요한 패키지 설치하기

requirements.txt에 작성된 패키지들을 설치합니다.

```
pip install -r requirements.txt
```

## 4. DB 생성하기

Django 기본 테이블들을 생성합니다.

```
python manage.py migrate
```

## 5. 기본 세팅 가져오기

실습에서는 admin 계정을 사용합니다.

아래 명령어를 실행해주세요.

```
python manage.py seed_demo
```

성공하면 아래와 같은 메시지가 출력됩니다.

```
admin 계정을 생성했습니다.
관리자 계정: admin / admin
```

## 7. 서버 실행하기

이제 Django 서버를 실행해봅시다!

```
python manage.py runserver
```
