import sqlite3
from flask import Flask
from flask import jsonify, request
from flask_marshmallow import Marshmallow
import pymysql
from pymysql import Error, cursors

app = Flask(__name__)


def db_connexion():
    conn = None
    try:
      conn = pymysql.connect(
    host="localhost",
    database="prj_flask",
    user="root",
    password="primatologue",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)
    except pymysql.error as e:
        print(e)
    return conn


@app.route("/api/article", methods=['GET', 'POST'])
# Ajouter les articles
def ajouter_article():
    conn = db_connexion()
    cursor = conn.cursor()
    # A) Consulter tous les articles.
    if request.method == 'GET':
       reque = "SELECT * FROM article"
       cursor.execute(reque)
       article = [
            dict(id=row['id'], nom=row['nom'],description=row['description'], prix=row['prix'], quantite=row['quantite'])
            for row in cursor.fetchall()
        ]
       if article is not None:
            return jsonify(article)
        
    #C) Ajouter un article
    if request.method == 'POST':
        new_nom = request.form.get('nom')
        new_description = request.form.get('description')
        new_prix = request.form.get('prix')
        new_quantite = request.form.get('quantite')
        

        sql_query = """ INSERT INTO article ( nom, description, prix, quantite)
        VALUES (%s,%s,%s,%s)"""
        cursor.execute(sql_query, ( new_nom, new_description, new_prix, new_quantite))
        conn.commit()
        return f"L'Article: {cursor.lastrowid} a été bien crée", 201

        

@app.route("/api/recherche_article_par_nom", methods=['GET'])
#F) Rechercher un article par mot clé
def rechercher_article_nom():
    conn = db_connexion()
    cursor = conn.cursor()
    if request.method == 'GET':
       
        new_nom = request.form.get('nom')
        select_query = "SELECT * FROM article WHERE nom = %s"
        cursor.execute(select_query, (new_nom))
        result = cursor.fetchall()
        if result:
            return jsonify(result)
             
             
        else:
           return "Aucun enrégistrement de ce id"
        
@app.route("/api/recherche_article_par_id", methods=['GET'])
#B)Consulter un article par son id.
def rechercher_article_id():
    conn = db_connexion()
    cursor = conn.cursor()
    if request.method == 'GET':
       
        new_id = request.form.get('id')
        select_query = "SELECT * FROM article WHERE id = %s"
        cursor.execute(select_query, (new_id))
        result = cursor.fetchall()
        if result:
            return jsonify(result)
             
             
        else:
           return "Aucun enrégistrement de ce nom"
          
@app.route("/api/Update_article", methods=['PUT'])
#D) Modifier un article.
def update_arcticle():
    conn = db_connexion()
    cursor = conn.cursor()
    if request.method == 'GET':
       
        new_id = request.form.get('id')
        nom = request.form.get('nom')
        description = request.form.get('description')
        prix = request.form.get('prix')
        quantite = request.form.get('quantite')
        update_query = "UPDATE article SET nom = %s, description = %s ,prix = %s , quantite = %s WHERE id = %s"
        cursor.execute(update_query, (nom, description, prix, quantite , new_id))       
        conn.commit()
    return f"L'Article: a été bien crée", 201


@app.route("/api/Delete_article", methods=['DELETE'])
#E) Supprimer un article.
def delete_arcticle():
    conn = db_connexion()
    cursor = conn.cursor()
    if request.method == 'GET':
       
        new_id = request.form.get('id')
        
        update_query = "DELETE FROM article WHERE id = %s"
        cursor.execute(update_query, ( new_id))       
        conn.commit()
    return f"L'Article: a été bien supprimé", 201
  

             
@app.route("/api/recherche_categorie", methods=['GET'])
def rechercher_categorie_nom():
    conn = db_connexion()
    cursor = conn.cursor()
    if request.method == 'GET':
       
        new_nom = request.form.get('nom')
        select_query = "SELECT * FROM categorie WHERE nom = %s"
        cursor.execute(select_query, (new_nom))
        result = cursor.fetchall()
        if result:
            return jsonify(result)
             
             
        else:
           return "Aucune Categorie enrégistrement en ce nom"            
        
 
@app.route("/api/Update_categorie", methods=['PUT'])
def update_categorie():
    conn = db_connexion()
    cursor = conn.cursor()
    if request.method == 'GET':
       
        new_id = request.form.get('id')
        nom = request.form.get('nom')
        
        update_query = "UPDATE article SET nom = %s WHERE id = %s"
        cursor.execute(update_query, (nom , new_id))       
        conn.commit()
    return "Categorie Modifié"


@app.route("/api/Delete_categorie", methods=['DELETE'])
def delete_categorie():
    conn = db_connexion()
    cursor = conn.cursor()
    if request.method == 'GET':
       
        new_id = request.form.get('id')
        
        update_query = "DELETE FROM categorie WHERE id = %s"
        cursor.execute(update_query, ( new_id))       
        conn.commit()
    return "Categorie Supprimé"

@app.route("/api/categorie", methods=['GET', 'POST'])
def ajouter_categorie():
    conn = db_connexion()
    cursor = conn.cursor()
    # Lister les Catégories
    if request.method == 'GET':
       reque = "SELECT * FROM categorie"
       cursor.execute(reque)
       categorie = [
            dict(id=row['id'], nom=row['nom'])
            for row in cursor.fetchall()
        ]
       if categorie is not None:
            return jsonify(categorie)
    # Enregistrer les catégories
    if request.method == 'POST':
       
        new_nom = request.form.get('nom')
        select_query = "SELECT * FROM categorie WHERE nom = %s"
        cursor.execute(select_query, (new_nom))
        result = cursor.fetchone()
        if result:
              
             return jsonify({'message': 'L\'enregistrement existe déjà'})
        else:
            sql_query = """ INSERT INTO categorie (nom)
            VALUES (%s)"""
            cursor.execute(sql_query, (new_nom))
            conn.commit()
            return f"La categorie: {cursor.lastrowid} a été bien crée", 201

    
      


if __name__ == "__main__":
    app.run(debug=True)
