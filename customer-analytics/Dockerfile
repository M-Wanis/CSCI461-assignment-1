
FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1


WORKDIR /app/pipeline/


RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential git curl \
    && rm -rf /var/lib/apt/lists/*


COPY . /app/pipeline/


RUN python -m pip install --upgrade pip && \
    pip install pandas numpy matplotlib seaborn scikit-learn scipy requests openpyxl


RUN mkdir -p /app/pipeline/results

WORKDIR /app/pipeline/


CMD ["/bin/bash"]
