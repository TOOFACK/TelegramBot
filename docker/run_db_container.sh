#!/bin/bash

name=$1
port=$2
user=$3
db=$4
password=$5
sudo docker run --name $name \
 -p $port:$port  \
 -e POSTGRES_USER=$user \
 -e POSTGRES_DB=$db \
 -e POSTGRES_PASSWORD=$password \
 -d postgres:14