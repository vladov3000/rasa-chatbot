# rasa assistant

## Google Cloud VM setup

1. Go to https://console.cloud.google.com/
2. Sign in with .edu
3. Activate Google Cloud $300 credit (requires credit card but no autocharge)
3. Click on the project select button right next to the "Google Cloud Platform" logo in the upper left
4. Select "New Project" in the upper right of the pop up
5. Create a new project called rasa
6. On the sidebar select Compute Engine -> VM Instances
7. Create VM instance:
8. Machine type set to n1-standard-4(4 vCPU, 15 GB memory)
9. Change Boot Disk Image to 100 GB Ubuntu 18.02
10. Create instance
11. Click on ssh button for instance
12. git clone https://github.com/vladov3000/rasa-tutorial.git
12. cd rasa-tutorial
13. sudo apt-get update
14. sudo apt install python3-pip
15. pip3 install --upgrade pip
16. pip3 install rasa==1.10.2
16. ls /home
17. export PATH=$PATH:/home/$USERNAMEHERE/.local/bin
18. rasa train
19. tmux (ctrl B, C to create window ctrl B, 1 to switch to window 1)
19. rasa run actions (in seperate window)
20. rasa shell

## Run Telegram API

1. sudo apt-get install nginx
2. sudo apt install docker.io
3. sudo apt install docker-compose
6. sudo groupadd docker
7. sudo usermod -aG docker $USER
8. newgrp docker 
4. sudo service nginx start
5. sudo service docker start
6. docker-compose up

Enviroment setup:

    Ubuntu 18
    python version: 3.6.9
    pip version: 20.1.2
    rasa == 1.10.2
    
Or use virtual env (will be have to be done for every tmux window):

    python3 -m venv ./venv
    source /venv/bin/activate
    pip install -r requirements.txt

To run rasa with command line shell:

    rasa train
    rasa run actions (in seperate window)
    rasa shell
    
To run tests:

    rasa test --stories tests/conversation_tests.md
