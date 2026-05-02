CREATE PROCEDURE insert_name_phone(phone_name VARCHAR(100), phone_phone VARCHAR(100))
LANGUAGE plpgsql AS $$
BEGIN 
    IF EXISTS (SELECT 1 FROM phonebook WHERE phone_name = name)
        THEN UPDATE phonebook 
        SET phone = phone_phone
        WHERE phone_name = name;
    ELSE 
        INSERT INTO phonebook (name, phone)
        VALUES (phone_name, phone_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_user(phone_name VARCHAR(100), phone_phone VARCHAR(100))
LANGUAGE plpgsql AS $$
BEGIN   
    DELETE FROM phonebook WHERE (phone_name IS NOT NULL AND name = phone_name)
    OR (phone_phone IS NOT NULL AND phone = phone_phone);
END;
$$;


CREATE OR REPLACE PROCEDURE add_many_users(users JSON)
LANGUAGE plpgsql AS $$ 
DECLARE 
    now_user JSON;  -- текущий пользователь (1 JSON запись )
    negative_users JSON := '[]'::JSON; -- пустой JSON массив для хранения невалидных пользователей
BEGIN 
    FOR now_user IN SELECT * FROM json_array_elements(users)
    LOOP 
        IF now_user->>'phone' ~ '^\+?\d+$' THEN 
            CALL insert_name_phone(
                now_user->>'name',
                now_user->>'phone'
            );
        ELSE 
            negative_users := negative_users || json_build_array(now_user)
        END IF;
    END LOOP;
END; 
$$;



