# Ethereum Transactions

A Django application for importing, storing, and managing Ethereum transactions.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. **Clone the repository**:

    **Using HTTPS:**
    ```bash
    git clone https://github.com/your-username/eth_transactions.git
    ```

    **Using SSH:**
    ```bash
    git clone git@github.com:your-username/eth_transactions.git
    ```

    Then navigate to the project directory:
    ```bash
    cd eth_transactions/eth_transactions
    ```

2. **Build and start the Docker containers**:
    ```bash
    docker compose up -d
    ```

3. **Access the Django application**:
    Open your web browser and go to `http://localhost:8000/admin/`.

### Creating Django Admin User
1. navigate to the eth_transactions directory containing Makefile
2. run the super_user command
    ```bash
    make super_user
    ```
3. enter the username, email and password as prompted
3. login to django admin and view the Transactions model (should have no data)

### Loading the CSV
1. navigate to the eth_transactions directory containing Makefile
2. run the load_csv command
    ```bash
    make load_csv
    ```

### CRUD with Django Admin
1. login to Django Admin, view the Transactions model

### Stopping the Application

1. **Stop the running containers**:
    ```bash
    docker-compose down
    ```

