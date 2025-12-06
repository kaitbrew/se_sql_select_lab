import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

df_first_five = pd.read_sql("""
                            SELECT employeeNumber, lastName
                            FROM employees
                            """,conn)


df_five_reverse = pd.read_sql("""
                              SELECT lastName, employeeNumber
                              FROM employees    
                              """,conn)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""
                       """,conn)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
                       """,conn)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""
                       """,conn)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""
                       """,conn)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""
                       """,conn)

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""
                       """,conn)