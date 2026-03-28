# 🧠  Analytics Pipeline (Cancer Data Project)

## 📘 Project Overview
This project implements a **complete automated data analytics pipeline** inside a **Docker environment**.  
It processes cancer dataset features — performing **data ingestion, preprocessing, analytics, visualization, and clustering** automatically.  
The pipeline demonstrates how machine learning and data analytics can be combined in a reproducible, containerized workflow.

---

## 👥 Team Members
1. **Mohamed Wanis**
2. **Hazem Gamal Muhammed**
3. **Ali Sameh Abdelaal**

---

 ## 🐳 Docker Build & Run Commands
 ```bash
  # Build the Docker image
 docker build -t csci461-customer-analytics:latest .

 # Run the container
 docker run -it --name csci461_run -v $(pwd):/app/pipeline csci461-customer-analytics:latest

 # Execute the main pipeline
 python ingest.py /app/pipeline/cancer_data.xlsx

 # (Optional) Run summary script
 chmod +x summary.sh
 ./summary.sh csci461_run

```
### Execution Flow
## 1️⃣ Build the Docker Image
 ```bash
  docker build -t csci461-customer-analytics:latest .

```

## 2️⃣ Run the Container
 ```bash
 docker run -it --name csci461_run -v $(pwd):/app/pipeline csci461-customer-analytics:latest


```
##  3️⃣ Execute the Pipeline
 ```bash
python ingest.py /app/pipeline/cancer_data.xlsx
 ```

## 🔁 Pipeline Flow
 ```bash
cancer_data.xlsx
      ↓
ingest.py → creates data_raw.csv
      ↓
preprocess.py → cleans & saves data_preprocessed.csv
      ↓
analytics.py → generates insights (3 text files)
      ↓
visualize.py → saves plots (.png)
      ↓
cluster.py → creates clusters.txt

 ```

## 📂 Results Location
 ```bash
/app/pipeline/results

 ```
