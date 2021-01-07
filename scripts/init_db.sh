#!/bin/bash

sleep 3

# migrate database
echo 'migrate database'
alembic upgrade head
