# Glossary — Module 01 (Docker & Terraform)

## Docker daemon (dockerd)
**Definition:** The background service that builds, runs, and manages containers, images, networks, and volumes.  
**Why it matters:** Your `docker` CLI commands talk to the daemon to do the actual work.  
**Example:** `docker info` shows daemon details.

## Docker CLI
**Definition:** The `docker` command-line tool you use to interact with the Docker daemon.  
**Why it matters:** It’s the main interface for running containers and managing images.  
**Example:** `docker ps`

## Image
**Definition:** A packaged snapshot/template containing everything needed to run an application.  
**Why it matters:** Containers are created from images.  
**Example:** `postgres:16`

## Container
**Definition:** A running instance of an image.  
**Why it matters:** This is what actually runs your application/service.  
**Example:** `docker run postgres:16`

## Port mapping
**Definition:** Exposing a container’s port to your machine using `HOST:CONTAINER`.  
**Why it matters:** Lets you connect via `localhost:<port>` from your host.  
**Example:** `-p 5432:5432`

## Volume (persistence)
**Definition:** A storage mechanism to keep data even if the container restarts or is recreated.  
**Why it matters:** Postgres data would otherwise be lost when the container is removed.  
**Example:** `-v pgdata:/var/lib/postgresql/data`

## Docker network
**Definition:** A virtual network that allows containers to communicate with each other.  
**Why it matters:** Containers can connect using container/service names instead of `localhost`.  
**Example:** connect to Postgres host `pgdatabase`

## Docker Compose
**Definition:** A tool to define and run multi-container applications using `docker-compose.yml`.  
**Why it matters:** One command can start Postgres + pgAdmin together.  
**Example:** `docker compose up -d`
