FROM nginx:1.19.0-alpine
RUN mkdir /btre
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/
WORKDIR /btre