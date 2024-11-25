// ROUTE API ================================================================================== //

const API_URL = 'http://127.0.0.1:5000/api/v1/auth/login';
const GET_ALL_PLACES = 'http://127.0.0.1:5000/api/v1/places';
const GET_PLACE = 'http://127.0.0.1:5000/api/v1/places/{place_id}'
const POST_REVIEW = 'http://127.0.0.1:5000/api/v1/reviews';
const GET_REVIEWS_FROM_PLACE = 'http://127.0.0.1:5000/api/v1/reviews/places/{place_id}';

// URL HTML =================================================================================== //

const LOGIN_PAGE_URL = 'http://127.0.0.1:5500/part4/front_end/login.html';
const INDEX_PAGE_URL = 'http://127.0.0.1:5500/part4/front_end/index.html';
const PLACE_PAGE_URL = 'http://127.0.0.1:5500/part4/front_end/place.html';
const REVIEW_PAGE_URL = 'http://127.0.0.1:5500/part4/front_end/add_review.html';

// AUTH ======================================================================================= //

// Fonction qui vérifie si l'utilisateur est loggé ou non
function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');
  if (!token) {
    loginLink.style.display = 'block';
  } else {
    loginLink.style.display = 'none';
}
}
// Fonction pour récupérer le cookie et ainsi vérifier si l'utilisateur est loggé
function getCookie(name) {
  const cookies = document.cookie.split(";");
  for (cookie of cookies) {
    if (cookie.startsWith(name + "=")) {
      return cookie.substring(name.length + 1);
    }
  }
  return null;
}

// LOGIN ====================================================================================== //

// Fonction pour gérer les cookies
function setAuthCookie(token) {
    const expiryDate = new Date();
    expiryDate.setDate(expiryDate.getDate() + 7);
    // crée un cooke avec le token et la date d'expiration disponible sur tout le site mais uniquement pour le site
    document.cookie = `token=${token}; expires=${expiryDate.toUTCString()}; path=/; SameSite=Strict`;
}

function loginLoad() {
    // Récupère le formulaire de login par son ID CSS
    const loginForm = document.getElementById('login-form');

    // si l'id existe dans la page
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // empêche le rechargement par défaut de la page après avoir submit les infos du login

            try {
                // Récupère les données du formulaire
                const formData = new FormData(event.target);
                // Envoie la requête au serveur
                const response = await fetch(API_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    // Convertit les données du formulaire en JSON
                    body: JSON.stringify({
                        email: formData.get('email'),
                        password: formData.get('password')
                    })
                });
                // Récupère la réponse du serveur en JSON
                const data = await response.json();

                // Vérifie si la connexion est réussie
                if (response.ok && data.access_token) {
                    // Sauvegarde le token dans un cookie en appelant la fonction setAuthCookie
                    setAuthCookie(data.access_token);
                    // Redirige vers la page principale
                    window.location.href = 'index.html';
                } else {
                    const errorElement = document.getElementById('error-message');
                    if (errorElement) {
                        errorElement.textContent = data.message || 'Échec de la connexion';
                        errorElement.style.display = 'block';
                    } else {
                        alert('Échec de la connexion');
                    }
                }
            } catch (error) {
                console.error('Erreur de login:', error);
                alert('Erreur lors de la connexion');
            }
        });
    }
}

// INDEX ====================================================================================== //

// inutile mais harmonise le nom des fonctions de base dans le DOMContentLoader
function indexLoad() {
  fetchPlaces();
}

// PLACES INDEX =============================================================================== //

// fonction pour récupérer la liste de places dans la DB
async function fetchPlaces() {
  try {
    // Effectue une requête API pour récupérer tous les lieux
    const response = await fetch(GET_ALL_PLACES);

    if (!response.ok) {
      throw new Error(`Erreur HTTP : ${response.status}`);
    }

    // Convertit le contenu de la réponse au format JSON et appelle une fonction pour l'afficher
    const places = await response.json();
    displayPlaces(places);
    return places;

  } catch (error) {
    console.error('Erreur de chargement des places :', error);
  }
}

function displayPlaces(places) {
  // récupère l'id "place-list" de la balise section de index.html
  const placesList = document.getElementById('places-list');
  // vide le contenu existant dans la section
  placesList.innerHTML = '';
  // boucle dans le dictionnaire "places", crée un élément div pour chaque lieu ajoute des class CSS pour le style
  // crée un attribut personnalisé pour le prix du lieu (pour le trier plus tard) et l'id de la place puis rempli le contenue HTML avec les infos du lieu
  places.forEach(place => {
    const placeElement = document.createElement('div');
    placeElement.classList.add('card', 'place-card');
    placeElement.dataset.price = place.price;
    placeElement.dataset.placeId = place.id;
    placeElement.innerHTML = `
      <h3 class="place-name">${place.title}</h3>
      <p class="place-price">Price per night: $${place.price}</p>
      <a href="place.html" class="button login-button">View Details</a>`;
    // Ajoute l'élément
    placesList.appendChild(placeElement);
  });
  priceFilter();
}

// PRICES FILTERING INDEX ===================================================================== //

function priceFilter() {
  const priceSelect = document.getElementById('price-filter'); // récup filtre
  const placeCards = document.querySelectorAll('.place-card'); // récup les cartes de lieux

  // regarde si le filtre change si oui convertie la valeur en int
  priceSelect.addEventListener('change', (event) => {
    const selectedPrice = parseInt(event.target.value); // Convertir en nombre

    placeCards.forEach(card => { // Parcourt toutes les cartes
      const placePrice = parseInt(card.dataset.price); // Récup prix stocké dans la carte du lieu

      // si le prix de la place est inférieur ou égal au prix selectionné (0 si 'All' est select)
      if (selectedPrice === 0 || placePrice <= selectedPrice) {
        card.style.display = 'block'; // affiche la carte
      } else { // sinon
        card.style.display = 'none'; // cache la carte
      }
    });
  });
}

// PLACE ====================================================================================== //

function placeLoad() {
  console.log("place")
}

// REVIEW ===================================================================================== //

function reviewLoad() {
  console.log("review")
}

// LOADER ===================================================================================== //

document.addEventListener('DOMContentLoaded', () => {
  checkAuthentication();
    if (window.location.href === LOGIN_PAGE_URL) {
      loginLoad();
  }

    if (window.location.href === INDEX_PAGE_URL) {
      indexLoad();
  }

    if (window.location.href === PLACE_PAGE_URL) {
      placeLoad();
  }

    if (window.location.href === REVIEW_PAGE_URL) {
      reviewLoad();
  }
});
