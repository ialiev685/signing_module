build:
	sudo docker build -t pycades-app .
stop:
	sudo docker stop pycades-app
start:
	make stop && sudo docker run -p 8004:8000 pycades-app
