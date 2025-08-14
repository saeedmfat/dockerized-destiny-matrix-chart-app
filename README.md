# Destiny Matrix Chart App 🌌

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/docker-3.8-yellow.svg)](https://docker.com)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](LICENSE)
![GitHub Last Commit](https://img.shields.io/github/last-commit/saeedmfat/dockerized-destiny-matrix-chart-app)



## ✨ Key Features

- **Precise Calculations**: Life Path, Expression & Soul Urge numbers
- **Full DevOps Pipeline**: CI/CD with GitHub Actions
- **Real-time Monitoring**: Prometheus + Grafana dashboard
- **Scalable Infrastructure**: Kubernetes-ready
- **Secure**: JWT Authentication (Coming Soon)

## 🚀 30-Second Deployment

```bash
# Clone with DevOps configs
git clone --branch devops https://github.com/saeedmfat/dockerized-destiny-matrix-chart-app.git
cd dockerized-destiny-matrix-chart-app

# Deploy with Observability
docker-compose -f docker-compose.prod.yml up -d
```

## 🌐 API Endpoints

| Endpoint | Method | Sample Request |
|----------|--------|----------------|
| `/api/calculate` | POST | `{"birth_day":15, "birth_month":3, "birth_year":1992}` |
| `/health` | GET | - |
| `/metrics` | GET | Prometheus Format |

```json
// Sample Response
{
  "life_path_number": 3,
  "interpretation": "Creative, expressive, social",
  "calculation_steps": "Day(15)→6 + Month(3)→3 + Year(1992)→21 = 30→3"
}
```

## 🛠️ Tech Stack Deep Dive

### Core Components
<div align="center">

| Layer | Technology | Version |
|-------|------------|---------|
| **API Framework** | FastAPI | 0.109+ |
| **Database** | PostgreSQL | 15 |
| **Monitoring** | Prometheus + Grafana | Latest |
| **Containerization** | Docker + Compose | 3.8+ |
| **Orchestration** | Kubernetes (Optional) | 1.28+ |

</div>

## 📊 Live Monitoring (Screenshots)

![Grafana Dashboard](https://raw.githubusercontent.com/saeedmfat/dockerized-destiny-matrix-chart-app/main/docs/grafana.png)

Access locally:
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000` (admin/admin)

## 🧑‍💻 Developer Guide

### Project Structure
```
dockerized-destiny-matrix-chart-app/
├── backend/               # FastAPI app
│   ├── app/              # Core logic
│   └── tests/            # Pytest cases
├── monitoring/           # Prometheus configs
├── k8s/                  # Kubernetes manifests
├── docker-compose.yml    # Dev config
├── docker-compose.prod.yml # Production
└── README.md
```

### Contribution Flow
```mermaid
graph LR
    A[Fork] --> B[Branch]
    B --> C[Code]
    C --> D[Test]
    D --> E[PR]
```

## 📜 License
MIT © [Saeed Marefat](https://github.com/saeedmfat)

## 🌟 Special Thanks
[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge)](https://buymeacoffee.com/saeedmfat)
