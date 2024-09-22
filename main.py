from flask import Flask

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(test.test_bp)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max-limit.
    app.run(debug=False, host='0.0.0.0', port=5000)