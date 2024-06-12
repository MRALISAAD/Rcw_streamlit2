import streamlit as st
import snowflake.connector as sc

def main():
    # Dashboard Title
    st.write("#### Dashboard - Ajout dans la table des étudiants")
    
    # Database Connection
    try:
        con = sc.connect(
            account='fcbzjch-ts19004',
            user='ALISAAD1',
            password='ALI123ali@'
        )    
        cursor = con.cursor()
    except sc.Error as e:
        st.error(f"Erreur de connexion à la base de données : {e}")
        return
    
    # Input Fields for Student Information
    personid = st.text_input("Entrez l'ID de la personne :")
    lastname = st.text_input("Entrez le nom de l'étudiant :")
    firstname = st.text_input("Entrez le prénom de l'étudiant :")
    address = st.text_input("Entrez l'adresse de l'étudiant :")
    city = st.text_input("Entrez la ville de l'étudiant :")
    
    # Adding Students
    if personid and lastname and firstname and address and city:
        btnAjouter = st.button("Ajouter l'étudiant")
        if btnAjouter:
            try:
                # Parameterized Query
                sql = "INSERT INTO rcw.persons.persons (PERSONID, LASTNAME, FIRSTNAME, ADDRESS, CITY) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (personid, lastname, firstname, address, city))
                con.commit()
                st.success("L'étudiant a été ajouté avec succès !")
            except sc.Error as e:
                st.error(f"Erreur lors de l'ajout de l'étudiant : {e}")
    else:
        st.warning("Tous les champs doivent être remplis avant de pouvoir ajouter cet étudiant.")

    # Closing Database Connection
    try:
        con.close()
    except sc.Error as e:
        st.error(f"Erreur lors de la fermeture de la connexion : {e}")

if __name__ == "__main__":
    main()
