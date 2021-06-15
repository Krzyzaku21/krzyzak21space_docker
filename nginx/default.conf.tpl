server {
    listen ${LISTEN_PORT};


    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
    location /staticfiles/ {
        alias /vol/static;
    }
    location /mediafiles/ {
        alias /vol/mediafiles;
    }
}