import logging
import logging.config
import yaml
import os


class Settings:
    def configure(self, logging_config_file='logging.yaml', logging_file=None, extra={}):
        if os.path.exists(logging_config_file):
            with open(logging_config_file, 'r', encoding='utf-8') as fin:
                yaml_config = yaml.load(fin, Loader=yaml.FullLoader)

                if yaml_config['handlers'] and yaml_config['handlers']['file'] and logging_file:
                    yaml_config['handlers']['file']['filename'] = logging_file

                if len(extra) > 0:
                    yaml_config['extra'] = extra

                logging.config.dictConfig(yaml_config)
        else:
            logging.basicConfig(level=logging.INFO)


settings = Settings() 