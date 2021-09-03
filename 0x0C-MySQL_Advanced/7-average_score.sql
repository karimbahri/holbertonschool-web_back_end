-- procedure creation to calculate average score
DELIMITER _|
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN UPDATE users SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id) WHERE user_id = id; END _|
