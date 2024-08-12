-- Creates a stored procedure AddBonus that adds
-- a new correction for a student.

DELIMITER //

DROP PROCEDURE IF EXISTS AddBonus;

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255), 
    IN score INT
)
BEGIN
    -- Inserts the project if it doesn't exist
    IF NOT EXISTS (SELECT name FROM projects WHERE name = project_name) THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    -- Inserts the correction with a direct subquery
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END//

DELIMITER ;

