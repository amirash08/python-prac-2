CREATE or REPLACE FUNCTION find_pattern(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN 
    RETURN QUERY 
    SELECT id, name, phone FROM phonebook 
    WHERE name ILIKE '%' || pattern || '%'
    OR phone ILIKE '%' || pattern || '%';
END; 
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION phonebook_paginated(phone_limit INT, phone_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN 
    RETURN QUERY 
    SELECT id, name, phone FROM phonebook
    ORDER BY id 
    LIMIT phone_limit OFFSET phone_offset;
END; 
$$ LANGUAGE plpgsql;


