"""Setup script for Hunter Assassin MySQL database.

Run this once on a new system to:
- Create the 'project' database (if it does not exist)
- Create the 'leaderboard' table (if it does not exist)
- Optionally create / configure the MySQL user the game will use
- Write db_config.json with the connection details used by the game

Usage (from project root):

    python3.12 setup_db.py

You must have:
- MySQL server running on localhost
- mysql-connector-python installed for the Python you use
"""

import getpass
from typing import Tuple

import mysql.connector as m

from db_config import _CONFIG_FILE  # type: ignore[attr-defined]


def prompt(text: str, default: str | None = None) -> str:
    if default is None:
        return input(text).strip()
    value = input(f"{text} [{default}]: ").strip()
    return value or default


def create_database_and_table(cnx: m.connection_cext.CMySQLConnection, db_name: str) -> None:
    cur = cnx.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
    cur.execute(f"USE `{db_name}`")
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS leaderboard (
            `rank` INT PRIMARY KEY,
            name VARCHAR(100),
            score INT,
            time INT
        )
        """
    )
    cnx.commit()
    cur.close()


def maybe_create_app_user(
    admin_cnx: m.connection_cext.CMySQLConnection,
    db_name: str,
    app_user: str,
    app_password: str,
    admin_user: str,
) -> None:
    """Create or grant privileges to the application user.

    If app_user == admin_user we assume the admin user will be used directly
    and only grant privileges (no separate CREATE USER needed).
    """

    cur = admin_cnx.cursor()

    if app_user != admin_user:
        # Create a dedicated user for the game if it does not exist
        cur.execute(
            "CREATE USER IF NOT EXISTS %s@'localhost' IDENTIFIED BY %s",
            (app_user, app_password),
        )

    # Grant privileges on the project database
    cur.execute(
        f"GRANT ALL PRIVILEGES ON `{db_name}`.* TO %s@'localhost'",
        (app_user,),
    )
    cur.execute("FLUSH PRIVILEGES")
    admin_cnx.commit()
    cur.close()


def write_config_file(host: str, user: str, password: str, database: str) -> None:
    data = {
        "host": host,
        "user": user,
        "password": password,
        "database": database,
    }
    _CONFIG_FILE.write_text(__import__("json").dumps(data, indent=2), encoding="utf-8")


def main() -> None:
    print("Hunter Assassin DB setup\n" + "-" * 30)

    host = prompt("MySQL host", "localhost")
    admin_user = prompt("MySQL admin username", "root")
    admin_password = getpass.getpass(f"Password for {admin_user}@{host} (can be empty): ")
    db_name = prompt("Database name to use", "project")

    print("\nThe game itself can use the same user, or a dedicated one.")
    app_user = prompt("MySQL username for the game", admin_user)
    if app_user == admin_user:
        app_password = admin_password
    else:
        app_password = getpass.getpass(f"Password for game user {app_user}@{host}: ")

    print("\nConnecting to MySQL as admin...")
    admin_cnx = m.connect(host=host, user=admin_user, password=admin_password or None)

    try:
        create_database_and_table(admin_cnx, db_name)
        maybe_create_app_user(admin_cnx, db_name, app_user, app_password, admin_user)
    finally:
        admin_cnx.close()

    write_config_file(host, app_user, app_password, db_name)

    print("\nSetup complete.")
    print(f"- Database: {db_name}")
    print("- Table: leaderboard")
    print(f"- Config written to: {_CONFIG_FILE}")
    print("You can now run the game menu, e.g. 'python3.12 Menu.py'.")


if __name__ == "__main__":
    main()
