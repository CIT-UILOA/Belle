## Grumpy (Backend)

### Workflow

#### Tags

For contributors, a tag is used for telling other contributors
about a specific code.

Example:

```python
  # AUDIT: Do we need a description for the mapped areas
  # description = Column(String, nullable=False)
```

> This tag is used for communicating with contributors if we should add this column or not.

Available tags:

- `AUDIT`: Tells contributors to check whether this feature is needed.
- `NOTE`: Marks an important comment that contributors should pay attention to.
