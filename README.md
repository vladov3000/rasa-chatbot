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
9. docker login
10. sudo service nginx start
11. sudo service docker start
13. sudo apt-get install snapd
14. sudo apt-get remove certbot  
NOTE: make sure to allow HTTP and HTTPS traffic to VM. 
15. docker build -t rasa/actions -f Dockerfile.actions .
13. docker-compose up

## Run Kubernetes

### Install kubernetes cli
    curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
    chmod +x ./kubectl
    sudo mv ./kubectl /usr/local/bin/kubectl
    kubectl version --client

### Install minikube
    curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \ && chmod +x minikube
    sudo mkdir -p /usr/local/bin/
    sudo install minikube /usr/local/bin/`
    minikube start --driver=docker
    kubectl get nodes
    
### Convert docker compose to kube resources
    curl -L https://github.com/kubernetes/kompose/releases/download/v1.21.0/kompose-linux-amd64 -o kompose
    chmod +x kompose
    sudo mv ./kompose /usr/local/bin/kompose
    kompose convert --volumes hostPath -o kuberes
    sed -ri "s/extensions\/v1beta1/networking.k8s.io\/v1/" kuberes/rasa-network-networkpolicy.yaml
    
### Run kubernetes
    sudo docker build -t rasa/train -f Dockerfile.train .
    docker save rasa/actions | pv | (eval $(minikube docker-env) && docker load)
    docker save rasa/train | pv | (eval $(minikube docker-env) && docker load)
    kubectl create configmap action-config --from-file=actions
    kubectl get configmap action-config -o yaml > kuberes/action-config.yml
    (Fix rasa-action-deploy to use config map instead of persistent volume)
    kubectl apply -f kuberes
    kubectl get pods
    sudo kubectl proxy --port=80

Enviroment setup:

    Ubuntu 18
    python version: 3.6.9
    pip version: 20.1.2
    rasa == 1.10.2
    
Or use virtual env (you will have to be source for every tmux window):

    python3 -m venv ./venv
    source /venv/bin/activate
    pip install -r requirements.txt

To run rasa with command line shell:

    rasa train
    rasa run actions (in seperate window)
    rasa shell
    
To run tests:

    rasa test --stories tests/conversation_tests.md
