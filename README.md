# SibdevDRFTest

## Инструкция

### Клонировать репозиторий

 ```
cd ~
git clone https://github.com/MelDxKviel/SibdevDRFTest.git
cd SibdevDRFTest
 ```

### Собрать приложение с помощью docker compose
```
docker-compose build
```

### Запустить приложение

```
docker-compose up
```

Перейти на адрес http://0.0.0.0:8000/api/customerdeals 

POST - файл .csv со сделками

GET - список из пяти клиентов, потративших больше всего денег
