https://helm.sh/docs/intro/cheatsheet/

```
helm create <name>                      # Creates a chart directory along with the common files and directories used in a chart.
helm package <chart-path>               # Packages a chart into a versioned chart archive file.
helm lint <chart>                       # Run tests to examine a chart and identify possible issues:
helm show all <chart>                   # Inspect a chart and list its contents:
helm show values <chart>                # Displays the contents of the values.yaml file
helm pull <chart>                       # Download/pull chart 
helm pull <chart> --untar=true          # If set to true, will untar the chart after downloading it
helm pull <chart> --verify              # Verify the package before using it
helm pull <chart> --version <number>    # Default-latest is used, specify a version constraint for the chart version to use
helm dependency list <chart>            # Display a list of a chart’s dependencies:
```

# Concepts
- 24 helm cmds and subflags
- v. imp cmds
  - upgrade | uninstall
- helm dev workflows
- dev basics
- helm template : actions whitespace
- default lower indent, unindent
- flow control actions, if else range
- equals to not ..
- helm variables
- named templates
- list and dict
- create and pkg charts
- dependencies : alias, condition, tags
- subcharts : pass vars from parent to sub and vice-versa: explicit and implicit
- helm starters and plugins
- build plugin
- helm hooks : pre, post, release lifecycle, hooks deletion & wait, test hook
- sign and verify charts using gnupg
- host helm repos in github
- integrate with artifactory hub
- helm values to validate json schema and impose restrictions on values 
- built in objs
- release .dotchart dotfiles
