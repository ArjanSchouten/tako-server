FROM nginx:alpine

RUN rm -rf /var/www
RUN rm -rf /etc/nginx
RUN mkdir -p /etc/nginx/logs

COPY conf /etc/nginx

RUN ln -s /etc/nginx/sites-available/takoserver.conf /etc/nginx/sites-enabled/takoserver.conf

EXPOSE 80 443
