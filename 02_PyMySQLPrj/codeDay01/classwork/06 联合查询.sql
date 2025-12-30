-- 对于union查询，就是把多次查询的结果合并起来，形成一个新的查询结果集。

-- ● 对于联合查询的多张表的列数必须保持一致，对数据类型不做要求。
-- ● 前提是单字段：union all 会将全部的数据直接合并在一起，union 会对合并之后的数据去重。

/* 语法：
SELECT 字段列表 FROM 表A ... 
UNION [ ALL ]
SELECT 字段列表 FROM 表B ....;
*/
-- UNION
SELECT stu_id, stu_name FROM student
UNION
SELECT stu_id, stu_name FROM student;

SELECT stu_age FROM student
UNION
SELECT stu_id FROM student;

-- UNION ALL
SELECT stu_id, stu_name FROM student
UNION ALL
SELECT stu_id, stu_name FROM student;


