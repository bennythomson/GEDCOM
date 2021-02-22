
CREATE TABLE IF NOT EXISTS individuals (
	ID varchar PRIMARY KEY,
	NAME text,
	SEX char,
	BIRT date,
	ALIVE boolean ,
	DEAT date ,
	CHIL varchar ,
	SPOUSE varchar 

);


CREATE TABLE IF NOT EXISTS families (
	id varchar PRIMARY KEY,
	divorced boolean ,
	husband_id text ,
	wife_id text ,
	children text 
	

);