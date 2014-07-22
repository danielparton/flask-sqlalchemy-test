from flask_app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../master.db'

if __name__ == '__main__':
    app.run(debug=True)
