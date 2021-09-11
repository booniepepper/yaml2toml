# yaml2toml

Convert yaml files to toml files.

```
$ cat example.yml
here
  - we
  - go

$ yaml2toml example.yml

$ cat example.toml
here = [ "we", "go",]
```

### Install

```shell
pip install yaml2toml
```

### Etc

Project: https://github.com/hiljusti/yaml2toml

By: J.R. Hill

License: MIT

---

_Note: This little script is nice for a one-off conversion. Check out [`yj`](https://github.com/sclevine/yj) for a tool with more formats, features, support, etc._
