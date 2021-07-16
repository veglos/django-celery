# README

A simple project that puts together django, celery, celery-beat, redis, postgresql and docker.

# Launch

1. Run docker-compose up
``` shell
docker-compose up
```

## SEND

Request

``` json
POST
URL: http://localhost:8000/myapp/
{
  "message": "hello world"
}
```

Response

``` json
{
  "task_id": "e29e9d24-259f-4211-ad7e-147c93a2ef32"
}
```

## Receive

Request
``` json
GET
URL: http://localhost:8000/myapp/e29e9d24-259f-4211-ad7e-147c93a2ef32
```

Response

``` json
{
  "task_id": "e29e9d24-259f-4211-ad7e-147c93a2ef32",
  "task_status": "SUCCESS",
  "task_result": true
}
```

# Debug

## logs
* watch logs from a single service of the compose
``` shell
docker-compose logs -f 'app'
docker-compose logs -f 'celery'
```

## pgadmin

``` shell
docker run --rm --name=pgadmin --env PGADMIN_DEFAULT_EMAIL='test@example.com' --env PGADMIN_DEFAULT_PASSWORD='123456' -p 8082:80 dpage/pgadmin4:latest
```

pgadmin url: http://localhost:8082/

## rediscomander
``` shell
docker run --rm --name=rediscomander --env REDIS_HOSTS=local:host.docker.internal:6379 -p 8081:8081 rediscommander/redis-commander:latest
```

rediscomander url: http://localhost:8081/

*NOTE*: **host.docker.internal** is for Mac and Windows. For linux see [this thread](https://stackoverflow.com/questions/48546124/what-is-linux-equivalent-of-host-docker-internal/61001152).