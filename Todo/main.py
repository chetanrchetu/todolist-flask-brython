from website import app,db,DATABASE_PATH
import os
from website.models import Taskdb 



if __name__=='__main__':
    if not os.path.exists(DATABASE_PATH):
        with app.app_context():
            db.create_all()
    app.run(debug=True) 