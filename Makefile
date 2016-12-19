bootstrap:
	docker run -d --name dnsmasq --restart always -p 53535:53/tcp -p 53535:53/udp --cap-add NET_ADMIN andyshinn/dnsmasq --address=/dev/127.0.0.1
	sudo mkdir -p /etc/resolver
	echo 'nameserver 127.0.0.1' | sudo tee /etc/resolver/dev
	echo 'port 53535' | sudo tee -a /etc/resolver/dev

setup:
	docker exec djangodocker_web_1 python manage.py migrate
	docker exec -it djangodocker_web_1 python manage.py createsuperuser

PHONY: bootstrap setup
