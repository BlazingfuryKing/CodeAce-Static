CREATE TABLE Members (Mem_ID TEXT PRIMARY KEY,
						Mem_Name TEXT,
						Mem_DOB TEXT)
						
CREATE TABLE Competitions (Comp_ID TEXT PRIMARY KEY, 
							Comp_Name TEXT)
							
							
CREATE TABLE Scores (Comp_ID TEXT , 
						Mem_ID TEXT,
						Score INT,
	PRIMARY KEY(Comp_ID,Mem_ID),
	FOREIGN KEY(Comp_ID) REFERENCES Competitions(Comp_ID),
	FOREIGN KEY(Mem_ID) REFERENCES Members(Mem_ID))
	
