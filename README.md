🤖 Cheapbot
-----------
![DALL·E 2023-12-26 13 57 02 - Design a logo for 'CheapBot' with a focus on the automation of DNS-01 challenges for NameCheap services  The logo should visually convey high-tech aut](https://github.com/ZiadMansourM/cheapbot/assets/64917739/6ddc5e43-ca8f-4b89-b0c7-64938d22fdbb)

This plugin helps automate the `dns-01` challenge using Namecheap API.

Repo | Link
:--: | :--:
Docker Hub | [🔗](https://hub.docker.com/repository/docker/ziadmmh/cheapbot/general/)
PyPi | [🔗](https://pypi.org/project/cheapbot/)


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
