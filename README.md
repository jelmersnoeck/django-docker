# Django Docker

This is an example project to run Django in a Docker container with a mounted
PostgreSQL database.

## Features

### Endpoints

The application exposes a single endpoint `http://django-docker.dev/hello-world/<id>`,
where <id> represents the id of a "Person" in the admin panel.

### Command line application

There is also a command line application to serve the Person's name when given
the correct ID.

```
$ docker exec djangodocker_web_1 python manage.py hello-world <id>
```

`<id>` represents the object id from the admin panel.

## Running the application.

### Prerequisites

#### Docker

As the purpose of this project is to show a Docker container running a Django
project with an PostgreSQL database attached, you'll need to have Docker
installed.

#### DNS Resolver

[Here](https://adrianperez.org/improving-dev-environments-all-the-http-things/) you can read more about this.

This isn't included in the docker-compose file because we can use this for other
projects as well, not specifically for this project.

To quickly set this up, run the dns-bootstrap script:

```
$ ./dns-bootstrap.sh
```

##### dnsmasq

To make it easy to run the application, we're using dnsmasq to resolve a
development domain to our docker container.

To do this, run a single docker container which will set up dnsmasq correctly
for you:

```
$ docker run -d --name dnsmasq --restart always -p 53535:53/tcp -p 53535:53/udp --cap-add NET_ADMIN andyshinn/dnsmasq --command --address=/dev/127.0.0.1
```

To make sure the `.dev` domain resolves on mac, you'll have to create a new dev
resolver which points to localhost.

```
$ sudo mkdir -p /etc/resolver
$ echo 'nameserver 127.0.0.1' | sudo tee /etc/resolver/dev
$ echo 'port 53535' | sudo tee -a /etc/resolver/dev
```

##### Reverse proxy

Because docker-compose sets up it's own network, we'll create the reverse proxy
through docker compose.

This could be resolved by creating a docker network, running the reverse proxy
in there and attaching our docker-compose services to that network. For
demonstration purposes however, it's simpler to put the nginx configuration in
the docker-compose file.

### Initial setup

The first time the project is run, we'll need to do some setup.

**Note:** Due to the web service starting quicker than the db initialisation,
the web service fails to launch properly the first time you run the application.
This causes the proxy to fail as well. To go around this, run the application
(`$ docker-compose up`)and follow the next few steps. Then stop the application
(by using `ctrl-c`). When you now re-run the application, everything will boot
correctly.

#### Migrations

When starting the project for the first time, you'll need to run migrations as
the database hasn't been set up yet.

```
$ docker exec djangodocker_web_1 python manage.py migrate
```

#### Superuser

A superuser allows you to log in to the admin section and create new people.

```
$ docker exec -it djangodocker_web_1 python manage.py createsuperuser
```
