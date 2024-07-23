Chess Tournament Management System
This project is a Django-based application for managing chess tournaments. The system allows administrators to create tournaments, manage participants, generate pairings based on the Swiss-system rules, and update match results. Regular users can view tournament details and rankings but have restricted access to management features.


Copy code
git clone https://github.com/yourusername/chess_tournament_management_system.git
cd chess_tournament_management_system
Environment Variables

Create a .env file in the project root with the following variables:

env
Copy code
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=chess_db
DATABASE_USER=chess_user
DATABASE_PASSWORD=chess_password
DATABASE_HOST=db
DATABASE_PORT=5432
Build and Run the Docker Containers

sh
Copy code
docker-compose up --build
Apply Migrations

sh
Copy code
docker-compose exec web python manage.py migrate
Create a Superuser

sh
Copy code
docker-compose exec web python manage.py createsuperuser
Access the Application

The application should be running at http://localhost:8000.

Running the Application
To start the application, use Docker Compose:

sh
Copy code
docker-compose up
This will start the Django development server and a PostgreSQL database.

API Endpoints
Here are the key API endpoints for managing the chess tournament system:

User Authentication
POST /api/token/: Obtain JWT token.
POST /api/token/refresh/: Refresh JWT token.
Tournaments
GET /api/tournaments/: List all tournaments.
POST /api/tournaments/: Create a new tournament (Admin only).
GET /api/tournaments/{id}/: Retrieve a specific tournament.
PUT /api/tournaments/{id}/: Update a specific tournament (Admin only).
DELETE /api/tournaments/{id}/: Delete a specific tournament (Admin only).
Matches
GET /api/matches/: List all matches.
POST /api/matches/: Create a new match (Admin only).
GET /api/matches/{id}/: Retrieve a specific match.
PUT /api/matches/{id}/: Update a specific match (Admin only).
DELETE /api/matches/{id}/: Delete a specific match (Admin only).
Rankings
GET /api/rankings/: List all rankings.
GET /api/filtered-rankings/: Filter rankings by tournament_id and/or participant_id.
Pairings
POST /api/generate-pairings/{tournament_id}/: Generate pairings for a tournament (Admin only).
Running Tests
To run the tests, use the following command:

sh
Copy code
docker-compose exec web python manage.py test
This will run all the unit tests defined in the project.

Contributing
We welcome contributions! Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
