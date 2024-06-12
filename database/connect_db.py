import psycopg2
from PyQt6.QtWidgets import QMessageBox
class Database:
    def __init__(self) -> None:
        self._host = "aws-0-ap-southeast-1.pooler.supabase.com"
        self._port = 6543
        self._user = "postgres.lvsotcbvutxvfdiiljju"
        self._password = "q,gkb9K8/*BVFKy"
        self._database = "postgres"
        self.conn = None
        self.cursor = None
        
    def connect_db(self):
        try:
            self.conn = psycopg2.connect(
            
            host=self._host,
            port=self._port,
            database=self._database,
            user=self._user,
            password=self._password)
            self.cursor = self.conn.cursor()  
        except Exception as e:
            return e
        
    
    def rollback(self):
        self.conn.rollback()

    def close_connection(self):
        self.conn.close()
        
    def close_cursor(self):
        self.cursor.close()




    def test(self):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = "select * from customer"

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
            
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.close_connection()
            self.close_cursor()
            
            



# from supabase import create_client

# url = 'https://lvsotcbvutxvfdiiljju.supabase.co'
# key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx2c290Y2J2dXR4dmZkaWlsamp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTc2NDgyNzIsImV4cCI6MjAzMzIyNDI3Mn0.EM4fyo9akODm18B-dhWb-lujVlmJx5jxgW9Uc0TOD2g'
# supabase  = create_client(url, key)

# results = supabase.from_("customers").select("cus_fname").execute()

# print(results)