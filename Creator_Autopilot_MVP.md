# Creator Autopilot MVP

### (Instagram Reels + YouTube)

------------------------------------------------------------------------

# 1️⃣ Team Split (2 Engineers, Equal Load)

## 👨‍💻 Engineer A --- Platform Backend + Data + Auth

Owns the product backend that the web app and n8n talk to.

### Responsibilities

1.  Auth + workspace\
2.  DB schema + migrations\
3.  Core REST API (content, templates, scheduling, posts, analytics)\
4.  Media storage service (S3/R2/GCS) + public URL generation for IG\
5.  Webhook endpoints for n8n callbacks + job state machine\
6.  Observability: logs, errors, audit trail

### Deliverables

-   Backend service running with DB + migrations\
-   API docs (OpenAPI/Swagger)\
-   Storage pipeline working (upload → asset record → public URL)\
-   Clean status transitions:\
    planned → generating → needs_review → approved → scheduled →
    publishing → posted / failed\
-   Webhook receivers for n8n: `/webhooks/n8n/...`

------------------------------------------------------------------------

## 👨‍💻 Engineer B --- Integrations + n8n Orchestration + Platform APIs

Owns execution via n8n and all external API integrations.

### Responsibilities

1.  n8n instance setup (secure, env vars, secrets)\
2.  Token usage strategy (safe token handling)\
3.  Meta Reels publish workflow (container → publish)\
4.  YouTube resumable upload workflow\
5.  Analytics sync workflows (IG + YT metrics pull)\
6.  Generation workflow skeleton (planner/judge/generator placeholders
    first)\
7.  Retry + idempotency strategy inside workflows

### Deliverables

-   n8n workflows:
    -   content.publish\
    -   analytics.sync\
    -   content.generate (stub → real)\
-   Working publishing to:
    -   Instagram Reels (Meta Graph API)\
    -   YouTube (resumable upload)\
-   Callbacks to backend with results + errors

------------------------------------------------------------------------

# 2️⃣ Backend-First Build Plan

## Phase 0 --- Contract First

### Status Machine

planned\
generating\
needs_review\
approved\
scheduled\
publishing\
posted\
failed

### Required Webhooks

-   POST /webhooks/n8n/content-generated\
-   POST /webhooks/n8n/content-published\
-   POST /webhooks/n8n/analytics-synced

------------------------------------------------------------------------

# 3️⃣ Milestones

### Milestone 1 (End Day 5)

Upload → schedule → publish → backend shows posted

### Milestone 2 (End Day 8)

OAuth publish without manual tokens

### Milestone 3 (End Day 12)

Analytics sync + dashboard endpoints

### Milestone 4 (Week 3+)

planner → generator → judge → approve → schedule → post

------------------------------------------------------------------------

# 🔟 Immediate Next Actions

## Engineer A

-   DB schema + migrations\
-   Auth endpoints\
-   Storage presign endpoints\
-   Minimal Content CRUD

## Engineer B

-   n8n setup + secure\
-   content.publish.instagram workflow\
-   Backend webhook integration test
