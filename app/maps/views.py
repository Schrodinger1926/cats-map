from flask import render_template, jsonify, request, flash
from .. import db
from ..models import Location
from . import maps


@maps.route('/', methods = ['GET', 'POST'])
def homepage():
   if request.method == 'GET':
     return render_template('index.html')


   if request.method == 'POST':
      # Parse data
      try:
         data = request.get_json()
         _lat, _lng, _address = data["lat"], data['lng'], data['address']
         
         # Make model instance
         loc = Location(lat = _lat, lng = _lng, address = _address)
         
         # save 
         db.session.add(loc)
         
         db.session.commit()

         return jsonify({"status": "OK"})
         
      except Exception:
         db.session.rollback()
         return jsonify({"status": "FAILED"})
      

@maps.route('/fetch')
def fetch():
   rows = Location.query.all()
   return render_template('fetch.html', rows = rows)


@maps.route('/clear')
def clear():
   try:
      # Bulk deletion
      deleted_rows_count = Location.query.delete()
      db.session.commit()

   except Exception:
      return jsonify({"status": "FAILED"})
   
   return jsonify({"status": "OK",
                   "deleted_rows_count": deleted_rows_count})

