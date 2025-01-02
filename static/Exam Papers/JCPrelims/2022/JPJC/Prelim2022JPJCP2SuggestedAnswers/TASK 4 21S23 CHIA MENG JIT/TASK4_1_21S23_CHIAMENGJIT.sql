DROP TABLE IF EXISTS 'ProductRental';
DROP TABLE IF EXISTS 'CustomerRental';
DROP TABLE IF EXISTS 'Customer';
DROP TABLE IF EXISTS 'Product';

CREATE TABLE `Customer` (
	`Email`	TEXT,
	`FirstName`	TEXT,
	`LastName`	TEXT,
	`ContactNumber`	TEXT,
	`DOB`	TEXT,
	`Address`	TEXT,
	PRIMARY KEY(`Email`)
);

CREATE TABLE `Product` (
	`CatalogueNumber`	INTEGER,
	`Category`	TEXT,
	`Brand`	TEXT,
	`Size`	INTEGER,
	`Fee`	INTEGER,
	PRIMARY KEY(`CatalogueNumber`)
);

CREATE TABLE `CustomerRental` (
	`ID`	INTEGER,
	`Email`	TEXT,
	`StartDate`	TEXT,
	`EndDate`	TEXT,
	FOREIGN KEY(`Email`) REFERENCES `Customer`(`Email`),
	PRIMARY KEY(`ID`)
);

CREATE TABLE `ProductRental` (
	`ID`	INTEGER,
	`CatalogueNumber`	INTEGER,
	`Returned`	TEXT,
	FOREIGN KEY(`CatalogueNumber`) REFERENCES `Product`(`CatalogueNumber`),
	FOREIGN KEY(`ID`) REFERENCES `CustomerRental`(`ID`),
	PRIMARY KEY(`ID`, 'CatalogueNumber')
);