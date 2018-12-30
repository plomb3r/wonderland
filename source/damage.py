from source.db_worker import SqlWorker
from source.config_reader import ConfigReader

sql = SqlWorker()
config = ConfigReader()
default_hp = int(config.config_get('user', 'default_hp'))


class Damage:
    @staticmethod
    def user_hp(user_id):
        return sql.select(f"""select user_hp from user where user_id={user_id}""")[0][0]

    @staticmethod
    def update_hp(user_id, point):
        try:
            sql.insert(f"""update user set user_hp = {point} where user_id = {user_id};""")
        except Exception as e:
            print(e)

    def take_heal(self, user_id, heal):
        hp = self.user_hp(user_id)
        if hp <= default_hp:
            if hp + heal >= default_hp:
                Damage.update_hp(user_id, default_hp)
            else:
                Damage.update_hp(user_id, hp + heal)
        else:
            Damage.update_hp(user_id, default_hp)

    def take_damage(self, user_id, dmg):
        hp = self.user_hp(user_id)
        if hp - dmg <= 0:
            Damage.update_hp(user_id, 0)
        else:
            Damage.update_hp(user_id, hp - dmg)
