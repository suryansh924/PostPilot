# Creator Autopilot MVP (PostPilot)

**Automated Content Creation & Publishing for Instagram Reels and YouTube Shorts**

This repository contains the backend and orchestration logic for the Creator Autopilot MVP. The system is designed to automate the entire content lifecycle: from planning and generation to scheduling, publishing, and analytics tracking. It leverages a TypeScript backend for core business logic and **n8n** for workflow orchestration and third-party integrations.

---

## 🏗️ Architecture

The system is split into two primary components:

### 1. **Core Backend (Engineer A)**
*   **Role:** Single source of truth for data, authentication, and state management.
*   **Tech Stack:** TypeScript (Node.js), PostgreSQL (with Prisma/Drizzle), S3-compatible Storage (R2/GCS).
*   **Responsibilities:**
    *   Auth & Workspace Management.
    *   REST API for the frontend and internal tools.
    *   Content State Machine tracking.
    *   Webhook receivers for n8n callbacks.
    *   Media storage & signing.

### 2. **Integration & Orchestration (Engineer B)**
*   **Role:** Execution engine for external platforms and AI workflows.
*   **Tech Stack:** n8n (Self-hosted via Docker), Meta Graph API, YouTube Data API.
*   **Responsibilities:**
    *   **Publishing Workflows:** Handling video uploads, captions, and platform-specific API quirks.
    *   **Analytics Sync:** Periodically fetching metrics from IG & YT.
    *   **Generation Pipeline:** Coordinating AI agents (Planner -> Generator -> Judge).

---

## 🚀 Development Roadmap (12-Day Sprint)

### **Phase 0: Contracts & Strategy (Day 1)**
*   **Status Machine Definition:**
    `planned` → `generating` → `needs_review` → `approved` → `scheduled` → `publishing` → `posted` / `failed`
*   **JSON Schemas:** `plan_json`, `judge_json`, `metrics_json`.
*   **Webhook Contracts:** Standardized payloads for n8n → Backend communication.

### **Phase 1: Foundations (Days 1–2)**
*   **Backend:**
    *   Project setup (TS/Node).
    *   Database schema & migrations (Users, Workspaces, Content Items).
    *   Auth endpoints (`/auth/signup`, `/auth/login`).
    *   Storage endpoints (`/assets/presign`, `/assets/complete`).
*   **n8n:**
    *   Docker deployment with security hardening.
    *   Connectivity verification (`/webhooks/n8n/ping`).

### **Phase 2: Core APIs + Publishing (Days 3–5)**
*   **Backend:**
    *   **Content API:** CRUD for content items, approval/rejection flows.
    *   **Scheduling API:** Managing post times.
    *   **Webhooks:** Handling `content-generated` and `content-published` events.
    *   **Idempotency:** Preventing duplicate processing.
*   **n8n:**
    *   **Instagram Reel Workflow:** Container creation -> Publish -> Callback.
    *   **YouTube Upload Workflow:** Resumable upload protocol.
    *   **Unified Publish Workflow:** Routing logic with retries.

### **Phase 3: Account Connections & OAuth (Days 6–8)**
*   **Backend:**
    *   OAuth endpoints for Instagram & YouTube (`/integrations/connect`, `/integrations/callback`).
    *   Token storage & refresh logic (encrypted storage).
*   **n8n:**
    *   Updated workflows to fetch tokens dynamically from the backend instead of static env vars.

### **Phase 4: Generation Pipeline Skeleton (Days 9–10)**
*   **Backend:** "Publish from Upload" mode features.
*   **n8n:** `content.generate` skeleton with placeholders for planner, generator, and judge agents.

### **Phase 5: Analytics & Dashboard (Days 11–12)**
*   **Backend:** Aggregated analytics endpoints (`/analytics/summary`).
*   **n8n:** `analytics.sync` workflow to pull latest performance data.

---

## 🔌 API & Webhook Specifications

### **Core Endpoints**
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/auth/signup` | Create new user/workspace |
| `POST` | `/assets/presign` | Get signed URL for file upload |
| `POST` | `/content` | Create content item(s) |
| `GET` | `/content/:id` | Get content details & status |
| `POST` | `/schedule` | Schedule approved content |
| `POST` | `/integrations/youtube/connect` | Start OAuth flow |

### **n8n Webhook Receivers (Backend)**
These endpoints are called by n8n workflows to update the backend state.
*   `POST /webhooks/n8n/content-generated` (Payload: `plan`, `assets`, `judge_result`)
*   `POST /webhooks/n8n/content-published` (Payload: `platform_post_id`, `url`, `status`)
*   `POST /webhooks/n8n/analytics-synced` (Payload: `metrics_snapshot`)

---

## 🛠️ Setup & Installation

### Prerequisites
*   Node.js & npm/pnpm
*   Docker & Docker Compose (for n8n)
*   PostgreSQL Database
*   S3-compatible Object Storage

### 1. Backend Setup
```bash
# Install dependencies
npm install

# Setup Environment variables
cp .env.example .env

# Run Database Migrations
npx prisma migrate dev

# Start Development Server
npm run dev
```

### 2. n8n Setup (Docker)
```bash
# Start n8n container
docker-compose up -d n8n

# Access n8n at http://localhost:5678
```

## 👥 Team Responsibilities

| Feature Area | Engineer A (Backend) | Engineer B (Integrations) |
| :--- | :--- | :--- |
| **Data & Auth** | DB Schema, Auth API, Token Storage | - |
| **Media** | S3 Uploads, CDN URLs | - |
| **Publishing** | Status State Machine, Scheduling Logic | IG/YT API Calls, Error Handling |
| **Generation** | `content-generated` Webhook | AI Agent Chains (Planner/Judge) |
| **Analytics** | Dashboard Aggregation API | Metrics Fetching Workflows |

---

*Generated based on architectural planning document - Feb 2026*
