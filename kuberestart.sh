kubectl delete --all pods
kubectl delete --all deployments
kubectl get configmap action-config -o yaml > kuberes/action-config.yml
kubectl apply -f kuberes
