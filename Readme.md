* code --remote=wsl+ubuntu .
* docker compose down -v
* docker compose up --build -d # -d to get terminal back
* docker-compose logs mysql
```
(base) navneet@Navspeak:~/projects/python/C1$ docker exec -it mysql-server bash
bash-5.1# ls -l /docker-entrypoint-initdb.d 
bash-5.1# mysql -u root -p

``` 
