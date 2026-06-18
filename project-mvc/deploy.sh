#!/bin/sh

docker stop app-v1 2>/dev/null || true
docker rm app-v1 2>/dev/null || true

docker stop app-v2 2>/dev/null || true
docker rm app-v2 2>/dev/null || true

docker run -d --name app-v2 -p 8080:5000 mvc-app:v2