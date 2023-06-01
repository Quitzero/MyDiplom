from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table, select
from geoalchemy2.functions import ST_AsGeoJSON


def read_table(engine, dataset_satellite, date_from, date_to, cloudiness_min, cloudiness_max, Ingestion_date_from, Ingestion_date_to):
    metadata = MetaData(schema='public')
    table = Table('test_satellite_boarders', metadata, autoload_with=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = select((ST_AsGeoJSON(table.c.geom)), table).where((table.c.satellite == dataset_satellite)&(cloudiness_min <= table.c.cloud_percentage )&(table.c.cloud_percentage <= cloudiness_max))
    if date_from is not None:
        query = query.where(date_from <= table.c.sensing_time)
    if date_to is not None:
        query = query.where(table.c.sensing_time <= date_to)
    if Ingestion_date_from is not None:
        query = query.where(Ingestion_date_from <= table.c.creation_time)
    if Ingestion_date_to is not None:
        query = query.where(table.c.creation_time <= Ingestion_date_to)


    result = session.execute(query).fetchall()
    session.close()

    return result

