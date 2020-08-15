	sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/certs/cert.key -out /etc/nginx/certs/cert.crt
	cp default /etc/nginx/sites-enabled/default
