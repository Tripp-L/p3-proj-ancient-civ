from models.__init__ import CONN, CURSOR
from models.culture import Culture

class Deity:
    all = []

    def __init__(self, name, domain, attributes, culture, id=None):
        self.id = id
        self.name = name
        self.domain = domain
        self.attributes = attributes
        self.culture = culture
        self.myths = []
        self.artifacts = []
        Deity.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 2:
            self._name = name
        else:
            raise ValueError('Name must be a string with at least 2 characters.')

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, domain):
        if isinstance(domain, str) and len(domain) >= 3:
            self._domain = domain
        else:
            raise ValueError('Domain must be a string with at least 3 characters.')

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        if isinstance(attributes, list) and all(isinstance(attr, str) for attr in attributes):
            self._attributes = attributes
        else:
            raise ValueError('Attributes must be a list of strings.')

    def add_myth(self, name, text):
        from models.myth import Myth
        myth = Myth(name=name, description=text, deity=self)
        self.myths.append(myth)
        return myth

    def remove_myth(self, myth):
        self.myths.remove(myth)

    def add_artifact(self, name, artifact_type, discovered_date, origin_date):
        from models.artifact import Artifact
        artifact = Artifact(name=name, artifact_type=artifact_type, discovered_date=discovered_date, origin_date=origin_date, culture=self.culture)
        self.artifacts.append(artifact)
        return artifact

    def myth_count(self):
        return len(self.myths)

    @classmethod
    def top_deity(cls, culture):
        deities = [deity for deity in cls.all if deity.culture == culture]
        if not deities:
            return None
        return max(deities, key=lambda d: len(d.artifacts))
    
    def save(self):
        if self.id is None:
            CURSOR.execute("INSERT INTO deities (name, domain, attributes, culture_id) VALUES (?, ?, ?, ?)", (self.name, self.domain, ','.join(self.attributes), self.culture.id))
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute("UPDATE deities SET name =?, domain =?, attributes =?, culture_id =? WHERE id =?", (self.name, self.domain, ','.join(self.attributes), self.culture.id, self.id))
        CONN.commit()
    
    @classmethod
    def all_from_db(cls):
        cls.all.clear()
        CURSOR.execute("SELECT id, name, domain, attributes, culture_id FROM deities")
        rows = CURSOR.fetchall()
        print(f"Fetched {len(rows)} deities from the database.")
        for row in rows:
            culture = next((culture for culture in Culture.all if culture.id == row[4]), None)
            print(f"Matching culture for deity {row[1]}: {culture}") 
            if culture:
                attributes = row[3].split(",")
                deity = Deity(id=row[0], name=row[1], domain=row[2], attributes=attributes, culture=culture)
                print(f"Deity loaded: {deity.name} (ID: {deity.id})")
        print(f"Loaded {len(cls.all)} deities into memory.")
        

    def __repr__(self):
        return f"<Deity {self.name}, Domain: {self.domain}, Attributes: {', '.join(self.attributes)}, Culture: {self.culture.name}>"