#!/bin/bash

# Remplace par l'URL réelle de ton API (par exemple : http://127.0.0.1:5000 pour un serveur local)
API_URL="http://127.0.0.1:5000"

# Test de connexion avec des données valides
echo "==> Testing login with valid credentials..."
curl -X POST "$API_URL/login" \
     -H "Content-Type: application/json" \
     -d '{"email": "test@example.com", "password": "testpassword"}'
echo -e "\n"

# Test de connexion avec des données invalides
echo "==> Testing login with invalid credentials..."
curl -X POST "$API_URL/login" \
     -H "Content-Type: application/json" \
     -d '{"email": "wrong@example.com", "password": "wrongpassword"}'
echo -e "\n"

# Test avec des données manquantes
echo "==> Testing login with missing fields..."
curl -X POST "$API_URL/login" \
     -H "Content-Type: application/json" \
     -d '{"email": "test@example.com"}'
echo -e "\n"
