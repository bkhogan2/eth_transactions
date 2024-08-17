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
    cd eth_transactions
    ```

2. **Build and start the Docker containers**:
    ```bash
    docker-compose up -d
    ```

3. **Access the Django application**:
    Open your web browser and go to `http://localhost:8000`.

### Loading the CSV
1. navigate to the eth_transactions directory containing manage.py
2. run the load_csv management command
    ```bash
    python manage.py load_csv /path/to/your/csv
    ```

### Stopping the Application

1. **Stop the running containers**:
    ```bash
    docker-compose down
    ```

