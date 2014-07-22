from flask_app import app, models, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../stage.db'

print models.User.query.all()

