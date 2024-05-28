from models.deity import Deity
from models.artifact import Artifact

class Myth:
    all = []

    def __init__(self, name, description, deity, artifact=None):
        self.name = name
        self.description = description
        self.deity = deity
        self.artifact = artifact
        Myth.all.append(self)

    def __repr__(self):
        return f"<Myth {self.name}>"

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
        if not isinstance(deity, Deity):
            self._deity = deity
        else:
            raise ValueError("Deity must be an instance of Deity class")
        
    @property
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
