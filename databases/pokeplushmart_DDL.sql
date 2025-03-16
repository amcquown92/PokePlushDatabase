SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;

CREATE TABLE `Customers` (
  `custID` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(50) NOT NULL,
  `lastName` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`custID`),
  UNIQUE KEY `custID` (`custID`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
INSERT INTO `Customers` (firstName, lastName, email, address) 
VALUES ('Chad','Thunderstone','chad.thunder@shockmail.com','123 Bolt Ave'),
('Gregory','Bubbles','bubbly.greg@fizzymail.com','456 Aqua St'),
('Xander','Volkov','darklord.volkov@fangmail.com','789 Shadow Ln'),
('Sasha','Evergreen','sasha.treehugger@leafmail.com','321 Forest Rd'),
('Dakota','Rivers','d.riptide@currentmail.com',NULL),
('Bianca','Summers','sunny.bianca@heatwave.net','159 Sunshine Blvd');
UNLOCK TABLES;

--
-- Table structure for table `Pokemon`
--

DROP TABLE IF EXISTS `Pokemon`;

CREATE TABLE `Pokemon` (
  `plushieID` int(11) NOT NULL AUTO_INCREMENT,
  `plushieName` varchar(50) NOT NULL,
  `plushieType` ENUM('Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy', 'Unknown', 'Shadow') NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stockQty` int(11) DEFAULT 0,
  PRIMARY KEY (`plushieID`),
  UNIQUE KEY `plushieID` (`plushieID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Pokemon`
--

LOCK TABLES `Pokemon` WRITE;
INSERT INTO `Pokemon` (plushieName, plushieType, price, stockQty) 
VALUES ('Pikachu','Electric', 45.00, 100),
('Squirtle','Water', 45.00, 76),
('Charizard','Fire', 75.00, 26),
('Ivysaur','Grass', 75.00, 100),
('Trubbish','Poison', 45.00, 200),
('Rattata','Normal', 25.00, 98);
UNLOCK TABLES;

--
-- Table structure for table `Sales`
--

DROP TABLE IF EXISTS `Sales`;

CREATE TABLE `Sales` (
  `saleID` int(11) NOT NULL AUTO_INCREMENT,
  `custID` int(11) NULL,
  `saleDate` date NOT NULL DEFAULT current_date,
  PRIMARY KEY (`saleID`),
  UNIQUE KEY `saleID` (`saleID`),
  KEY `custID` (`custID`),
  CONSTRAINT `Sales_ibfk_1` FOREIGN KEY (`custID`) REFERENCES `Customers` (`custID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Sales`
--

LOCK TABLES `Sales` WRITE;
INSERT INTO `Sales` (custID, saleDate)
VALUES ((SELECT custID FROM `Customers` WHERE `firstName` = 'Chad' AND `lastName` = 'Thunderstone'),'2025-02-01'),
((SELECT custID FROM `Customers` WHERE `firstName` = 'Chad' AND `lastName` = 'Thunderstone'),'2025-02-01'),
((SELECT custID FROM `Customers` WHERE `firstName` = 'Gregory' AND `lastName` = 'Bubbles'),'2025-01-15'),
((SELECT custID FROM `Customers` WHERE `firstName` = 'Xander' AND `lastName` = 'Volkov'),'2025-01-08'),
((SELECT custID FROM `Customers` WHERE `firstName` = 'Sasha' AND `lastName` = 'Evergreen'),'2025-01-28'),
((SELECT custID FROM `Customers` WHERE `firstName` = 'Dakota' AND `lastName` = 'Rivers'),'2025-01-31'),
((SELECT custID FROM `Customers` WHERE `firstName` = 'Bianca' AND `lastName` = 'Summers'),'2025-02-07'),
((SELECT custID FROM `Customers` WHERE `firstName` = 'Bianca' AND `lastName` = 'Summers'),'2025-02-07');
UNLOCK TABLES;

--
-- Table structure for table `SaleItems`
--

DROP TABLE IF EXISTS `SaleItems`;

CREATE TABLE `SaleItems` (
  `saleItemID` int(11) NOT NULL AUTO_INCREMENT,
  `saleID` int(11) NOT NULL,
  `plushieID` int(11) NOT NULL,
  `quantity` int(11) NOT NULL DEFAULT 1,
  PRIMARY KEY (`saleItemID`),
  UNIQUE KEY `saleItemID` (`saleItemID`),
  KEY `FK_SaleItems_saleID` (`saleID`),
  KEY `FK_SaleItems_plushieID` (`plushieID`),
  CONSTRAINT `FK_SaleItems_plushieID` FOREIGN KEY (`plushieID`) REFERENCES `Pokemon` (`plushieID`) ON DELETE CASCADE,
  CONSTRAINT `FK_SaleItems_saleID` FOREIGN KEY (`saleID`) REFERENCES `Sales` (`saleID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `SaleItems`
--

LOCK TABLES `SaleItems` WRITE;
INSERT INTO `SaleItems` (saleID, plushieID, quantity)
VALUES ((SELECT saleID FROM Sales WHERE saleDate = '2025-02-01' AND custID = (SELECT custID FROM Customers WHERE firstName = 'Chad' AND lastName = 'Thunderstone') LIMIT 1),
 (SELECT plushieID FROM Pokemon WHERE plushieName = 'Pikachu' LIMIT 1), 1),
 
((SELECT saleID FROM Sales WHERE saleDate = '2025-02-01' AND custID = (SELECT custID FROM Customers WHERE firstName = 'Chad' AND lastName = 'Thunderstone') LIMIT 1),
 (SELECT plushieID FROM Pokemon WHERE plushieName = 'Squirtle' LIMIT 1), 1),
 
((SELECT saleID FROM Sales WHERE saleDate = '2025-01-15' AND custID = (SELECT custID FROM Customers WHERE firstName = 'Gregory' AND lastName = 'Bubbles') LIMIT 1),
 (SELECT plushieID FROM Pokemon WHERE plushieName = 'Charizard' LIMIT 1), 1),
 
((SELECT saleID FROM Sales WHERE saleDate = '2025-01-08' AND custID = (SELECT custID FROM Customers WHERE firstName = 'Xander' AND lastName = 'Volkov') LIMIT 1),
 (SELECT plushieID FROM Pokemon WHERE plushieName = 'Squirtle' LIMIT 1), 1),
 
((SELECT saleID FROM Sales WHERE saleDate = '2025-01-28' AND custID = (SELECT custID FROM Customers WHERE firstName = 'Sasha' AND lastName = 'Evergreen') LIMIT 1),
 (SELECT plushieID FROM Pokemon WHERE plushieName = 'Ivysaur' LIMIT 1), 1),
 
((SELECT saleID FROM Sales WHERE saleDate = '2025-01-31' AND custID = (SELECT custID FROM Customers WHERE firstName = 'Dakota' AND lastName = 'Rivers') LIMIT 1),
 (SELECT plushieID FROM Pokemon WHERE plushieName = 'Trubbish' LIMIT 1), 1),
 
((SELECT saleID FROM Sales WHERE saleDate = '2025-02-07' AND custID = (SELECT custID FROM Customers WHERE firstName = 'Bianca' AND lastName = 'Summers') LIMIT 1),
 (SELECT plushieID FROM Pokemon WHERE plushieName = 'Rattata' LIMIT 1), 1),
 
((SELECT saleID FROM Sales WHERE saleDate = '2025-02-07' AND custID = (SELECT custID FROM Customers WHERE firstName = 'Bianca' AND lastName = 'Summers') LIMIT 1),
 (SELECT plushieID FROM Pokemon WHERE plushieName = 'Trubbish' LIMIT 1), 1);
UNLOCK TABLES;


SET FOREIGN_KEY_CHECKS=1;
COMMIT;
