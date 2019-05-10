### 数据库的创建
#### 查看已有的数据库
show databases;

#### 创建数据库
create database chenriyuelakedb; 

#### 使用该数据库
use chenriyuelakedb;   

#### 创建表格 user
CREATE TABLE `user` (`id` int(11) NOT NULL AUTO_INCREMENT COMMENT '序号', `username` varchar(20) NOT NULL COMMENT '用户名', `realname` varchar(20) NOT NULL COMMENT '真实名', `company` varchar(50) NOT NULL COMMENT '公司', `password` varchar(40) NOT NULL COMMENT '密码', `email` varchar(20) NOT NULL COMMENT '邮箱', `phonenum` varchar(15) NOT NULL COMMENT '手机号', PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='用户表'; 

#### 查看表格
show tables;

#### 查看表格结构
desc user;

#### 创建表格sensor data
CREATE TABLE `sensordata` ( `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '序号', `recordtime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '时间', `light` varchar(10) NOT NULL COMMENT '光照', `temperature` varchar(10) NOT NULL COMMENT '温度', `humidity` varchar(10) NOT NULL COMMENT '湿度', PRIMARY KEY (`id`) ) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='传感信息表';

#### 查看表格
show tables;

#### 查看表格结构
desc sensordata;

### 数据库的测试
insert into user(username, realname,company, password, email,phonenum) values ('admin', ' 陈老师', '中大', '1111111','xachen@cjlu.edu.cn', '13067841001'); 


insert into sensordata (light, temperature, humidity) values ('100.3', '25.8', '90.2'); 
insert into sensordata (light, temperature, humidity) values ('90.1', '26.2', '91.3'); 