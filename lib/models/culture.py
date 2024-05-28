# from models.deity import Deity
# from models.artifact import Artifact

class Culture:
    all = []
    
    def __init__(self, name, region, era, id=None):
        self.id = id
        self.name = name
        self.region = region
        self.era = era
        self.deities = []
        self.artifacts = []
        Culture.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 20:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 20 characters.")
        
    @property
    def region(self):
        return self._region
    
    @region.setter
    def region(self, region):
        if isinstance(region, str) and 1 <= len(region) <= 20:
            self._region = region
        else:
            raise ValueError("Region must be a string between 1 and 20 characters.")
        
    @property 
    def era(self, era):
        if isinstance(era, str) and 1 <= len(era) <= 50:
            self._era = era
        else:
            raise ValueError("Era must be a string between 1 and 50 characters.")
        
    def add_deity(self, name, domain, attributes):
        from models.deity import Deity
        deity = Deity(name=name, domain=domain, attributes=attributes, culture=self)
        self.deities.append(deity)
        return deity
    
    def add_artifact(self, name, artifact_type, discovered_date, origin_date):
        from models.artifact import Artifact
        artifact = Artifact(name=name, artifact_type=artifact_type, discovered_date=discovered_date, origin_date=origin_date, culture=self)
        self.artifacts.append(artifact)
        return artifact
    
    def __repr__(self):
        return f"<Culture {self.name}>"
        