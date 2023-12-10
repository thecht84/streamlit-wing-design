
FROM python:3.11-slim-bullseye

WORKDIR /opt/st-wing-design/

RUN apt-get update && apt-get install -y \
    zsh \
    libgl1-mesa-glx \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /opt/st-wing-design/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app/app.py"]
