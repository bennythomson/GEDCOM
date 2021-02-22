# GEDCOM

Parses and displays the data contained in a GEDCOM File.

Sample output:

```

Please specify GEDCOM file: 
simpson_family.ged
+----+--------------------+-----+--------------+-------+-------------+------+--------+
| ID |        NAME        | SEX |     BIRT     | ALIVE |     DEAT    | CHIL | SPOUSE |
+----+--------------------+-----+--------------+-------+-------------+------+--------+
| I1 |  Homer /Simpson/   |  M  | 12 MAY 1956  |   T   |     None    | F2@  |  F1@   |
| I2 |  Marge /Bouvier/   |  F  | 19 MAR 1956  |   T   |     None    | None |  F1@   |
| I3 | Abraham /Simpson/  |  M  | 19 MAY 1920  |   T   |     None    | None |  F3@   |
| I4 |   Mona /Olsen/     |  F  | 15 MAR 1929  |   F   | 6 JUL 2007  | None |  F2@   |
| I5 |  Amber /Simpson/   |  F  | 4 APR 1940   |   T   |     None    | None |  F3@   |
| I6 |  Abbey /Simpson/   |  F  | 8 NOV 1960   |   T   |     None    | F3@  |  None  |
| I7 |  Bart /Simpson/    |  M  | 1 APR 1979   |   T   |     None    | F1@  |  None  |
| I8 |  Lisa /Simpson/    |  F  | 9 MAY 1984   |   T   |     None    | F1@  |  None  |
| I9 | Maggie /Simpson/   |  F  | 17 DEC 1989  |   T   |     None    | F1@  |  None  |
+----+--------------------+-----+--------------+-------+-------------+------+--------+
+----+----------+------------+---------+----------+
| id | divorced | husband_id | wife_id | children |
+----+----------+------------+---------+----------+
| F1 |   None   |   @I1@     |  @I2@   |  @I9@    |
| F2 |   None   |   @I3@     |  @I4@   |  @I1@    |
| F3 |   None   |    None    |   None  |   None   |
+----+----------+------------+---------+----------+

```
