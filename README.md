# python_confighandler

Example:

```python
config_settings = [
    {'name': 'db_uri', 'section': 'DATABASE', 'key':  'URI'},
    {'name': 'special_key', 'section': 'APP', 'key':  'SPECIAL_KEY'}
]

CONFIGS = ConfigHandler().get_configs(
    'settings.cfg', config_settings, use_env_as_fallback=True)

if CONFIGS is None:
    raise Exception('ERROR: Could not get configs
```
    
