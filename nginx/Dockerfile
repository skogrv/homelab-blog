FROM nginx:1.27.3-perl

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
ENV HOME=/usr/src/app
ENV APP_HOME=/usr/src/app/blog
RUN mkdir -p $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME