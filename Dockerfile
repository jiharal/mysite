FROM python:3.8.6-alpine

RUN apk --update --no-cache add apache2 apache2-dev wget ca-certificates make gcc musl-dev

ADD . /mysite

WORKDIR /mysite
RUN pip3 install pyarmor
RUN pip3 install django
ADD _pytransform.so /usr/local/lib/python3.8/site-packages/pyarmor/platforms/linux/x86_64/
RUN pyarmor obfuscate --src="." -r --output=/app mysite/wsgi.py
RUN mv ../app /home/apache

ENV PYTHON_VERSION=3.8
ENV MOD_WSGI_VERSION=4.7.1
ENV MOD_WSGI_SRC_URL="https://github.com/GrahamDumpleton/mod_wsgi/archive/${MOD_WSGI_VERSION}.tar.gz"

RUN wget -O /usr/src/mod_wsgi.tar.gz "${MOD_WSGI_SRC_URL}" && \
    tar -zxvf /usr/src/mod_wsgi.tar.gz -C /usr/src && \
    rm /usr/src/mod_wsgi.tar.gz



WORKDIR /usr/src/mod_wsgi-${MOD_WSGI_VERSION}

ENV CFLAGS="-I/usr/local/include/python${PYTHON_VERSION}m/ -L/usr/local/lib/"
RUN ln -s /usr/lib/libpython${PYTHON_VERSION}m.so /usr/lib/libpython${PYTHON_VERSION}.so && \
    ./configure \
        --with-python=/usr/local/bin/python${PYTHON_VERSION} \
        --with-apxs=/usr/bin/apxs && \
    make && make install clean
RUN rm -rf /usr/src/mod_wsgi-${MOD_WSGI_VERSION}

# Set Apache2 Configurations
# =============================================================================
# Create PID file directory for /run/apache2/httpd.pid
RUN mkdir -p /run/apache2

# Set Servername to something.
RUN sed -i -r 's@#Servername.*@Servername wsgi@i' /etc/apache2/httpd.conf

# Direct access and error logs to stderr for Docker.
RUN sed -i -r 's@(CustomLog .*)@\1\nTransferLog /dev/stderr@i' /etc/apache2/httpd.conf
RUN sed -i -r 's@Errorlog .*@Errorlog /dev/stderr@i' /etc/apache2/httpd.conf

# Direct *.wsgi scripts to mod_wsgi
RUN echo -e "\n\n\
LoadModule wsgi_module modules/mod_wsgi.so\n\
WSGIPythonPath /home/apache\n\
WSGIScriptAlias / /home/apache/mysite/wsgi.py\n\
<Directory /home/apache/mysite>\n\
    <Files wsgi.py>\n\
        Require all granted\n\
    </Files>\n\
</Directory>" >> /etc/apache2/httpd.conf

# "apache" runs a sample "hello world" WSGI script.
# =============================================================================
WORKDIR /home/apache

# Start Apache2 service without mod_wsgi-express
EXPOSE 80
CMD ["httpd", "-D", "FOREGROUND", "-e", "info"]