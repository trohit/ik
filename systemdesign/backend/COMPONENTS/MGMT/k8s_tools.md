# Tools

- [k8s autocomplete in bash](https://stackoverflow.com/questions/53444924/how-to-enable-kubernetes-commands-autocomplete)
```
# update settings
cat <<'EOF' >> ~/.bashrc
source <(kubectl completion bash)
alias k=kubectl
complete -o default -F __start_kubectl k
EOF

# reload settings
source ~/.bashrc 
```

- [helm auto complete](https://helm.sh/docs/helm/helm_completion_bash/)

```
# update settings
cat <<'EOF' >> ~/.bashrc
source <(helm completion bash)
alias h=helm
EOF

helm completion bash > /etc/bash_completion.d/helm

# reload settings
source ~/.bashrc 
```


- [Flux](https://fluxcd.io/): an open src tool that works with k8s for CD (continuous deployment). Alternatives inckude [ArgoCD](https://argoproj.github.io/)
- Helm 
  - Helm is a package manager for Kubernetes that uses a packaging format called Charts123.
  - A Helm Chart is a collection of files that describe a set of Kubernetes resources1.
  - Charts are easy to create, version, share, and publish2.
  - Helm Charts follow a directory structure/tree1.
  - The Helm Charts can be archived and sent to a Helm Chart Repository1.
  - Helm helps you manage Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application2.
  - Helm streamlines installing, upgrading, fetching dependencies, and configuring deployments on Kubernetes with simple CLI commands3.
  - [Crunchydata Postgres](https://www.crunchydata.com/):
- [K8s py client](https://github.com/kubernetes-client/python)
  - pip install kubernetes
- k9s
- [k8s lens](https://k8slens.dev/) 

## YAML Generators
- https://static.brandonpotter.com/kubernetes/DeploymentBuilder.html
- https://k8syaml.com/
- https://gimlet.io/k8s-yaml-generator
- https://syshunt.com/kubernetes-yaml-generator/
