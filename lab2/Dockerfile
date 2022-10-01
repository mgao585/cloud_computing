FROM python:3.10.7
USER root
RUN pip3 install jupyter
ENV JUPYTER_USER mgao
RUN useradd -m $JUPYTER_USER;

EXPOSE 8888

RUN mkdir home/$JUPYTER_USER/jupyter_notebook;\
    cd home/$JUPYTER_USER/jupyter_notebook;\
    chown ${JUPYTER_USER} .;\
    wget 'https://raw.githubusercontent.com/mschermann/forensic_accounting/master/Introduction.ipynb';

USER ${JUPYTER_USER}
CMD jupyter notebook --ip=0.0.0.0 --port 8888

COPY requirements.txt .
RUN pip install -r requirements.txt


#sources:
#https://docs.docker.com/engine/reference/builder/#environment-replacement
#https://faun.pub/set-current-host-user-for-docker-container-4e521cef9ffc
#https://smallbusiness.chron.com/give-permissions-ubuntu-33174.html
