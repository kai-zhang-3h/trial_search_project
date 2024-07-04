# Trial Search (English follows Japanese)

## 1 概要

このプロジェクトの主体は[jrct website](https://rctportal.niph.go.jp/s/result?age%5Bage_gt%5D=&age%5Bage_lt%5D=&age%5Bage_range%5D=&date%5Bdate_item%5D%5B%5D=none&date%5Bstart_date%5D%5B%5D=&date%5Bend_date%5D%5B%5D=&crc%5B%5D=clinical_research&crc%5B%5D=chiken&q=&t=chiken&other%5Bother_item%5D%5B%5D=none&other%5Bkeyword%5D%5B%5D=&other%5Bnegative_keyword%5D%5B%5D=&submit=%E5%86%8D%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B)をスクレイピングして、データベースに保存するスパイダーです。

この文書に、詳しい例を含めて、起動と実行に関する重要なコマンドをて紹介します。

## 2 ディレクトリ構造

    ├─pyenv
    │  └─src
    │      └─trial_search_crawler
    │          └─trial_search_crawler
    │              ├─spiders
    │              └─utils
    └─sqlenv
        └─mysql
            ├─db
            │  ├─#innodb_redo
            │  ├─#innodb_temp
            │  ├─jrctdb
            │  ├─mysql
            │  ├─performance_schema
            │  ├─sys
            │  └─testdb
            └─initdb.d

## 3 主なコマンド
注意事項:
- 特別な指定がなければ, スパイダーの名前は `jrct`となります。 
- 特別な指定がなければ, python docker imageの名前は `python_app`となって、python docker containerの名前は `python_run`となります。
- 特別な指定がなければ, mysql docker imageの名前は `mysql_app`となって、python docker containerの名前は `mysql_run`となります。
- 覚えてください: dockerの環境で, mysql containerをpython containerの前に起動することです

### **3.1 前提 - Docker環境 (mysql)**
#### 3.1.1 mysql docker composeの構築と実行
このステップはプロジェクトとmuysql docker環境に接続できます。これはスパイダーの実行の前提としています。(ローカル環境実行とDocker環境実行両方)
>> C:\trial_search_project\sqlenv> docker-compose up -d

注意事項:
- `-d`： 他のプロセスを妨害しないため、バックグラウンド処理する変数です

### **3.2 オプション1 - ローカル環境 (Python)**
#### 3.2.1 ローカル環境でスパイダーを実行する
上のDocker環境 (mysql)の実行は前提です.
>> C:\trial_search_project\pyenv\src\trial_search_crawler> py -m scrapy crawl jrct

**今、jrct websiteのスクレイピングが始まる!**

注意事項: 
- Scrapyの環境変数を設定すれば、`scrapy crawl jrct`を利用して構わないです
- 出力ファイルは`scrapy crawl jrct -o output.json`で設定できます。
- logファイルは`scrapy crawl jrct --logfile jrctlog.txt`で設定できます。

### **3.3 オプション2 - Docker環境 (Python)**
このステップはプロジェクトとmuysql docker環境に接続できます。これはスパイダーの実行の前提としています。(ローカル環境実行とDocker環境実行両方)
#### 3.3.1 container状態の検出
アクティブとインアクティブのcontainerを検出できます

>> C:\trial_search_project\pyenv> docker ps -a
    
    CONTAINER ID   IMAGE        COMMAND                  CREATED      STATUS                      PORTS
         NAMES
    fbf573271d7d   python_app   "/bin/bash -c 'cd sr…"   4 days ago   Exited (0) 4 days ago
         python_run
    cb4612edaa85   mysql_app    "docker-entrypoint.s…"   7 days ago   Exited (255) 46 hours ago   0.0.0.0:3306->3306/tcp, 33060/tcp   mysql_run

#### 3.3.2 Python Containerの削除
もし存在すれば、Python Containerを削除されます。新しいcontainerを起動するため、古いcontainerの削除は必要です

>> C:\trial_search_project\pyenv> docker rm fb
    
    fb

#### 3.3.3 Container (Python) の構築
>> C:\trial_search_project\pyenv> docker build ./ -t python_app

#### 3.3.4 スパイダーの実行
In this step, we officially run spider in docker
>> C:\trial_search_project\pyenv> docker run --name python_run --env-file env.txt --network mynetwork -it -v c:/trial_search_share:/share python_app

**今、jrct websiteのスクレイピングが始まる!**

注意事項: 

- `--name`: containerの名前
- `env-file`: 環境変数を記載されたファイル
- `--network`: mysqlフォルダのdocker-compose.ymlで記載したネットワークの名前
- `-v`: volume, dockerとhostを共有するフォルダを指定する(Full Path)
- `-it`: `-i` と `-t`の組み合わせ

## 4 手順の例
### **4.1 どやってローカル環境でスパイダーを実行しますか？**

4.1.1 mysql docker composeの構築と実行
>> C:\trial_search_project\sqlenv> docker-compose up -d

    [+] Running 1/0
    ✔ Container mysql_run  Running

4.1.2 ローカル環境でSpiderの実行
>> C:\trial_search_project\pyenv\src\trial_search_crawler> py -m scrapy crawl jrct

### **4.2 どやってDocker環境でスパイダーを実行しますか？**

4.2.1 mysql docker composeの構築と実行
>> C:\trial_search_project\sqlenv> docker-compose up -d

    [+] Running 1/0
    ✔ Container mysql_run  Running
4.2.2 container状態の検出
>> C:\trial_search_project\pyenv> docker ps -a
    
    CONTAINER ID   IMAGE        COMMAND                  CREATED      STATUS                      PORTS
         NAMES
    fbf573271d7d   python_app   "/bin/bash -c 'cd sr…"   4 days ago   Exited (0) 4 days ago
         python_run
    cb4612edaa85   mysql_app    "docker-entrypoint.s…"   7 days ago   Exited (255) 46 hours ago   0.0.0.0:3306->3306/tcp, 33060/tcp   mysql_run
4.2.3 Python Containerの削除
>> C:\trial_search_project\pyenv> docker rm fb
    
    fb
    
4.2.4 Python Containerの構築
>> C:\trial_search_project\pyenv> docker build ./ -t python_app
4.2.5 Docker環境でスパイダーの実行 (Python Containerの実行)
>> C:\trial_search_project\pyenv> docker run --name python_run --env-file env.txt --network mynetwork -it -v c:/trial_search_share:/share python_app

## 5 他のコマンド

### **5.1 Docker環境 (mysql)**

#### 5.1.1 mysql docker composeの中止
>> C:\trial_search_project\sqlenv> docker-compose down

    [+] Running 1/1
    ✔ Container mysql_run  Removed
#### 5.1.2 mysql containerの中/bin/bashを起動します
bashターミナルでデータベースを操作するため、bashターミナルの起動は必要です
>> C:\trial_search_project\sqlenv> docker exec -it mysql_run /bin/bash

注意事項:

- `-i`: 添付されなくても、STDINを開放しております、even if not attached
- `-t`: pseudo-TTYを配属します

#### 5.1.3 /bin/bashの中でmysqlを起動します
In order to explore database in terminal. We then launch mysql inside bash terminal
>> bash-4.4# mysql -uroot -ppass

    mysql: [Warning] Using a password on the command line interface can be insecure.
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 9
    Server version: 8.0.34 MySQL Community Server - GPL

    Copyright (c) 2000, 2023, Oracle and/or its affiliates.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

今mysqlコマンドを実行できます

#### 5.1.4 mysqlから脱出

>> mysql> exit;
    
    Bye

#### 5.1.5 /bin/bashから脱出
>> bash-4.4# exit
    
    exit

### **5.2 ローカル環境 (Python)**

#### 5.2.1 local envでスパイダーをチェックする
スパイダーのチェックだけしたければ、データベースへの接続は必要ないです。
>> C:\trial_search_project\pyenv\src\trial_search_crawler> py -m scrapy check jrct

注意事項: 
- Scrapyの環境変数を設定すれば、`scrapy check jrct`を利用して構わないです

### **5.3 Docker環境 (Python)**

#### 5.3.1 Image状態の検出

このステップは全てのimageを展示します。もし全てのimageは編集がなければ、このステップは必要ないです。
>> C:\trial_search_project> docker images

    REPOSITORY         TAG       IMAGE ID       CREATED         SIZE
    python_app         latest    880ff5acfbeb   7 hours ago     158MB
    mysql_app          latest    7bec084e660e   7 hours ago     577MB
    centos             centos7   eeb6ee3f44bd   22 months ago   204MB
    jayudev/mysql5.7   latest    702fb0b7837f   4 years ago     372MB

#### 5.3.2 Imageの削除

このステップはimageを削除します。もし全てのimageは編集がなければ (ソースコード、 Dockerfile、docker-compose.ymlなど), このステップは必要ないです. ただし、例えば, mysql image (7b)は編集があったら、このimageを削除することです。
>> C:\trial_search_project> docker rmi 7b

    Untagged: mysql_app:latest
    Deleted: sha256:7bec084e660e916bd1b85fec2ab3562864f68f8cb349c431dd0f147a2cf16e35

---

# Trial Search 

## 1 Overview

The project Trial Search mainly consists of a spider that scrapes the [jrct website](https://rctportal.niph.go.jp/s/result?age%5Bage_gt%5D=&age%5Bage_lt%5D=&age%5Bage_range%5D=&date%5Bdate_item%5D%5B%5D=none&date%5Bstart_date%5D%5B%5D=&date%5Bend_date%5D%5B%5D=&  crc%5B%5D=clinical_research&crc%5B%5D=chiken&q=&t=chiken&other%5Bother_item%5D%5B%5D=none&other%5Bkeyword%5D%5B%5D=&other%5Bnegative_keyword%5D%5B%5D=&submit=%E5%86%8D%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B) and stores the data in mysql database.

In this article, we will list and explain some core commands related to the launch and execution of spider, with a detailed example.

## 2 Directory Structure

    ├─pyenv
    │  └─src
    │      └─trial_search_crawler
    │          └─trial_search_crawler
    │              ├─spiders
    │              └─utils
    └─sqlenv
        └─mysql
            ├─db
            │  ├─#innodb_redo
            │  ├─#innodb_temp
            │  ├─jrctdb
            │  ├─mysql
            │  ├─performance_schema
            │  ├─sys
            │  └─testdb
            └─initdb.d
## 3 Major Command
Notes:
- Unless otherwise specifed, the name of spider is `jrct`. 
- Unless otherwise specifed, the name of python docker image is `python_app` and the name of python docker container is `python_run`
- Unless otherwise specifed, the name of mysql docker image is `mysql_app` and the name of mysql docker container is `mysql_run`
- Do remember: in docker env, launch mysql container before python container

### **3.1 Preliminary - docker env (mysql)**
#### 3.1.1 build and run
This step will ensure the connection to the docker env of mysql database, which is a preliminary condition for running spider in both local env and docker env.
>> C:\trial_search_project\sqlenv> docker-compose up -d

    [+] Running 1/0
    ✔ Container mysql_run  Running

Notes:
- `-d`： launch in the background without interfering other procedure

### **3.2 Option 1 - Local Env (Python)**
#### 3.2.1 run spider in Local Env
You need to first finish the execution of Docker Env (mysql) above.
>> C:\trial_search_project\pyenv\src\trial_search_crawler> py -m scrapy crawl jrct

**Now, the Spider starts scrapying jrct website!**

Notes: 
- If you have set env variables of scrapy, you may directly use `scrapy crawl jrct`
- You may specify output file with `scrapy crawl jrct -o output.json`
- You may specify logfile with `scrapy crawl jrct --logfile jrctlog.txt`

### **3.3 Option 2 - docker env (python)**
You need to first finish the execution of Docker Env (mysql) above.
#### 3.3.1 inspect container status
We can figure out containers that are both active and inactive
>> C:\trial_search_project\pyenv> docker ps -a
    
    CONTAINER ID   IMAGE        COMMAND                  CREATED      STATUS                      PORTS
         NAMES
    fbf573271d7d   python_app   "/bin/bash -c 'cd sr…"   4 days ago   Exited (0) 4 days ago
         python_run
    cb4612edaa85   mysql_app    "docker-entrypoint.s…"   7 days ago   Exited (255) 46 hours ago   0.0.0.0:3306->3306/tcp, 33060/tcp   mysql_run
#### 3.3.2 Remove python 
Remove python container if it exists. This is necessary as we need to launch a new python container to run the spider
>> C:\trial_search_project\pyenv> docker rm fb
    
    fb

#### 3.3.3 build
>> C:\trial_search_project\pyenv> docker build ./ -t python_app
#### 3.3.4 run

In this step, we officially run spider in docker

>> C:\trial_search_project\pyenv> docker run --name python_run --env-file env.txt --network mynetwork -it -v c:/trial_search_share:/share python_app

**Now, the Spider starts scrapying jrct website!**

Notes: 

- `--name`: name of container
- `env-file`: file that contains environment variables
- `--network`: name of network in docker-compose.yml of mysql folder
- `-v`: volume, the folder that is shared between docker and host (use full path instead of relative path)
- `-it`: combination of `-i` and `-t`

## 4 Example Procedure

### **4.1 How to Run Spider in Local Env**

4.1.1 Build and run mysql docker compose
>> C:\trial_search_project\sqlenv> docker-compose up -d

    [+] Running 1/0
    ✔ Container mysql_run  Running

4.1.2 Run spider
>> C:\trial_search_project\pyenv\src\trial_search_crawler> py -m scrapy crawl jrct

### **4.2 How to Run Spider in Docker Env**

4.2.1 Build and run mysql docker compose
>> C:\trial_search_project\sqlenv> docker-compose up -d

    [+] Running 1/0
    ✔ Container mysql_run  Running
4.2.2 Inspect container status
>> C:\trial_search_project\pyenv> docker ps -a
    
    CONTAINER ID   IMAGE        COMMAND                  CREATED      STATUS                      PORTS
         NAMES
    fbf573271d7d   python_app   "/bin/bash -c 'cd sr…"   4 days ago   Exited (0) 4 days ago
         python_run
    cb4612edaa85   mysql_app    "docker-entrypoint.s…"   7 days ago   Exited (255) 46 hours ago   0.0.0.0:3306->3306/tcp, 33060/tcp   mysql_run
4.2.3 Remove python container if either exists
>> C:\trial_search_project\pyenv> docker rm fb
    
    fb
    
4.2.4 Build python container
>> C:\trial_search_project\pyenv> docker build ./ -t python_app
4.2.5 Run python container
>> C:\trial_search_project\pyenv> docker run --name python_run --env-file env.txt --network mynetwork -it -v c:/trial_search_share:/share python_app

## 5 Other Commands
### **5.1 Docker Env (mysql)**

#### 5.1.1 shut down
>> C:\trial_search_project\sqlenv> docker-compose down

    [+] Running 1/1
    ✔ Container mysql_run  Removed
#### 5.1.2 launch bash terminal inside mysql container
In order to explore database in terminal. We first launch bash terminal
>> C:\trial_search_project\sqlenv> docker exec -it mysql_run /bin/bash

Notes:

- `-i`: Keep STDIN open even if not attached
- `-t`: Allocate a pseudo-TTY
#### 5.1.3 launch mysql inside /bin/bash
In order to explore database in terminal. We then launch mysql inside bash terminal
>> bash-4.4# mysql -uroot -ppass

    mysql: [Warning] Using a password on the command line interface can be insecure.
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 9
    Server version: 8.0.34 MySQL Community Server - GPL

    Copyright (c) 2000, 2023, Oracle and/or its affiliates.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

Now you can run mysql commands

#### 5.1.4 Exit mysql

>> mysql> exit;
    
    Bye

#### 5.1.5 Exit /bin/bash
>> bash-4.4# exit
    
    exit

### **5.2 Local Env (Python)**

#### 5.2.1 Check Spider in Local Env
There is no need to connect to database if you only want to check the spider
>> C:\trial_search_project\pyenv\src\trial_search_crawler> py -m scrapy check jrct

Notes: 
- If you have set env variables of scrapy, you may directly use `scrapy check jrct`

### **5.3 Docker Env (Python)**

#### 5.3.1 Inspect Image Status

This step will list all the images. If no image is modified, we do not need to inspect the images.
>> C:\trial_search_project> docker images

    REPOSITORY         TAG       IMAGE ID       CREATED         SIZE
    python_app         latest    880ff5acfbeb   7 hours ago     158MB
    mysql_app          latest    7bec084e660e   7 hours ago     577MB
    centos             centos7   eeb6ee3f44bd   22 months ago   204MB
    jayudev/mysql5.7   latest    702fb0b7837f   4 years ago     372MB

#### 5.3.2 Remove Images

This step will remove images. If no image is modified (source code or Dockerfile, docker-compose.yml), we do not need to remove the images. However, if for example, mysql image (7b) is modified. We need to remove the modified image
>> C:\trial_search_project> docker rmi 7b

    Untagged: mysql_app:latest
    Deleted: sha256:7bec084e660e916bd1b85fec2ab3562864f68f8cb349c431dd0f147a2cf16e35