import configparser
import logging
import os

LOGGER = logging.getLogger(__name__)


class ConfigHandler():
    def get_config_entry_from_file(self, config, section_name, key_name):
        try:
            return config.get(section_name, key_name)
        except:
            LOGGER.error('could not find {} in section {}.'.format(
                key_name, section_name ))
            return None

    def get_configs(self, config_file_name, config_settings, use_env_as_fallback=False):
        configs = {}

        # if using a config file, get the config information out of it
        if config_file_name and os.path.exists(config_file_name):
            config = configparser.ConfigParser()
            config.read(os.path.join(config_file_name))

            for entry in config_settings:
                configs[entry['name']] = self.get_config_entry_from_file(
                    config, entry.get('section', ''), entry.get('key', ''))

            return configs

        elif not use_env_as_fallback:
            return None

        # if not using a config file, try to get it from the env.
        for entry in config_settings:
            configs[entry['name']] = os.environ.get(entry.get('key', ''))

        return configs
