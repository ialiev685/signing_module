#!/bin/sh

set -e  # Останавливаем скрипт при любой ошибке

docker-compose down
docker-compose up -d --build
cd web
export NODE_ENV=production

yarn install --frozen-lockfile
yarn build

sudo mkdir -p /var/www/signature-verification.net.ru
sudo chmod -R 755 /var/www/signature-verification.net.ru

sudo cp -r /root/github/signing_module/web_module/dist/* /var/www/signature-verification.net.ru
sudo cp /root/github/signing_module/web_module/nginx/nginx.conf /etc/nginx/sites-available/signing_module.conf
sudo nginx -t
sudo systemctl reload nginx
