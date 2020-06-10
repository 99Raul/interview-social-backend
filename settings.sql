-- settings.sql
CREATE DATABASE posts;
CREATE USER postsuser WITH PASSWORD 'posts';
GRANT ALL PRIVILEGES ON DATABASE posts TO postsuser;