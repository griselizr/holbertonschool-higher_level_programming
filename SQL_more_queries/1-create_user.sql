-- creates the MySQL server user user_0d_1. 
CREATE 'user_0d_1' IF NOT EXISTS
SET PASSWORD user_0d_1@localhost = PASSWORD(user_0d_1_pwd);
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
FlUSH PRIVILEGES;
