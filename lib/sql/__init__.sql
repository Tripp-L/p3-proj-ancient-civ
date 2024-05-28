DROP TABLE IF EXISTS cultures;
DROP TABLE IF EXISTS deities;
DROP TABLE IF EXISTS artifacts;
DROP TABLE IF EXISTS myths;


CREATE TABLE cultures (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  region TEXT NOT NULL,
  era TEXT NOT NULL
);

CREATE TABLE deities (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  domain TEXT NOT NULL,
  attributes TEXT NOT NULL,
  culture_id INTEGER,
  FOREIGN KEY (culture_id) REFERENCES cultures(id)
);

CREATE TABLE artifacts (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  artifact_type TEXT NOT NULL,
  discovered_date TEXT NOT NULL,
  origin_date TEXT NOT NULL,
  culture_id INTEGER,
  FOREIGN KEY (culture_id) REFERENCES cultures(id)
);

CREATE TABLE myths (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  deity_id INTEGER,
  FOREIGN KEY (deity_id) REFERENCES deities(id)
);
