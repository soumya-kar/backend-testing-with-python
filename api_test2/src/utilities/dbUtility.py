import pymysql
from api_test2.src.utilities.credentialsUtility import CredentialsUtility


class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials(self)
        self.host = 'localhost'

    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.creds['db_user'],
                                     password=self.creds['db_password'], port=8889)
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()
        try:
            with conn.cursor(pymysql.cursors.DictCursor) as curr:
                curr.execute(sql)
                rs_dict = curr.fetchall()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error: {str(e)}")
        finally:
            conn.close()

        return rs_dict




    def execute_sql(self, sql):
        pass
