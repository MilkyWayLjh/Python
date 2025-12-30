-- 语法：
-- SELECT 字段列表 FROM 表名 GROUP BY 分组字段名
-- SELECT 字段列表 FROM 表名 [ WHERE 条件 ] GROUP BY 分组字段名 [ HAVING 分组后过滤条件 ];
-- 注意: 使用了分组之后,select后面只能写分组的字段,或者聚合函数
-- ●  where与having区别 
--   ○  执行时机不同:where是分组之前进行过滤，不满足where条件，不参与分组;而having是分组 之后对结果进行过滤。 
--   ○  判断条件不同:where不能对聚合函数进行判断，而having可以。 
-- ●  group_concat() 
-- 		将组内的字段，连接成一个字符串！分组之后的字段聚合

-- 用class_id 来分组查询  查看每个班级的人数
SELECT class_id, COUNT(class_id) FROM student GROUP BY class_id;
SELECT class_id, COUNT(*) FROM student GROUP BY class_id;

-- 每个班学生的平均年龄
SELECT class_id, AVG(stu_age) FROM student GROUP BY class_id

-- 每个班的最小年龄
SELECT class_id, MIN(stu_age) FROM student GROUP BY class_id;

-- 同一年龄的人的个数
SELECT stu_age, COUNT(*) FROM student GROUP BY stu_age;

-- GROUP_CONCAT使用
-- 查看每个班级的人数和班级所有人的姓名
SELECT class_id, COUNT(*), GROUP_CONCAT(stu_name)FROM student GROUP BY class_id;

-- GROUP BY 和 WHERE 同时使用
-- 查询每个班年龄大于30的所有同学姓名
SELECT class_id, GROUP_CONCAT(stu_name) FROM student WHERE stu_age > 30 GROUP BY class_id;

-- HAVING使用, 对分组之后的数据进行过滤
-- 查询每个年龄人数大于1的年龄和人数
SELECT stu_age, COUNT(*) FROM student GROUP BY stu_age
HAVING COUNT(*) > 1;

-- 查询班级人数大于3的班级
SELECT class_id FROM student GROUP BY class_id
HAVING COUNT(*) > 3;

-- 平均年龄大于30的班级
SELECT class_id FROM student GROUP BY class_id
HAVING AVG(stu_age) > 30;


