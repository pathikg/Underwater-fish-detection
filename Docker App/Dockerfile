FROM python:3.7-slim

RUN pip install -U pip

WORKDIR /app

COPY . ./

RUN pip install -r ./requirements.txt

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run", "streamlit_app.py" ]