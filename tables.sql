create database coin;

create table coin.coin_price
(
    id           varchar,
    icon         varchar,
    name         varchar,
    symbol       varchar,
    rank         bigint,
    price        double precision,
    volume       double precision,
    "websiteUrl" varchar
);