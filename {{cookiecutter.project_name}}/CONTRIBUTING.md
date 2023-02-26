# Contributing to {{cookiecutter.project_name}}

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

# Report Bugs

Report bugs at https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/issues

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

# Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement a fix for it.

# Implement Features


Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

# Write Documentation

Cookiecutter PyPackage could always use more documentation, whether as part of
the official docs, in docstrings, or even on the web in blog posts, articles,
and such.

# Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/issues.

If you are proposing a new feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are welcome :)

# Get Started!

Ready to contribute? Here's how to set up `{{cookiecutter.project_name}}` for local
development. Please note this documentation assumes you already have
`poetry` and `Git` installed and ready to go.

1. Fork the `{{cookiecutter.project_name}}` repo on GitHub. 

2. Clone your fork locally:
```bash
cd <directory_in_which_repo_should_be_created>
git clone git@github.com:YOUR_NAME/{{cookiecutter.project_name}}.git
```

3. Now we need to install the environment. Navigate into the directory

```bash
cd {{ cookiecutter.project_name }}
``` 

If you are using ``pyenv``, select a version to use locally. (See installed versions with ``pyenv versions``)
```bash
pyenv local <x.y.z>
```

Then, install and activate the environment with:

```bash
poetry install
poetry shell
```

## Development

1. Install pre-commit to run linters/formatters at commit time:
```bash
poetry run pre-commit install
```

2. Create a branch for local development:
```bash
git checkout -b name-of-your-bugfix-or-feature 
```
Now you can make your changes locally.

3. Don't forget to add test cases for your added functionality to the ``tests`` directory.
4. When you're done making changes, check that your changes pass the formatting tests.
```bash
make check 
``` 

5. Now, validate that all unit tests are passing:
```bash
make test
```

6. Before raising a pull request you should also run tox. This will run the tests across different versions of Python:
```bash
tox 
```

This requires you to have multiple versions of python installed. 
This step is also triggered in the CI/CD pipeline, so you could also choose to skip this
step locally.

7. Reflect your changes in the documentation. Update relevant files in
  the `docs` directory, and potentially the `README`. You can check the
  updated documentation with
``` bash
make docs
```

8. Commit your changes and push your branch to GitHub:
```bash
git add .
git commit -m "<type>[(scope)]: Your detailed description of your changes. [Body]"
git push origin name-of-your-bugfix-or-feature 
```

9. Submit a pull request through the GitHub website.

# Commit message convention

Commit messages must follow our convention based on the
[Angular style](https://gist.github.com/stephenparish/9941e89d80e2bc58a153#format-of-the-commit-message)
or the [Karma convention](https://karma-runner.github.io/4.0/dev/git-commit-msg.html):

```
<type>[(scope)]: Subject

[Body]
```

**Subject and body must be valid Markdown.**
Subject must have proper casing (uppercase for first letter
if it makes sense), but no dot at the end, and no punctuation
in general.

Scope and body are optional. Type can be:

- `fix`: Bug fix.
- `feat`: New feature.
- `docs`: About documentation.
- `style`: A change in code style/format.
- `refactor`: Changes that are not features or bug fixes.
- `perf`: About performance.
- `test`: About tests.
- `build`: About packaging, building wheels, etc.
- `ci`: About Continuous Integration.
- `chore`: About packaging or repo/files management.
- `revert`: Reverts a previous commit.

If you write a body, please add trailers at the end
(for example issues and PR references, or co-authors),
without relying on GitHub's flavored Markdown:

```
Body.

Issue #10: https://github.com/namespace/project/issues/10
Related to PR namespace/other-project#15: https://github.com/namespace/other-project/pull/15
```

These "trailers" must appear at the end of the body,
without any blank lines between them. The trailer title
can contain any character except colons `:`.
We expect a full URI for each trailer, not just GitHub autolinks
(for example, full GitHub URLs for commits and issues,
not the hash or the #issue-number).

We do not enforce a line length on commit messages summary and body,
but please avoid very long summaries, and very long lines in the body,
unless they are part of code blocks that must not be wrapped.

# Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

* The pull request should include tests.
* If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring, and add the feature to
   the list in README.rst.
