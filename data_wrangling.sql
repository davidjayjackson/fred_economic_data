SELECT  t.date,t.GS30,i.CPIAUCNS,m.MORTGAGE30US,u.UNRATE
FROM treasury t
INNER JOIN inflation i
ON t.date = i.date
INNER JOIN mortgage m
ON t.date = m.date
INNER JOIN unemployment u
ON t.date = u.date;

CREATE TABLE IF NOT EXISTS fred (
    date DATE NOT NULL,
    GS30 REAL NOT NULL,
    CPIAUCNS REAL NOT NULL,
    MORTGAGE30US REAL NOT NULL,
    UNRATE REAL NOT NULL
);

INSERT INTO fred (date, GS30, CPIAUCNS, MORTGAGE30US, UNRATE)
SELECT t.date, t.GS30, i.CPIAUCNS, m.MORTGAGE30US, u.UNRATE
FROM treasury t
INNER JOIN inflation i
ON t.date = i.date
INNER JOIN mortgage m
ON t.date = m.date
INNER JOIN unemployment u
ON t.date = u.date;

UPDATE fred SET date = STRFTIME('%Y-%m-%d', date);