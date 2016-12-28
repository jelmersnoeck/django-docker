bootstrap:
	docker run -d --name dnsmasq --restart always -p 53535:53/tcp -p 53535:53/udp --cap-add NET_ADMIN andyshinn/dnsmasq --address=/dev/127.0.0.1
	sudo mkdir -p /etc/resolver
	echo 'nameserver 127.0.0.1' | sudo tee /etc/resolver/dev
	echo 'port 53535' | sudo tee -a /etc/resolver/dev
	docker-compose up

setup:
	docker-compose exec web python manage.py migrate
	docker-compose exec web python manage.py createsuperuser

PHONY: bootstrap setup
