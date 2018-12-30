from source.config_reader import ConfigReader
from source.db_worker import SqlWorker

config = ConfigReader()
sql = SqlWorker()


class User:

    def __init__(self, name, default_hp=int(config.config_get('user', 'default_hp'))):
        self.name = name
        self.default_hp = default_hp

    def hero(self, boost_hp=None):
        if boost_hp is None:
            hero_hp = self.default_hp
        else:
            hero_hp = boost_hp
        return hero_hp

    def create_hero(self):
        user_id = None
        try:
            last_user_id = sql.select("""select max(user_id) from user;""")
        except Exception as e:
            print(e)
        else:
            user_id = last_user_id[0][0] + 1
            try:
                sql.insert(
                    f"""insert into user (user_id, user_name, user_hp) values ({user_id}, '{self.name}', {self.hero()});
                """)
            except Exception as e:
                print(e)
        return user_id



