from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Boolean, MetaData, ForeignKey
# https://coderlessons.com/tutorials/bazy-dannykh/sqlalchemy/sqlalchemy-kratkoe-rukovodstvo
engine = create_engine('sqlite:///bd/bd.db', echo = False) # sqlite:///:memory:
Base = declarative_base()

class Games(Base):
    __tablename__ = 'games'
    
    id = Column(Integer, primary_key = True)
    character_id = Column(String, ForeignKey('character.id'))
    path = Column(String) # путь до файла
    ascension_level = Column(Integer) # уровень возвышения
    victory = Column(Boolean) # победа/поражение
    enemies_id = Column(Integer, ForeignKey('enemies.id')) # кто убил героя

    battles = relationship("Battle", backref = "games")
    
    def __init__(self, path, info):
        self.path = path
        self.ascension_level = info.get('ascension_level', 0)
        self.victory = info.get('victory')
        self.enemies_id = info.get('killed_by', '')

class Enemies(Base):
    __tablename__ = 'enemies'
    id = Column(Integer, primary_key = True)
    enemies = Column(String)
    level = Column(Integer)
    games = relationship("Games", backref = 'enemies')
    battles = relationship("Battle", backref = 'enemies')
    state_enemies = relationship("StateEnemies", backref = 'enemies')
    
    def __init__(self, enemies, level = None):
        self.enemies = enemies
        self.level = None
        self.set_level(level)
    
    def set_level(self, level):
        if level == None: return 
        if level > 50: 
            self.level = 4
        elif level < 17: 
            self.level = 1
        elif level > 16 and level < 34:
            self.level = 2
        else:
            self.level = 3 
        
        
        

class Battle(Base):
    __tablename__ = 'battle'
    id = Column(Integer, primary_key = True)
    games_id = Column(Integer, ForeignKey('games.id'))
    enemies_id = Column(Integer, ForeignKey('enemies.id'))
    damage = Column(Integer)
    floor = Column(Integer)
    turns = Column(Integer)
    #enemies = relationship("Enemies", backref = "battle")
    

    def __init__(self, info):
        self.damage = int(info.get('damage', 0))
        self.floor = int(info.get('floor', 0))
        self.turns = int(info.get('turns', 0))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    games = relationship("Games", backref = 'character')
    state_enemies = relationship("StateEnemies", backref = 'character')
    


class StateEnemies(Base):
    __tablename__ = 'state_enemies'
    id = Column(Integer, primary_key = True)
    character_id = Column(String, ForeignKey('character.id'))
    enemies_id = Column(Integer, ForeignKey('enemies.id'))
    battle_count = Column(Integer)
    battle_kill = Column(Integer)

    def __init__(self, character_id, enemies_id):
        self.character_id = character_id
        self.enemies_id = enemies_id
        self.battle_count = 0
        self.battle_kill = 0
    
    def add_state(self, kill = False):
        self.battle_count += 1
        if kill: self.battle_kill += 1
    '''
    @classmethod
    def add_battle(cls, kill = False):
        # проверить, выводится бой с врагом при поражении, или нет
        cls.battle_count += 1
        if kill: cls.battle_kill += 1
    '''

#Games.invoices = relationship("Battle", order_by = Battle.id, back_populates = "games")
#Battle.invoices = relationship("Enemies", order_by = Enemies.id, back_populates = "battle")





Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()

from sqlalchemy.orm.exc import NoResultFound
# ...

def get_or_create(model, check = False, **kwargs):
    """
    Usage:
    class Employee(Base):
        __tablename__ = 'employee'
        id = Column(Integer, primary_key=True)
        name = Column(String, unique=True)

    get_or_create(Employee, name='bob')
    """
    instance = get_instance(model = model, **kwargs)
    c = False
    if instance is None:
        instance = create_instance(model = model, **kwargs)
        c = True
    if not check: return instance
    return instance, c


def create_instance(model, **kwargs):
    """create instance"""
    try:
        instance = model(**kwargs)
        session.add(instance)
        session.flush()
    except Exception as msg:
        mtext = 'model:{}, args:{} => msg:{}'
        print(mtext.format(model, kwargs, msg))
        session.rollback()
        raise(msg)
    return instance


def get_instance(model, **kwargs):
    """Return first instance found."""
    try:
        return session.query(model).filter_by(**kwargs).first()
    except NoResultFound:
        return