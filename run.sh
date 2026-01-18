#!/bin/bash

# 1. Start FastAPI in the background (&) on port 8000
echo "Starting API..."
uvicorn src.main:app --host 0.0.0.0 --port 8000 &

# 2. Start Streamlit in the foreground on the port Render provides ($PORT)
echo "Starting Frontend..."
streamlit run src/frontend.py --server.port $PORT --server.address 0.0.0.0