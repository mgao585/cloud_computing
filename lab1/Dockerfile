FROM python:latest
RUN apt-get update; \
    apt-get install wget; \
    wget 'https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv'; \
    grep -o '.[A-Z]* INC' fb_sub.csv | head -1 | cut -d ' ' -f 1 | cut -d ',' -f 2 > company.txt; 
