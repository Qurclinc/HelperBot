#!/bin/bash

sudo docker-compose down

git pull origin master

sudo docker-compose up --build -d