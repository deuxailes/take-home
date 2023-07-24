How I did this:

Installed Helmify -> https://github.com/arttor/helmify

Then:

  258  cd helm-chart/
  259  ../helmify
  260  cat ../k8s/deploy.yaml
  261  cat ../k8s/deploy.yaml | ../helmify mychart

