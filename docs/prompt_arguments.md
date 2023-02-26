# Prompt arguments

When running the command ``fcp`` a prompt will start which enables you to configure your repository. The
prompt values and their explanation are as follows:

---

**author**

 Your full name.

**email**

Your email address.

**github_username**

Your github handle, i.e. `<handle>` in `https://github.com/<handle>`

**project_name**

Your project name. Should be equal to the name of your repository
and it should only contain alphanumeric characters and `-`'s.

**project_slug**

The project slug, will default to the `project_name` with all `-`'s
replaced with `_`. This will be how you import your code later, e.g.

``` python
from <project_slug> import foo
```

**project_description**

A short description of your project.

**version**

A version of your project.

**include_github_actions**

`"y"` or `"n"`. Adds a `.github` directory with various actions and
workflows to setup the environment and run code formatting checks
and unittests.

**publish_to**

`"pypi"` or `"none"`. Adds functionality to the
`Makefile` and Github workflows to make publishing your code as
simple as creating a new release release on Github.

**mkdocs**

`"y"` or `"n"`. Adds [MkDocs](https://www.mkdocs.org/)
documentation to your project. This includes automatically parsing
your docstrings and adding them to the documentation. Documentation
will be deployed to the `gh-pages` branch.

**codecov**

`"y"` or `"n"`. Adds code coverage checks with [codecov](https://about.codecov.io/).

**commitizen**

`"y"` or `"n"`. Adds tool to generate meaningful commits [commitizen](https://commitizen-tools.github.io/commitizen/).

**open_source_license**

Choose a [license](https://choosealicense.com/). Options:
    `["1. MIT License", "2. BSD license", "3. ISC license",  "4. Apache Software License 2.0", "5. GNU General Public License v3", "6. Not open source"]`

---
