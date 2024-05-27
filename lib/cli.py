# lib/cli.py

from helpers import (
    exit_program,
    create_culture,
    view_all_cultures,
    find_culture_by_name,
    update_culture,
    delete_culture,
    create_diety,
    view_all_dieties,
    find_diety_by_name,
    update_diety,
    delete_diety,
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


def main():
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
            create_diety()
        elif choice == "7":
            view_all_dieties()
        elif choice == "8":
            find_diety_by_name()
        elif choice == "9":
            update_diety()
        elif choice == "10":
            delete_diety()
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
    print("6. Create Diety")
    print("7. View All Diety")
    print("8. Find Diety by Name")
    print("9. Update Diety")
    print("10. Delete Diety")
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
