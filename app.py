from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemple de données - à remplacer par une base de données plus tard
data = []


# Endpoint pour publier un article
@app.route('/api/publier', methods=['POST'])
def publier_article():
    article = request.get_json()
    data.append(article)
    return jsonify({"message": "Article publié avec succès!"}), 201


# Endpoint pour récupérer les articles
@app.route('/api/articles', methods=['GET'])
def get_articles():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
