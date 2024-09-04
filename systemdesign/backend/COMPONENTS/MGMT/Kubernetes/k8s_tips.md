# enable auto complete in bash for kubectl cmds
- https://kubernetes.io/docs/reference/kubectl/quick-reference/
```
sudo apt-get install bash-completion
kubectl completion bash | sudo tee /etc/bash_completion.d/kubectl > /dev/null
```
