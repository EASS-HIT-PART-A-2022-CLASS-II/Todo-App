FROM python:3.9

#RUN pip install fastapi
#RUN pip install "uvicorn[standard]"

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY ./app /code/app


EXPOSE 8080

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8080"]
