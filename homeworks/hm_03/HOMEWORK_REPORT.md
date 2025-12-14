# Отчет по выполнению ДЗ 3

## Этап подготовки базы данных и окружения

1. PosgresDB будет запущен в докер контейнере
2. DBeaver уже установлен
3. Подключение настроено ![Подключение настроено](./screenshots/image.png)
4. Восстановил базу данных
```
# восстановление базы данных из бекапа
docker exec -i bigdata_hm3_db pg_restore -U postgres -d dvd_rental --clean --if-exists /backups/dvd-rental.backup
# проверка табличек
docker exec -it bigdata_hm3_db psql -U postgres -d dvd_rental -c "\dt"
# вывод
             List of relations
 Schema |     Name      | Type  |  Owner   
--------+---------------+-------+----------
 public | actor         | table | postgres
 public | address       | table | postgres
 public | author        | table | postgres
 public | category      | table | postgres
 public | city          | table | postgres
 public | country       | table | postgres
 public | customer      | table | postgres
 public | film          | table | postgres
 public | film_actor    | table | postgres
 public | film_category | table | postgres
 public | inventory     | table | postgres
 public | language      | table | postgres
 public | orders        | table | postgres
 public | payment       | table | postgres
 public | rental        | table | postgres
 public | staff         | table | postgres
 public | store         | table | postgres
```
5. ER-диаграмма
![ER-диаграмма](./screenshots/er_diagram.png)

## Этап SQL и получение данных