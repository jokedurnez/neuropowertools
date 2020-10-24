FROM continuumio/conda-ci-linux-64-python3.8
RUN mkdir $HOME/code
WORKDIR $HOME/code

# get dependencies
COPY environment.yml $HOME/code/
COPY ../* $HOME/code/
RUN conda config --set restore_free_channel true
RUN conda config --append channels conda-forge
RUN conda env create --name neuropower -f environment.yml
RUN echo "source activate neuropower" >> ~/.bashrc

