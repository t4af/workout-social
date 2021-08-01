"""
    INSTALLATIONS:
    * Google Cloud SQL Connector
        * For Windows, go to Command Prompt and type the following:
            * python -m pip install --upgrade pip
                * This updates Pip to the latest version
            * pip install cloud-sql-python-connector[pymysql]
                * This installs the connector to your local device
"""
import getpass
import os
from google.cloud.sql.connector import connector


######################################################################################################


class GcpSqlConnection:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connectionString = "speedy-carver-321508:us-west2:workout-social"
        self.dbName = "workout_social"
        self.username = "root"

        return

    def connect(self):
        """
            NOTES:
            * Having trouble seeing the password prompt?
                * If using Pycharm, go to the run configuration and check the box for
                  "Emulate terminal in output console"
        """
        print("Username: %s" % self.username)
        pswd = getpass.getpass(prompt="Password: ")

        self.conn = connector.connect(
            self.connectionString,
            "pymysql",
            user=self.username,
            password=pswd,
            db=self.dbName
        )

        if self.conn:
            self.cursor = self.conn.cursor()
            print("Connected to database '%s' as user '%s'" % (self.dbName, self.username))
        else:
            print("Invalid credentials; now exiting")

        return

    def query_table(self, table):
        self.cursor.execute("SELECT * from %s" % table)
        query = self.cursor.fetchall()

        for row in query:
            print(row)

        return


######################################################################################################


def samplefunc_query_simple():
    # Add GCP service account key to system's environment variables
    service_account_key_path = "./gcp/cloudsql/workoutSocial-cloudsql-serviceAccountKey-mainAccount.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_key_path

    # Create/establish connection
    db_connection = GcpSqlConnection()
    db_connection.connect()

    # Query DB for info
    db_connection.query_table("profiles")


######################################################################################################


''' The following should be commented out before committing/pushing the code.
    However, while developing, please do the following:
        * put code you'd like to run, into a sample function
        * set up the run configuration to execute this file only
        * uncomment the function call below so the code can execute
'''
# samplefunc_query_simple()
