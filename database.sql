create database mydatabase;

create table mydatabase.message
(
  id    serial not null
    constraint message_pkey
    primary key,
  nome  text   not null,
  msg text   not null
);
