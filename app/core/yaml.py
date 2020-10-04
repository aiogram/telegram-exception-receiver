import yaml

_cfg = None


def get_cfg(app=None):
    global _cfg
    if isinstance(_cfg, dict):
        if app:
            return _cfg.get(app)
        return _cfg

    with open('config.yml', 'r') as file:
        _cfg = yaml.load(file, Loader=yaml.FullLoader)
        if app:
            return _cfg.get(app)
        return _cfg
