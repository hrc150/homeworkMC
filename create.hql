create database test;
use test;
CREATE TABLE IF NOT EXISTS test.Comments(
ceo_id int,
ckto_num int,
atm int,
poo char(70),
region char(30),
city char(30),
address char(100),
location char(100),
comments char(255),
appeal_date timestamp,
cat_id int,
appeal_cat char(50),
org_id int,
cncl_flg binary,
channel char(50),
appeal_idnt char(50),
success_flg char(15),
equip_type char(15),
status char(15),
status_desc char(100),
status_desc_stm char(15) )
stored as textfile;
