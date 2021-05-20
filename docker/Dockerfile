FROM python:3.9

RUN pip install --upgrade pip
RUN pip install \
    streamlit \
    sweat \
    httpx \
    bokeh \
    arrow

RUN mkdir /app
WORKDIR /app
COPY . /app/

ENV PORT 8501
EXPOSE 8501

CMD streamlit run --server.enableCORS false --server.port=8501 main.py
