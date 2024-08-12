--  SQL script that creates a function SafeDiv that divides
--  (divides) the first by the second number and returns
--  0 if the second number is equal to 0.

DELIMITER //

DROP FUNCTION IF EXISTS SafeDiv;

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    -- Return 0 if b is 0, otherwise return a divided by b
	RETURN IF (b = 0, 0, a / b);
END //

DELIMITER ;
