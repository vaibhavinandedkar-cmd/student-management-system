#!/bin/bash

# Student Management System - Startup Script
# Usage: ./start.sh [dev|prod|docker]

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Student Management System${NC}"
echo -e "${GREEN}========================================${NC}"

# Parse arguments
MODE=${1:-dev}

case $MODE in
  dev)
    echo -e "${YELLOW}Starting in DEVELOPMENT mode...${NC}"
    
    # Activate virtual environment
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
    fi
    
    source venv/bin/activate
    
    # Install dependencies
    echo "Installing dependencies..."
    pip install -r requirements.txt > /dev/null 2>&1 || true
    
    # Initialize database if needed
    if [ ! -f ".db_initialized" ]; then
        echo "Initializing database..."
        python init_db.py
        python seed_db.py
        touch .db_initialized
    fi
    
    # Set environment variables
    export FLASK_ENV=development
    export FLASK_DEBUG=1
    export PORT=${PORT:-5001}
    
    echo -e "${GREEN}✓ Starting Flask development server${NC}"
    echo -e "${GREEN}  URL: http://127.0.0.1:$PORT/dashboard${NC}"
    echo ""
    
    python run.py
    ;;
    
  prod)
    echo -e "${YELLOW}Starting in PRODUCTION mode...${NC}"
    
    # Activate virtual environment
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
    fi
    
    source venv/bin/activate
    
    # Install dependencies
    echo "Installing dependencies..."
    pip install -r requirements.txt > /dev/null 2>&1 || true
    
    # Set environment variables
    export FLASK_ENV=production
    export FLASK_DEBUG=0
    export PORT=${PORT:-5001}
    
    echo -e "${GREEN}✓ Starting Gunicorn server${NC}"
    echo -e "${GREEN}  URL: http://0.0.0.0:$PORT${NC}"
    echo ""
    
    gunicorn -c gunicorn_config.py run:app
    ;;
    
  docker)
    echo -e "${YELLOW}Starting with Docker Compose...${NC}"
    
    # Check if Docker is installed
    if ! command -v docker-compose &> /dev/null; then
        echo -e "${RED}Error: Docker Compose is not installed${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✓ Building and starting containers${NC}"
    docker-compose up -d
    
    echo -e "${GREEN}Waiting for services to be ready...${NC}"
    sleep 5
    
    echo -e "${GREEN}✓ Services started successfully${NC}"
    echo -e "${GREEN}  Web UI: http://localhost/dashboard${NC}"
    echo -e "${GREEN}  PostgreSQL: localhost:5432${NC}"
    echo ""
    echo -e "${YELLOW}Useful commands:${NC}"
    echo "  docker-compose logs -f web     # View app logs"
    echo "  docker-compose logs -f db      # View database logs"
    echo "  docker-compose down            # Stop all services"
    echo "  docker-compose ps              # Show running containers"
    ;;
    
  *)
    echo -e "${RED}Unknown mode: $MODE${NC}"
    echo -e "${YELLOW}Usage: ./start.sh [dev|prod|docker]${NC}"
    echo ""
    echo "  dev    - Start development server with Flask (port 5001)"
    echo "  prod   - Start production server with Gunicorn"
    echo "  docker - Start with Docker Compose"
    exit 1
    ;;
esac
