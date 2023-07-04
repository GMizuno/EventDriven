create database coin;

create table coin_price
(
    exchange    varchar,
    "coinId"    varchar,
    price       float,
    volume      double precision,
    event_time  varchar,
    insert_date timestamp default now()
);

create table coin_agg
(
    name        varchar,
    max_price   float,
    min_price   float,
    avg_price   float,
    insert_date timestamp default now()
);