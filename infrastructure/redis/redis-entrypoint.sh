#!/bin/sh

# This script substitutes env variables into redis.conf and launches Redis server
# We use entrypoint script to overcome difficulties with env substitution in Docker file.
# We substitute only variables that are required by our conf file.
# That's why we provide '${REDIS_PASSWORD} ${REDIS_USERNAME}' pattern

envsubst '${REDIS_PASSWORD} ${REDIS_USERNAME}' < /usr/local/etc/redis/redis_template.conf > /usr/local/etc/redis/redis.conf
redis-server /usr/local/etc/redis/redis.conf