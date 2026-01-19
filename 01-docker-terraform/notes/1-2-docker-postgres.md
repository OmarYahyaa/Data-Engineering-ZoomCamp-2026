# 1.2 — Docker + Postgres Notes

## Goal
Build an end-to-end local data-engineering workflow using Docker: run Postgres in containers, ingest data into the database, use pgAdmin for inspection, and manage services cleanly with Docker Compose (using Codespaces for a consistent environment).


## Prerequisites
1. GitHub account 
2. Python installed
3. Docker installed

## Key concepts
### Docker fundamentals
- **Isolation:** A container is isolated from your host machine, so actions inside the container don’t affect your system.
- **Image vs Container:** An image is a snapshot/template; a container is a running instance created from that image.
- **Stateless by default:** Containers don’t preserve changes by default; when you rerun from the same image, you typically start “fresh” again.
### Volumes
- **Volume (-v):** Map a host folder into a container so files can be accessed from both sides (and to preserve data).
### Postgres with Docker
- **Environment variables (-e):** Used to configure containers (e.g., Postgres user/password/database).
- **Port mapping (-p HOST:CONTAINER):** Expose a container port to your machine (so localhost:<port> forwards into the container).
### Networking
- **Localhost confusion:** When multiple containers need to talk, they must be on the same Docker network and connect using the container/service name (not localhost).
### Docker Compose
- **Compose = multiple services in one file:** A docker-compose.yml defines everything needed to run Postgres + pgAdmin together.
- **Same network by default:** Services in the same compose file run on the same default network and can reach each other by service name (e.g., pgdatabase).

## Deep Understanding
### VM vs Docker vs Codespaces
![VM vs Docker vs Codespaces](assets/vm-vs-docker-vs-codespaces.png)
- **VM (VirtualBox):** Full guest OS → heavier, strong isolation.
- **Docker:** Shared host kernel via Docker daemon → lightweight, fast.
- **Codespaces:** Cloud VM (hidden) + containerized dev env → consistent Linux setup.

## Practice with instructor

## Commands & Shortcuts
> [!NOTE]
> - Bash is case senstive.
> - Put flags/tags right after the command (before the package names), so it’s clear they apply to the command.

| Command | Description |
| :---: | --- |
| `python -V` <br> `python --version` | Check Python version |
| `apt update` | Refreshes your system’s package lists (downloads the latest info about available updates) |
| `apt install -y python3` | Installs Python 3 using apt, and -y auto-answers yes to prompts (so it installs without asking) |
| `echo 'PS1="> "' > ~/.bashrc` | Overwrites your entire bash configuration and simplifies your terminal prompt |
| `source ~/.bashrc` | Reloads your .bashrc in the current terminal, applying changes immediately |
| `cp /etc/skel/.bashrc ~/.bashrc` | Copies the system’s default .bashrc from /etc/skel/ into your home directory,<br> making your ~/.bashrc the default one. |
| `docker` | Prints the help/usage text for docker (proves the Docker CLI is installed and runnable) |
| `dcoker run hello-world` | Does an end-to-end Docker test |
| `dcoker run -it ubuntu` | Starts a new container from the ubuntu image and gives you an interactive terminal inside it |
| `docker run -it python:3.9.16` | Starts an interactive container from the Python 3.9.16 image<br>- `-slim` install light Python version<br>- `--rm` auto-deletes container when you exit<br>- `--entrypoint=bash` forces the container to start with bash instead of the image’s default command |
| `docker ps -a` | Lists all containers (running and stopped) |
| `docker ps -aq` | Lists only the container IDs for all containers (running and stopped) |
| `docker rm $(docker ps -aq)`| Removes all containers |

| Shortcut | Description |
| --- | --- |
| `Ctrl + D` | EOF (end-of-file), logs you out / closes the current shell (if the line is empty). |

## Gotchas / Warnings
> [!CAUTION]
> Dont use `rm -rf /` on your computer as it attempts to delete everything on the machine, including critical system files, and can render the OS unbootable (data loss), But you can use it inside docker container as it isolated from your system.

> [!CAUTION]
> `>` overwrites `.bashrc`. Use `>>` to append safely. ( `echo 'PS1="> "' >> ~/.bashrc` )

## New terms
- [GitHub Codespaces](GLOSSARY.md#github-codespaces)
- [.gitignore](GLOSSARY.md#gitignore)
- [Docker](GLOSSARY.md#docker)
- [Docker daemon](GLOSSARY.md#docker-daemon)
- [Docker CLI](GLOSSARY.md#docker-cli)
- [Image](GLOSSARY.md#image)
- [Container](GLOSSARY.md#container)
- [Bind mount](GLOSSARY.md#bind-mount)
- [Volume](GLOSSARY.md#volume)

## References
- [GitHub CodeSpaces Explained](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces)
- [Docker Explained](https://docs.docker.com/get-started/docker-overview/)












