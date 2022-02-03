from flask import Flask, render_template, request, redirect, url_for
import sys
import pymysql
import folium
import json
import requests


#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
  return render_template("index.html")

@app.route('/Loki') # 접속하는 url
def Loki():

  return render_template("Loki.html")


# sql = "SELECT AVG(latitude), AVG(longitude), AVG(altitude) FROM gps_data ORDER BY seq DESC LIMIT 10;"
  # cur.execute(sql)

@app.route('/Duckpod1') # 접속하는 url
def Duckpod1():
  # map을 만드는 코드
  map = folium.Map(
    location=[45.5233, -122.6759]
  )
  db = pymysql.connect(host="localhost", user="root", passwd="290290", db="gps_db", charset="utf8")
  cur = db.cursor()
  sql = "SELECT seq, time_stamp, latitude, longitude, altitude FROM gps_data ORDER BY seq DESC LIMIT 1;"
  cur.execute(sql)
  gps_data_rows = cur.fetchall()
  start_latitude, start_longitude = gps_data_rows[0][2], gps_data_rows[0][3]

  sql = "SELECT seq, time_stamp, quaternion_w, quaternion_x, quaternion_y, quaternion_z, linear_acceleration_x, linear_acceleration_y, linear_acceleration_z, angular_velocity_x, angular_velocity_y, angular_velocity_z FROM imu_data ORDER BY seq DESC LIMIT 1;"
  cur.execute(sql)
  imu_data_rows = cur.fetchall()


  ################### map 작업


  map = folium.Map(location=[start_latitude, start_longitude], tiles="Stamen Toner", zoom_start=13)

  start_tooltip = "Start location"
  last_tooltip = "last location"

  folium.CircleMarker(
    radius=10,
    location=[start_latitude, start_longitude],
    popup=start_tooltip,
    color="crimson",
    fill=False,
  ).add_to(map)

  folium.CircleMarker(
    location=[37.4551, 126.950],
    radius=10,
    popup=last_tooltip,
    color="#3186cc",
  ).add_to(map)

  map.add_child(folium.LatLngPopup())

  map.save('templates/map.html')














  return render_template("Duckpod1.html", gps_data_tuple = gps_data_rows, imu_data_tuple = imu_data_rows)


@app.route('/Duckpod2') # 접속하는 url
def Duckpod2():
  return render_template("Duckpod2.html")

@app.route('/Duckpod_gps')
def Duckpod_gps():
  db = pymysql.connect(host="localhost", user="root", passwd="290290", db="gps_db", charset="utf8")
  cur = db.cursor()
  sql = "SELECT seq, time_stamp, latitude, longitude, altitude FROM gps_data ORDER BY seq DESC LIMIT 1;"
  cur.execute(sql)
  gps_data_rows = cur.fetchall()
  print(type(gps_data_rows))
  start_latitude, start_longitude = gps_data_rows[0][2], gps_data_rows[0][3]

  # url = (
  #   "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
  # )
  # vis1 = json.loads(requests.get(f"{url}/vis1.json").text)
  # vis2 = json.loads(requests.get(f"{url}/vis2.json").text)
  # vis3 = json.loads(requests.get(f"{url}/vis3.json").text)
  # map = folium.Map(location=[46.3014, -123.7390], zoom_start=7, tiles="Stamen Terrain")
  #
  # folium.Marker(
  #   location=[47.3489, -124.708],
  #   popup=folium.Popup(max_width=450).add_child(
  #     folium.Vega(vis1, width=450, height=250)
  #   ),
  # ).add_to(map)
  #
  # folium.Marker(
  #   location=[44.639, -124.5339],
  #   popup=folium.Popup(max_width=450).add_child(
  #     folium.Vega(vis2, width=450, height=250)
  #   ),
  # ).add_to(map)
  #
  # folium.Marker(
  #   location=[46.216, -124.1280],
  #   popup=folium.Popup(max_width=450).add_child(
  #     folium.Vega(vis3, width=450, height=250)
  #   ),
  # ).add_to(map)
  #

  # map = folium.Map(
  #   location=[45.5233, -122.6759],
  #   zoom_start=13,
  #   tiles="Stamen Terrain"
  # )
  # folium.Marker(
  #   [45.3288, -121.6625], popup="<i>Start location</i>", tooltip=start_tooltip
  # ).add_to(map)
  # folium.Marker(
  #   [45.3311, -121.7113], popup="<b>Last location</b>", tooltip=last_tooltip
  # ).add_to(map)

  map = folium.Map(location=[start_latitude, start_longitude], tiles="Stamen Toner", zoom_start=13)

  start_tooltip = "Start location"
  last_tooltip = "last location"

  folium.CircleMarker(
    radius=10,
    location=[start_latitude, start_longitude],
    popup=start_tooltip,
    color="crimson",
    fill=False,
  ).add_to(map)

  folium.CircleMarker(
    location=[37.4551, 126.950],
    radius=10,
    popup=last_tooltip,
    color="#3186cc",
  ).add_to(map)

  map.add_child(folium.LatLngPopup())

  return map._repr_html_()
@app.route('/roslibjs') # 접속하는 url
def Roslibjs():
  return render_template("roslibjs.html")

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/Description') # 접속하는 url
def Description():
  return render_template("Description.html")


if __name__=="__main__":
  app.run( host="127.0.0.1", port="5000", debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)
