
import pyperclip
import csv2sqltable.convert as c2s

sql = c2s.transform('cust_dimen.csv')
pyperclip.copy(sql)
print(sql)
