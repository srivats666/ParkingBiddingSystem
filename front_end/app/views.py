from app import app
from flask import render_template
from flask import jsonify


@app.route('/')
@app.route('/index')
def index():
  user = { 'nickname': 'Miguel' } # fake user
  return render_template("index.html", title = 'Home', user = user)

@app.route('/api/list/<lat>/<long>')
def get_lots(lat, long):
  jsonresponse = [{"name": "Garage1", "lat": 37.76425207, "long": -122.4207729, "occ": "122", "oper": "200"}, {"name": "Garage2", "lat": 37.7832776731, "long": -122.405537559, "occ": "35", "oper": "130"}]
  return jsonify(jsonresponse)


 