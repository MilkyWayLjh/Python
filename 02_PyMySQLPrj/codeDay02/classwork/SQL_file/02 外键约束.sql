-- 外键约束
-- 概念
-- ● 说明
-- 外键约束就是两张表之间建立的一种强连接的关系
-- ● 作用
-- 保证数据的一致性和完整性
-- ● 实现外键约束的条件
-- 1.外键约束通常是两个表之间的约束，A表的数据被B表所引用，A表称为主表（parent table），B表称为从表（child table）。
-- 2.外键约束要求表的存储引擎必须是innoDB，而不能是MyISAM。
-- 3.外键约束的主表和从表的关联字段，数据类型要求严格一致。一般使用主键id进行关联。
-- 4.一般把外键创建在多的一方(从表),也就是引用的这一方(主表)
-- 
-- 设置外键
-- 主表: 数据本身所在的那张表就是主表,按照1对多的关系来说,就是1的那张表.class
-- 从表: 引用数据的那张表, 按照1对多的关系来说,就是多的那张表.student


-- 语法：
-- -- 添加外键索引
-- alter table 从表 add [constraint 约束名字] foreign key (外键字段) references 主表(关联字段) 
-- [on delete {级别}]
-- [on update {级别}]
-- 
-- -- 查看建表语句
-- show create table 表名;
-- 
-- -- 删除外键索引
-- ALTER TABLE student DROP FOREIGN KEY 约束名称;
-- 
-- 
-- 三个{级别}：
-- 
-- 1. 严格限制：restrict。严格限制不允许任何操作。默认就是严格限制。
-- 2. 级联操作：cascade。主表（关联字段）更新或删除时，从表也跟着改变。
-- 3. 设置NULL：set null。主表（关联字段）更新或删除时，从表置NULL。

ALTER TABLE student ADD CONSTRAINT fk_stu_cls FOREIGN KEY (class_id) REFERENCES class (class_id);

SHOW CREATE TABLE student;

-- 删除外键
-- ALTER TABLE student DROP FOREIGN KEY fk_stu_cls;



