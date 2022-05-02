CREATE ROLE fastdemo_dev_admin WITH LOGIN PASSWORD 'fastdemo_dev_admin';
ALTER ROLE fastdemo_dev_admin SET client_encoding TO 'utf8';
ALTER ROLE fastdemo_dev_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE fastdemo_dev_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE fastdemo_dev TO fastdemo_dev_admin;
GRANT ALL PRIVILEGES ON DATABASE fastdemo_test TO fastdemo_dev_admin;
ALTER USER fastdemo_dev_admin CREATEDB;

CREATE ROLE fastdemo_dev_user WITH LOGIN PASSWORD 'fastdemo_dev_user';
ALTER ROLE fastdemo_dev_user SET client_encoding TO 'utf8';
ALTER ROLE fastdemo_dev_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE fastdemo_dev_user SET timezone TO 'UTC';
GRANT CONNECT ON DATABASE fastdemo_dev TO fastdemo_dev_user;
GRANT CONNECT ON DATABASE fastdemo_test TO fastdemo_dev_user;