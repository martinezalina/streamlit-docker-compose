# Dockerized Streamlit App

### Prototyping a user interface with Streamlit and docker-compose

Sometimes we need to resolve very quickly a delivery or we have to validate a protopyte.

The objective of this project is to provide an interface that allows to a person (who don't handle Conda or Jupyter Notebook) select an xls, process its content and obtain the result needed.

Here we go!

> Note: This is a project based on [this one](https://github.com/martinezalina/streamlit-docker).
> The **difference** is that here I used **docker compose**. Why?... This variant, among other things, allows us to see the results of the code while we are coding without the need to do a ´docker ps´, ´docker stop container id´, ´docker build´, etc. In other words, it saves us **a lot of time**.

### Run the app

The first time the project is used, the following commands should be run:

1. Build container:
   `docker-compose build`

2. Run container:
   `docker-compose up -d`

3. You can now view your Streamlit app in your browser http://localhost:8501

4. Browse to upload the xls file and select the example file located ./example/

5. Download the new file generated width the transform

6. To shut down container:
   `docker-compose down`

## Additional Information

#### Stack

- Docker
- Docker-Compose
- Python
- Streamlit
- Pandas
- openpyxl
- xlrd

#### Dependency documentation

- https://docs.streamlit.io/
- https://docs.streamlit.io/en/stable/streamlit_configuration.html
- https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
