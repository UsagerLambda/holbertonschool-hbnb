document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const errorMessage = document.getElementById('error-message');
  const loadingIndicator = document.getElementById('loading-indicator');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = document.getElementById('email').value.trim();
      const password = document.getElementById('password').value.trim();

      errorMessage.style.display = 'none';
      errorMessage.textContent = '';
      loadingIndicator.style.display = 'block';

      try {
        await loginUser(email, password);
      } catch (error) {
        loadingIndicator.style.display = 'none';
        errorMessage.style.display = 'block';
        errorMessage.textContent = error.message;
      }
    });
  }
});

async function loginUser(email, password) {
  const apiUrl = 'http://127.0.0.1:5000/login';

  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    });

    if (response.ok) {
      const data = await response.json();

      document.cookie = `token=${data.access_token}; path=/; Secure; SameSite=Strict`;
      window.location.href = 'index.html';
    } else {
      const errorData = await response.json();
      throw new Error('Login failed. Please try again.' || errorData.message);
    }
  } catch (error) {
    console.log(error);
    throw new Error(error);
  }
}


function getCookie(name) {
  const cookies = document.cookie.split('; ');
  for (const cookie of cookies) {
      const [key, value] = cookie.split('=');
      if (key === name) return value;
  }
  return null;
}

function checkAuthentication() {
  const token = getCookie('token');
  const loginButton = document.querySelector('.login-button');

  if (!token) {
      loginButton.style.display = 'block';
  } else {
      loginButton.style.display = 'none';
      fetchPlaces(token);
      getPlaceIdFromURL();
    }
}

async function getPlaceIdFromURL() {
  const queryString = window.location.search;
  const token = getCookie("token");

  const urlParams = new URLSearchParams(queryString);
  const id = urlParams.get('id');
  if(id)
    fetchPlaceDetails(token, id);
  else
    console.error("ID Not found");
  
}
async function fetchPlaceDetails(token, placeId) {
  try {
    const response = await fetch('http://127.0.0.1:5000/places/' + placeId, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
        },
    });

    if (response.ok) {
        const place = await response.json();
        displayPlaceDetails(place);
    } else {
        console.error('Failed to fetch places:', response.statusText);
    }
} catch (error) {
    console.error('Error fetching places:', error);
}
}

function generateStars(rating) {
  let stars = '';
  for (let i = 1; i <= 5; i++) {
      if (i <= rating) {
          stars += '★';
      } else {
          stars += '☆';
      }
  }
  return stars;
}

function displayPlaceDetails(place) {
  console.log(place);
  const placeInfo = document.getElementById('place-info');
  const placeName = document.getElementById('main-title');

  if(placeInfo) {
    placeInfo.innerHTML = `
      <p><strong>Host:</strong> ${place.host_name}</p>
      <p><strong>Price per night:</strong> $${place.price_per_night}</p>
      <p><strong>Description:</strong> ${place.description}</p>
      <p><strong>Amenities:</strong> ${place.amenities}</p>
    `;
  }

  const reviewList = document.getElementById("reviews");
  reviewList.innerHTML = "<h2>Reviews</h2>";
  place.reviews.forEach(review => {
      const placeCard = document.createElement('div');
      placeCard.className = 'review-card';
      placeCard.innerHTML = `
          <p><strong>${review.user_name}:</strong> ${review.comment}</p>
          <p>Rating: ${generateStars(review.rating)}</p>
                `;
      reviewList.appendChild(placeCard);
  });
  if(placeName) {
    placeName.innerHTML = place.description
  }
}



async function fetchPlaces(token) {
  try {
      const response = await fetch('http://127.0.0.1:5000/places', {
          method: 'GET',
          headers: {
              'Authorization': `Bearer ${token}`,
              'Content-Type': 'application/json',
          },
      });

      if (response.ok) {
          const places = await response.json();
          displayPlaces(places);
      } else {
          console.error('Failed to fetch places:', response.statusText);
      }
  } catch (error) {
      console.error('Error fetching places:', error);
  }
}


function displayPlaces(places) {
  const placesList = document.getElementById('places-list');
  if(placesList) {
    placesList.innerHTML = '';

    places.forEach(place => {
        const placeCard = document.createElement('div');
        placeCard.className = 'place-card';
        placeCard.innerHTML = `
            <h2>${place.description}</h2>
            <p>Price per night: $${place.price_per_night}</p>
            <button class="details-button" onclick="window.location.href='place.html?id=${place.id}'">View Details</button>
        `;
        placesList.appendChild(placeCard);
    });
  }
}


function filterPlacesByPrice() {
  const selectedPrice = document.getElementById('price-filter').value;
  const places = document.querySelectorAll('.place-card');

  places.forEach(place => {
      const priceText = place.querySelector('p').textContent;
      const price = parseInt(priceText.replace('Price per night: $', ''));

      if (selectedPrice === 'all' || price <= parseInt(selectedPrice)) {
          place.style.display = 'block';
      } else {
          place.style.display = 'none';
      }
  });
}


if(document.getElementById('price-filter'))
  document.getElementById('price-filter').addEventListener('change', filterPlacesByPrice);

document.addEventListener('DOMContentLoaded', () => {
  checkAuthentication();
});


document.addEventListener('DOMContentLoaded', async () => {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const placeId = urlParams.get('id');

  if (placeId) {
      try {
          const response = await fetch(`/places/${placeId}`);
          if (response.ok) {
              const place = await response.json();
              displayPlaceDetails(place);
          } else {
              console.error("Place not found");
              document.getElementById('place-info').innerHTML = "<p>Place not found.</p>";
          }
      } catch (error) {
          console.error("Error fetching place details:", error);
      }
  } else {
      console.error("No place ID provided in the URL");
  }
});

function displayPlaceDetails(place) {
  const placeInfo = document.getElementById('place-info');
  const placeName = document.getElementById('main-title');

  if (placeInfo) {
      placeInfo.innerHTML = `
          <p><strong>Host:</strong> ${place.host_name}</p>
          <p><strong>Price per night:</strong> $${place.price_per_night}</p>
          <p><strong>Description:</strong> ${place.description}</p>
          <p><strong>Amenities:</strong> ${place.amenities.join(", ")}</p>
      `;
  }

  if (placeName) {
      placeName.textContent = place.description;
  }

  const reviewsList = document.getElementById('reviews-list');
  if (reviewsList) {
      place.reviews.forEach(review => {
          const reviewCard = document.createElement('div');
          reviewCard.className = 'review-card';
          reviewCard.innerHTML = `
              <p><strong>${review.user_name}:</strong> ${review.comment}</p>
              <p>Rating: ${generateStars(review.rating)}</p>
          `;
          reviewsList.appendChild(reviewCard);
      });
  }
}

function generateStars(rating) {
  let stars = '';
  for (let i = 1; i <= 5; i++) {
      stars += i <= rating ? '★' : '☆';
  }
  return stars;
}

