
from models.deity import Deity
from models.artifact import Artifact
from models.__init__ import CONN, CURSOR


class Myth:
    all = []

    def __init__(self, name, description, deity, artifact=None, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.deity = deity
        self.artifact = artifact
        Myth.all.append(self)

    @classmethod
    def create_myth(cls, name, description, deity, artifact=None):
        myth = cls(name, description, deity, artifact)
        return myth

    @staticmethod
    def view_all_myths():
        return Myth.all

    @classmethod
    def find_myth_by_name(cls, name):
        return next((myth for myth in cls.all if myth.name == name), None)

    def update_myth(self, name=None, description=None, deity=None, artifact=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if deity:
            self.deity = deity
        if artifact:
            self.artifact = artifact

    @classmethod
    def delete_myth(cls, myth):
        cls.all.remove(myth)

    @property
    def deity(self):
        return self._deity

    @deity.setter
    def deity(self, deity):
        if isinstance(deity, Deity):
            self._deity = deity
        else:
            raise ValueError("Deity must be an instance of Deity class")
        
    @property
    def artifact(self):
        return self._artifact
    
    @artifact.setter
    def artifact(self, artifact):
        if artifact is None or isinstance(artifact, Artifact): 
            self._artifact = artifact
        else:
            raise ValueError("Artifact must be an instance of Artifact class")
        
    @classmethod
    def find_myths_by_deity(cls, deity):
        return [myth for myth in cls.all if myth.deity == deity]  

    @classmethod
    def find_myths_by_artifact(cls, artifact):
        return [myth for myth in cls.all if myth.artifact == artifact]
    

    def save(self):
        if self.id is None:
            CURSOR.execute("INSERT INTO myths (name, description, deity_id) VALUES (?, ?, ?)", (self.name, self.description, self.deity.id))
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute("UPDATE myths SET name=?, description=?, deity_id=? WHERE id=?", (self.name, self.description, self.deity.id, self.id))
        CONN.commit()

    @classmethod
    def all_from_db(cls):
        cls.all.clear()
        CURSOR.execute("SELECT id, name, description, deity_id FROM myths")
        rows = CURSOR.fetchall()
        print(f"Fetched {len(rows)} myths from the database.")
        for row in rows:
            deity = next((deity for deity in Deity.all if deity.id == row[3]), None)
            if deity:
                myth = Myth(id=row[0], name=row[1], description=row[2], deity=deity)
                print(f"Myth loaded: {myth.name} (ID: {myth.id})")
        print(f"Loaded {len(cls.all)} myths into memory.")

    def repr(self):
        return f"<Myth {self.name}, Deity: {self.deity.name}>"
    
