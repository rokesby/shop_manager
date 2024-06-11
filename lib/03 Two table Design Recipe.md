# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed. 

As a shop manager
So I can manage orders
I want to be able to create a new order.
```

```
Nouns:

Items
  - Item
    - Name - text
    - Unit Price - real
    - Stock Quantity - int

Orders
  - Order 
  - item_id - int
  - date_order_placed - date
  - customer name - text


```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| album                 | title, release year
| artist                | name

1. Name of the first table (always plural): `albums` 

    Column names: `title`, `release_year`

2. Name of the second table (always plural): `artists` 

    Column names: `name`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: albums
id: SERIAL
title: text
release_year: int

Table: artists
id: SERIAL
name: text
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one Item [TABLE ONE] have many Orders[TABLE TWO]? (Yes)
2. Can one Order [TABLE TWO] have many Items[TABLE ONE]? (No)

You'll then be able to say that:

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one artist have many albums? YES
2. Can one album have many artists? NO

-> Therefore,
-> An artist HAS MANY albums
-> An album BELONGS TO an artist

-> Therefore, the foreign key is on the albums table.
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
);

-- Then the table with the foreign key second.
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
-- The foreign key name is always {other_table_singular}_id
  artist_id int,
  constraint fk_artist foreign key(artist_id)
    references artists(id)
    on delete cascade
);

Orders
  - Order 
  - item_id - int
  - date_order_placed - date
  - customer name - text


--DROP SEQUENCE IF EXISTS items_id_seq;
--DROP SEQUENCE IF EXISTS orders_id_seq;

DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name text,
  unit_price real,
  stock_quantity int
);

-- Then the table with the foreign key second.
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_name text,
  date_order_placed date,
  item_id int,
  constraint fk_item foreign key(item_id)
    references items(id)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO items (name, unit_price, stock_quantity) VALUES ('Football', 8.99, 101);
INSERT INTO items (name, unit_price, stock_quantity) VALUES ('Swimming cap)', 2.99, 400);
INSERT INTO items (name, unit_price, stock_quantity) VALUES ('Baseball bat', 19.99, 10);
INSERT INTO items (name, unit_price, stock_quantity) VALUES ('Gloves', 10.99, 350);


INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Smith', '11-Jun-2024', 1);
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Cane', '11-Jun-2024', 2);
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Jones', '11-Jun-2024', 3);
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Green', '11-Jun-2024', 4);
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Brown', '11-Jun-2024', 1);


```

## 6. Create the tables

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```