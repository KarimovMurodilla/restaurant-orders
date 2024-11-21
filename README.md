# Loyiha haqida
Restoran Buyurtma Berish Tizimi

#### Ishlatilgan framework va texnologiyalar:
* FastAPI
* PostgreSQL
* MongoDB
* Docker
* SQLAlchemy
* Alembic


> Loyiha [UoW design pattern](https://en.wikipedia.org/wiki/Unit_of_work) asosida qurilgan
## Sozlamalar

### .env ni sozlab olish
> Ushbu loyihada ikkta muhit sozlangan:
1. .env - local da ishga tushurish uchun
2. .env-non-dev - docker orqali ishga tushurish uchun

#### .env fayl namuna:
```
SECRET=12345abcd
BOT_TOKEN=1234:abcd

DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASS=

MONGO_HOST=
MONGO_PORT=
MONGO_USER=
MONGO_PASS=

```

#### env-non-dev namuna:
```
SECRET=abcd&1234
BOT_TOKEN=1234:abcd

DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASS=

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

MONGO_HOST=
MONGO_PORT=
MONGO_USER=
MONGO_PASS=
```

## Dasturni ishga tushurish

### docker-compose orqali
```
docker-compose up --build
```
#### Docker konteynerlar ishga tushganidan keyn, app ning ichiga kirib migratsiya qilish kerak bo'ladi
```
docker exec -it restaurant_app /bin/bash
```
```
alembic upgrade head
```

> API ushbu host va port orqali ishga tushadi: [0.0.0.0:8879](http://0.0.0.0:8879)

### Python orqali ishga tushurish
1. Kerakli modullarni yuklab olish
```
pip install -r requirements.txt
```
2. Migratsiyalar
```
alembic revision --autogenerate --m="Initial check"
```
```
alembic upgrade head
```

3. Dasturni ishga tushirish
```
python src/main.py
```
> API ushbu host va port orqali ishga tushadi: [localhost:8000](http://localhost:8000)

### Tekshirish va Testlash
Swagger orqali tekshirish uchun /docs ga o'tiladi. Misol uchun [0.0.0.0:8879/docs](http://0.0.0.0:8879/docs)
