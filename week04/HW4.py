import pandas as pd
import numpy as np
df = pd.DataFrame()
# 1. SELECT * FROM data;
print(df)
# 2. SELECT * FROM data LIMIT 10;
print(df.head(10))
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(df['id'])
# 4. SELECT COUNT(id) FROM data;
print(df['id'].count())
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(df[(df['id']<1000)&(df['age']>30)])
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(df.groupby('id').count_values())
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(df.merge(t1,t2,how = 'inner', on = 'id'))
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(df.merge(table1,table2,how = 'outer')) 
print(df.concat(table1,table2))
# 9. DELETE FROM table1 WHERE id=10;
del table1[table1['id'] == 10]
# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(table1.drop(['column_name'],axis = 1))