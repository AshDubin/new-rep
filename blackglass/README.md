# BlackGlass OSINT Platform

This repository contains a containerised OSINT dashboard built with FastAPI and React.

## Setup

1. Install Docker and Docker Compose.
2. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
3. Run the helper script to build and start the stack:
   ```bash
   ./scripts/run.sh
   ```

The stack includes a Celery worker, PostgreSQL, Redis, and NGINX with Certbot for HTTPS. Access the frontend at `https://localhost` once certificates are generated.
