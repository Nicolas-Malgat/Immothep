# Immothep

La société Immothep, nouveau fleuron de l'immobilier Français, souhaite créer un module d'estimation de biens basé sur l'intelligence artificielle pour enrichir sa plateforme et acquérir de nouveaux acheteurs/vendeurs.

### Les contraintes

Vous devrez fournir un seul **Jupyter Notebook** (vous pouvez cependant avoir plusieurs fichiers Python en support de votre fichier Jupyter .ipynb).

Le web service (ou API) devra être en python et répondre au contrat suivant :

**Url de la requête**

GET sur l'url http://localhost:5003/api/estimate (en local sur votre machine)

**Paramètres de la requête**

- metre_carre : le nombre de m² habitables loi Carrez
- nb_pieces : nombre de pièces principales
- terrain : le nombre de m² du terrain
- code_postal : le code postal où se trouve le bien

**Retour de la requête**

Le retour de la requête devra contenir au minimum l'estimation dans un format JSON

```JSON
{ "estimation": "130 000€" }
```


L'API pourra utiliser n'importe quel Framework. Par défaut, vous pouvez utiliser  **[Fast Api](https://fastapi.tiangolo.com)**  dont la documentation est fournie.


---
Pour choisir votre modèle d'apprentissage, un article (qui contient un cheat sheet) est aussi fourni. Il est  **recommandé d'utiliser le package Scikit Learn  **pour ce développement**.

### [Aide pour choisir le modèle](https://towardsdatascience.com/the-beginners-guide-to-selecting-machine-learning-predictive-models-in-python-f2eb594e4ddc)