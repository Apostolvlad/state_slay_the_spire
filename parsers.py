import json
import os
from bd import session, Games, Battle, Enemies, Character, StateEnemies, get_or_create
from sqlalchemy.orm import subqueryload

def get_folder(path = 'runs'):
    # названия папок
    names = os.listdir(path)
    for name in names:
        path_folder = f'{path}\\{name}'
        for files in os.listdir(path_folder):
            file_path = f'{path_folder}\\{files}'
            with open(file_path) as f: info = f.read()
            info_dict = json.loads(info)

            #
            c = get_or_create(model = Character, name = info_dict.get('character_chosen'))
            e = get_or_create(model = Enemies, enemies = info_dict.get('killed_by'))
            #print(c.id)
            s_e, status_state = get_or_create(model = StateEnemies, check = True, character_id = c.id, enemies_id = e.id)
            g = Games(file_path, info_dict)
            e.games.append(g)
            c.games.append(g)
            if status_state:
                e.state_enemies.append(s_e)
                c.state_enemies.append(s_e)
            s_e.add_state(True)

            for info in info_dict.get('damage_taken'):
                e = get_or_create(model = Enemies, enemies = info.get('enemies'))
                e.set_level(info.get('floor'))

                s_e, status_state = get_or_create(model = StateEnemies, check = True, character_id = c.id, enemies_id = e.id)
                if status_state:
                    e.state_enemies.append(s_e)
                    c.state_enemies.append(s_e)
                s_e.add_state(False)

                b = Battle(info)
                g.battles.append(b)
                e.battles.append(b)
                
                
            
    session.commit()

class ErrorFinish(Exception): pass

def get_character_name():
    result = list()
    for element in session.query(Character.name).all(): result.append(element[0])
    return result #session.query(Character)#.#Character)#.Select(Character.name)

def check_procent(num1, num2):
    if num1 == 0: return 100
    return round(100.0 - num1 / num2 * 100.0)

def get_enemies(name):
    c1 = session.query(Character).options(subqueryload(Character.state_enemies)).filter_by(name = name).one() #
    for row in c1.state_enemies: 
        yield (row.enemies.enemies, row.enemies.level, row.battle_count, row.battle_kill, check_procent(row.battle_kill, row.battle_count))
    raise ErrorFinish()



if __name__ == "__main__":
    #get_folder()
    #get_enemies()
    get_character_name()