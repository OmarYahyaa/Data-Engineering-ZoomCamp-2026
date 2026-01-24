# Bind mount practice (Host folder ↔ Container)

## Goal
Practice Docker **bind mounts** by mounting a host folder into a container and running a Python script that reads files from the mounted directory.

## What this demonstrates
- `-v /host/path:/container/path` maps a **real host folder** into the container.
- Editing files on the host is reflected instantly inside the container (great for development).
- Using `--rm` keeps the environment clean by removing the container on exit.

## Project structure
- `test/`
  - `file1.txt`, `file2.txt`, `file3.txt`
  - `script.py` (lists files + prints file contents)

## Run
From this folder:

```bash
cd 01-docker-terraform/src/bind-mount-practice

docker run -it --rm \
  -v "$(pwd)/test:/app/test" \
  --entrypoint=bash \
  python:3.9.16-slim
```
Inside the container:
```bash
cd /app/test
python script.py
```

