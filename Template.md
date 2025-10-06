# Smart Advisor Blueprint

> An intelligent course planner that helps Civil Engineering students find the perfect courses and professors based on their unique learning preferences.
> _Maintained by **Kanishkar Manoj**_


![screenshot placeholder](./docs/screenshot.png)


## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Quickstart](#quickstart)
- [Environment Variables](#environment-variables)
- [Scripts](#scripts)
- [Testing / Linting / Format](#testing--linting--format)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [Maintainers](#maintainers)
- [License](#license)


## Overview
Smart Advisor Blueprint is a web application designed to simplify the course selection process for Civil Engineering students at our university, who currently lack an official course flowchart. By analyzing user preferences and academic history, it provides personalized recommendations for courses and professors. The outcome is a perfectly tailored semester schedule that aligns with the student's learning style and academic goals, presented in an intuitive, easy-to-use interface.


## Features
- **Automated Transcript Analysis:** Simply upload your unofficial transcript to automatically populate your academic history and completed courses.
- **In-Depth Preference Profile:** Fine-tune your recommendations by specifying your ideal class and professor style, including:
    - **Grading Style:** (e.g., test-heavy, project-based, homework-focused)
    - **Attendance Policy:** (e.g., mandatory, optional, lecture recordings available)
    - **Teaching Style:** (e.g., theoretical, hands-on, group project oriented)
    - **Pace & Difficulty:** (e.g., fast-paced, heavy workload, light reading)
    - **Professor Attributes:** (e.g., gives good feedback, tough grader, accessible outside class)
- **Smart Course & Professor Matching:** Receive a tailored list of courses and professors that fit your unique academic needs and learning style.
- **Interactive Schedule Builder:** Browse your personalized recommendations, save your favorites, and build your ideal semester schedule in one place.


## Tech Stack
- **Frontend:** React
- **Backend:** Flask
- **DB:** Postgres
- **Infra:** Vercel, Render, GitHub Actions


## Getting Started


### Prerequisites
- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/en/) (v18.x or newer)
- [Python](https://www.python.org/) (v3.10.x or newer)
- (Optional) [Docker Desktop](https://www.docker.com/products/docker-desktop/) if you want containerized development.


### Quickstart
```bash
# 1. Clone the repository
git clone [https://github.com/kanishkarmanoj/SmartAdvisors.git](https://github.com/kanishkarmanoj/SmartAdvisors.git)
cd SmartAdvisors

# 2. Install Backend Dependencies (Python)
# Create a virtual environment and activate it
python -m venv .venv
source .venv/bin/activate
# Install required packages
pip install -r requirements.txt # Make sure you have a requirements.txt file

# 3. Install Frontend Dependencies (Node.js)
# This assumes your package.json is in the root or a /client folder
npm install

# 4. Run the Development Servers
# In your first terminal, run the Backend (Flask)
flask --app server run --debug # Change 'server' to the name of your main python file

# In a second terminal, run the Frontend (React)
npm run dev