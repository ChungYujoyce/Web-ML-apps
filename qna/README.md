### Run locally
- Open a virtual environment and install all dependencies by following `requirements.txt`
- Go to backend folder and run 
  `uvicorn main:app --reload`, this would turn on question answering API on the backend.
- Go to frontend folder and use any live server to open index.html
  - For instance, if you're using VSCode, you can download [live server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer), right click on a `HTML` file from Explorer Window and click on `Open with Live Server`.
- Type your question in the textbox and see the result showing below!

### Deploy on AWS EC2, with nginx web server

1. Follow this [Youtube](https://www.youtube.com/watch?v=o9TOERzCneI&t=1305s&ab_channel=ABSatyaprakash) to create a EC2 instance.
2. Follow the instructions below to install Nginx and run the service.
  
You can create a self-signed ssl certificate inside `/etc/nginx/ssl` using the following command:

```
sudo openssl req -batch -x509 -nodes -days 365 \
-newkey rsa:2048 \
-keyout /etc/nginx/ssl/server.key \
-out /etc/nginx/ssl/server.crt
```
After creating the EC2 instance (Ubuntu OS) and installing nginx, you need to add the following inside `/etc/nignx/sites-enabled` in a file which we can call `fastapi_nginx`.

```
server {
        listen 80;
        listen 443 ssl;
        ssl on;
        ssl_certificate /etc/nginx/ssl/server.crt;
        ssl_certificate_key /etc/nginx/ssl/server.key;
        server_name xx.xxx.xxx.xx;
        location / {
                 proxy_pass http://127.0.0.1:8000;
        }
}
```
Here xx.xxx.xxx.xx needs to be replaced with your instance's public IP address.

Now, if we run our app using uvicorn, we can see the app running at the public IP and interact with it. However, we need to ensure that uvicorn keeps running even though we are not connected via SSH.

Inside `/etc/systemd/system` we create a new service - `qna.service`

```[Unit]
Description=Uvicorn instance to serve QnA-RoBERTa-FastAPI
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/qna
Environment="PATH=/home/ubuntu/qna/venv/bin"
ExecStart=/home/ubuntu/qna/venv/bin/uvicorn main:app

[Install]
WantedBy=multi-user.target
```

After saving this file - run the command from your home directory.

```
sudo systemctl start nginx && cd /etc/systemd/system && sudo systemctl start qna.service
```

### Result returned from EC2

![API call](ec2.gif)
