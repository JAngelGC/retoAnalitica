FROM gitpod/workspace-base
RUN sudo apt-get update
RUN sudo apt-get install python3-pip
USER gitpod
RUN pip install pandas
RUN pip install seaborn