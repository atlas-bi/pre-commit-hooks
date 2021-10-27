# Pre-commit hooks

## Clean Model Context

This pre-commit hook is used to remove connection strings from a dotnet model context from the auto generated (scaffold) model context. Dotnet inserts the connection string that was used to generate the model, and adds a note that it should be removed :) Thank Dotnet for adding an extra step for developers to loose sleep over 😢

### General Usage

Add the following hook to the ``.pre-commit-config.yaml``:

```yaml
repos:
  - repo: https://github.com/atlas-bi/pre-commit-hooks
    rev: <VERSION> # Get the latest from: https://github.com/atlas-bi/pre-commit-hooks/releases
    hooks:
      - id: clean_model_context

```
