# 1.1 — Introduction (Launch Stream) Notes

## Goal
Understand the course structure, prerequisites, homework/project workflow, and how to succeed in the ZoomCamp.

## What this session covers
- Course structure + where to find everything (GitHub repo + course docs)
- Prerequisites and how to self-check readiness
- Logistics: homework, leaderboard, learning in public, FAQ contributions
- Certificate requirements (project + peer review)
- Q&A highlights (AI usage, tools flexibility, cloud/local options)

## Key concepts

### 1) Where the course lives
- **GitHub repo is the main gateway**: modules are organized in folders (01…06 + workshops + project).
- Each module has a **README** that contains the links to videos, resources, and homework instructions.

### 2) Prerequisites (Important)
- Be comfortable with **programming basics**: CLI, loops, conditionals.
- Know **some SQL** (there is a refresher, but starting from zero will be hard).
- The course is **not fully beginner-friendly**; the “test” is Module 01: if you can get Docker working (or debug it), you’re ready.

### 3) Cohort-specific materials
- Cohort-specific content (homework links/streams/FAQ for 2026) is stored under a **2026 folder** in the repo.

### 4) Homework workflow
- Homeworks are **optional**, used to test your knowledge.
- Submission is typically **multiple-choice** via the course management platform.
- You often need to submit a **GitHub URL** pointing to your work folder.

### 5) Certificate requirements
- **Project is required** (not optional if you want the certificate).
- You submit your project + do **peer review** for other projects (e.g., review 3 peers).

### 6) Learning in public (Extra points)
- Sharing what you learned (LinkedIn/Twitter/etc.) gives **extra points**.
- GitHub notes alone count, but sharing publicly increases visibility and opportunities.

### 7) FAQ contributions
- If you find/improve answers, you can contribute via GitHub (edit/create issue → PR flow).

### 8) Tools vs concepts
- The course teaches **concepts**, tools are used to demonstrate them.
- You *can* use other tools (AWS/Azure/Airflow), but the course team may not support troubleshooting outside the official stack.

### 9) Dataset used in the course
- The course uses the **NYC Taxi dataset** across modules (messy/realistic).
- Some materials use CSV backups; newer data may be in parquet—links are in docs/materials.

## Action checklist (What I should do now)
- [ ] Star the official course repo (helps visibility + easy bookmark)
- [ ] Read the course docs pages: prerequisites → getting started → resources → logistics
- [ ] Open Module 01 README and follow it in order
- [ ] Create my personal course repo and keep work organized per module
- [ ] Submit homework using my GitHub folder URL (when required)
- [ ] Decide: cloud (GCP) or local-only path (local is allowed, Terraform may be skipped)

## Q&A takeaways
- Using AI is OK **if you understand every line** you submit/use.
- If you lack prerequisites, it’s better to build fundamentals first, then reattempt.
- Projects + learning in public can improve visibility; applying early helps understand interview gaps.
> [!IMPORTANT]
> Key information users need to know to achieve their goal.
> Advanced topics (from previous cohort Q&A)
> - Modern lakehouse table formats: **Delta Lake** / **Apache Iceberg**.
> - **dbt at scale:** prefer **incremental models** over full refresh for large datasets.
> - **Streaming engines:** Spark is common; **Flink** is often chosen for lower-latency use cases.
> - **Governance & catalogs:** lineage/metadata/ownership (e.g., DataHub / Unity Catalog).
> - **Python performance:** alternatives like **Polars** may be used instead of pandas in some teams.

> Source question (timestamp): [Watch the Q&A](https://youtu.be/X8cEEwi8DTM?list=PL3MmuxUbc_hJZdpLpRHp7dg6EOx828q6y&t=4146)

## References
- [Course GitHub repo](https://github.com/DataTalksClub/data-engineering-zoomcamp)
- [Course documentation site](https://datatalks.club/docs/courses/data-engineering-zoomcamp/)
- [Course management site](https://courses.datatalks.club/de-zoomcamp-2026/)
- [NYC Taxi dataset](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [FAQ site](https://datatalks.club/faq/data-engineering-zoomcamp.html)



