-- trigger creation
-- it decrements the quantity of an item after ordering it
CREATE TRIGGER decrement
AFTER INSERT
ON orders FOR EACH
ROW UPDATE items 
SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name;
