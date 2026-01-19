# Glossary — Module 01 (Docker, Postgres, GCP, Terraform)

## GitHub Codespaces
A cloud-hosted development environment (VS Code + Linux VM) that can come preconfigured with tools like Docker.

## .gitignore
A file that tells Git which files/folders to exclude from tracking and commits, helping keep the repo clean by ignoring generated files (caches) and sensitive/local files (e.g., `.env`, keys, large datasets).


## Docker
A platform for building, shipping, and running applications in containers.

## Docker daemon (dockerd)
The background service that builds, runs, and manages containers, images, networks, and volumes.

## Docker CLI
The `docker` command-line tool you use to communicate with the Docker daemon.

## Image
A packaged template/snapshot that contains everything needed to run an application.

## Container
A running instance of an image.

## Tag
A version label for an image (e.g., `postgres:16`, `python:3.12-slim`).

## Docker Hub (Registry)
A place where Docker images are stored and downloaded from (e.g., pulling `postgres`).

## `docker run`
Command to create and start a container from an image.

## Interactive mode (`-it`)
Runs a container interactively with a terminal attached (e.g., `docker run -it ubuntu bash`).

## Auto-remove (`--rm`)
Removes the container automatically when it stops (useful for temporary runs).

## Environment variables (`-e`)
Key-value settings passed into a container (commonly used to configure Postgres user/password/db).

## Bind mount
A mount type that maps a **specific folder/file from the host machine** directly into a container.

## Port mapping (`-p HOST:CONTAINER`)
Exposes a container port to your machine so you can access it via `localhost:<host_port>`.

## Localhost (host vs container)
`localhost` inside a container refers to that container itself, not your laptop/host machine.

## Volume (persistence)
Storage that keeps data even if the container is removed/recreated (critical for databases).

## Bind mount (`-v /host/path:/container/path`)
Maps a folder from your machine into the container (share files between host and container).

## Docker network
A virtual network that allows containers to communicate with each other.

## Service name / Container name
A name used to reach a container on the same Docker network (instead of using `localhost`).

## PostgreSQL (Postgres)
A relational database often used in data engineering.

## Postgres container
Running PostgreSQL as a Docker container instead of installing it locally.




