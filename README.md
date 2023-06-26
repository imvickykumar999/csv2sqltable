# `Python Package` : [`csv2sqltable`](https://pypi.org/project/csv2sqltable/)

    !pip install csv2sqltable -U

![image](https://github.com/imvickykumar999/csv2sqltable/assets/50515418/d10799b2-875d-46ff-81f6-565771f6c44f)

-----------

`Input` : `customer.csv`
------

customer_id | customername | lastname | country | age | phone
----------- | ------------ | -------- | ------- | --- | -----
1 | Shubham | Thakur | India | 23 | xxxxxxxxxx
2 | Aman | Chopra | Australia | 21 | xxxxxxxxxx
3 | Naveen | Tulasi | "Sri Lanka" | 24 | xxxxxxxxxx
4 | Aditya | Arpan | Austria | 21 | xxxxxxxxxx
5 | "Nishant. Salchichas S.A." | Jain | Spain | 22 | xxxxxxxxxx

--------

`Code` : `run in google colab`
-----

    import csv2sqltable.convert as c2s
    
    print(c2s.transform('customer.csv'))

------------

`Output` : `copy and paste in cell`
-------

    !pip install "SQLAlchemy<1.4"
    
    %%sql
    /*
    %reload_ext sql
    
    %%sql sqlite:///vicks.db
    */
    
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

------------

`Sub Output` : `on ruuning magic sql command`
-----------

<div id="output-area"><span id="output-header"> </span><div id="output-body"><div class="stream output-id-1"><div class="output_subarea output_text"><pre> * sqlite:///vicks.db
Done.
5 rows affected.
Done.
</pre></div></div><div class="execute_result output-id-2"><div class="output_subarea output_html rendered_html"><table>
    <tbody><tr>
        <th>customer_id</th>
        <th>customername</th>
        <th>lastname</th>
        <th>country</th>
        <th>age</th>
        <th>phone</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Shubham</td>
        <td>Thakur</td>
        <td>India</td>
        <td>23</td>
        <td>xxxxxxxxxx</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Aman</td>
        <td>Chopra</td>
        <td>Australia</td>
        <td>21</td>
        <td>xxxxxxxxxx</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Naveen</td>
        <td>Tulasi</td>
        <td>Sri Lanka</td>
        <td>24</td>
        <td>xxxxxxxxxx</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Aditya</td>
        <td>Arpan</td>
        <td>Austria</td>
        <td>21</td>
        <td>xxxxxxxxxx</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Nishant. Salchichas S.A.</td>
        <td>Jain</td>
        <td>Spain</td>
        <td>22</td>
        <td>xxxxxxxxxx</td>
    </tr>
</tbody></table></div></div></div><span id="output-footer"></span></div>


