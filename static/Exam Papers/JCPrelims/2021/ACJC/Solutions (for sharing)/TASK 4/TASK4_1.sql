CREATE TABLE Kiosk (
	KioskID INTEGER PRIMARY KEY,
	Location TEXT,
	Rating FLOAT
);

CREATE TABLE BentoBox (
	BentoName TEXT PRIMARY KEY,
	ProductionCost FLOAT,
	ContainEgg INTEGER,
	ContainNut INTEGER,
	ContainSeafood INTEGER
);

CREATE TABLE KioskBento (
	KioskID INTEGER REFERENCES Kiosk(KioskID),
	BentoName TEXT REFERENCES BentoBox(BentoName),
	SellPrice FLOAT,
	PRIMARY KEY(KioskID, BentoName)
);