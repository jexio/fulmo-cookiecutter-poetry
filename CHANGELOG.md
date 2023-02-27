## 0.4.2 (2023-02-27)


- bump: version 0.4.1 → 0.4.2
- bump: version 0.4.0 → 0.4.1
- bump: version 0.4.0 → 0.4.1
- fix(github): build wily cache before ranking for all files
- bump: version 0.3.1 → 0.4.0

## 0.4.0 (2023-02-27)


- bump: version 0.3.1 → 0.4.0
- chore: update dependencies
- feat(tasks): extract total maintainability index from wily `rank` function
- docs: add wily badge
- chore: update dependencies
- chore: update python versions
- docs: fix broken links and size of cookie image
- ci(github): prevent generation commitizen hook if commitizen tool was rejected during project creation
- bump: version 0.3.0 → 0.3.1
- fix(tasks): fix broken name

## 0.3.0 (2023-02-27)


- bump: version 0.2.0 → 0.3.0
- docs: fix broken links
- fix(github): add interrogate tool in quality workflow
- feat(cookiecutter): add initial template for project generation
- feat(cli): add cli to run the cookiecutter with the directory passed
- test(cookiecutter): check that files that use the cookiecutter template insert data without errors
- feat(cookiecutter): add pre/post generation hooks
- feat(task): add makefile and cli to run development tasks
- For more details see `docs/makefile.md`
- chore(git): add initial git files
- The purpose of each file is described below:
1. `.gitignore` file specifies intentionally untracked files that Git should ignore.
2. Configuration file `pre-commit-config.yaml` for the framework to manage and support multi-language pre-commit hooks.
- chore(cookiecutter): add cookiecutter template
- chore(dependency): add initial poetry files
- docs: add template `mkdocs.yml` for static site generator MkDocs
- docs: add MIT license file
- chore(ide): add .editorconfig file
- ci(github): add initial workflow files
- Also add auxiliary files:
1. Tox. A generic virtual environment management and test command line tool.
- docs: add initial documentations
