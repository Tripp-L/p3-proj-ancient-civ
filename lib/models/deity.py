from models.myth import Myth
from models.artifact import Artifact
from models.culture import Culture

class Deity:
    all = []

    def __init__(self, name, domain, attributes, culture):
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
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError('Name must be a string with at least 3 characters.')

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._domain = value
        else:
            raise ValueError('Domain must be a string with at least 3 characters.')

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        if isinstance(value, list) and all(isinstance(attr, str) for attr in value):
            self._attributes = value
        else:
            raise ValueError('Attributes must be a list of strings.')

    def add_myth(self, name, text):
        myth = Myth(name=name, description=text, deity=self)
        self.myths.append(myth)
        return myth

    def remove_myth(self, myth):
        self.myths.remove(myth)

    def add_artifact(self, name, artifact_type, discovered_date, origin_date):
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

    def __repr__(self):
        return f"<Deity {self.name}>"