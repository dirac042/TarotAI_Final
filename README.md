# TarotAI_Final

UNIST STEM AI팀 멘티들이 제작한 새로운 타로 AI 프로그램
(made in 2024.07.31 ~ 2024.08.03)

## 사용 방법:

0. 시연 영상 (2024.08.04) : [영상 보러가기](https://www.youtube.com/live/WciFbBl84ns?si=cR7kVtUddei3W3qd&t=1604)

1. 리포지토리를 클론합니다.

```shell
git clone https://github.com/dirac042/TarotAI_Final.git
```

2. 코드를 실행하기 위해 파이썬 패키지를 설치합니다.

   1. (방법 1) Makefile 이용하기

   ```shell
   make install
   ```

   2. (방법 2) install.sh 실행하기

   ```shell
   chmod +x install.sh  # install.sh 최고 권한 부여
   ./install.sh         # install 실행
   ```

3. secret,py 파일을 생성하고, 아래와 같은 형식으로 작성합니다.
```python
sender_email = "YOUR_EMAIL_ADDRESS"
password = "YOUR_EMAIL_PASSWORD"
```

4. my_api_key 파일에 여러분의 API 키를 넣어주세요. ("" 필요 없음.)

5. main.py 파일을 실행합니다.

```shell
python3 main.py   # or 'python main.py'
```
