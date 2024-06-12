CREATE TABLE items (
  id integer primary key,
  name text,
  unit_price real,
  stock_quantity int
);
                   
CREATE TABLE orders (
  id integer primary key,
  customer_name text,
  date_order_placed text,
  item_id int,
  foreign key (item_id) references items(id)
);                   
                   
INSERT INTO items (name, unit_price, stock_quantity) VALUES ('Football', 8.99, 101);
INSERT INTO items (name, unit_price, stock_quantity) VALUES ('Swimming cap', 2.99, 400);
INSERT INTO items (name, unit_price, stock_quantity) VALUES ('Baseball bat', 19.99, 10);
INSERT INTO items (name, unit_price, stock_quantity) VALUES ('Gloves', 10.99, 350);                   
                   
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Smith', '2024-06-11', 1);
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Canes', '2024-06-11', 2);
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Jones', '2024-06-11', 3);
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Green', '2024-06-11', 4);
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Brown', '2024-06-11', 1);                   
