# lib/cli.py

from helpers import (
    exit_program,
    create_culture,
    view_all_cultures,
    find_culture_by_name,
    update_culture,
    delete_culture,
    create_deity,
    view_all_deities,
    find_deity_by_name,
    update_deity,
    delete_deity,
    create_artifact,
    view_all_artifacts,
    find_artifact_by_name,
    update_artifact,
    delete_artifact,
    create_myth,
    view_all_myths,
    find_myth_by_name,
    update_myth,
    delete_myth,
)

from models.culture import Culture
from models.deity import Deity


def main():
    Culture.all_from_db()
    Deity.all_from_db()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_culture()
        elif choice == "2":
            view_all_cultures()
        elif choice == "3":
            find_culture_by_name()
        elif choice == "4":
            update_culture()
        elif choice == "5":
            delete_culture()
        elif choice == "6":
            create_deity()
        elif choice == "7":
            view_all_deities()
        elif choice == "8":
            find_deity_by_name()
        elif choice == "9":
            update_deity()
        elif choice == "10":
            delete_deity()
        elif choice == "11":
            create_artifact()
        elif choice == "12":
            view_all_artifacts()
        elif choice == "13":
            find_artifact_by_name()
        elif choice == "14":
            update_artifact()
        elif choice == "15":
            delete_artifact()
        elif choice == "16":
            create_myth()
        elif choice == "17":
            view_all_myths()
        elif choice == "18":
            find_myth_by_name()
        elif choice == "19":
            update_myth()
        elif choice == "20":
            delete_myth()
        else:
            print("Invalid choice. Please choose a valid option.")



def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create Culture")
    print("2. View All Cultures")
    print("3. Find Culture by Name")
    print("4. Update Culture")
    print("5. Delete Culture")
    print("6. Create Deity")
    print("7. View All Deity")
    print("8. Find Deity by Name")
    print("9. Update Deity")
    print("10. Delete Deity")
    print("11. Create Artifact")
    print("12. View All Artifacts")
    print("13. Find Artifact by Name")
    print("14. Update Artifact")
    print("15. Delete Artifact")
    print("16. Create Myth")
    print("17. View All Myths")
    print("18. Find Myth by Name")
    print("19. Update Myth")
    print("20. Delete Myth")


if __name__ == "__main__":
    main()
