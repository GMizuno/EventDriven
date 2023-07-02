create database coin;

create table coin_price
(
    exchange    varchar,
    pair        varchar,
    "pairPrice"   varchar,
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
    count       bigint,
    insert_date timestamp default now()
);