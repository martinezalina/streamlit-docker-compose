FROM python:3.8


RUN mkdir /code
WORKDIR /code

ADD /requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /code/
EXPOSE 8501

CMD streamlit run src/app.py

#ENTRYPOINT ["streamlit", "run"]
#CMD ["app.py"]