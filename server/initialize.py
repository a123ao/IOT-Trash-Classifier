from sqlmodel import SQLModel

import src.models

if __name__ == '__main__':
    SQLModel.metadata.create_all(src.models.engine)

    session = next(src.models.connect_db())
    session.close()

    print('Database initialized successfully.')