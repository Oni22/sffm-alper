from sql_app.database import SessionLocal
#Festlegen der Lokalität der Datenverarbeitung von Objekten der Datenbank 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Erstellen der Datenbankübertragung