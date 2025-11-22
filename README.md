The needs a .env file and a .env.dev file...
The first should contain (currently the default sqlite3 db): DATABASE_URL=sqlite:///./db.sqlite3

The second should contain these vars:
DATABASE_URL=sqlite:///./db.sqlite3
JWT_SECRET_KEY
JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES
