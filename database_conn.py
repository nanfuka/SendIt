import psycopg2

class Database:
    def __init__(self):
        try:
            postgresdb = 'dffr8equenfo0j'
            Host="ec2-54-197-249-140.compute-1.amazonaws.com"
            User="wvgwrqdyzjrxko"
            Password="f557b9a8e7220d2390c0d9523bcba7db876d11290434b73aab18288e99ee4d7f"
          

            
            self.connection = psycopg2.connect(
                    database=postgresdb, host=Host, user=User,
                    password=Password, port="5432"
                )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            create_table_users = """CREATE TABLE IF NOT EXISTS users(
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(100),
            email VARCHAR(100),
            password VARCHAR(100))"""
            self.cursor.execute(create_table_users)
            self.connection.commit()
        except:
            print('cannot connect to database')

    def create_table_users(self):
        create_table_users = """CREATE TABLE IF NOT EXISTS users(
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(100),
            email VARCHAR(100),
            password VARCHAR(100))"""
        self.cursor.execute(create_table_users)
        self.connection.commit()

        create_table_parsels = """CREATE TABLE IF NOT EXISTS parcels(
            parcel_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            name_of_reciever VARCHAR(100) NOT NULL,
            source VARCHAR(100) NOT NULL,
            destination VARCHAR(100) NOT NULL,
            status VARCHAR DEFAULT 'in_transit',
            presentlocation VARCHAR(100) NOT NULL,
            FOREIGN KEY (user_id)
                REFERENCES users(user_id)
        )"""
        self.cursor.execute(create_table_parsels)
        self.connection.commit()

    def create_table_parsels(self):
        create_table_parsels = """CREATE TABLE IF NOT EXISTS parcels(
            parcel_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            name_of_reciever VARCHAR(100) NOT NULL,
            source VARCHAR(100) NOT NULL,
            destination VARCHAR(100) NOT NULL,
            status VARCHAR DEFAULT 'in_transit',
            presentlocation VARCHAR(100) NOT NULL,
            FOREIGN KEY (user_id)
                REFERENCES users(user_id)
        )"""
        self.cursor.execute(create_table_parsels)
        self.connection.commit()

    # def drop_tables(self):
    #     """
    #     method drops tables
    #     """
    #     create_table_users = "DROP TABLE users cascade"
    #     create_table_parsels = "DROP TABLE parcels cascade"
    #     self.cursor.execute(drop_user_table)
    #     self.cursor.execute(drop_parcel_table)

database = Database()
database.create_table_users()
database.create_table_parsels()