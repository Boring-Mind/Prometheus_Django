#!/bin/sh

# This script substitutes env variables into redis.conf and launches Redis server
# We use entrypoint script to overcome difficulties with env substitution in Docker file.

envsubst < /usr/local/etc/redis/redis_template.conf > /usr/local/etc/redis/redis.conf
redis-server /usr/local/etc/redis/redis.conf