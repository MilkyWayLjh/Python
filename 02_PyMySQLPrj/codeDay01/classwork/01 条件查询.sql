-- SELECT 字段列表 FROM 表名 WHERE 条件列表;
-- 比较运算符
-- 查询学生id大于3的学生信息
SELECT * FROM student WHERE stu_id > 3;

-- 逻辑运算符
-- 查询学生id为1，学号为itsrc-012的学生信息
SELECT * FROM student WHERE stu_id=1 OR stu_no = 'itsrc-012';

-- 模糊查询
-- 查询姓名以袁开始的学生信息
SELECT * FROM student WHERE stu_name LIKE '袁_'; 

-- 范围查询
-- 连续范围内查询
-- 查询学生id3到6之间的学生信息
SELECT * FROM student WHERE stu_id BETWEEN 3 AND 6;
-- 查询学生id不在3到6之间的学生信息
SELECT * FROM student WHERE stu_id NOT BETWEEN 3 AND 6;

-- 非连续范围查询  字段 in （1， 4， 5， 7）
-- 查询学生id是1， 4， 5， 7 的学生信息
SELECT * FROM student WHERE stu_id IN (1, 4, 5, 7);
-- 查询学生id不是1， 4， 5， 7 的学生信息
SELECT * FROM student WHERE stu_id NOT IN (1, 4, 5, 7);

-- 查询为null  字段 IS NULL
-- 查询classid为null的数据
SELECT * FROM student WHERE class_id IS NULL;
-- 查询非null，字典 IS NOT NULL
SELECT * FROM student WHERE class_id IS NOT NULL;
