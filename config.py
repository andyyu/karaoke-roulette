import os
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = "postgresql://andyhsyu@gmail.com:h4o2n6gseok@localhost/HEROKU_POSTGRESQL_GRAY_URL"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'cs33physics1bphysics4almath32b'