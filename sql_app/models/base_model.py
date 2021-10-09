from sql_app.database import DBModel, SessionLocal
import uuid

class BaseModel(DBModel):
    __abstract__ = True

    def save(self):
        try:
            db = SessionLocal()
            print(db)
            db.add(self)
            db.commit()
            db.refresh(self)
        except Exception as e:
            db.rollback()
            raise
        finally:
            db.close()
    
    def delete(self):
        try:
            db = SessionLocal()
            db.delete(self)
            db.commit()
        except:
            db.rollback()
            raise
        finally:
            db.close()

    def create_uuid(self):
        return str(uuid.uuid4())
