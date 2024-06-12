import streamlit as st
import snowflake.connector as sc
import pandas as pd

def main():
    st.write("#### Dashboard d'affichage des données de la table des etudiants")

    try:
        # Connect to Snowflake
        con = sc.connect(
            account='fcbzjch-ts19004',
            user='ALISAAD1',
            password='ALI123ali@'
        )
        cursor = con.cursor()

        # Function to fetch student data
        def dataEtudiants():
            sql = "SELECT * FROM RCW.PERSONS.PERSONS"
            cursor.execute(sql)
            rows = cursor.fetchall()

            # Define column names as per your table schema
            column_names = [desc[0] for desc in cursor.description]
            return pd.DataFrame(rows, columns=column_names)

        # Fetch data and display it
        donnees = dataEtudiants()
        st.write(donnees)

    except sc.Error as e:
        st.warning(f"Une erreur est survenue: {e}")
    except Exception as e:
        st.warning(f"Une erreur inattendue est survenue: {e}")
    finally:
        # Ensure the connection is closed
        try:
            con.close()
        except:
            pass

if __name__ == "__main__":
    main()
