
glog
userid int
appid int
type ["imp"|"clk"]
ds timestamp

drop table clks;

create table clks
as
(
  select * from D 
  where type = 'clk'
);

drop table imp;

create table imp
as
(
  select * from D
  where type = 'imp
);
--CTR
(select count(*) from clks) / (select count(*) from imp)

-- 0.8

drop table fraud_cnt;

create table fraud_cnt
as
(
  select
  a.user_id, 
  a.app_id,
  a.ds,
  count(b.type) as clks,
  count(c.type) as impressions,
  (count(c.type) - count(b.type)) as delta_fraud
  from D a
  left outer join clks b
  on a.user_id = b.user_id
  and a.app_id = b.app_id
  and a.ds = b.ds
  left outer join imp c
  on a.user_id = c.user_id 
  and a.app_id = c.app_id
  and a.ds = c.ds
  group by 1,2
  order by 4
);

select * from fraud_cnt where delta_fraud < 0;

select * from fraud_cnt where delta_fraud < 0 limit 100;

drop table fraud_cnt2;

create table fraud_cnt2
as
(
  select
  a.user_id, 
  a.app_id,
  (max(b.ds) - min(c.ds)) as delta_time
  from(select user_id, app_id from D group by 1,2) a
  left outer join (select user_id, app_id, ds from D where type = 'clk') b
  on a.user_id = b.user_id
  and a.app_id = b.app_id
  left outer join (select user_id, app_id, ds from D where type = 'imp') c
  on a.user_id = c.user_id
  and a.app_id = c.app_id
);





(select count(*) from (select b.* from fraud_cnt a join clks b on a.user_id = b.user_id and a.app_id = b.app_id where a.delta_fraud >=0)) / (select count(*) from (select b.* from fraud_cnt a join imp b on a.user_id = b.user_id and a.app_id = b.app_id where a.delta_fraud >=0))

