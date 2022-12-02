# QRkot
QRKot — приложение для Благотворительного фонда поддержки котиков
Это учебный проект FastAPI. Фонд собирает пожертвования на различные 
целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на 
обустройство кошачьей колонии в подвале, на корм оставшимся без попечения 
кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Подготовка к работе:

<details>
    <summary><b>Клонируйте репозиторий:</b></summary>

```shell
git clone git@github.com:rasputin-pro/QRkot_spreadsheets.git
```
</details>

<details>
    <summary><b>Создайте файл <code>.env</code> в корне проекта 
со своими данными:</b></summary>

```dotenv
APP_TITLE=Кошачий благотворительный фонд (0.1.0)
DESCRIPTION=Сервис для поддержки котиков!
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=QU:=r6S7+{'et=rf
FIRST_SUPERUSER_EMAIL=superuser@example.com
FIRST_SUPERUSER_PASSWORD=5>~H*d&:Yz5jXrna
# Доступ к сервисному аккаунту Google Cloud Platform
EMAIL=
TYPE=
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
```
> Данные для доступа к сервисному аккаунту Google Cloud Platform возьмите из
> `*.json` файла, полученного после создания аккаунта.
</details>

<details>
    <summary><b>Создайте и активируйте виртуальное окружение.</b></summary>

```shell
python3 -m venv venv
# Linux/MacOS
source venv/bin/activate
# Windows
source venv/scripts/activate
```
</details>

<details>
    <summary><b>Установите зависимости из файла requirements.txt</b></summary>

```shell
pip install -r requirements.txt
```
</details>

<details>
    <summary><b>Примените миграции:</b></summary>

```shell
alembic upgrade head
```
</details>

<details>
    <summary><b>Для запуска программы выполните команду:</b></summary>

```shell
uvicorn app.main:app --reload
```
</details>

## Документация
После запуска программы документация будет доступна по адресам:

[http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)

[http://127.0.0.1:8080/redoc](http://127.0.0.1:8080/redoc)
