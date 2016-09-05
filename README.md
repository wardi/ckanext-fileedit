
## Minimal config

```ini
ckan.plugins = ... file_edit

file_edit.editable_files = [{"path": "/path/to/my/file"}]
```

## Full config

```ini
ckan.plugins = ... file_edit

file_edit.editable_files = [
  {
    "path": "/path/to/my/file",
    "label": "My File",
    "validate": "ckanext.mytheme.validators:file_validator",
    "after_update": "ckanext.mytheme.tasks:notify_owner"
  },
  {
    "path": "/path/to/another_file"
  }]
```

Indentation on the left is required for the ini parser to pass the
complete JSON `editable_files` value

