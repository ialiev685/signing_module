build:
	sudo docker compose up --build -d
stop:
	sudo docker compose down
start:
	docker-compose up -d
write:
	 pip freeze>requirements.txt