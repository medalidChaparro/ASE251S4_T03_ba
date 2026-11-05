import os
import pyodbc

def get_sqlserver_connection():
    connection_string = (
        f"DRIVER={{{os.getenv('SQL_DRIVER')}}};"
        f"SERVER={os.getenv('SQL_SERVER')};"
        f"DATABASE={os.getenv('SQL_DATABASE')};"
        f"Trusted_Connection={os.getenv('SQL_TRUSTED_CONNECTION')};"
        f"TrustServerCertificate={os.getenv('SQL_TRUST_SERVER_CERTIFICATE')};"
    )

    return pyodbc.connect(connection_string)