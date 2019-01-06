# SQL Basic
* **Primary Key**: it is a column that has a unique value for every row.

* **Foreign Key**: the primary key in another table.

* **LIMIT**: showing the first several rows of the table

<center>LIMIT row_num</center>

* **ORDER BY**: sort our results using the data in any column. The **ORDER BY** statement always comes in a query after the SELECT and FROM statements, but before the **LIMIT** statement.

<center>ORDER BY col_name (DESC)</center>

* **WHERE**: display subsets of tables based on conditions that must be met.

<center>WHERE col_name (>, <, >=, <=, !=, =) value</center>

* **Derived Columns**: a new column that is a combination of existing columns. We can create an alias for the new column using **AS**.

* **LIKE**: perform operations similar to using **WHERE** and `=`, but for cases when you might not know exactly what you are looking for.

<center>WHERE col_name LIKE value</center>

* **IN**: perform operations similar to using **WHERE** and `=`, but for more than one condition.

* **NOT**: This is used with **IN** and **LIKE** to select all of the rows **NOT LIKE** or **NOT IN** a certain condition.

* **AND & BETWEEN**: These allow you to combine operations where all combined conditions must be true.

* **OR**: This allow you to combine operations where at least one of the combined conditions must be true.

# SQL Joins
* **INNER JOIN**:

![](/sql/inner_join.png)

<center>FROM table1 (AS t1) JOIN table2 (AS t2) ON condition</center>

* **LEFT and RIGHT JOIN**:

![](/sql/left_join.png)

<center>FROM table1 LEFT JOIN table2 ON condition</center>

![](/sql/right_join.png)

<center>FROM table1 RIGHT JOIN table2 ON condition</center>




Provide the **name** for each region for every **order**, as well as the **account name** and the **unit price** they paid (total_amt_usd/total) for the order. However, you should only provide the results if the **standard order quantity** exceeds 100 and the **poster order quantity** exceeds 50. Your final table should have 3 columns: **region name**, **account name**, and **unit price**. Sort for the smallest **unit price** first. In order to avoid a division by zero error, adding .01 to the denominator here is helpful (total_amt_usd/(total+0.01).  

# SQL Aggregations
* **NULL**: data does not exist.
<center>IS NULL or IS NOT NULL</center>

* **COUNT**
* **SUM**
* **MIN** & **MAX**
* **AVG**
* **MEDIAN** ?
* **GROUP BY**
* **DISTINCT**
* **HAVING**: same as **WHERE**, but is used for aggregated columns.
* 
