
# DROP TABLES
drop_I94_Immigration = "DROP TABLE IF EXISTS I94_Immigration;"
drop_World_Temperature = "DROP TABLE IF EXISTS World_Temperature;"
drop_City_Demographic = "DROP TABLE IF EXISTS City_Demographic;"
drop_airport_codes = "DROP TABLE IF EXISTS airport_codes;"
drop_194Visa = "DROP TABLE IF EXISTS Visa;"


# CREATE TABLES


Immigration_I94_create= """
  CREATE TABLE IF NOT EXISTS public.I94_Immigration (
    cicid    FLOAT PRIMARY KEY,
    Year     FLOAT,
    i94mon   FLOAT ,
    i94cit      FLOAT,
    i94res  FLOAT,
    i94mode FLOAT,
    i94addr  VARCHAR,
    depdate  FLOAT,
    i94bir  FLOAT,
    i94visa     FLOAT ,
    gender  VARCHAR,
    visatype VARCHAR  
);
"""


 
World_Temperature_create = """
 CREATE TABLE IF NOT EXISTS public.World_Temperature (
    dt                      date,
    average_temperature            FLOAT,
    average_temperature_uncertainty FLOAT,
    city                           VARCHAR,
    country                        VARCHAR,
    latitude                       VARCHAR,
    longitude                      VARCHAR
);
"""
    
City_Demographic_create = """
 CREATE TABLE IF NOT EXISTS public.City_Demographic (
    City                   VARCHAR,
    State                  VARCHAR,
    Media_Age              FLOAT,
    Male_population        VARCHAR,
    Female_population      VARCHAR,
    Total_population       VARCHAR,
    Num_veterans           VARCHAR,
    Foreign_born           VARCHAR,
    Avg_household_size FLOAT,
    State_code             VARCHAR(2),
    race                   VARCHAR,
    count                  INT
);
"""


airport_codes_create = """
 CREATE TABLE IF NOT EXISTS public.airport_codes (
    ident    VARCHAR PRIMARY KEY,
    type         VARCHAR,
    name         VARCHAR,
    elevation_ft FLOAT,
    continent    VARCHAR,
    iso_country  VARCHAR,
    iso_region   VARCHAR, 
    municipality VARCHAR, 
    gps_code     VARCHAR,
    iata_code    VARCHAR,
    local_code   VARCHAR,
    coordinates  VARCHAR
);
"""

visa_create = """
 CREATE TABLE IF NOT EXISTS public.Visa (
 i94visa     FLOAT PRIMARY KEY,
 name        VARCHAR
);
"""

    
# insert TABLES


visa_insert = ("""
INSERT INTO Visa (i94visa,name) VALUES (%s, %s)""")


I94_Immigration_insert = ("""
INSERT INTO I94_Immigration (cicid, Year,i94mon, i94cit,i94res,i94mode,i94addr,depdate,i94bir,i94visa,gender,visatype) \
VALUES ( %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)""")

World_Temperature_insert = ("""
INSERT INTO World_Temperature (dt, average_temperature, average_temperature_uncertainty, city, country, \
latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s)""")

City_Demographic_insert = """
INSERT INTO City_Demographic (City, State, Media_Age, Male_population, Female_population, Total_population, \
Num_veterans, Foreign_born, Avg_household_size, State_code, race, count) VALUES (%s, %s, %s, %s, \
%s, %s, %s, %s, %s, %s, %s, %s)"""


airport_codes_insert = """
INSERT INTO airport_codes (ident, type, name, elevation_ft,continent,local_code,iso_country,iso_region,municipality,gps_code,iata_code,local_code,coordinates) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""




# QUERY LISTS
DropTable_queries = [drop_I94_Immigration,drop_World_Temperature,drop_City_Demographic,drop_airport_codes ,drop_194Visa]
CreateTable_queries = [Immigration_I94_create,World_Temperature_create, City_Demographic_create,airport_codes_create,visa_create]