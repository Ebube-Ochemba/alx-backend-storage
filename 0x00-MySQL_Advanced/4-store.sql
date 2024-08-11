-- SQL script that creates a trigger that decreases the quantity
-- of an item after adding a new order.

-- Drop the trigger if it already exists
DROP TRIGGER IF EXISTS decrease_item_quantity;

-- Create the trigger
CREATE TRIGGER decrease_item_quantity
    AFTER INSERT ON orders
    FOR EACH ROW
        UPDATE items
        SET quantity = quantity - NEW.number
        WHERE name = NEW.item_name;
