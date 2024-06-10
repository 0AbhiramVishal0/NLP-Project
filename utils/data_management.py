import pandas as pd
from sqlalchemy import create_engine

def save_to_database(df, db_name='tweets.db', table_name='tweets'):
    engine = create_engine(f'sqlite:///{db_name}')
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def load_from_database(db_name='tweets.db', table_name='tweets'):
    engine = create_engine(f'sqlite:///{db_name}')
    df = pd.read_sql(f'SELECT * FROM {table_name}', con=engine)
    return df