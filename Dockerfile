FROM python:3.11-slim

WORKDIR /app

# System deps for torch
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install the topogpt3 package
COPY . .
RUN pip install --no-cache-dir -e .

EXPOSE 7860

CMD ["python", "gradio_app.py"]
