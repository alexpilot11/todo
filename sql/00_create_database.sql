CREATE ROLE flint_dev_admin WITH LOGIN PASSWORD 'flint_dev_admin';
ALTER ROLE flint_dev_admin SET client_encoding TO 'utf8';
ALTER ROLE flint_dev_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE flint_dev_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE flint_dev TO flint_dev_admin;
GRANT ALL PRIVILEGES ON DATABASE flint_test TO flint_dev_admin;
ALTER USER flint_dev_admin CREATEDB;

CREATE ROLE flint_dev_user WITH LOGIN PASSWORD 'flint_dev_user';
ALTER ROLE flint_dev_user SET client_encoding TO 'utf8';
ALTER ROLE flint_dev_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE flint_dev_user SET timezone TO 'UTC';
GRANT CONNECT ON DATABASE flint_dev TO flint_dev_user;
GRANT CONNECT ON DATABASE flint_test TO flint_dev_user;