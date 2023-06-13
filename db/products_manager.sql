DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    name varchar(255)
);

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    manufacturer_id INT NOT NULL REFERENCES manufacturers(id) ON DELETE CASCADE,
    title varchar(255),
    description varchar(255),
    stock_quantity INT NOT NULL,
    buying_cost INT NOT NULL,
    selling_price INT NOT NULL
);