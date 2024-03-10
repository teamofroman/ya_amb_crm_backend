# Бэкенд CRM-системы для Амбассадоров Яндекс Практикума.

## Команда:

- Роман [@rsaleksandrov](https://t.me/rsaleksandrov);
- Михаил [@greenpandorik](https://t.me/greenpandorik);
- Никита [@Rederickmind](https://t.me/Rederickmind);
- Дмитрий [@DimaC1985](https://t.me/DimaC1985).

## Стек технологий:

- **Python**
  - python 3.10
- **Разработка** (requirements.txt)
    - django 4.2.7
    - djangorestframework
    - drf-yasg
    - psycopg2-binary 2.9.9
    - gunicorn 21.2.0
    - python-dotenv 1.0.1
- **Стилизация** (requirements_style.txt)
    - black
    - isort
    - flake8
    - pep8-naming
    - flake8-broken-line
    - flake8-return
    - flake8-isort
- **Дополнительно** (для развертывания/деплоя)
    - docker
    - docker compose
    - PostgreSQL (docker image)
    - Nginx (docker image)

## Документая API

- Локально - файл [api_spec_new.yaml](api_spec_new.yaml)
- глобально - https://ambassadorsyapractice.ru/docs


## Установка для разработки

1. Клонируем репозиторий https://github.com/Praktikum-Am-CRM/backend
2. Переходим в папку с проектом и создаем виртуальное окружение
    ```shell
    python -m venv venv
    ```
3. Активируем ВО
   - Windows
     ```shell 
     .\venv\Scripts\activate
     ```
   - Linux/Mac
     ```shell
     source ./venv/bin/activate
     ```
4. Обновляем `pip`, устанавливаем зависимости
   ```shell
   python.exe -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
   Для поддержания стилистики устанавливаем
   ```shell
   pip install -r requirements_style.txt
   ```
5. В папке `infra` создаем файл `.env`. Образец заполнения в файле `example.
   env`.
   - Настройки django:
     - `ALOWED_HOSTS` - список хостов, на которых может запускаться проект. В обазятельном порядке указываются `django` и IP или доменное имя хоста, на котором развернут сервер. Хосты указываются через запятую, без http  и портов
     - `CSRF_TRUSTED_ORIGINS` - список доверенных хостов, с которых могут приходить запросф. В обазятельном порядке указываются `django` и IP или доменное имя хоста, на котором развернут сервер. Хосты указываются через запятую, с указанием протокола (http://, https://)  и порта. 
     - `SECRET_KEY` - буквенно-цифровая последовательность для шифрования (буквы - английские)
     - `ENGINE` - механизм, который используется для поключения к БД. В данном проекте должно быть равно `django.db.backends.postgresql`
     - `DEBUG` - если указано `True`, то при ошибках выводится отладочная информация, если `False` - выводится просто ошибка сервера
     - `USE_POSTGRES_DB` - если указано `True`, используется PostgreSQL, если 
       `False` - SQLite
   - Настройки для подключения к БД:
     - `POSTGRES_DB` - имя БД
     - `POSTGRES_HOST` - хост, на котором располагается БД. В данном проекте - `postgres`
     - `POSTGRES_PORT` - порт подключения к БД. В данном проекте - `5432`
     - `POSTGRES_USER` - имя пользователя для подключения к БД
     - `POSTGRES_PASSWORD` - пароль для подключения к БД
6. Запуск
    - в отладочном режиме
      ```shell
      python manage.py runserver
      ```
6. ...

### Запуск с использованием докера

В папке `infra` расположены два файла для запуска докер контейнеров:
- `docker-compose-local.yml` - для полноценного развертывания в "боевую" 
  систему. Поднимает контейнеры `postgres` (БД), `django` (собственно 
  бэкенд) и `nginx` (http сервер)
- `docker-compose-postgres-only.yml` - поднимает только контейнер `postgres` 
  (БД)

> **ВАЖНО:** Для работы с использованием контейнеров в файле `.env` надо 
установить `POSTGRES_DB=True`. В противном случае даже в контейнере будет 
использоваться SQLite.

Для запуска контейнеров переходим в папку `infra` и выполняем команду
```shell
docker compose --file <имя соответствующего yml файла> up --build
```

Если нужен запуск в режиме демона, то в конце добавляем ключ `-d`.
Для Linux (и скорее всего Mac) в начале указываем команду `sudo`

### Вспомогательные средства
Для облегчения работы можно воспользоваться имеющимся в проекте Makefile 
(на Windows для работы надо установить утилиту `make`).
Параметры:
- `style` - проверка кода на соответствие стилю
- `migrate` - выполнение миграций (создание и применений)
- `superuser` - создание суперпользователя
- `run` - запуск сервера в отладочном режиме

## Деплой

### 1. Подготовка сервера

#### 1.1 Системные требования

Системные требования соответствую системным требованиям к Ubuntu Server 22.04

- **CPU** - 1Ghz и выше (2 ядра и более)
- **Память** - 1Gb и выше (лучше не менее 2Gb)
- **Дисковое пространство** - 20Gb минимум (лучше 25-30Gb). Размер 
  определяется интенсивностью использования CRM

#### 1.3 Установка и настройка Docker

##### Установка Docker

Для запуска проекта используется система контейниризации 
[Docker](https://docs.docker.com/engine/install/).

Для начала удаляем предыдущие установки docker, если они были

```shell
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

Устанавливаем Docker engine

```shell
curl -fsSL https://get.docker.com | sudo sh -
```

#### Настройка Docker

Останавливаем службу `docker`

```shell
sudo systemctl stop docker
sudo systemctl stop docker.socket
```

В каталоге `/etc/docker/` создаем файл `daemon.json`:

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "10"
  }
}
```

Запускаем службу `docker`

```shell
sudo systemctl start docker
```

### 2. Подготовка переменных окружения на GitHub

Для автоматического развертывания проекта в репозитории на [GitHub]
(https://github.com/) необходимо задать следующие секретные переменые 
(`Settings` -> `Secrets and variables` -> `Actions`):

- Настройки для бэкенда:
  - `ALOWED_HOSTS` - список хостов, на которых может запускаться проект. В 
    обазятельном порядке указываются `backend` и IP или доменное имя хоста, на 
    котором развернут сервер. Хосты указываются через запятую, без http и портов
  - `CSRF_TRUSTED_ORIGINS` - список доверенных хостов, с которых могут 
    приходить запросы. В обазятельном порядке указываются `backend` и IP или 
    доменное имя хоста, на котором развернут сервер. Хосты указываются 
    через запятую, с указанием протокола (http://, https://) и порта. 
  - `SECRET_KEY` - буквенно-цифровая последовательность для шифрования 
    (буквы - английские)
  - `ENGINE` - механизм, который используется для поключения к БД. В данном 
    проекте должно быть равно `django.db.backends.postgresql`
  - `DEBUG` - если указано `True`, то при ошибках выводится отладочная  
    информация, если `False` - выводится просто ошибка сервера
  - `USE_POSTGRES_DB` - если указано `True`, то будет использоваться БД 
    Postgres, если `False` - SQLite
- Настройки для подключения к БД:
  - `POSTGRES_DB` - имя БД
  - `POSTGRES_HOST` - хост, на котором располагается БД. В данном проекте - `postgres`
  - `POSTGRES_PORT` - порт подключения к БД. В данном проекте - `5432`
  - `POSTGRES_USER` - имя пользователя для подключения к БД
  - `POSTGRES_PASSWORD` - пароль для подключения к БД
- Настройки для подключения к [DockerHub](https://hub.docker.com/):
  - `DOCKER_USERNAME` - имя пользователя для подключения к [DockerHub](https://hub.docker.com/)
  - `DOCKER_PASSWORD` - пароль для подключения к [DockerHub](https://hub.docker.com/)
- Настройки для подключения к серверу, на котором развертывается проект, по 
  SSH:
  - `SSH_HOST` - IP адрес или доменное имя сервера
  - `SSH_KEY` - SSH ключ (закрытый) для подключения к серверу. Открытый ключ должен быть размещен на  сервере
  - `SSH_PHRASE` - пароль для SSH ключа
  - `SSH_USER` - имя пользователя для подключения к серверу

### 3. Деплой проекта на сервер

Деплой проекта на сервер осуществляется автоматически при заливке кода в 
ветку `main` репозитория. Отслеживать процесс деплоя на сервер можно на 
вкладке `Actions`.

По умолчанию деплой осуществляется папку `/home/<SSH_USER>/yaambcrm/infra/`. 
Папка имеет следующую структуру

```
.
├── cert        - папка с SSL сертификатами
├── nginx_conf  - папка с конфигурационными файли web сервера NGINX
├── .env        - конфигурационный файл с переменными окружения
└── docker-compose-prod.yml - Конфигурационный файл для развертывания докер контейнеров
```

## 4. Первоначальная настройка

После первого деплоя проекта на сервер необходимо создать 
супер-пользователя для дальнейшей настройки проекта

### 4.1 Создание суперпользователя

Что бы производить последующие настройки необходимо создать 
супер-пользователя. Для этого:

- переходим в папку `/home/<SSH_USER>/yaambcrm/infra/`

  ```shell
  cd /home/<SSH_USER>/azubot/infra/
  ```

- выполняем команду

  ```shell
  sudo docker compose --file ./docker-compose-prod.yml exec -ti backend bash

- После появления приглашения выполняем команду

  ```shell
  python manage.py createsuperuser
  ```

  и отвечаем на вопросы.

- Если требуется дополнительно загрузить тестовые данные, выполняем команду

  ```shell
  python manage.py lodadata static/base_<дата и время>.json
  ```
> Примечание: по умолчанию файл с данными на сервер не переносится. Его можно 
взять из папки `data` репозитория и скопировать на сервер в папку 
`/home/<SSH_USER>/yaambcrm/frontend/static/` (эта папка будет доступна в 
контейнере `backend` по пути `static`)

- Выходим из оболочки, выполнив команду `exit` или нажав `Ctrl+d`

