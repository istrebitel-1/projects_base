#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL

create database portal
    with
    owner = postgres
    encoding = 'UTF8'
    lc_collate = 'en_US.utf8'
    lc_ctype = 'en_US.utf8'
    tablespace = pg_default
    connection limit = -1;

create user robot_portal WITH PASSWORD 'robot_portal';

\c portal;

create schema portal authorization robot_portal;

EOSQL
