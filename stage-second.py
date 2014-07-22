from flask_app import db, models, app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../stage.db'

db.drop_all()
db.create_all()

newuser = models.User('parton', 'danny.parton@email.com')
db.session.add(newuser)
newuser = models.User('chodera', 'john.chodera@email.com')
db.session.add(newuser)
db.session.commit()

