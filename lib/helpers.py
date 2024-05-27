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
        for culture in Culture.all:
            print(culture)
            
    def find_culture_by_name():
        name = input("Name: ")
        cultures = [culture for culture in Culture.all]
        if cultures:
            for culture in cultures:
                print(culture)
            else:
                print(f"Culture {name} not found.")
                
    def create_deity():
        name = input("Name: ")
        domain = input("Domain: ")
        attributes = input("Attributes: ")
        culture_name = input("Culture: ")
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
        for deity in Deity.all:
            print(deity)
            
    def find_deity_by_name():
        name = input("Name: ")
        deities = [deity for deity in Deity.all if deity.name == name]
        if deities:
            for deity in deities:
                print(deity)
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
        for artifact in Artifact.all:
            print(artifact)
            
    def find_artifact_by_name():
        name = input("Name: ")
        artifacts = [artifact for artifact in Artifact.all if artifact.name == name]
        if artifacts:
            for artifact in artifacts:
                print(artifact)
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
            
    def delete_myth():
        name = input("Name: ")
        myths = [myth for deity in Deity.all for myth in deity.myths if myth.name == name]
        if myths:
            for myth in myths:
                myth.deity.remove_myth(myth)
                print(f"Myth {myth.name} deleted!")
            else:
                print(f"Myth {name} not found.")
                
    def view_all_myths():
        for deity in Deity.all:
            for myth in deity.myths:
                print(myth)
                
    def find_myth_by_name():
        name = input("Name: ")
        myths = [myth for deity in Deity.all for myth in deity.myths if myth.name == name]
        if myths:
            for myth in myths:
                print(myth)
            else:
                print(f"Myth {name} not found.")
