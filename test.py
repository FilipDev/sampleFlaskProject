from flask import Blueprint

test_bp = Blueprint('main', __name__)


@test_bp.route('/')
def index():
    return 'Hello, World!'


@test_bp.route('/test')
def test():
    return 'Hello, World!'