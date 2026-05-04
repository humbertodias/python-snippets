Install minikube
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

Start
```
minikube start
```

Build container
```
eval $(minikube docker-env)
docker build -t click-app api
```

Install kubectl
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

Build infra
```
kubectl apply -f redis.yml
kubectl apply -f deployment.yml
kubectl apply -f service.yml
```


Pods
```
kubectl get pods
```

minikube service click-service

Access
http://192.168.49.2:30007/