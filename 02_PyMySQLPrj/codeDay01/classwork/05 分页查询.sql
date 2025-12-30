-- 分页查询
-- 语法：
-- 	SELECT 字段列表 FROM 表名 LIMIT 起始索引, 查询记录数;   
-- 起始索引从0开始
-- 起始索引，默认就是0。如果使用0，就可以省略。

-- 查询学生表的2条数据
SELECT * FROM student LIMIT 0, 2;
SELECT * FROM student LIMIT 2;
-- 查询学生表的下标2开始的5条数据
SELECT * FROM student LIMIT 2, 5;

-- 查询学生表中最后3名同学
SELECT * FROM student ORDER BY stu_id DESC LIMIT 0, 3;
SELECT * FROM student ORDER BY stu_id DESC LIMIT 3;


-- 分页原理
-- 当前第几页			每页显示条数 （2）
-- 页数					START	LIMIT
-- 	1					0		2
-- 	2					2		2
-- 	3					4		2
-- 	4					6		2
-- 						START = (当前页-1) * 每页显示条数
SELECT * FROM student LIMIT 2;
SELECT * FROM student LIMIT 2, 2;
SELECT * FROM student LIMIT 4, 2;
SELECT * FROM student LIMIT 6, 2;



