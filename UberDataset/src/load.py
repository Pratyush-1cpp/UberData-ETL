from sqlalchemy import create_engine
from config import DB_CONFIG

class Load:

    def __init__(self):
        self.engine = create_engine(
            f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
            f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        )

    def run(self, df):
        df.to_sql("uber_data", self.engine, if_exists="replace", index=False)
        print("Data Loaded to PostgreSQL ✅")

#-> vs code -> database -> connection         