-- 事务
-- mysql使用事务, 存储引擎必须是innodb的存储引擎
-- 概念
-- ● 说明: 把一组sql语句的操作,绑定为一个原子的操作,要成功全部成功,如果一个失败,全部失败.
-- ● 作用: 
--   ○ 保证数据库当中数据的完整性

-- 终端下面, mysql的事务是默认自动开启提交的

-- 1 手动开启事务
-- start transaction; 或者 begin;

-- 2 sql语句操作

-- 3 提交或者回滚 
	-- 提交 commit	(手动开启事务到提交之间的所有操作持久化)
	-- 回滚 rollback	(手动开启事务到回滚之间的所有操作都取消)
	
	
-- 特点：
-- ● 原子性（Atomicity）: 一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
-- ● 一致性（Consistency）: 事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
-- ● 隔离性（Isolation）: 一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
-- ● 持久性（Durability）: 持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。
--                       接下来的其他操作或故障不应该对其有任何影响。


-- 默认自动开启提交
SELECT * FROM student where stu_id = 1;
UPDATE student SET stu_age = 24 WHERE stu_id = 1;
UPDATE student SET stu_age = 25 WHERE stu_id = 1;


-- 手动开启事务  (一组事务全部框选在一起运行)
START TRANSACTION;

SELECT * FROM student where stu_id = 1;
UPDATE student SET stu_age = stu_age + 1 WHERE stu_id = 1;
SELECT * FROM student where stu_id = 1;

-- ROLLBACK
COMMIT

