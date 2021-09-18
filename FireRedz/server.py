# fmt: off
import logging; log = logging.getLogger('werkzeug').disabled = True
from utility import log
from flask import Flask; app = Flask(__name__); app.logger.disabled = True; app.route('/')(lambda: 'fuck you'); app.before_request(lambda: log.safe_print('Requested!')); app.run(port=6969)
