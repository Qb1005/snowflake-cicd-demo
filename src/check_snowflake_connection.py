import os

import snowflake.connector


def check_connection():

    conn = snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        role=os.getenv("SNOWFLAKE_ROLE"),
    )

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            CURRENT_USER(),
            CURRENT_ROLE(),
            CURRENT_DATABASE(),
            CURRENT_SCHEMA(),
            CURRENT_WAREHOUSE()
    """)

    result = cursor.fetchone()

    print(result)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    check_connection()