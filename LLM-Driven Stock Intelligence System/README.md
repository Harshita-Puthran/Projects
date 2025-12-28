# LLM-Powered Stock Decision Intelligence System

This project implements an end-to-end decision intelligence pipeline that combines
quantitative stock market indicators with Large Language Model (LLM) reasoning.

## What this project does
- Fetches historical stock data via FastAPI
- Engineers technical indicators (MA, volatility, returns)
- Uses an LLM to generate explainable financial analysis
- Converts LLM reasoning + signals into actionable decisions
- Applies confidence-aware risk and position sizing

## Key Highlights
- Explainable AI (no black-box predictions)
- Faithfulness checks to prevent hallucinations
- Decision intelligence beyond raw analytics
- Designed for real-world deployment

## Tech Stack
- Python, Pandas, NumPy
- FastAPI (REST endpoints)
- HuggingFace Transformers (LLM inference)
- Decision & risk engines
