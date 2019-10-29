# Start from the ubuntu image
FROM ubuntu:18.04

# Install and configure Apache server
RUN apt-get update --fix-missing
RUN apt-get install --fix-missing
RUN apt-get -y install python3.6
RUN apt-get -y install python3-pip
RUN pip3 install pandas
RUN apt-get -y install apache2

# Set cgi
COPY ./apache2.conf /etc/apache2/apache2.conf
COPY ./serve-cgi-bin.conf /etc/apache2/conf-available/serve-cgi-bin.conf
RUN cd /etc/apache2/mods-enabled
RUN a2enmod cgi
RUN ln -s ../mods-available/cgi.load
CMD apachectl -D FOREGROUND


# Copy our code to this image
#COPY ./source_code /var/www/html/
COPY ./html/. /var/www/html/
COPY ./cgi-bin/. /var/www/cgi-bin/

# Set Permissions
RUN chmod -R 777 /var/www/

# Install python2 and pandas
