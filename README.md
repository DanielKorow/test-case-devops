---
Зависимости:
- docker:20.10.12
- docker-compose:1.25.0
Проверялось на ubuntu:20.04
---
Запуск:
```
./up.sh
```
Запускаются 4 контейнера:
- Контейнер с приложением
- Контенйер с базой данных (postgresql)
- Контейнер с админкой для базы данных
- Контейнер с fluentbit для сбора логов.
---
Доступ к pgsql:
http://127.0.0.1:8080 (8080 - должен быть свободен, в противном случае надо поменять мапинг в docker-compose.yml)
```
server: 172.19.0.10
username: fluentbit
password: fluentbit
database: fluentbit
```
---
SQL command
**Query** в **Postgresql** для просмотра логов приложения.
```
select data::json->'container_name' as container_name,
       data::json->'log' as log
from fluentbit
where data->>'container_name'='app'
limit 50;
```
