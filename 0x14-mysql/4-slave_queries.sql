-- Only on Slave
-- Queries (Must change to correct data)
-- Master values
-- SHOW MASTER STATUS; (in master)
CHANGE MASTER TO MASTER_HOST='100.25.220.47',MASTER_USER='replica_user',
MASTER_PASSWORD='replica_user_pwd', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS= 154;

START SLAVE;

SHOW SLAVE STATUS\G
