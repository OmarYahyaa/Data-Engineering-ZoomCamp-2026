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

## Docker Hub
A place where Docker images are stored and downloaded from (e.g., pulling `postgres`).

## Bind mount
A mount type that maps a **specific folder/file from the host machine** directly into a container.

## Volume
Storage that keeps data even if the container is removed/recreated (critical for databases).








