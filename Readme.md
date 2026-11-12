# Flask Trading API

The back end for a paper stock-trading web app, built as a project for the Coding Temple software engineering bootcamp (2023). It is a Flask REST API that handles user sign-up and login, places paper-trading orders through the [Alpaca](https://alpaca.markets/) API, returns account and position data, and serves market news. Data is stored in PostgreSQL with SQLAlchemy.

The React front end lives in a separate repository: [arou21/Trading-App](https://github.com/arou21/Trading-App).

## Features

- **Sign up and log in** — users register with name, email, and password; requests are authenticated with HTTP Basic auth (Flask-HTTPAuth).
- **Buy stock** — places a market buy order through Alpaca's paper-trading API and saves the order and transaction to the database.
- **Order history** — lists saved orders, or one order by ID.
- **Account and positions** — returns the Alpaca paper account's cash, buying power, and portfolio value, plus open positions with profit and loss.
- **Sell positions** — submits a sell order for a symbol and quantity.
- **Market news** — returns news from Alpaca's market data API.
- **Database migrations** — schema managed with Flask-Migrate (Alembic).
- **CORS enabled** so the React front end can call the API from another port.

## Getting Started

### Prerequisites

- Python 3.10 (the pinned package versions are from early 2023)
- A PostgreSQL database
- A free [Alpaca](https://alpaca.markets/) account with paper-trading API keys

### Installation

```bash
git clone https://github.com/arou21/Flask_Trading_APP.git
cd Flask_Trading_APP
python3.10 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install alpaca-py           # used by the code but not yet in requirements.txt
```

### Environment variables

Copy `.env.example` to `.env` and fill in your values:

```
FLASK_APP=run.py
SECRET_KEY=change-me
DATABASE_URL=postgresql://user:password@host:5432/dbname
ALPACA_API_KEY=your-alpaca-paper-key-id
ALPACA_SECRET_KEY=your-alpaca-paper-secret
APCA_API_KEY_ID=your-alpaca-paper-key-id
APCA_API_SECRET_KEY=your-alpaca-paper-secret
```

The `APCA_` variables repeat the same Alpaca keys. They are needed because `alpaca_trade_api.REST()` in `app/routes.py` reads them automatically. Never commit your `.env` file; it is already listed in `.gitignore`.

### Set up the database and run

```bash
flask db upgrade
flask run
```

The API runs at `http://localhost:5000`, which is where the front end expects it.

## API Endpoints

Endpoints marked **Auth** require HTTP Basic authentication (email and password).

| Method | Endpoint | Auth | Description |
| --- | --- | --- | --- |
| POST | `/api/signup` | | Create a user. JSON body: `first_name`, `last_name`, `email`, `password` |
| POST | `/api/login` | Auth | Verify credentials and return the user |
| GET | `/account` | Auth | Alpaca paper account details |
| GET | `/positions` | Auth | Open positions with current price and profit/loss |
| POST | `/api/buystock` | Auth | Place a market buy order. JSON body: `symbol`, `quantity` |
| GET | `/api/orders` | Auth | List saved orders |
| GET | `/orders/<order_id>` | Auth | Get one saved order |
| POST | `/sell-position` | Auth | Sell shares. Form fields: `symbol`, `qty` |
| GET | `/api/news` | | Market news from Alpaca |

## Data Model

| Table | Key fields |
| --- | --- |
| `user` | first and last name, email (unique), password, funds |
| `stock` | symbol, name |
| `position` | user, stock symbol, quantity, current value |
| `order` | user, stock symbol, order type, quantity, status, Alpaca order ID, transaction |
| `trade` | user, order, stock symbol, quantity, price, timestamp |
| `transaction` | user, transaction type, amount, date |

## Project Structure

```
Flask_Trading_APP/
├── app/
│   ├── __init__.py      # App setup, CORS, database, login manager
│   ├── routes.py        # All active API routes
│   ├── api/             # Earlier experiments with Alpaca and Polygon APIs (not registered)
│   └── auth/            # Earlier version of the auth routes (not registered)
├── migrations/          # Alembic database migrations
├── config.py            # Reads settings from environment variables
├── models.py            # SQLAlchemy models
├── forms.py             # WTForms forms
├── requirements.txt
└── run.py               # Entry point
```

## Built With

- [Flask 2.2](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) and [Flask-Migrate](https://flask-migrate.readthedocs.io/)
- [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/), Flask-Login, and Flask-CORS
- [PostgreSQL](https://www.postgresql.org/) (psycopg2)
- [Alpaca](https://alpaca.markets/) trading and market data APIs (`alpaca-py`, `alpaca-trade-api`)
- python-dotenv

## Known Issues and Possible Improvements

- **Passwords are stored as plain text.** Hash them with Werkzeug's `generate_password_hash` and `check_password_hash`.
- **All users share one Alpaca paper account.** Orders and positions come from a single set of API keys, and each user's `funds` value is never updated.
- **Order history isn't filtered by user.** `/api/orders` returns every user's orders.
- **Selling doesn't match the front end.** The front end calls `/sell-position` with GET and no data, while the API expects a POST with form fields. The sell order also uses the older `alpaca_trade_api` call style with a limit order and no price, so it likely fails.
- **Missing endpoints.** The front end calls `/api/watchlist` and `/stock-quotes/<symbol>`, which don't exist yet.
- **`/api/stock_data` references an undefined variable** and returns an error.
- **The app contacts Alpaca on startup.** `app/routes.py` fetches the account when it loads, so the server won't start without valid keys.
- **`alpaca-py` is missing from `requirements.txt`.**
- **Cleanup:** remove or finish the unused code in `app/api/` and `app/auth/`.