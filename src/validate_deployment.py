import os

import snowflake.connector


def main():
    connection = snowflake.connector.connect(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USER"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
        database=os.environ["SNOWFLAKE_DATABASE"],
        schema=os.environ["SNOWFLAKE_SCHEMA"],
        role=os.environ["SNOWFLAKE_ROLE"],
    )

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT
                CURRENT_DATABASE(),
                CURRENT_SCHEMA(),
                CURRENT_ROLE()
            """
        )

        database, schema, role = cursor.fetchone()

        print(f"Validating database: {database}")
        print(f"Validating schema:   {schema}")
        print(f"Using role:          {role}")

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_SCHEMA = CURRENT_SCHEMA()
              AND TABLE_NAME = 'DOES_NOT_EXIST'
            """
        )

        customer_table_count = cursor.fetchone()[0]

        if customer_table_count != 1:
            raise RuntimeError("DOES_NOT_EXIST table was not found")

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM INFORMATION_SCHEMA.VIEWS
            WHERE TABLE_SCHEMA = CURRENT_SCHEMA()
              AND TABLE_NAME = 'CUSTOMER_SUMMARY'
            """
        )

        customer_view_count = cursor.fetchone()[0]

        if customer_view_count != 1:
            raise RuntimeError("CUSTOMER_SUMMARY view was not found")

        print("Deployment validation passed.")

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()