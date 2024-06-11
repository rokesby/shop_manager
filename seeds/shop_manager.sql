DROP TABLE IF EXISTS items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name text,
  unit_price real,
  stock_quantity int
);

-- Then the table with the foreign key second.
-- TODO: Change the date_order_placed into a DATE field and the unit test will break - need to recheck the python date type for this property.
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_name text,
  date_order_placed text,
  item_id int,
  constraint fk_item foreign key(item_id)
    references items(id)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO items (name, unit_price, stock_quantity) VALUES ('Football', 8.99, 101);
INSERT INTO items (name, unit_price, stock_quantity) VALUES ('Swimming cap', 2.99, 400);
INSERT INTO items (name, unit_price, stock_quantity) VALUES ('Baseball bat', 19.99, 10);
INSERT INTO items (name, unit_price, stock_quantity) VALUES ('Gloves', 10.99, 350);


INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Smith', '2024-06-11', 1);
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Canes', '2024-06-11', 2);
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Jones', '2024-06-11', 3);
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Green', '2024-06-11', 4);
INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES ('Mr Brown', '2024-06-11', 1);

