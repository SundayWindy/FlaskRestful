from blueprints.api import api_bp
from blueprints.health import health_bp

__all__ = ["all_blueprints"]

all_blueprints = [api_bp, health_bp]
