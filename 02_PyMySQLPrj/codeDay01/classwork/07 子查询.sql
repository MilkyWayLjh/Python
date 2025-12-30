-- 子查询[重点]
-- ● 什么是子查询
-- 	一个查询语句出现在另一个语句内，就是子查询语句！
-- ● 目的
-- 	先利用一个查询获得中间数据，再利用该中间数据，进行下一次的处理！

-- 子查询分类
-- ●  按子查询的位置划分： 
--   ○  where型子查询：子查询在 where 子句内 
--   ○  from型子查询：子查询在 from 子句内
-- ●  按返回数据划分：
--   ○ 标量子查询（子查询结果为单个值）
--   ○ 列子查询（子查询结果为一列）
--   ○ 行子查询（子查询结果为一行）
--   ○ 表子查询（子查询结果为多行多列）	注意： 必须要给子查询语句起一个别名


-- 标量子查询
-- 查询1班的学生信息
-- a. 查询1班的id
SELECT class_id FROM class WHERE class_name = '1班';
-- b. 使用class_id获取这个班级的所有学生信息
SELECT * FROM student WHERE class_id = 1;
-- 合并子查询
SELECT * FROM student WHERE class_id = (SELECT class_id FROM class WHERE class_name='1班');


-- 列子查询
-- 查询1班和2班所有学生信息
-- a. 查找1班和2班的班级id
-- SELECT class_id FROM class WHERE class_name = '1班' OR class_name = '2班';
SELECT class_id FROM class WHERE class_name in ('1班', '2班');
-- b. 通过class_id获取学生信息
-- SELECT * FROM student WHERE class_id = 1 OR class_id = 2;
SELECT * FROM student WHERE class_id IN (1, 2);
-- 合并子查询
SELECT * FROM student WHERE class_id in (SELECT class_id FROM class WHERE class_name = '1班' OR class_name = '2班');


-- 行子查询（子查询结果为一行）
-- 查询class_id=1这个班级最大的人,年龄最大的人
-- a. 获取class_id = 1的最大的年龄
SELECT class_id, max(stu_age) FROM student WHERE class_id = 1;
-- b. 通过这个最大年龄值和班级id来得到这个学生的信息
SELECT * FROM student WHERE class_id = 1 and stu_age = 35;
-- 合并子查询
SELECT * FROM student WHERE (class_id, stu_age) = (SELECT class_id, max(stu_age) FROM student WHERE class_id = 1);


-- 表子查询（子查询结果为多行多列）
-- a. 查询id大于3的所有学生信息
SELECT * FROM student WHERE stu_id > 3;
-- b. 在id大于3的学生里找出年龄小于40的学生信息
SELECT * FROM (SELECT * FROM student WHERE stu_id > 3) AS sub_table WHERE stu_age < 40;


