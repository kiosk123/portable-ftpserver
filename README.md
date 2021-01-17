# pyftpdlib을 이용한 portable FTP서버

FTP서버를 파이썬을 이용하여 간단하게 구성할 수 있도록 함 [참고](https://pyftpdlib.readthedocs.io/en/latest/index.html)

## Getting Started

pyftpdlib 설치 - debian 기준  

```
# python 패키지 관리 도구 없으면 실행
sudo apt-get install python3-pip 

pip3 install pyftpdlib
```


디렉터리 전체를 다운받고 ftpserver 디렉터리로 이동 후 다음의 명령을 차례로 실행한다.

```
chmod +x start.sh
chmod +x stop.sh

``` 


### 서버실행

```
./start.sh
```

### 서버 실행여부 확인

```
# 프로세스 실행여부 확인
ps -ef | grep python

# 네트워크 포트 할당여부 확인
netstat -ntlp | grep 33333

```

### 서버중지

```
./stop.sh
```



### ftp서버의 설정값은 config.py에서 수정

```
userid='user'				#사용자계정
userpass='userpass'	#사용자비번
homedir='/home/user'#홈디렉터리
blocking=True				#블로킹여부
perm='elradfmw'			#퍼미션
port=33333					#포트
uselog=True					#로그사용여부
logpath='log/ftpserver.log'	#로그를 기록할 파일경로
loglevel=INFO				#로그레벨 설정
```

### 크론탭에 재부팅시 실행되도록 설정

```
# 사용자 계정에서 크론탭 에디터 실행
crontab -e

# ftp실행 쉘스크립트 실행코드를 작성하고 저장
@reboot cd <ftpserver 디렉터리 경로>
@reboot ./start.sh

# 재부팅
reboot
```
