from app import db

# from manage import app, db


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    address = db.Column(db.String(500), index=True)

    def __repr__(self):
        return "GeoCoordinates: ({:5.2f},{:5.2f})".format(self.lat, self.lng)