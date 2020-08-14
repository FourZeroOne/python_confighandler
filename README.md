# python_confighandler

Example:

```python
from confighandler import ConfigHandler

config_settings = [
    {'name': 'db_uri', 'section': 'DATABASE', 'key':  'URI'},
    {'name': 'special_key', 'section': 'APP', 'key':  'SPECIAL_KEY'}
]

config_schema = {
    'DATABASE': {'URI': {name: 'db_uri', required: True}},
    'APP': {'SPECIAL_KEY': {name: 'special_key', required: True}}
}

# all required
# use default var name handling: <variable> if already exists use: <section>_<variable>
# no schema; just parse and return
# ENV Fallback (only possible if schema is set!)


CONFIGS = ConfigHandler().get_configs(
    'settings.cfg', config_settings, use_env_as_fallback=True)

if CONFIGS is None:
    raise Exception('ERROR: Could not get configs
```


## Next:
* parse config file without python config
* handle dynamic content linked_section
