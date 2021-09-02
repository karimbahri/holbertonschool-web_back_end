-- trigger creation
-- it reset valid_email if email has been changed
DELIMITER _|

CREATE TRIGGER email_validator BEFORE UPDATE ON users FOR EACH ROW
BEGIN
IF NEW.email <> OLD.email THEN SET NEW.valid_email = 0; END IF;
END; _|
