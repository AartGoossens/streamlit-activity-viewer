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

ENV PORT 8080
EXPOSE 8080

CMD streamlit run --server.enableCORS false --server.port=8080 main.py
