import os
from pathlib import Path

import snowflake.connector


def connect():
    return snowflake.connector.connect(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USER"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
        database=os.environ["SNOWFLAKE_DATABASE"],
        schema=os.environ["SNOWFLAKE_SCHEMA"],
        role=os.environ["SNOWFLAKE_ROLE"],
    )


def deploy():
    sql_file = Path("sql/deploy.sql")
    sql = sql_file.read_text()

    conn = connect()

    try:
        cursor = conn.cursor()

        print(
            f"Deploying to database: "
            f"{os.environ['SNOWFLAKE_DATABASE']}"
        )

        for statement in sql.split(";"):
            statement = statement.strip()

            if statement:
                print(f"Executing: {statement[:100]}")
                cursor.execute(statement)

        print("Deployment completed successfully.")

    finally:
        conn.close()


if __name__ == "__main__":
    deploy()