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
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError('Name must be a string with at least 3 characters.')

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