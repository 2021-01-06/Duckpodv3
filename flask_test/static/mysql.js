var mysql = require('mysql')
var roslib = require('roslib')
var ros = new roslib.Ros();
console.log('required mysql, ros')

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '290290',
  database : 'gps_db'
});

connection.connect();
console.log('Database Connected');

  ros.on('error', function(error) {
    console.log(error);
  });

  ros.on('connection', function() {
    console.log('Ros Connection made!');
  });

  ros.on('close', function() {
    console.log('Ros Connection closed.');
  });

  ros.connect('ws://localhost:9090');

  var gnss_listener = new roslib.Topic({
    ros : ros,
    name : '/gnss',
    messageType : 'sensor_msgs/NavSatFix'
  });

  var imu_listener = new roslib.Topic({
    ros : ros,
    name : '/imu/data',
    messageType : 'sensor_msgs/Imu'
  });

  gnss_listener.subscribe(function(message) {
//    console.log(message.header.stamp)
//    console.log('latitude :' + message.latitude + ', longitude :' + message.longitude + ', altitude :' + message.altitude);
    connection.query('insert into gps_data(latitude, longitude, altitude) values(' + message.latitude + ', ' + message.longitude + ', ' + message.altitude + ')'), function(error, results, fields){
    if (error) {
        console.log(error);
    }

    console.log(results);
    }
  });
  imu_listener.subscribe(function(message) {
//    console.log("quaternion :" + message.orientation.w, message.orientation.x, message.orientation.y, message.orientation.z)
//    console.log("linear_acceleration :" + message.linear_acceleration.x, message.linear_acceleration.y, message.linear_acceleration.z)
//    console.log("angular_velocity : " + message.angular_velocity.x, message.angular_velocity.y, message.angular_velocity.z)
    connection.query('insert into imu_data(quaternion_w, quaternion_x, quaternion_y, quaternion_z, linear_acceleration_x, linear_acceleration_y, linear_acceleration_z, angular_velocity_x, angular_velocity_y, angular_velocity_z) values(' + message.orientation.w + ', ' + message.orientation.x + ', ' + message.orientation.y + ', ' + message.orientation.z + ', ' + message.linear_acceleration.x + ', ' + message.linear_acceleration.y + ', ' + message.linear_acceleration.z + ', ' + message.angular_velocity.x + ', ' + message.angular_velocity.y + ', ' + message.angular_velocity.z + ')'), function(error, results, fields){
    if (error) {
        console.log(error);
    }
    console.log(results);
    }
  })


//console.log('Database Disconnected');
//connection.end();
