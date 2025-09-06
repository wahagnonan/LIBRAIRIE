# Portfolio Django – SORO Wahagnona Jean

Ce projet est un portfolio web développé avec Django, permettant de présenter mes compétences, expériences, projets et formations. Il inclut également une fonctionnalité pour que les clients puissent soumettre un projet via un formulaire, dont les données sont enregistrées dans la base de données et consultables dans l’interface d’administration.

## Fonctionnalités principales

- **Page d’accueil personnalisée** : Présentation, compétences, expériences, projets récents, formations, langues et centres d’intérêt.
- **Bouton de soumission de projet** : Un bouton bien visible sur la page d’accueil permet aux visiteurs de soumettre un projet.
- **Formulaire de soumission** : Les clients peuvent remplir un formulaire (nom, email, titre du projet, description) accessible via `/soumettre-projet/`.
- **Stockage en base de données** : Les projets soumis sont enregistrés dans la base de données SQLite.
- **Consultation dans l’admin Django** : Les projets soumis sont visibles et gérables dans l’interface d’administration.

## Installation et utilisation

1. **Cloner le dépôt**
	```bash
	git clone https://github.com/wahagnonan/LIBRAIRIE.git
	cd LIBRAIRIE/PortFolio
	```
2. **Installer les dépendances**
	```bash
	pip install django
	```
3. **Appliquer les migrations**
	```bash
	python manage.py makemigrations
	python manage.py migrate
	```
4. **Lancer le serveur**
	```bash
	python manage.py runserver
	```
5. **Accéder au site**
	- Page d’accueil : [http://localhost:8000/](http://localhost:8000/)
	- Formulaire de projet : [http://localhost:8000/soumettre-projet/](http://localhost:8000/soumettre-projet/)

## Structure du projet

- `PortFolio/` : Projet Django principal
- `core/` : Application Django contenant les modèles, vues et formulaires
- `templates/` : Templates HTML (base.html, submit_project.html, project_submitted.html)
- `static/` : Fichiers statiques (CSS, images)

## Auteur

SORO Wahagnona Jean
Contact : jeansoro303@gmail.com
LinkedIn : https://linkedin.com/in/jean-soro
GitHub : https://github.com/wahagnonan