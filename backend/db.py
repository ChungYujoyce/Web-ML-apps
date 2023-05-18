import os
import sqlite3

# only one connection to the database
def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    
    return getinstance

class DatabaseDriver(object):
    """
    handling r/w data with the database
    """

    def __init__(self):
        """
        secure a connection with the db adn store it
        in an instance variable
        """

        self.conn = sqlite3.connect("post.db", check_same_thread=False)
        self.create_post_table()
        self.create_subpost_table()

    def create_post_table(self):
        try:
            self.conn.execute(
                """
                CREATE TABLE post (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    liked BOOLEAN NOT NULL
                );
                """
            )
            self.conn.commit()
        except Exception as e:
            print(e)

    def delete_post_table(self):
        self.conn.execute("DROP TABLE IF EXISTS post;")

    def get_all_posts(self):
        cursor = self.conn.execute("SELECT * FROM post;")
        posts = []

        for row in cursor: # friendly for python parsing
            posts.append({"id": row[0], "content": row[1], "liked": bool(row[2])})

        return posts
    
    def insert_post_table(self, content, liked):
        cursor = self.conn.execute("INSERT INTO post (content, liked) VALUES (?,?);", (content, liked))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_post_by_id(self, id):
        cursor = self.conn.execute("SELECT * FROM post WHERE ID = ?;", (id,))

        for row in cursor: # friendly for python parsing
            return ({"id": row[0], "content": row[1], "liked": bool(row[2])})

        return None
    
    def update_post_by_id(self, id, content, liked):
        self.conn.execute(
            """
            UPDATE post SET content=?, liked=? WHERE id=?;
            """,
            (content, liked, id)
        )
        self.conn.commit()

    def delete_post_by_id(self, id):
        self.conn.execute(
            """
            DELETE FROM post WHERE id=?;
            """,
            (id,)
        )

    # subposts
    def create_subpost_table(self):
        try:
            # post_id INT NOT NULL; (not UNIQUE)
            # one post can be referenced by many subposts
            self.conn.execute(
                """
                CREATE TABLE subposts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    liked BOOLEAN NOT NULL,
                    post_id INT NOT NULL,
                    FOREIGN KEY (post_id) REFERENCES posts(id)
                );
                """
            )
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_all_subposts(self):
        cursor = self.conn.execute("SELECT * FROM subposts;")
        subposts = []

        for row in cursor: # friendly for python parsing
            subposts.append({"id": row[0], "content": row[1], "liked": bool(row[2]), "post_id": row[3]})

        return subposts
    
    def insert_subposts(self, content, liked, post_id):
        cursor = self.conn.execute("INSERT INTO subposts (content, liked, post_id) VALUES (?, ?, ?);",
                                   (content, liked, post_id))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_subpost_by_id(self, id):
        # get subposts by id
        cursor = self.conn.execute("SELECT * FROM subposts WHERE id = ?;", (id,))

        for row in cursor: 
            return ({"id": row[0], "content": row[1], "liked": bool(row[2]), "post_id": row[3]})

        return None
    
    def get_subposts_of_post(self, id):
        # get all subposts given a post id
        cursor = self.conn.execute("SELECT * FROM subposts WHERE post_id = ?;", (id,))
        subposts = []

        for row in cursor:
            subposts.append({"id": row[0], "content": row[1], "liked": bool(row[2]), "post_id": row[3]})

        return subposts

# only <=1 instnace of the database driver
# exists within the app at all times
DatabaseDriver = singleton(DatabaseDriver)