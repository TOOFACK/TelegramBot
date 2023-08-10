#!/bin/bash

POETRY_VERSION=$1
IMG_TAG_OUT=$2

docker build \
    --tag $IMG_TAG_OUT \
    -f Dockerfile.dev \
    --build-arg POETRY_VERSION=$POETRY_VERSION \
    .