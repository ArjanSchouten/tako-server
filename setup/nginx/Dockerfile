FROM nginx:alpine

RUN rm -rf /var/www && \
    rm -rf /etc/nginx && \
    mkdir -p /etc/nginx/logs

COPY conf /etc/nginx

RUN rm -r /etc/nginx/sites-enabled && \
    mkdir -p /etc/nginx/sites-enabled && \
    ln -s /etc/nginx/sites-available/takoserver.conf /etc/nginx/sites-enabled/takoserver.conf

EXPOSE 80 443
