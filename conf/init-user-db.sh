#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER fluentbit WITH PASSWORD 'fluentbit';
    CREATE DATABASE fluentbit;
    GRANT ALL PRIVILEGES ON DATABASE fluentbit TO fluentbit;
    ALTER DATABASE fluentbit OWNER TO fluentbit;
EOSQL
