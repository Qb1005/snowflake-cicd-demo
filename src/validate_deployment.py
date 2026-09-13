import os

import snowflake.connector


def main():
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
        SELECT COUNT(*)
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = CURRENT_SCHEMA()
          AND TABLE_NAME = 'CUSTOMERS'
        """
    )

    count = cursor.fetchone()[0]

    if count != 1:
        raise RuntimeError("CUSTOMERS table is missing")

    print("Deployment validation passed.")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()