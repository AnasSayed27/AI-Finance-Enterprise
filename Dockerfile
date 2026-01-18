FROM python:3.10-slim

WORKDIR /app

# 1. Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy the entire project
COPY . .

# 3. Fix Line Endings for run.sh (Safety for Windows Users)
# This converts Windows text format to Linux format automatically
RUN sed -i 's/\r$//' run.sh
RUN chmod +x run.sh

# 4. Expose ports (8000 for Internal API, 8501 for Public UI)
EXPOSE 8000
EXPOSE 8501

# 5. Run the script
CMD ["./run.sh"]