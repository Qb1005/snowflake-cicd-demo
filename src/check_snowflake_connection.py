import os

import snowflake.connector


def check_connection():
    conn = snowflake.connector.connect(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USER"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
        database=os.environ["SNOWFLAKE_DATABASE"],
        schema=os.environ["SNOWFLAKE_SCHEMA"],
        role=os.environ["SNOWFLAKE_ROLE"],
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            CURRENT_USER(),
            CURRENT_ROLE(),
            CURRENT_DATABASE(),
            CURRENT_SCHEMA(),
            CURRENT_WAREHOUSE()
        """
    )

    result = cursor.fetchone()

    print("Snowflake session:")
    print(f"User:      {result[0]}")
    print(f"Role:      {result[1]}")
    print(f"Database:  {result[2]}")
    print(f"Schema:    {result[3]}")
    print(f"Warehouse: {result[4]}")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    check_connection()