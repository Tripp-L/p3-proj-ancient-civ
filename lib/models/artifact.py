# from models.culture import Culture

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
        
    def __repr__(self):
        return f'<Artifact: {self.name}>'
    
    