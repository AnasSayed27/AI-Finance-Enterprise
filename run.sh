echo "Starting API..."
uvicorn src.main:app --host 0.0.0.0 --port 8000 &

echo "Starting Frontend..."
streamlit run src/frontend.py --server.port $PORT --server.address 0.0.0.0