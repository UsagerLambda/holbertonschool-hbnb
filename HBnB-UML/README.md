# HBnB - HolbertonBnB Project

This repository contains the implementation of **HBnB**, a web-based platform inspired by AirBnB. The project includes several features like user registration, place creation, review submission, and fetching a list of places, all while following a clean architecture and best practices.

## Table of Contents
- [Project Overview](#project-overview)
- [Architecture](#architecture)
  - [Sequence Diagrams](#sequence-diagrams)
  - [Class Diagrams](#class-diagrams)
  - [Layered Architecture](#layered-architecture)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Authors](#authors)

---

## Project Overview

The **HBnB** project is a system that allows users to:
- Register and manage their profile.
- Create and list places.
- Leave reviews for places.
- View places and reviews from other users.

It follows a **layered architecture** to separate concerns, with an emphasis on security, data validation, and error handling. Key components include an API for communication between the user interface and business logic, and a database that stores user, place, and review data.

---

## Architecture

### Sequence Diagrams

The project follows a typical web-based architecture where:
- **User** interacts with the **API** to send requests such as `register()`, `createPlace()`, and `leaveReview()`.
- The **API** layer handles requests, authenticates users, and forwards the information to the **Business Logic Layer**.
- The **Business Logic Layer** manages operations like data encryption, data validation, and database interactions.
- The **Database** stores user information, places, reviews, and amenities.

Key HTTP response codes and errors handled:
- **HTTP 201**: Successful creation of resources.
- **HTTP 200**: Successful retrieval of data.
- **Error 409**: Conflict in data (e.g., duplicate entries).
- **Error 400**: Bad request (invalid data or syntax).

If you want to take a look at our [Sequence Diagram](https://www.zupimages.net/up/24/40/nblh.jpg)

### Class Diagrams

The system includes the following main classes:
- **User**: Handles registration, profile updates, and deletion.
- **Place**: Manages place creation, deletion, and listing.
- **Review**: Allows users to create, update, and list reviews.
- **Amenity**: Stores amenities associated with places.

Each class has corresponding attributes like `id`, `created_at`, and methods for CRUD operations.

If you want to take a look at our [Class Diagram](https://www.zupimages.net/up/24/40/fgdd.jpg)

### Layered Architecture

The project is built using a **layered architecture** pattern:
1. **Presentation Layer**: Interfaces for User, Place, Review, and Amenity.
2. **Business Logic Layer**: Implements the core logic for managing users, places, reviews, and amenities.
3. **Database Layer**: Handles database operations through repositories (`UserRepository`, `PlaceRepository`, etc.).

The **Facade Pattern** is used between the presentation and business logic layers to simplify the interaction and provide a unified interface.

Here is an example of our Layered Architecture:

![Layered Architecture](https://www.zupimages.net/up/24/40/zgs2.jpg)
---

## Features

- **User Registration**: Register with an email, username, and password.
- **Profile Management**: Update and delete user profiles.
- **Place Creation**: Create, list, and delete places.
- **Review Submission**: Leave reviews for places.
- **Amenity Management**: Add and update amenities for places.
- **Error Handling**: Comprehensive error handling with specific exceptions for invalid inputs (e.g., `InvalidEmailException`, `InvalidReviewException`).

---

## Installation

To run the **HBnB** project locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hbnb.git

2. Navigate into the project directory:
```bash
cd HBnB-UML
```

## Authors

This project is being done by [Nour Chaouch](https://github.com/NChaouch/), [Clement Chassemon](https://github.com/UsagerLambda) and [Florian Bombeeck](https://github.com/Pandor3)
