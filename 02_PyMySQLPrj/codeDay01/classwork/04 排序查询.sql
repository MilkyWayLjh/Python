-- 排序查询
-- 语法：
-- 	SELECT 字段列表 FROM 表名 ORDER BY 字段1 [排序方式] , 字段2 [排序方式], 字段N [排序方式];
-- ● 排序方式 
--   ○ ASC : 升序(默认值)
--   ○ DESC: 降序

-- SELECT 字段列表 FROM 表名 ORDER BY 字段1 排序方式1 , 字段2 排序方式2;
SELECT * FROM student ORDER BY stu_age;  -- 默认就是 ASC 升序
SELECT * FROM student ORDER BY stu_age DESC;  -- 降序 DESC


-- 多字段排序
-- 先用年龄排序，再用学号排序
SELECT * FROM student ORDER BY stu_age ASC, stu_no DESC;

-- 先班级降序，再学号升序
SELECT * FROM student ORDER BY class_id DESC, stu_no;


