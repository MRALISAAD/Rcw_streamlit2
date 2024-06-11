
import streamlit as st
import snowflake.connector as sc
import pandas as pd

def main():
    st.write("#### Dashboard d'affichage des données de la table des etudiants")


    try:
        con = sc.connect (
            account='fcbzjch-ts19004',
            user='ALISAAD1',
            password='ALI123ali@'
        )

    
        cursor = con.cursor()


        def dataEtudiants():
            sql = "SELECT * FROM rcw.persons.etudiants"
            df = cursor.execute(sql).fetchall()

            return pd.DataFrame(df,columns=['NOM','PRENOM','AGE'])
        
        donnees = dataEtudiants()

        st.write(donnees)

    except:
        st.warning("Une erreur est survenue")








if __name__ == "__main__":
    main()