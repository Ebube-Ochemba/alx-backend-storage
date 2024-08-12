-- SQL script that creates a stored procedure
-- ComputeAverageScoreForUser that computes and store the
-- average score for a student

DELIMITER //

-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Create the stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    -- Update the user's average_score with the computed average from corrections
    UPDATE users
    SET average_score = (
        SELECT AVG(score) 
        FROM corrections
        WHERE user_id = user_id
    )
    WHERE id = user_id;
END;//

DELIMITER ;
