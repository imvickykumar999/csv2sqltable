# Python Package : [csv2sqltable](https://pypi.org/project/csv2sqltable/)

    pip install csv2sqltable -U

![image](https://github.com/imvickykumar999/csv2sqltable/assets/50515418/d10799b2-875d-46ff-81f6-565771f6c44f)

-----------

Input: `customer.csv`:
------

customer_id | customername | lastname | country | age | phone
----------- | ------------ | -------- | ------- | --- | -----
1 | Shubham | Thakur | India | 23 | xxxxxxxxxx
2 | Aman | Chopra | Australia | 21 | xxxxxxxxxx
3 | Naveen | Tulasi | "Sri Lanka" | 24 | xxxxxxxxxx
4 | Aditya | Arpan | Austria | 21 | xxxxxxxxxx
5 | "Nishant. Salchichas S.A." | Jain | Spain | 22 | xxxxxxxxxx

Code:
-----

    import csv2sqltable.convert as c2s
    
    print(c2s.transform('customer.csv'))
    
Output:
-------

    %%sql
    -- DROP TABLE customer;
    
    CREATE TABLE customer (
    customer_id VARCHAR(100),
    customername VARCHAR(100),
    lastname VARCHAR(100),
    country VARCHAR(100),
    age VARCHAR(100),
    phone VARCHAR(100)
    );
    
    INSERT INTO customer (customer_id, customername, lastname, country, age, phone)
    VALUES
    ('1', 'Shubham', 'Thakur', 'India', '23', 'xxxxxxxxxx'),
    ('2', 'Aman', 'Chopra', 'Australia', '21', 'xxxxxxxxxx'),
    ('3', 'Naveen', 'Tulasi', 'Sri Lanka', '24', 'xxxxxxxxxx'),
    ('4', 'Aditya', 'Arpan', 'Austria', '21', 'xxxxxxxxxx'),
    ('5', 'Nishant. Salchichas S.A.', 'Jain', 'Spain', '22', 'xxxxxxxxxx');
    
    SELECT * FROM customer;
