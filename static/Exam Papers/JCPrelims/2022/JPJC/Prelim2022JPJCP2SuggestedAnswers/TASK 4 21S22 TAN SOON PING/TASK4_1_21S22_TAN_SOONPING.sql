create table Customer(
	Email TEXT,
	FirstName TEXT,
	LastName TEXT,
	ContactNumber TEXT,
	DOB TEXT,
	Address TEXT,
	primary key (Email)
);

create table Product(
	CatalogueNumber INTEGER,
	Category TEXT,
	Brand TEXT,
	Size INTEGER,
	Fee INTEGER,
	primary key (CatalogueNumber)
);

create table CustomerRental(
	ID INTEGER,
	Email TEXT,
	StartDate TEXT,
	EndDate TEXT,
	primary key (ID),
	foreign key (Email) references Customer(Email)
);

create table ProductRental(
	ID INTEGER,
	CatalogueNumber INTEGER,
	Returned INTEGER,
	primary key (ID,CatalogueNumber)
	foreign key (ID) references CustomerRental(ID),
	foreign key (CatalogueNumber) references Product(CatalogueNumber)
);