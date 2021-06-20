from base import session_factory

def create_database(name):

    session = session_factory()
    session.execute(f"CREATE DATABASE {name}")
    session.close()

    return f"Table {name} is created"


def delete_database(name):

    session = session_factory()
    session.execute(f"DROP DATABASE {name}")
    session.close()

    return f"Table {name} is deleted."


def backup_database(name, path):
    
    session = session_factory()
    session.execute(f"BACKUP DATABASE {name} TO DISK={path}")
    session.close()

    return f"Backup is created for database {name} on path {path}"