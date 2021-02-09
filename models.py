class User(object):
    """class for creating Users in the database"""

    def __init__(self, username = "", first_name = "", last_name = "", password = ""):
        self._id = -1
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self._password = password

    @property
    def id(self):
        return self._id

    def add_user(self, cursor):
        if self._id == -1:
            sql = """INSERT INTO users (username, first_name, last_name, password) VALUES (%s, %s, %s, %s)"""
            values = (self.username, self.first_name, self.last_name, self._password)
            cursor.execute(sql, values)
            return 'user_added'
        return False


    def __str__(self):
        return self.username
