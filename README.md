🤖 Cheapbot - [🐳 Docker Hub](https://hub.docker.com/repository/docker/ziadmmh/cheapbot/general)
-----------
This plugin helps automate the `dns-01` challenge using Namecheap API.


🔧 Usage
--------
```console
ziadh@Ziads-MacBook-Air example % tree
.
├── docker-compose.yml
└── namecheap.ini

0 directories, 2 files
```

```yml
version: '3'
services:
  certbot:
    image: ziadmmh/cheapbot:v0.0.1
    volumes:
      - ./certs:/etc/letsencrypt/live
      - ./logs:/var/log/letsencrypt
      - ./namecheap.ini:/root/.secrets/certbot/namecheap.ini
    command: >
      certbot certonly
      --authenticator cheapbot -v
      --cheapbot-propagation-seconds 600
      --cheapbot-credentials /root/.secrets/certbot/namecheap.ini
      --non-interactive --expand
      --force-renewal
      --server https://acme-v02.api.letsencrypt.org/directory
      --agree-tos --email "EMAIL"
      --cert-name DOMAIN_NAME
      -d SUBDOMAIN.DOMAIN_NAME, www.DOMAIN_NAME
```
