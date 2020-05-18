CREATE TABLE cities AS
  SELECT 38 AS latitude, 122 AS longitude, "Berkeley" AS name UNION
  SELECT 42,			 71,			   "Cambridge"        UNION
  SELECT 45,			 93,			   "Minneapolis";

CREATE TABLE parents AS
  SELECT "delano" AS parent,	"herbert" AS child UNION
  SELECT "abraham",			"barack"			  UNION
  SELECT "abraham",			"clinton"		  UNION
  SELECT "fillmore",			"abraham"		  UNION
  SELECT "fillmore",			"delano"			  UNION
  SELECT "fillmore",			"grover"			  UNION
  SELECT "eisenhower",		"fillmore";

-- CREATE TABLE dogs AS
--   SELECT "abraham" AS name,	"long" AS fur	UNION
--   SELECT "barack",			"short"			UNION
--   SELECT "clinton",			"long"			UNION
--   SELECT "delano",			"long"			UNION
--   SELECT "eisenhower",		"short"			UNION
--   SELECT "fillmore",			"curly"			UNION
--   SELECT "grover",			"short"			UNION
--   SELECT "herbert",			"curly";

CREATE TABLE grandparents AS
  SELECT a.parent AS grandog, b.child AS granpup
  FROM parents AS a, parents AS b
  WHERE b.parent = a.child;

CREATE TABLE restaurant AS
  SELECT 101 AS "table", 2 AS single, 2 AS couple UNION
  SELECT 102 		     , 0			    , 3			  UNION
  SELECT 103 	     	 , 4			    , 1;

CREATE TABLE ints AS
  SELECT "zero" AS word, 0 AS one, 0 AS two, 0 AS four, 0 AS eight UNION
  SELECT "one"         , 1	   , 0		, 0        , 0          UNION
  SELECT "two"         , 0	   , 2		, 0        , 0          UNION
  SELECT "three"       , 1	   , 2		, 0        , 0          UNION
  SELECT "four"        , 0	   , 0		, 4        , 0          UNION
  SELECT "five"        , 1	   , 0		, 4        , 0          UNION
  SELECT "six"         , 0	   , 2		, 4        , 0          UNION
  SELECT "seven"       , 1	   , 2		, 4        , 0          UNION
  SELECT "eight"       , 0	   , 0		, 0        , 8          UNION
  SELECT "nine"        , 1	   , 0		, 0        , 8;

CREATE TABLE nouns AS
  SELECT "dog" AS phrase	UNION
  SELECT "cat"		   	UNION
  SELECT "bird";

CREATE TABLE ands AS
  SELECT first.phrase || " and " || second.phrase AS phrase FROM nouns AS first, nouns AS second WHERE first.phrase <> second.phrase;

CREATE TABLE dogs AS
    SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
    SELECT "barack"         , "short"      , 52           UNION
    SELECT "clinton"        , "long"       , 47           UNION
    SELECT "delano"         , "long"       , 46           UNION
    SELECT "eisenhower"     , "short"      , 35           UNION
    SELECT "fillmore"       , "curly"      , 32           UNION
    SELECT "grover"         , "short"      , 28           UNION
    SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
    SELECT "toy" AS size, 24 AS min, 28 AS max UNION
    SELECT "mini"       , 28       , 35        UNION
    SELECT "medium"     , 35       , 45        UNION
    SELECT "standard"   , 45       , 60;
