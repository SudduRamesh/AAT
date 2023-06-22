from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


app = Flask(__name__)


#Bootstrap 
Bootstrap(app)

app.config['SECRET_KEY'] = '5e1bb16dd3f06a66f28a565245a3824f8a2554436b2919ed'

# suppress SQLAlchemy warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#DB Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c22057404:wehfox-gusne2-kojmUd@csmysql.cs.cf.ac.uk:3306/c22057404_table_4_aat_db'
# mysql+pymysql://c22057404:wehfox-gusne2-kojmUd@csmysql.cs.cf.ac.uk:3306/c22057404_table_4_aat_db

#Admin email
app.config['MAIL_USERNAME'] = 'chane.c.sun@gmail.com'

#DB
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from blog import routes