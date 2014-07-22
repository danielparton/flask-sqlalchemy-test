from flask_app import db, models, app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../stage.db'

db.create_all()

newuser = models.User('parton', 'danny.parton@email.com')
db.session.add(newuser)
db.session.commit()

