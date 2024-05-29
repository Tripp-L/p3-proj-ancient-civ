# lib/helpers.py

from models.culture import Culture
from models.deity import Deity
from models.artifact import Artifact
from models.myth import Myth


def exit_program():
    print("Goodbye!")
    exit()
    
def create_culture():
    name = input("Name: ")
    region = input("Region: ")
    era = input("Era: ")
    
    try:
        culture = Culture(name=name, region=region, era=era)
        print(f"Culture {culture.name} created!")
    except Exception as e:
        print(e)
        
def view_all_cultures():
    if Culture.all:
        for culture in Culture.all:
            print(culture)
    else:
        print("No cultures found.")
        
def find_culture_by_name():
    name = input("Name: ")
    Culture.all_from_db()
    culture = next((culture for culture in Culture.all if culture.name == name), None)
    if culture:
        print(culture)
    else:
        print(f"Culture {name} not found.")
            
def update_culture():
    name = input("Name: ")
    culture = next((culture for culture in Culture.all if culture.name == name), None)
    if culture:
        new_name = input("Enter new name: ")
        new_region = input("Enter new region: ")
        new_era = input("Enter new era: ")
        
        if new_name:
            culture.name = new_name
        if new_region:
            culture.region = new_region
        if new_era:
            culture.era = new_era
            
        print(f"Culture {culture.name} updated!")
    else:
        print(f"Culture {name} not found.")
        
def delete_culture():
    name = input("Name: ")
    culture = next((culture for culture in Culture.all if culture.name == name), None)
    if culture:
        Culture.all.remove(culture)
        print(f"Culture {culture.name} deleted!")
    else:
        print(f"Culture {name} not found.")
            
def create_deity():
    name = input("Name: ")
    domain = input("Domain: ")
    attributes = input("Attributes: ").split(", ")
    culture_name = input("Culture: ")
    Culture.all_from_db()
    culture = next((culture for culture in Culture.all if culture.name == culture_name), None)      
    
    if culture:
        try:
            deity = Deity(name=name, domain=domain, attributes=attributes, culture=culture)
            print(f"Deity {deity.name} created!")
        except Exception as e:
            print(e)
            
    else:
        print(f"Culture {culture_name} not found.")
        
def view_all_deities():
    Culture.all_from_db()
    Deity.all_from_db()
    if Deity.all:
        for deity in Deity.all:
            print(deity)
    else:
        print("No deities found.")
        
def find_deity_by_name():
    name = input("Name: ")
    Culture.all_from_db()
    Deity.all_from_db()
    deity = next((deity for deity in Deity.all if deity.name == name), None)
    if deity:
        print(deity)
    else:
        print(f"Deity {name} not found.")
        
def update_deity():
    name = input("Name: ")
    Deity.all_from_db()
    deity = next((deity for deity in Deity.all if deity.name == name), None)
    if deity:
        new_name = input("Enter new name: ")
        new_domain = input("Enter new domain: ")
        new_attributes = input("Enter new attributes: ").split(", ")
        
        if new_name:
            deity.name = new_name
        if new_domain:
            deity.domain = new_domain
        if new_attributes:
            deity.attributes = new_attributes
            
        deity.save()    
        print(f"Deity {deity.name} updated!")
    else:
        print(f"Deity {name} not found.")
        
def delete_deity():
    name = input("Name: ")
    deity = next((deity for deity in Deity.all if deity.name == name), None)
    if deity:
        Deity.all.remove(deity)
        print(f"Deity {deity.name} deleted!")
    else:
        print(f"Deity {name} not found.")
            
def create_artifact():
    name = input("Name: ")
    artifact_type = input("Artifact Type: ")
    discovered_date = input("Discovered Date: ")
    origin_date = input("Origin Date: ")
    culture_name = input("Culture: ")
    culture = next((culture for culture in Culture.all if culture.name == culture_name), None)
    
    if culture:
        try:
            artifact = Artifact(name=name, artifact_type=artifact_type, discovered_date=discovered_date, origin_date=origin_date, culture=culture)
            print(f"Artifact {artifact.name} created!")
        except Exception as e:
            print(e)
            
    else:
        print(f"Culture {culture_name} not found.")
        
def view_all_artifacts():
    Artifact.all_from_db()
    if Artifact.all:
        for artifact in Artifact.all:
            print(artifact)
    else:
        print("No artifacts found.")
        
def find_artifact_by_name():
    name = input("Name: ")
    artifacts = [artifact for artifact in Artifact.all if artifact.name == name]
    if artifacts:
        for artifact in artifacts:
            print(artifact)
    else:
        print(f"Artifact {name} not found.")
            
def update_artifact():
    name = input("Name: ")
    artifact = next((artifact for artifact in Artifact.all if artifact.name == name), None)
    if artifact:
        new_name = input("Enter new name: ")
        new_artifact_type = input("Enter new artifact type: ")
        new_discovered_date = input("Enter new discovered date: ")
        new_origin_date = input("Enter new origin date: ")
        
        if new_name:
            artifact.name = new_name
        if new_artifact_type:
            artifact.artifact_type = new_artifact_type
        if new_discovered_date:
            artifact.discovered_date = new_discovered_date
        if new_origin_date:
            artifact.origin_date = new_origin_date
            
        print(f"Artifact {artifact.name} updated!")
        
def delete_artifact():
    name = input("Name: ")
    artifact = next((artifact for artifact in Artifact.all if artifact.name == name), None)
    if artifact:
        Artifact.all.remove(artifact)
        print(f"Artifact {artifact.name} deleted!")
    else:
        print(f"Artifact {name} not found.")
            
def create_myth():
    name = input("Name: ")
    description = input("Description: ")
    deity_name = input("Deity: ")
    deity = next((deity for deity in Deity.all if deity.name == deity_name), None)
    
    if deity:
        try:
            myth = Myth(name=name, description=description, deity=deity)
            deity.myths.append(myth)
            print(f"Myth {myth.name} created!")
        except Exception as e:
            print(e)
            
    else:
        print(f"Deity {deity_name} not found.")
        

def view_all_myths():
    Myth.all_from_db()
    if Myth.all:
        for myth in Myth.all:
            print(myth)
    else:
        print("No myths found.")            
            
def find_myth_by_name():
    name = input("Name: ")
    myth = Myth.find_myth_by_name(name)
    if myth:
        print(myth)
    else:
        print(f"Myth {name} not found.")
   
    
def update_myth():
    name = input("Name: ")
    myth = Myth.find_myth_by_name(name)
    if myth:
        new_name = input("Enter new name: ")
        new_description = input("Enter new description: ")
        myth.update_myth(name=new_name, description=new_description)
        print(f"Myth {myth.name} updated!")
    else:
        print(f"Myth {name} not found.")
  
        
def delete_myth():
    name = input("Name: ")
    myths = [myth for deity in Deity.all for myth in deity.myths if myth.name == name]
    if myths:
        for myth in myths:
            myth.deity.remove_myth(myth)
            print(f"Myth {myth.name} deleted!")
        else:
            print(f"Myth {name} not found.")

