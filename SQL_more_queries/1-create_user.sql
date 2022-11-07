-- creates the MySQL server user user_0d_1. 
CREATE USER IF NOT EXISTS
GRANT *.* TO user_0d_1@localhost;
 SET PASSWORD FOR user_0d_1'@'localhost = PASSWORD(user_0d_1_pwd);
