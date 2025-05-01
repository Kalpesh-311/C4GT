# Protean Plus Insight Chatbot

## Overview
Protean Plus Insight Chatbot is an intelligent, multilingual chatbot designed to provide real-time insights from KPI data. It integrates Natural Language Processing (NLP), vector databases, and large language models (LLMs) to answer user queries related to business KPIs and data. This system uses a REST API architecture and provides a dynamic dashboard for real-time updates.

## High-Level Architecture


## Features
- **Multilingual Support**: Supports multiple languages including Hindi, Marathi, and English. 
- **KPI Querying**: Users can query KPIs like sales, revenue, and stockouts.
- **Real-Time Dashboard**: Provides live graphs and metrics with drill-down capabilities.
- **AI-powered Insights**: Uses LLM (e.g., OpenChat, LLaMA 2) for natural language answers based on the user's query.
- **Role-Based Access Control**: Different user roles (Admin, Manager, Executive) with specific access levels.
- **Audit Logs**: Logs every query and response for tracking and auditing purposes.

## Tech Stack

| **Component**        | **Tech Stack**                                             |
|----------------------|------------------------------------------------------------|
| **Backend APIs**      | Python + FastAPI                                           |
| **Frontend (Dashboard)** | ReactJS + Recharts                                      |
| **Vector Database**   | Milvus / Weaviate                                          |
| **Embedding Model**   | Sentence-Transformers multilingual                         |
| **LLM**               | LLaMA 2 / OpenChat                                         |
| **Language tools**    | Indic NLP, Muril                                           |
| **Hosting**           | AWS/GCP, Docker                                            |
| **Security**          | JWT, RBAC, SSL                                             |

## Setup

### Prerequisites

1. Python 3.x
2. Node.js (for the React frontend)
3. Docker (for containerization)
4. A cloud account (AWS/GCP) for hosting the application

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Kalpesh-311/Protean-Plus.git
