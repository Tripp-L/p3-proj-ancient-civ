This project is designed for professionals in the archeology/ history field. This app data contains information using Python object relationships and SQL for organization. Professionals in archeology/ history will be able to use this app data in their field of work as it is designed to change for new findings and update data from previous finds. Technology is always providing new information about history and archeological finds. Professionals in this field will be able to use this information to do all of the following that will appear in the CLI:

- Change the data accordingly by being able to create a new cultre,
- View all cultures already stored in the data base,
- Find a culture by name
- Update a culture's information
- Delete a culture from the database
- Create a new deity
- View all deities already stored in the database
- Find a deity by name
- Update a deity's information
- Delete a deity from the database
- Create a new artifact
- View all artifacts already stored in the database
- Find an artifact by name
- Update an artifact's information
- Delete an artifact from the database
- Create a new myth
- View all myths already stored in the database
- Find a myth by name
- Update a myth's information
- Delete a myth from the database

Directory Structure:

├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
├── models
│ ├── **init**.py
│ ├── artifact.py
│ ├── culture.py
│ ├── deity.py
│ └── myth.py
├── sql
│ ├── **init**.sql
│ └── seed.sql
├── cli.py
├── debug.py
├── helpers.py
└── init_db.py
├── development.db
