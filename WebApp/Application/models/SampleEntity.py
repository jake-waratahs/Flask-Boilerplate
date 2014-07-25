from Application import db

class SampleEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # string = db.Column(db.String(120), unique=False)
    # bool = db.Column(db.Boolean, unique=False)
    # text = db.Column(db.Text, unique=False)

    # Many to One Setup.
    # client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    # client = db.relationship('Client', backref=db.backref('weighings', lazy='dynamic'))

    def __init__(self):
        # Do some setup, or use initialiser params to make a more inline object creation
        pass

    def __repr__(self):
        return '<Client %r>' % self.id

    def toDict(self):
        return dict(id=self.id)

