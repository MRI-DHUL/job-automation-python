from db.database import engine
from db.models import Base

Base.metadata.create_all(bind=engine)
print("All tables created successfully.")