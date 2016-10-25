FROM nginx:alpine

RUN rm -rf /var/www && \
    rm -rf /etc/nginx && \
    mkdir -p /etc/nginx/logs

COPY conf /etc/nginx

RUN rm -rf /etc/nginx/sites-enabled && \
    mkdir -p /etc/nginx/sites-enabled && \
    ln -s /etc/nginx/sites-available/takoserver.conf /etc/nginx/sites-enabled/takoserver.conf && \
    ln -s /etc/nginx/sites-available/letsencrypt.conf /etc/nginx/sites-enabled/letsencrypt.conf

EXPOSE 80 443
