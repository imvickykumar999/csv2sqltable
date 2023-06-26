def transform(file_name = 'student.csv'):
  import pandas as pd

  df = pd.read_csv(file_name)
  table = file_name.split('.')[0]
  x = ''

  for i in df.columns:
    x += i + ' VARCHAR(100),\n'

  x += '\b\b'
  y = ''
  for row in df.iterrows():
    y += '('
    for j in row[1]:
      y += f"'{j}', "
    y += '\b\b),\n'

  y += '\b'
  z = ''
  for i in df.columns:
    z += f"{i}, "

  z += '\b\b'
  return f'''%%sql
/*
!pip install "SQLAlchemy<1.4"

%reload_ext sql

%%sql sqlite:///vicks.db
*/

-- DROP TABLE {table};

CREATE TABLE {table} (
{x}
);

INSERT INTO {table} ({z})
VALUES
{y}\b;

SELECT * FROM {table};'''