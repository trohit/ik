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
```
# helm
completion  (generate autocompletion scripts for the specified shell)                           push        (push a chart to remote)
create      (create a new chart with the given name)                                            registry    (login to or logout from a registry)
dependency  (manage a chart's dependencies)                                                     repo        (add, list, remove, update, and index chart repositories)
env         (helm client environment information)                                               rollback    (roll back a release to a previous revision)
get         (download extended information of a named release)                                  search      (search for a keyword in charts)
help        (Help about any command)                                                            show        (show information of a chart)
history     (fetch release history)                                                             status      (display the status of the named release)
install     (install a chart)                                                                   template    (locally render templates)
lint        (examine a chart for possible issues)                                               test        (run tests for a release)
list        (list releases)                                                                     uninstall   (uninstall a release)
package     (package a chart directory into a chart archive)                                    upgrade     (upgrade a release)
plugin      (install, list, or uninstall Helm plugins)                                          verify      (verify that a chart at the given path has been signed and is valid)
pull        (download a chart from a repository and (optionally) unpack it in local directory)  version     (print the client version information)

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
