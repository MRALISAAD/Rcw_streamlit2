FROM python:3.9-slim

WORKDIR /app

COPY ./requirement.txt /app

RUN pip install --no-cache-dir --requirement /app/requirement.txt

COPY ./ /app/

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]