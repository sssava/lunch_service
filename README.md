## How to start a project
1. create and activate virtual environment
2. add .env file with variables: SECRET_KEY, DEBUG, NAME, USER, PASSWORD,
HOST, PORT
3. run in terminal command docker compose up and open in your browser localhost/< routes api.urls>

### URLS:
1. api/users/create/ ALLOWED METHODS: POST. You can create restaurant or employee
2. api/menu/ ALLOWED METHODS: GET, POST Restaurant can post menu or employees can get daily menu and results
3. api/votes ALLOWED METHODS: GET, POST Employees can vote for menu
4. api/token ALLOWED METHODS: POST Users can get authentication token
5. api/token/refresh/ ALLOWED METHODS: POST Users can get refresh token

