# Duckpod
\<ARIL\>
<br>
2022-02-14 : github create
<br>
2022-02-15 : flask app add
<br>
2022-02-18 : server's mysql code add
<br>
2022-02-21 : remote sensor data insert db success
<br>
<br>
<br>
<br>
# Applications
Mysql for server DB
<br>
flask_test for Web
<br>
<br>
<br>
<br>
<br>
# Mysql
sudo apt-get update
<br>
sudo apt-get install mysql-server
<br>
# Mysql Workbench
sudo apt update
<br>
sudo apt install mysql-workbench
<br>
issues : login-error --- authentication problem, need to change from * to native_password
<br>
solutions : ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
<br>
make user, host with ip %(open to all IP) with mysql workbench 
<br>
make bind-address = 127.0.0.1 unavailable in /etc/mysql/mysql.conf.d/mysqld.cnf
<br>
<br>
<br>
<br>
<br>
<br>
# Docker install
 sudo apt-get update
<br>
 sudo apt-get install docker-ce docker-ce-cli containerd.io
<br>
ref : https://docs.docker.com/engine/install/ubuntu/
<br>
<br>
<br>
<br>
<br>
# How to use
<p>this is in progress so this will not work well<p>
<br>
activate gps_data.sql file in Mysql on server computer
<br>
roslaunch gps or imu ... sensors in Duckpod --- you need to edit codes
<br>
activate app.py file in flask_test on server computer or local computer to see DB data --- selective
# To do
<br>
Complete Dockerfile
<br>
<br>
<br>
<br>
<br>
  
# Issues
too many requirements in requirements.txt --- we need to test on docker
