create table public.message
(
  id    serial not null
    constraint message_pkey
    primary key,
  name  text   not null,
  msg text   not null
);
