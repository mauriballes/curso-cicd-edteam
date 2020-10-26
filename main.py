from app import app, database
from models import create_tables

if __name__ == '__main__':
    create_tables(database)  # Create DB
    app.run(host='0.0.0.0', port='5000')  # Init Server
