-- 通过建立索引,可以提高查询效率
-- explain查询使用了索引的字段，查询stu_id = 7的学生数据
EXPLAIN SELECT * FROM student WHERE stu_id = 7;
-- rows = 1  因为有索引，只查询了一次就找到了

-- 查询stu_no = itsrc-014的数据,stu_no也使用了索引
EXPLAIN SELECT * FROM student WHERE stu_no = 'itsrc-014';
-- rows = 1  因为有索引，只查询了一次就找到了

-- 查询stu_age = 45的数据，没有设置索引
EXPLAIN SELECT * FROM student WHERE stu_age = 45;
-- rows = 7  没有设置索引，得一行一行查，所以要查7次

