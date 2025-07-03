#Dockerfile

From python:3.9-slim
WORKDIR /Myapps
COPY . .
RUN pip install -r requirements.txt 
EXPOSE 5001
CMD ["python", "app.py"]
