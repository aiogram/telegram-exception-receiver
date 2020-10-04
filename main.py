from app import web_app
from app.core.yaml import get_cfg

if __name__ == '__main__':
    web_server_cfg = get_cfg('web_server')
    web_app.run(**web_server_cfg)
