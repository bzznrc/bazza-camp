#!/usr/bin/env python
# coding: utf-8

from IPython import get_ipython

# %% [cell 1]
# # Is It S-Q-L or 'Sequel'? 🤷‍♂️
#
# **SQL** stands for **Structured Query Language**. SQL lets you access and manipulate databases. SQL is your friend.
#
# Programmers can be quite particular about how it's pronounced. To avoid losing half the audience at the second line, we'll be pronunciation-agnostic.
#
# ### Declarative, Not Imperative 👑
#
# Most programming languages are considered *imperative*, meaning that the programmer defines the specific steps of the program (the **how** of the program).
#
# SQL, on the other hand, is a *declarative* language. This means that the programmer outlines the **what**, or the desired results, and an automated component (called the *query engine*) figures out the "how" to retrieve those results.
#
# ### Nice. What Is a Database Then? 💾
#
# A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a **Database Management System (DBMS)**. Yes, I borrowed this from Google.
#
# Basically, a database is a collection of data tables. You can think of the tables as if they were Excel files, but with the difference that they're usually centralized somewhere instead of being random files.

# %% [cell 2]
# Load the SQL extension
get_ipython().system('pip -q install ipython-sql')
get_ipython().run_line_magic('load_ext', 'sql')

# Connect to the existing SQLite database file
get_ipython().run_line_magic('sql', 'sqlite:///my_database.db')

# %% [cell 3]
# # SELECT Statement 👉
#
# Let's start with the basics. The basic structure of every query will be:
#
# - **SELECT** *[DISTINCT]* [columns]
#   - Here we list all the columns we want in the result set. We can use the wildcard `*` to include all available columns.
#   - We can use `DISTINCT` to have only one occurrence of each distinct row.
# - **FROM** [table]
#   - Here we specify the table we get the data from.
#
# After those two statements, we can have the following, in this order (these are all optional):
#
# - **WHERE** [conditions]
#   - Here we add the filters we might want to apply to the data.
# - **GROUP BY** [column]
#   - Here we specify the column(s) we want our data to be grouped by in the result set.
#   - Grouping is not a straightforward concept; we'll see it in a dedicated lesson.
# - **ORDER BY** [column] *[ASC/DESC]*
#   - Here we specify the column(s) we want our data to be ordered by in the result set.
#   - We can add `ASC` if we want them to be in ascending order, `DESC` for descending order. The default is ascending.
# - **LIMIT** [number of rows]
#   - Cuts the result to the first N rows.

# %% [cell 4]
# **Note:** In the previous lesson, we set up our data tables (`sql_101_transactions`, `sql_101_product`, and `sql_101_store`). Make sure those tables are created and populated with data before running the queries below.

# %% [cell 5]
# Let's see an example. This is a comment in SQL.
#
# This is the most basic query we can have. It means "Select all columns (`*`) from the table `sql_101_transactions`". Let's run it.

# %% [cell 6]
# This query selects all columns from the sql_101_transactions table.

get_ipython().run_cell_magic('sql', '', """SELECT * -- Selecting all the columns
FROM sql_101_transactions -- From the sql_101_transactions table
LIMIT 5;""")

# %% [cell 7]
# Here, we added a `LIMIT` clause to only show the first 5 rows.

# %% [cell 8]
# Now, let's add a `WHERE` clause to limit the results after a certain date and an `ORDER BY` clause to see the transactions with the biggest amount first.

# %% [cell 9]
# Adding WHERE and ORDER BY clauses

get_ipython().run_cell_magic('sql', '', """SELECT * -- Selecting all the columns
FROM sql_101_transactions -- From the sql_101_transactions table
WHERE transaction_date >= '2024-06-01' -- With the date being June 1 or later
ORDER BY amount DESC; -- Ordering by amount in descending order""")

# %% [cell 10]
# # LIMIT Clause 👮‍♂️
#
# The `LIMIT` clause is useful when you need to quickly assess the structure of a table because it effectively truncates the result set to a manageable number of records.

# %% [cell 11]
# Example using LIMIT to display the first 5 rows

get_ipython().run_cell_magic('sql', '', """SELECT *
FROM sql_101_transactions
LIMIT 5;""")

# %% [cell 12]
# # WHERE Clause 📌
#
# The `WHERE` clause is *where* you put your filters (pun intended).
#
# The most basic form of filter is based on a column value, and you can use comparison operators to express it:
#
# - `COLUMN = value`
# - `COLUMN <> value` (*`<>` means "is different from"; some other languages use the symbol `!=` for this*)
# - `COLUMN <, <=, >, >= value`
# - `COLUMN IN (value1, value2, value3, ...)`
# - `COLUMN NOT IN (value1, value2, value3, ...)`
# - Any combination of the above using `AND` and `OR` and isolating logical blocks with parentheses `( )`

# %% [cell 13]
# Let's see how to apply the WHERE clause to add a filter to the query.

get_ipython().run_cell_magic('sql', '', """SELECT *
FROM sql_101_transactions
WHERE sku_id IN (1, 2, 3);""")

# %% [cell 14]
# This query selects all transactions where the `sku_id` is either 1, 2, or 3.

# %% [cell 15]
# # Fun Exercises 📚

# %% [cell 16]
# **Exercise 1:**
#
# Select all transactions where the `price_per_unit` is higher than 2 and the `store_id` is 1.

# %% [cell 17]
# Write your SQL query here:

get_ipython().run_cell_magic('sql', '', """SELECT *
FROM sql_101_transactions
WHERE price_per_unit > 2 AND store_id = 1;""")

# %% [cell 18]
# **Exercise 2:**
#
# Select all transactions where the `amount` is less than or equal to 2 and the `sku_id` is not in (3, 4, 5).

# %% [cell 19]
# Write your SQL query here:

get_ipython().run_cell_magic('sql', '', """SELECT *
FROM sql_101_transactions
WHERE amount <= 2 AND sku_id NOT IN (3, 4, 5);""")

# %% [cell 20]
# **Exercise 3:**
#
# Find all transactions that occurred between '2024-06-01' and '2024-06-30'.

# %% [cell 21]
# Write your SQL query here:

get_ipython().run_cell_magic('sql', '', """SELECT *
FROM sql_101_transactions
WHERE transaction_date BETWEEN '2024-06-01' AND '2024-06-30';""")

# %% [cell 22]
# # Selecting Specific Columns 📋
#
# We can limit the list of columns that we select in a query by listing them:
#
# - **SELECT** `column1`, `column2`, `column3`, ...

# %% [cell 23]
# Let's play with the SELECT statement to avoid displaying the IDs of the records.

get_ipython().run_cell_magic('sql', '', """SELECT transaction_date, customer_id, amount,
       amount * price_per_unit AS total_price
FROM sql_101_transactions
WHERE customer_id = 101;""")

# %% [cell 24]
# In this query, we also calculated a new column `total_price` by multiplying `amount` and `price_per_unit`.

# %% [cell 25]
# # ORDER BY Clause 🔼🔽
#
# We can sort our results in ascending or descending order. It works on numerical data as well as text data.
#
# - **ORDER BY** `column` *[ASC/DESC]*
#   - `ASC` for ascending order (default).
#   - `DESC` for descending order.

# %% [cell 26]
# Now let's remove the filter to get all transactions and order them by `total_price`.

get_ipython().run_cell_magic('sql', '', """SELECT *,
       amount * price_per_unit AS total_price
FROM sql_101_transactions
ORDER BY total_price DESC; -- Sorting by total_price in descending order""")

# %% [cell 27]
# # DISTINCT Keyword 🥇
#
# If we use `DISTINCT`, the query will run as normal, but before displaying, every duplicate row will be removed. This is convenient if we're searching for a list of unique values.
#
# Later on, we'll see the `GROUP BY` clause, which will allow us to get much more complex results, and we'll see that `DISTINCT` is just a more limited and simplified version of a `GROUP BY` in effect.

# %% [cell 28]
# This is how we check the full list of SKUs.

get_ipython().run_cell_magic('sql', '', """SELECT DISTINCT sku_id
FROM sql_101_transactions;""")

# %% [cell 29]
# This will give us all the unique combinations of customers and SKUs.

get_ipython().run_cell_magic('sql', '', """SELECT DISTINCT customer_id, sku_id
FROM sql_101_transactions
ORDER BY customer_id, sku_id; -- Ordering to keep customer records together""")

# %% [cell 30]
# # Other Fun Exercises 📚

# %% [cell 31]
# **Exercise 4:**
#
# Find all unique `customer_id` values who have purchased products from `sku_id` 1.

# %% [cell 32]
# Write your SQL query here:

get_ipython().run_cell_magic('sql', '', """SELECT DISTINCT customer_id
FROM sql_101_transactions
WHERE sku_id = 1;""")

# %% [cell 33]
# **Exercise 5:**
#
# Select all transactions where the `amount` multiplied by `price_per_unit` (i.e., `total_price`) exceeds 10.

# %% [cell 34]
# Write your SQL query here:

get_ipython().run_cell_magic('sql', '', """SELECT *,
       amount * price_per_unit AS total_price
FROM sql_101_transactions
WHERE amount * price_per_unit > 10;""")

# %% [cell 35]
# # String Functions ✂️
#
# Formatting is important. Sometimes, we need to manipulate string data to extract or combine certain parts.
#
# SQLite doesn't support `LEFT`, `RIGHT`, or `CONCAT` functions directly, but we can use `substr` and the concatenation operator `||`.

# %% [cell 36]
# Example using substr function
# Let's extract parts of the product names from the sql_101_product table.

get_ipython().run_cell_magic('sql', '', """SELECT product_name,
       substr(product_name, 1, 5) AS short_name,
       substr(product_name, -5, 5) AS end_name
FROM sql_101_product
LIMIT 10;""")

# %% [cell 37]
# In this query, we take the first 5 characters and the last 5 characters of the `product_name` column.

# %% [cell 38]
# Example using concatenation operator to combine strings
# Let's create a full description by combining brand and product_name.

get_ipython().run_cell_magic('sql', '', """SELECT brand || ' ' || product_name AS full_description,
       *
FROM sql_101_product
LIMIT 10;""")

# %% [cell 39]
# # Table Statements 🛠
#
# So far, we've been selecting data from tables, but SQL also allows you to modify the tables themselves.
#
# Very briefly, these are the kinds of commands SQL supports:
#
# - **DDL** – Data Definition Language (`CREATE`, `ALTER`, `DROP`)
# - **DQL** – Data Query Language (`SELECT`)
# - **DML** – Data Manipulation Language (`INSERT`, `UPDATE`, `DELETE`)
# - **DCL** – Data Control Language (permissions)
# - **TCL** – Transaction Control Language (`COMMIT`, `ROLLBACK`)

# %% [cell 40]
# Let's create a new table called hkt_sql_customers.

get_ipython().run_cell_magic('sql', '', """CREATE TABLE hkt_sql_customers (
    customer_id INT,
    customer_name TEXT,
    customer_age INT
);""")

# %% [cell 41]
# We have now created a new table `hkt_sql_customers`.

# %% [cell 42]
# Inserting data into the table.

get_ipython().run_cell_magic('sql', '', """INSERT INTO hkt_sql_customers (customer_id, customer_name, customer_age)
VALUES (101, 'Alice', 30),
       (102, 'Bob', 35),
       (103, 'Charlie', 25);""")

# %% [cell 43]
# Altering the table to add a new column.

get_ipython().run_cell_magic('sql', '', """ALTER TABLE hkt_sql_customers ADD COLUMN customer_email TEXT;""")

# %% [cell 44]
# Inserting a new row with the additional column.

get_ipython().run_cell_magic('sql', '', """INSERT INTO hkt_sql_customers (customer_id, customer_name, customer_age, customer_email)
VALUES (104, 'Diana', 28, 'diana@example.com');""")

# %% [cell 45]
# Updating rows where `customer_email` is NULL.

get_ipython().run_cell_magic('sql', '', """UPDATE hkt_sql_customers
SET customer_email = 'unknown@example.com'
WHERE customer_email IS NULL;""")

# %% [cell 46]
# Deleting a row from the table.

get_ipython().run_cell_magic('sql', '', """DELETE
FROM hkt_sql_customers
WHERE customer_id = 103;""")

# %% [cell 47]
# Selecting all data from `hkt_sql_customers` to see the current state.

get_ipython().run_cell_magic('sql', '', """SELECT *
FROM hkt_sql_customers;""")

# %% [cell 48]
# Dropping the table.

get_ipython().run_cell_magic('sql', '', """DROP TABLE hkt_sql_customers;""")

# %% [cell 49]
# # Conclusion 🎉
#
# In this lesson, we've covered the basics of SQL, including how to select data, filter it, order it, perform basic data manipulation, and work with string functions using the tables we have created.
#
# SQL is a powerful language for interacting with databases, and understanding these fundamentals is essential for anyone working with data.
#
# In the next lessons, we'll delve deeper into grouping data, joining tables, and more advanced SQL functionalities.

