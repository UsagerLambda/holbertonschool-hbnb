# HBnB (Holberton AirBnB)

## Description

HBnB est une application de type AirBnB, structurée en trois couches (Présentation, Logique Métier et Persistance) pour gérer les utilisateurs, les lieux, les avis et les commodités. Le projet est conçu avec Flask et Flask-RESTx pour créer une API RESTful.

## Structure du Projet

```bash
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── amenities.py
│   │       ├── auth.py
│   │       ├── places.py
│   │       ├── protected.py
│   │       ├── reviews.py
│   │       ├── users.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── amenities.py
│   │   ├── baseModel.py
│   │   ├── PlaceAmenities.py
│   │   ├── places.py
│   │   ├── reviews.py
│   │   ├── users.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   │   ├── repositories/
│   │       ├── AmenityRepository.py
│   │       ├── PlaceAmenitiesRepository.py
│   │       ├── PlaceRepository.py
│   │       ├── ReviewRepository.py
│   │       ├── UserRepository.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── database/
│   ├── Amenity.sql
│   ├── data.sql
│   ├── generate_uuid.py
│   ├── initial_data.sql
│   ├── insertion_place_amenity.sql
│   ├── Place_Amenity.sql
│   ├── Place.sql
│   ├── Review.sql
│   ├── schema.sql
│   ├── script.py
│   ├── test.sql
│   ├── User.sql
├── front_end/
│   ├── add_review.html
│   ├── index.html
│   ├── login.html
│   ├── place.html
│   ├── scripts.js
│   ├── styles.css
│   ├── images/
│       ├── icon_bath.png
│       ├── icon_bed.png
│       ├── icon_wifi.png
│       ├── icon.png
│       ├── logo.png
├── instance/
│   ├── development.db
├── tests/
│   ├── conftest.py
│   ├── create_database.py
│   ├── run_test.sh
│   ├── test_01_users.py
│   ├── test_02_places.py
│   ├── test_03_reviews.py
│   ├── test_04_amenities.py
│   ├── test_05_admin.py
│   ├── test_database.sql
│   ├── utils.py
│   ├── .pytest_cache/*
├── run.py
├── config.py
├── requirements.txt
├── create_db.sh
├── run_app.sh
├── README.md
```

## Installation
### 1. Clone le dépôt:
```bash
git clone https://github.com/ton-utilisateur/hbnb.git
```
### 2. Accède au dossier du projet:
```bash
cd hbnb
```
### 3. Installe les dépendances:
```bash
pip install -r requirements.txt
```

## Utilisation
<span style="color: yellow;">(Une base de données par défaut est déjà prédéfinie, si vous souhaitez simplement tester le code.)</span>.
### Pour créer une nouvelle base de données et exécuter le serveur, lancez le fichier **create_db.sh**
```bash
./create_db.sh
```
### Pour lancer le serveur, exécutez le fichier **run_app.sh** <span style="color: green;">(Option suggérée)</span>
```bash
./run_app.sh
```

L'application sera accessible à l'adresse http://127.0.0.1:5000.

Vous pouvez accéder à l'interface de l'application en utilisant l'extension VS Code ``Live Server``. Après son installation, cliquez sur son icône en bas à droite de l'écran, puis sélectionnez le fichier ``index.html`` situé dans le dossier ``part4/front_end/``. L'application s'ouvrira ensuite dans votre navigateur.

## Login infos

### User 1
```
first_name: John
last_name: Doe
email: john.doe@mail.com
password: Pass1234
```

### User 2
```
first_name: Alice
last_name: Smith
email: alice.smith@mail.com
password: Alice2024
```

### User 3
```
first_name: Bob
last_name: Johnson
email: bob.johnson@mail.com
password: Secure
```

## Diagrammes

```mermaid
erDiagram
   USER ||--o{ PLACE : owns
   USER ||--o{ REVIEW : writes
   PLACE ||--o{ REVIEW : receives
   PLACE ||--o{ PLACE_AMENITY : contains
   AMENITY ||--o{ PLACE_AMENITY : associated_with

   USER {
       int id
       string first_name
       string last_name 
       string email
       string password
       bool is_admin
   }

   PLACE {
       int id
       string title
       string description
       float price
       float latitude
       float longitude
       int owner_id 
   }

   REVIEW {
       int id
       string text
       int rating
       int user_id
       int place_id
   }

   AMENITY {
       int id
       string name
   }

   PLACE_AMENITY {
       int place_id
       int amenity_id
   }
```
```mermaid
erDiagram
    USER ||--o{ PLACE : owns
    USER ||--o{ REVIEW : writes
    PLACE ||--o{ REVIEW : receives
    PLACE ||--o{ PLACE_AMENITY : contains
    AMENITY ||--o{ PLACE_AMENITY : associated_with
    USER ||--o{ RESERVATION : makes
    PLACE ||--o{ RESERVATION : booked_for

    USER {
        int id
        string first_name
        string last_name 
        string email
        string password
        bool is_admin
    }

    PLACE {
        int id
        string title
        string description
        float price
        float latitude
        float longitude
        int owner_id 
    }

    REVIEW {
        int id
        string text
        int rating
        int user_id
        int place_id
    }

    AMENITY {
        int id
        string name
    }

    PLACE_AMENITY {
        int place_id
        int amenity_id
    }

    RESERVATION {
        int id
        date start_date
        date end_date
        int user_id
        int place_id
    }
```
