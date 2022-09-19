sudo apt-get update
sudo snap install docker
sudo docker build -t fastapi .
sudo docker run -itd -p 80:80/tcp fastapi