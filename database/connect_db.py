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

#empoyee functions
    def check_emp_id(self, emp_id):
        
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = f"select emp_id from employee where emp_id = '{emp_id}' "

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()
            
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()

    def add_employee(self, emp_data):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = f"""
        insert into employee(emp_id, emp_fname, emp_minitial, emp_lname, emp_date_hired, emp_email_address, emp_address, emp_contact_num, emp_sex, emp_available)
        values(
            '{emp_data["emp_id"]}',
            '{emp_data["emp_fname"]}',
            '{emp_data["emp_minitial"]}',
            '{emp_data["emp_lname"]}',
            '{emp_data["emp_date_hired"]}',
            '{emp_data["emp_email_address"]}',
            '{emp_data["emp_address"]}',
            '{emp_data["emp_contact_num"]}',
            '{emp_data["emp_sex"]}',
            '{emp_data["emp_available"]}'
        )
        """
        
        try:
            self.cursor.execute(sql)
            self.conn.commit()    
                
        except Exception as e:
            self.conn.rollback()
            return e
        
        finally:
            self.conn.close()
            self.cursor.close()
            
    def add_employee_history(self, emp_id, emp_hist_data):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        if emp_hist_data:
            if isinstance(emp_hist_data[0], list):
                for i, row_data in enumerate(emp_hist_data):
                    self.cursor.execute(f"""
                                        insert into employment_history (emp_id, eh_job_description, eh_establishment, eh_date_started, eh_date_ended)
                                        values ('{emp_id}', '{row_data[0]}', '{row_data[1]}', '{row_data[2]}', '{row_data[3]}' )""")
            else:
                self.cursor.execute(f"""
                                    insert into employment_history (emp_id, eh_job_description, eh_establishment, eh_date_started, eh_date_ended)
                                        values ('{emp_id}', '{emp_hist_data[0]}', '{emp_hist_data[1]}', '{emp_hist_data[2]}', '{emp_hist_data[3]}' )
                                    """)        
        
        try:
            self.conn.commit()    
                
        except Exception as e:
            self.conn.rollback()
            return e
        
        finally:
            self.conn.close()
            self.cursor.close()
            
    def add_employee_services(self, emp_id, emp_services):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        for service in emp_services:
            
            service_ = service.replace(" ", "_")
            sql = f"""
                        update employee set emp_is_{service_} = 'TRUE' where emp_id = '{emp_id}';
                    """
                    
            sql2 = f"""
                        insert into {service_} (emp_id, ser_name)
                        values ('{emp_id}', '{service}');
                    """
            self.cursor.execute(sql+sql2)
        try:
            self.conn.commit()    
                
        except Exception as e:
            self.conn.rollback()
            return e
        
        finally:
            self.conn.close()
            self.cursor.close()
            
    def select_all_employees(self):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = "select emp_id, concat(emp_fname, ' ', emp_minitial, ' ', emp_lname) as name, emp_sex, emp_date_hired, emp_contact_num, emp_email_address, emp_address, emp_available from employee"

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
            
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()

    def select_employee(self, emp_id):
                
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = f"select emp_fname, emp_minitial, emp_lname, emp_sex, emp_address, emp_contact_num, emp_date_hired, emp_email_address, emp_available from employee where emp_id = '{emp_id}' "

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()
            
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()

    def select_all_available_employees(self):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = f"""
            select emp_id, emp_fname, emp_minitial, emp_lname, emp_sex from employee where emp_available = 'TRUE'
        """
        

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
            
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()

    def select_available_employees_by_service(self, service_name):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        service_name = service_name.replace(" ", "_")
        
        sql = f"""
            select employee.emp_id, employee.emp_fname, employee.emp_minitial, employee.emp_lname, employee.emp_sex from employee 
            inner join {service_name} on employee.emp_id = {service_name}.emp_id
            where emp_available = 'TRUE'
        """

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
            
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()
        
    def select_employment_history(self, emp_id):
        
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = f"select eh_id, eh_job_description, eh_establishment, eh_date_started, eh_date_ended from employment_history where emp_id = '{emp_id}' "

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
            
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()
#TODO: REWRITED THIS FUNCTION
    def select_employee_services(self, emp_id, services):
        employee_services = []
        
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        


        for service in services:
            service_ = service[1].replace(" ", "_")
            self.cursor.execute(f"""
                                select emp_is_{service_} from employee where emp_id = '{emp_id}'
                                """)
            try:
                flag = self.cursor.fetchone()
                if flag[0] is True:
                    employee_services.append(service[1])
            except Exception as e:
                self.conn.rollback()
                return e
            
        self.conn.close()
        self.cursor.close()
        return employee_services
    
    def update_employee(self, emp_id, emp_data):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = f"""
        update employee set 
        emp_fname = '{emp_data["emp_fname"]}',
        emp_minitial = '{emp_data["emp_minitial"]}',
        emp_sex = '{emp_data["emp_sex"]}',
        emp_lname = '{emp_data["emp_lname"]}',
        emp_date_hired = '{emp_data["emp_date_hired"]}',
        emp_email_address = '{emp_data["emp_email_address"]}',
        emp_address = '{emp_data["emp_address"]}',
        emp_contact_num = '{emp_data["emp_contact_num"]}',
        emp_available = '{emp_data["emp_available"]}'
        where emp_id = '{emp_id}'
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()
    
    def update_employee_history(self, emp_hist_id, emp_hist_data):
        
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = f"""
        update employment_history set 
        eh_job_description = '{emp_hist_data[0]}',
        eh_establishment = '{emp_hist_data[1]}',
        eh_date_ended = '{emp_hist_data[2]}',
        eh_date_started = '{emp_hist_data[3]}'
        where eh_id = '{emp_hist_id}'
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()
    
    def update_employee_services(self, emp_id, emp_services):
        services = self.select_services()

        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection

        for service in services:
            service_ = service[1].replace(" ", "_")
            if service[1] in emp_services:
                sql = f"""
                    update employee set emp_is_{service_} = TRUE where emp_id = '{emp_id}';
                """
                
                sql2 = f"""
                        insert into {service_} (emp_id, ser_name)
                        values ('{emp_id}', '{service[1]}')
                        on conflict (emp_id) do nothing;
                    """
                self.cursor.execute(sql+sql2)
            else:
                sql = f"""
                    update employee set emp_is_{service_} = FALSE where emp_id = '{emp_id}';
                """
                
                sql2 = f"""
                        delete from {service_} where emp_id = '{emp_id}'
                    """
                self.cursor.execute(sql+sql2)
            
        try:
            self.conn.commit()
                    
        except Exception as e:
            self.conn.rollback()
            return e
            
        self.conn.close()
        self.cursor.close()

    def delete_employee(self, emp_id):
        self.connect_db()
        
        sql = f"""
            delete from employee where emp_id = '{emp_id}'
        """
            
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()
            
    def delete_employee_history(self, emp_hist_id):
        print(emp_hist_id)
        self.connect_db()
        
        sql = f"""
            delete from employment_history where eh_id = '{emp_hist_id}'
        """
            
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()


#customer functions
        
    def add_customer(self, cus_data, app_data):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        

        try:
            sql = f"""
            select service.ser_id, employee.emp_id from employee, service
            where concat(employee.emp_fname, ' ', employee.emp_lname) = '{app_data[4]}' and service.ser_name = '{app_data[3]}';
        """
            self.cursor.execute(sql)
            emp_id_ser_id = self.cursor.fetchone()
            
            sql1 = f"""
                insert into customer(cus_id, cus_fname, cus_minitial, cus_lname, cus_contact_num, cus_sex)
                values(
                    '{cus_data[0]}',
                    '{cus_data[1]}',
                    '{cus_data[2]}',
                    '{cus_data[3]}',
                    '{cus_data[4]}',
                    '{cus_data[5]}'
                );
            """
            sql2 = f"""
                insert into appointment (app_date_time, cus_id, ser_id, emp_id)
                values (
                    '{app_data[0]} {app_data[1]}', '{app_data[2]}', '{emp_id_ser_id[0]}', '{emp_id_ser_id[1]}'
                );
            """            
            self.cursor.execute(sql1+sql2)
            self.conn.commit()
            
        except Exception as e:
            self.conn.rollback()
            return e
        
        finally:
            self.conn.close()
            self.cursor.close()
        
    def select_all_customers(self):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = f"""
            select  customer.cus_id, 
                    appointment.app_id,
                    concat(customer.cus_fname, ' ', customer.cus_minitial, ' ', customer.cus_lname) as "cus name", 
                    customer.cus_sex,
                    customer.cus_contact_num,
                    service.ser_name,
                    concat(employee.emp_fname, ' ', emp_lname) "assigned employee",
                    app_date_time
            from customer
            left join appointment on  customer.cus_id =  appointment.cus_id  
            left join employee on appointment.emp_id = employee.emp_id
            left join service on appointment.ser_id = service.ser_id        
        """

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
            
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()
        
    def select_customer(self, app_id):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = f"""
           select  customer.cus_fname, 
                    customer.cus_minitial, 
                    customer.cus_lname, 
                    customer.cus_sex,
                    service.ser_name,
                    customer.cus_contact_num,
                    appointment.app_date_time,
                    concat(employee.emp_fname, ' ', employee.emp_lname)
            from customer
            left join appointment on  customer.cus_id =  appointment.cus_id  
            left join employee on appointment.emp_id = employee.emp_id
            left join service on appointment.ser_id = service.ser_id  
            where appointment.app_id = '{app_id}'
        """

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()
            
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()
    
    def check_cus_id(self, cus_id):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = f"select cus_id from customer where cus_id = '{cus_id}' "

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()
            
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()

    def update_customer(self, cus_id, cus_data, app_id, app_data):
        self.connect_db()
                
       
        try:

            sql1 = f"""
                select service.ser_id, employee.emp_id from employee, service
                where concat(employee.emp_fname, ' ', employee.emp_lname) = '{app_data[3]}' and service.ser_name = '{app_data[2]}';
            """
            self.cursor.execute(sql1)
            emp_id_ser_id = self.cursor.fetchone()
            sql2 = f"""
                update customer set cus_fname = '{cus_data[0]}', 
                                    cus_minitial = '{cus_data[1]}', 
                                    cus_lname = '{cus_data[2]}', 
                                    cus_contact_num = '{cus_data[3]}', 
                                    cus_sex = '{cus_data[4]}' 
                where cus_id = '{cus_id}';
            """
            sql3 =  f"""
                update appointment set app_date_time = '{app_data[0]}', ser_id = '{emp_id_ser_id[0]}', emp_id = '{emp_id_ser_id[1]}' where app_id = '{app_id}';
            """
            
            self.cursor.execute(sql2+sql3)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()
        
    def delete_customer(self, cus_id):
        print(cus_id)
        self.connect_db()
        
        sql = f"""
            delete from customer where cus_id = '{cus_id}';
        """    
            
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()
        
    def complete_cus_app(self, app_id, cus_id):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        try:
 
            sql1 = f"""
                insert into transaction_history
                        (th_cus_fname, 
                        th_cus_minitial, 
                        th_cus_lname, 
                        th_cus_sex, 
                        ser_id, 
                        emp_id, 
                        th_app_date_time)

                select  customer.cus_fname, 
                        customer.cus_minitial, 
                        customer.cus_lname, 
                        customer.cus_sex, 
                        service.ser_id, 
                        employee.emp_id,
                        appointment.app_date_time
                from customer
                inner join appointment on appointment.cus_id = appointment.cus_id
                inner join service on appointment.ser_id = service.ser_id
                inner join employee on appointment.emp_id = employee.emp_id
                where appointment.app_id = '{app_id}' and customer.cus_id = '{cus_id}';
            """
            sql2 = f"""
                delete from customer where cus_id = '{cus_id}';
            """
            self.cursor.execute(sql1+sql2)
            self.conn.commit()
            print("added to transac history")
        except Exception as e:
            self.conn.rollback()
            return e
        
        finally:
            self.conn.close()
            self.cursor.close()

#service functions
    def add_service(self, service_data):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = f"""
        insert into service (ser_name, ser_price)
        values(
            '{service_data[0]}',
            '{service_data[1]}'
        )
        """
        
        try:
            self.cursor.execute(sql)
            self.conn.commit()    
                
        except Exception as e:
            self.conn.rollback()
            return e
        
        finally:
            self.conn.close()
            self.cursor.close()
        
    def create_service_table(self, service_name):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        service_name = service_name.replace(" ", "_")
        
        sql = f"""
            create table {service_name}(
                emp_id      text     primary key,
                ser_name    varchar(50) not null,
                foreign key (emp_id)    references employee (emp_id) 
                                                                        on update cascade
                                                                        on delete cascade,
                foreign key (ser_name)  references service (ser_name)
                                                                        on update cascade
                                                                        on delete cascade
            );
        """
        
        sql2 = f"""
        alter table employee 
        add column emp_is_{service_name} bool default false;
        """
        
        try:
            self.cursor.execute(sql+sql2)
            self.conn.commit()    
                
        except Exception as e:
            self.conn.rollback()
            return e
        
        finally:
            self.conn.close()
            self.cursor.close()

    def update_service(self, service_id, service_data):
        self.connect_db()
        
        service_name = service_data[0]
        
        sql = f"""
            update service set ser_name = '{service_name}', ser_price = '{service_data[1]}' where ser_id = '{service_id}'
        """
            
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()
        
    def update_service_table(self, service_id, service_name):
        
        old_service_name = self.select_service(service_id=service_id).replace(" ", "_")
      
        self.connect_db()
        
        service_name = service_name.replace(" ", "_")

        sql = f"""
                alter table {old_service_name} rename to {service_name}        
        """
            
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()
        
    def delete_service(self, service_name):
        self.connect_db()
        
        sql = f"""
            delete from service where ser_name = '{service_name}';
        """    
            
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()
        
    def delete_service_table(self, service_name):
        self.connect_db()
        
        service_name = service_name.replace(" ", "_")
        
        sql = f"""
            drop table {service_name};
        """
            
        sql2 = f"""
            alter table employee
            drop column emp_is_{service_name};
        """
        try:
            self.cursor.execute(sql+sql2)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()

    def select_services(self):
        connection = self.connect_db()
        
        if isinstance(connection, Exception):
            return connection
        
        sql = "select ser_id, ser_name, ser_price from service"
        
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        
        except Exception as e:
            self.conn.rollback()
            return e
        
        finally:
            self.conn.close()
            self.cursor.close()

    def select_service(self, service_id):
        self.connect_db()
        
        sql = f"""
            select ser_name from service where ser_id = '{service_id}'
        """
            
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()[0]
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()

    def select_service_by_name(self, service_name):
        self.connect_db()
        
        sql = f"""
            select ser_id, ser_name, ser_price from service where ser_name = '{service_name}'
        """
            
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            return e
        finally:
            self.conn.close()
            self.cursor.close()


#transaction function

    def select_all_transac(self):
        pass
    
    def select_transac_by_date(self):
        pass
    
    def select_all_transac_descending(self):
        pass












# from supabase import create_client

# url = 'https://lvsotcbvutxvfdiiljju.supabase.co'
# key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx2c290Y2J2dXR4dmZkaWlsamp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTc2NDgyNzIsImV4cCI6MjAzMzIyNDI3Mn0.EM4fyo9akODm18B-dhWb-lujVlmJx5jxgW9Uc0TOD2g'
# supabase  = create_client(url, key)

# results = supabase.from_("customers").select("cus_fname").execute()

# print(results)