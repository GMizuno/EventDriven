create database coin;

create table coin_price
(
    id           varchar,
    icon         varchar,
    name         varchar,
    symbol       varchar,
    rank         bigint,
    price        double precision,
    volume       double precision,
    "websiteUrl" varchar,
    event_time   varchar,
    insert_date  timestamp default now()
);

create table coin_agg
(
    name        varchar,
    max_price   float,
    min_price   float,
    avg_price   float,
    count       bigint,
    insert_date timestamp default now()
);