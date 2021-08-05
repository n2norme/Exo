from model.db import DB


class User():
    def __init__(self):
        self.conn = DB.connect()

    def fetch_all_user(self):
        self.conn.execute(
            """ SELECT * from user
            """
        )
        rows = self.conn.fetchall()
        return rows

    def add_user(self, data):
        self.conn.execute(
            f"""
            insert into user(id, nom,prenom) values("{data.get('id')}", "{data.get('nom')}", "{data.get('prenom')}");
            """
        )

    def deleteById(self, id):
        self.conn.execute(
            f""" DELETE FROM user WHERE id = {id} """
        )

    def update(self, data):
        self.conn.execute(
            f""" UPDATE user SET nom = '{data.get('nom')}', prenom = '{data.get('prenom')}' WHERE id = '{int(data.get('id'))}' """
        )