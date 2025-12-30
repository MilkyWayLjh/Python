-- SELECT 聚合函数(字段列表) FROM 表名;
-- count 统计记录数量
-- 查询学生数量
SELECT COUNT(*) FROM student;
SELECT COUNT(class_id) FROM student;

-- sum 字段求和
-- 查询学生总年龄
SELECT SUM(stu_age) FROM student;

-- max 字段最大值
-- 查询学生最大年龄
SELECT MAX(stu_age) FROM student;

-- min 字段最小值
-- 查询学生最小年龄
SELECT MIN(stu_age) FROM student;

-- avg 字段平均值
-- 查询学生平均年龄
SELECT AVG(stu_age) FROM student;


