# Script: 023_backup_mysql_database.py

import subprocess

def backup_mysql_db(db_name, db_user, db_password, backup_path):
    """
    Creates a backup of a MySQL database using mysqldump.
    :param db_name: Name of the database to back up.
    :param db_user: Username for the MySQL database.
    :param db_password: Password for the MySQL database.
    :param backup_path: Path to save the backup file.
    """
    dump_command = f"mysqldump -u {db_user} -p{db_password} {db_name} > {backup_path}"
    try:
        subprocess.run(dump_command, shell=True, check=True)
        print(f"Database '{db_name}' backed up successfully to {backup_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error backing up database: {e.stderr}")
    except PermissionError:
        print("Permission denied. Run this script with appropriate permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    db_name = 'my_database'  # Replace with your database name
    db_user = 'username'  # Replace with your database username
    db_password = 'password'  # Replace with your database password
    backup_path = '/path/to/backup.sql'  # Replace with your desired backup file path
    
    backup_mysql_db(db_name, db_user, db_password, backup_path)
