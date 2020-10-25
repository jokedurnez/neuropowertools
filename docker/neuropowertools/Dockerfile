FROM continuumio/conda-ci-linux-64-python3.8
WORKDIR /code/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD entrypoint.sh .

# install psycopg2 dependencies
USER root
RUN apt-get update \
    && apt-get install -y postgresql gcc python3-dev musl-dev

# get dependencies
COPY docker/neuropowertools/environment.yml /code/
COPY . /code/
RUN conda config --set restore_free_channel true
RUN conda config --append channels conda-forge
RUN conda env create --name neuropower -f environment.yml
#RUN echo 'source activate neuropower' >> ~/.bashrc

ENTRYPOINT ["/code/entrypoint.sh"]