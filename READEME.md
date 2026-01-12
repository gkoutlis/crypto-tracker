# 🚀 Crypto-Tracker: The Pulse of the Market 🪙

Welcome to my first serious engineering playground! This isn't just a script; it's a fully containerized backend engine that hunts for crypto prices while we sleep. 😴💻

### 🛠 The "Under the Hood" Stuff (Technical)
* **Automated Data Ingestion:** A Python-based service that polls the CoinGecko API for real-time BTC, ETH, and ADA prices.
* **Relational Persistence:** Leverages a **MariaDB 10.6** instance to store price history with structured precision.
* **Infrastructure as Code:** Orchestrated via **Docker Compose**, separating the database, the UI (phpMyAdmin), and the logic into isolated networks.
* **Security Ops:** Zero hardcoded secrets! Everything is injected via environment variables for a "production-ready" posture.

### 🎮 Why it's Cool (The Fun Part)
* **Set it & Forget it:** Run `docker compose up -d` and watch your database grow 📈.
* **Ubuntu Powered:** Developed and tested on **Ubuntu 24.04 LTS**, because we love the terminal life 🐧.
* **Expert-in-the-Making:** This is Step 1 of my journey to becoming a Data Science and Prompt Engineering master.

---
"In code we trust, everything else we track." ₿
