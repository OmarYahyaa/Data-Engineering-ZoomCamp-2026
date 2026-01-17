# 1.2 — Docker + Postgres Notes

## Prerequisites
1. GitHub account to use CodeSpaces
2. Python installed
3. Docker installed

## Key concepts
### What is CodeSpaces? 
- It's a development environment that's hosted in the cloud.
- Each codespace you create is hosted by GitHub in a Docker container, running on a virtual machine.
- By default, the codespace development environment is created from an Ubuntu Linux image
- You can connect to your codespaces from your browser, from Visual Studio Code, or by using GitHub CLI.
- Reference: [Link](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces)
### 2) What is Docker?
- Docker is an open platform for developing, shipping, and running applications.
- Docker enables you to separate your applications from your infrastructure.
- Reference: [Link1](https://docs.docker.com/get-started/docker-overview/) [Link2](https://www.geeksforgeeks.org/devops/introduction-to-docker/)

## Commands
> [!NOTE]
>Bash is case senstive.
```bash
# Check Python version
python -V
python --version

# Overwrites your entire bash configuration and simplifies your terminal prompt
echo 'PS1="> "' > ~/.bashrc

# Check for docker installation
docker

# Run an image to test our docker connection
docker run hello-world

# Interact with docker image
dcoker run -it ubuntu

#
```

