# coding:utf-8

from ihome import create_app, db
from flask_script import Manager
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand

# app = create_app("develop")
app = create_app("product")

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

CORS(app, resources=r"/*")

if __name__ == '__main__':
    manager.run()