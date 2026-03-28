# **Names Of Team Work In This Project:**
**1)Mohamed Wanis**
**2)Hazem Gamal Muhammed**
**3)Ali Sameh Abdelaal**
# 

# **all Docker build / run commands used.**



docker build -t csci461-customer-analytics:latest .

docker run -it --name csci461\_run -v $(pwd):/app/pipeline csci461-customer-analytics:latest

python ingest.py /app/pipeline/cancer\_data.xlsx

chmod +x summary.sh

./summary.sh csci461\_run

# **execution flow**



#### 1\. Build the Docker Image

docker build -t csci461-customer-analytics:latest .

#### 2\. Run the Container

docker run -it --name csci461\_run -v $(pwd):/app/pipeline csci461-customer-analytics:latest

#### 3\. Execute the Pipeline

python ingest.py /app/pipeline/cancer\_data.xlsx

#### Pipeline Flow

cancer\_data.xlsx

      ↓

ingest.py → creates data\_raw.csv

      ↓

preprocess.py → cleans \& saves data\_preprocessed.csv

      ↓

analytics.py → generates insights (3 text files)

      ↓

visualize.py → saves plots (.png)

      ↓

cluster.py → creates clusters.txt



#### Results Location

/app/pipeline/results

##### Contents:



data\_raw.csv — raw converted data



data\_preprocessed.csv — cleaned data



insight1.txt, insight2.txt, insight3.txt — analytical insights



all\_features\_hist.png, correlation\_heatmap.png — visualizations



clusters.txt — K-Means cluster counts





#### **Screen Shots**

