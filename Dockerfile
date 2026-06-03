FROM python:3.11-slim

WORKDIR /app

# Copiamo prima il file dei requisiti e installiamo Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamo tutto il resto del codice
COPY . .

# Apriamo la porta 5000 per far passare il traffico web dell'API
EXPOSE 5000

CMD ["python", "app.py"]