# Disini kita menggunakan python versi alpine
FROM python:3.8.6-alpine

# Menginstall beberapa lib pendukung.
RUN apk --update --no-cache add apache2 apache2-dev wget ca-certificates make gcc musl-dev

# Menambahakn projek kedalam kontainer tepanya di folder mysite.
ADD . /mysite

# Mengeset working direktori ke folder mysite.
WORKDIR /mysite

# Menginstall pyarmor menggunakan pip3
RUN pip3 install pyarmor
# Mengintall django menggunkan pip3
RUN pip3 install django

# Menambahkan file  _pytransform.so ke folder /usr/local/lib/python3.8/site-packages/pyarmor/platforms/linux/x86_64/
ADD _pytransform.so /usr/local/lib/python3.8/site-packages/pyarmor/platforms/linux/x86_64/

# Melakukan encrypt code pada projek, nanti outputnya ke folder /app
RUN pyarmor obfuscate --src="." -r --output=/app mysite/wsgi.py

# Menyimpan folder app ke /home/apache
RUN mv ../app /home/apache

# Menghapus projek original
RUN rm -rf /mysite

# Mendefinisikan versi python untuk keperluan install mod_wsgi.
ENV PYTHON_VERSION=3.8
ENV MOD_WSGI_VERSION=4.7.1
ENV MOD_WSGI_SRC_URL="https://github.com/GrahamDumpleton/mod_wsgi/archive/${MOD_WSGI_VERSION}.tar.gz"

# Proses download file mod_wsgi pada github
RUN wget -O /usr/src/mod_wsgi.tar.gz "${MOD_WSGI_SRC_URL}" && \
    tar -zxvf /usr/src/mod_wsgi.tar.gz -C /usr/src && \
    rm /usr/src/mod_wsgi.tar.gz


# Mengeset working dir ke /usr/src/mod_wsgi-4.7.1
WORKDIR /usr/src/mod_wsgi-${MOD_WSGI_VERSION}

# Proses installasi mod_wsgi.
ENV CFLAGS="-I/usr/local/include/python${PYTHON_VERSION}m/ -L/usr/local/lib/"
RUN ln -s /usr/lib/libpython${PYTHON_VERSION}m.so /usr/lib/libpython${PYTHON_VERSION}.so && \
    ./configure \
        --with-python=/usr/local/bin/python${PYTHON_VERSION} \
        --with-apxs=/usr/bin/apxs && \
    make && make install clean
RUN rm -rf /usr/src/mod_wsgi-${MOD_WSGI_VERSION}

# Membuat file PID untuk apache2
RUN mkdir -p /run/apache2

# Set Servername
RUN sed -i -r 's@#Servername.*@Servername wsgi@i' /etc/apache2/httpd.conf
RUN sed -i -r 's@(CustomLog .*)@\1\nTransferLog /dev/stderr@i' /etc/apache2/httpd.conf
RUN sed -i -r 's@Errorlog .*@Errorlog /dev/stderr@i' /etc/apache2/httpd.conf

# Konfigurasi agar default rederingnya ke /home/apache/mysite
RUN echo -e "\n\n\
LoadModule wsgi_module modules/mod_wsgi.so\n\
WSGIPythonPath /home/apache\n\
WSGIScriptAlias / /home/apache/mysite/wsgi.py\n\
<Directory /home/apache/mysite>\n\
    <Files wsgi.py>\n\
        Require all granted\n\
    </Files>\n\
</Directory>" >> /etc/apache2/httpd.conf

# Set working dir ke /home/apache
WORKDIR /home/apache

# se default port ke 80
EXPOSE 80
CMD ["httpd", "-D", "FOREGROUND", "-e", "info"]