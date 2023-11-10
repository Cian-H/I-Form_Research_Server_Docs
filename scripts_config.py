import os
from pathlib import Path

import tomlkit as toml


VIRTUAL_ENV = Path(os.environ.get("VIRTUAL_ENV", ".venv"))
    

def insert_env_vars(split_config):
    """
    Inserts environment variables into the config file
    where they follow the format {$ENV_VAR_NAME}
    """
    config_str = toml.dumps(split_config)
    split_config = config_str.split("{$")
    if len(split_config) > 1:
        c_head = split_config[0]
        c_tail = split_config[1:]
        c_parsed_tail = [
            "".join((os.environ[x0], x1)) for x0, x1 in
            (
                (y[:i], y[i+1:]) for i, y in
                zip(
                    (z.find("}") for z in c_tail),
                    c_tail
                )
            )
        ]
        config_str = "".join((c_head, *c_parsed_tail))
    return toml.loads(config_str)


def parse_config():
    with open("pyproject.toml", "rt") as f:
        config = toml.load(f)["tool"]["scripts-config"]
    config = insert_env_vars(config)
    return config


def init():
    config = parse_config()
    globals().update(config)


init()