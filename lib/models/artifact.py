from models.culture import Culture
from models.__init__ import CONN, CURSOR

class Artifact:
    all = []
    
    def __init__(self, name, artifact_type, discovered_date, origin_date, culture):
        self.name = name
        self.artifact_type = artifact_type
        self.discovered_date = discovered_date
        self.origin_date = origin_date
        self.culture = culture
        self.deities = []
        Artifact.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError('Name must be a string of at least 3 characters')
        
    @property
    def artifact_type(self):
        return self._artifact_type
    
    @artifact_type.setter
    def artifact_type(self, artifact_type):
        if isinstance(artifact_type, str) and len(artifact_type) >= 3:
            self._artifact_type = artifact_type
        else:
            raise ValueError('Artifact type must be a string of at least 3 characters')
        
    @property
    def discovered_date(self):
        return self._discovered_date
    
    @discovered_date.setter
    def discovered_date(self, discovered_date):
        if isinstance(discovered_date, str) and len(discovered_date) >= 3:
            self._discovered_date = discovered_date
        else:
            raise ValueError('Discovered date must be a string with at least 3 characters')
        
    @property
    def origin_date(self):
        return self._origin_date
    
    @origin_date.setter
    def origin_date(self, origin_date):
        if isinstance(origin_date, str):
            self._origin_date = origin_date
        else:
            raise ValueError('Origin date must be a string')
        
    @property
    def culture(self):
        return self._culture
    
    @culture.setter
    def culture(self, culture):
        from models.culture import Culture
        if isinstance(culture, Culture):
            self._culture = culture
        else:
            raise ValueError('Culture must be a Culture object')
        
    def save(self):
        if self.id is None:
            CURSOR.execute("INSERT INTO artifacts (name, artifact_type, discovered_date, origin_date, culture_date, culture_id) VALUES (?, ?, ?, ?, ?)",
                           (self.name, self.artifact_type, self.discovered_date, self.culture_id, self.id))    
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute("UPDATE artifacts SET name=?, artifact_type=?, dicovered_date=?, origin_date=?, culture_id=? WHERE id=?",
                           (self.name, self.artifact_type, self.discovered_date, self.origin_date, slef.culture.id, self.id))
        CONN.commit()

    @classmethod
    def all_from_db(cls):
        cls.all.clear()
        CURSOR.execute("SELECT id, name, artifact_type, dicovered_date, origin_date, culture_id FROM artifacts")
        rows = CURSOR.fetchall()
        print(f"Fetched {len(rows)} artifacts fromm the database.")
        for row in rows:
            culture = next((culture for culture in Culture.all if culture.id == row[5]), None)
            if culture:
                artifact = Artifact(id=row[0], name=row[1], artifact_type=row[2], discovered_date=row[3], origin_date=row[4], culture=culture)      
                print(f"Artifact loaded: {artifact.name} (ID: {artifact.id})")
        print(f"Loaded {len(cls.all)} artifacts into memory.")


        
    def __repr__(self):
        return f'<Artifact: {self.name}, Type: {self.artifact_type}, Discovered: {self.discovered_date}, Origin: {self.origin_date}, Culture: {self.culture.name}>'
    
    