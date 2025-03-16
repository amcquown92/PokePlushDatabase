 -- get ALL pokemon IDs and Names (for dropdowns)
SELECT plushieID, plushieName FROM Pokemon;

-- get ALL Sales with customer names (Sales page)
SELECT Sales.saleID, Customers.firstName, Customers.lastName, Sales.saleDate
FROM Sales
INNER JOIN Customers ON Sales.custID = Customers.custID;

-- get a single sale's Data (edit Sale)
SELECT * FROM Sales WHERE saleID = :saleID_selected_from_sales_page;

-- get ALL Customers (for Add/Edit Sales form dropdowns)
SELECT custID, firstName, lastName FROM Customers;

-- get ALL SalesItems with Pokemon details (SalesItems page)
SELECT SalesItems.saleItemID, Sales.saleID, Pokemon.plushieName, SalesItems.quantity
FROM SalesItems
INNER JOIN Sales ON SalesItems.saleID = Sales.saleID
INNER JOIN Pokemon ON SalesItems.plushieID = Pokemon.plushieID;

-- add a new plushie (insert new Pokemon plush into inventory)
INSERT INTO Pokemon (plushieName, plushieType, price, stockQty)
VALUES (:plushieName_input, :plushieType_input, :price_input, :stockQty_input);

-- associate sale with plushie (create M:N relationship)
INSERT INTO SalesItems (saleID, plushieID, quantity)
VALUES (:saleID_selected, :plushieID_selected, :quantity_input);

-- add a new Customer (insert new Customer into inventory)
INSERT INTO Customers (firstName, lastName, email, address)
VALUES (:firstName_input, :lastName_input, :email_input, :address_input);

-- add a new Sale (insert new Sale into inventory)
INSERT INTO Sales (custID, saleDate)
VALUES (:custID_input, :saleDate_input);

-- update Pokemon data
UPDATE Pokemon
SET plushieName = :plushieName_input,
    plushieType = :plushieType_input,
    price = :price_input,
    stockQty = :stockQty_input
WHERE plushieID = :plushieID_selected;

-- update  Customers data
UPDATE Customers
SET firstName = :firstName_input,
    lastName = :lastName_input,
    email = :email_input,
    address = ;address_input 
WHERE custID = :custID_selected;

-- update Sales data
UPDATE Sales
SET custID = custID_input,
    saleDate = saleDate_input
WHERE saleID = saleID_selected;

-- update  SaleItems data
UPDATE SaleItems
SET saleID = saleID_input,
    plushieID = plushieID_input,
    quantity = quantity_input
WHERE saleItemID = saleItemID_selected;

-- delete a Pokemon plushie from inventory
DELETE FROM Pokemon
WHERE plushieID = :plushieID_selected;

-- remove SaleItem (delete M:N relationship)
DELETE FROM SalesItems
WHERE saleID = :saleID_selected AND plushieID = :plushieID_selected;

-- remove Customer from database
DELETE FROM Customers
WHERE custID = :custID_selected;

--remove a Sale from database
DELETE FROM Sales 
WHERE saleID  :saleID_selected;