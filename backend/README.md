### Fllow [Cornell](https://www.youtube.com/@CornellAppDev/playlists) Backend Course to strengthen my skills.


`app.py`
- Connects server to client
- Defines routes and responses
- handles all logic and operations
  
`db.py`
- Connects server to database
- Defines tables and its columns
- Inserts, updates, retrieves, and delete information from table.

Run `python app.py` for task 1 & 2.

1. CRUD: Use sqlite3 and flask to build basic CRUD actions to save and udpate posts.
2. Relation Database: Add table with foreign key to reference other table.

Run `python app_orm.py` for task 3.

3. Abstractions (ORM): 
   - Query and manipulate data using Objects. 
   - Still preserve the database for SQL and storage benefits
   - Allows us to reason about entries as instances of an object
   - ORM Drawbacks
     - Slower query performance for more complex queries
     - Increases application code (SQL + abstraction code)
     - Abstracts away fundamentals of SQL
   - Implement `app_orm.py` and `db_orm.py`.
     - Build association table.

