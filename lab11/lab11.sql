.read sp20data.sql

CREATE TABLE obedience AS
  SELECT "seven", "instructor" FROM "students";

CREATE TABLE smallest_int AS
  SELECT "time", "smallest" FROM "students" WHERE "smallest" > 2 ORDER BY "smallest" ASC LIMIT 20;

CREATE TABLE matchmaker AS
  -- SELECT "t1.pet" AS pet, "t1.song" AS song, "t1.color", "t2.color" FROM "students" AS t1, "students" AS t2 WHERE "t1.time" < "t2.time" AND "t1.pet" = "t2.pet" AND "t1.song" = "t2.song";
  select t1.pet, t1.song, t1.color, t2.color from students as t1, students as t2 WHERE t1.time < t2.time AND t1.pet = t2.pet AND t1.song = t2.song;

CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

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

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper SELECT name, height, height FROM dogs;
-- INSERT INTO stacks_helper SELECT t1.dogs || ", " || t2.dogs, t1.stack_height+t2.stack_height, t2.last_height FROM stacks_helper AS t1, stacks_helper AS t2 WHERE t1.dogs < t2.dogs;
INSERT INTO stacks_helper SELECT t1.dogs || ", " || t2.name, t1.stack_height+t2.height, t2.height FROM stacks_helper AS t1, dogs AS t2 WHERE t1.dogs < t2.name;
INSERT INTO stacks_helper SELECT t1.dogs || ", " || t2.name, t1.stack_height+t2.height, t2.height FROM stacks_helper AS t1, dogs AS t2 WHERE t1.dogs NOT LIKE "%" || t2.name || "%";
INSERT INTO stacks_helper SELECT t1.dogs || ", " || t2.name, t1.stack_height+t2.height, t2.height FROM stacks_helper AS t1, dogs AS t2 WHERE t1.dogs NOT LIKE "%" || t2.name || "%";

CREATE TABLE stacks AS
  SELECT * FROM stacks_helper WHERE stack_height >= 170;

CREATE TABLE smallest_int_having AS
 SELECT time, smallest FROM students GROUP BY smallest HAVING count(smallest) = 1 ORDER BY smallest ASC;

CREATE TABLE sp20favpets AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

CREATE TABLE sp20dog AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

CREATE TABLE obedienceimages AS
  SELECT seven, instructor, count(*) FROM obedience WHERE seven = "7" GROUP BY instructor ORDER BY instructor;
