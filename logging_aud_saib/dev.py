import logging
import sys
import time
import requests
from logging.handlers import TimedRotatingFileHandler, SMTPHandler, HTTPHandler
import json

FORMATTER_STRING = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
FORMATTER = logging.Formatter(FORMATTER_STRING)
LOG_FILE = "/tmp/my_app.log" # use fancy libs to make proper temp file

# Настройки для SMTP
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "alerts@example.com"
SMTP_PASSWORD = "your_password"
EMAIL_FROM = "alerts@example.com"
EMAIL_TO = ["admin@example.com"]
EMAIL_SUBJECT = "КРИТИЧЕСКАЯ ОШИБКА В ПРИЛОЖЕНИИ"

# Настройки для HTTP
HTTP_HOST = "logs.example.com"
HTTP_URL = "/api/logs"
HTTP_METHOD = "POST"

class CustomHTTPHandler(HTTPHandler):
    def emit(self, record):
        try:
            payload = {
                'timestamp': self.formatter.formatTime(record),
                'level': record.levelname,
                'logger': record.name,
                'message': record.getMessage()
            }
            
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer your_api_token'
            }
            
            requests.request(
                method=self.method,
                url=f"https://{self.host}{self.url}",
                headers=headers,
                data=json.dumps(payload)
            )
        except Exception:
            self.handleError(record)

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # Capture all logs
    
    # Консольный обработчик
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    console_handler.setLevel(logging.INFO)  # On console show only INFO+
    logger.addHandler(console_handler)

    # Файловый обработчик с ротацией
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.DEBUG)  # In file log everything
    logger.addHandler(file_handler)
    
    # SMTP обработчик для критических сообщений
    smtp_handler = SMTPHandler(
        mailhost=(SMTP_SERVER, SMTP_PORT),
        fromaddr=EMAIL_FROM,
        toaddrs=EMAIL_TO,
        subject=EMAIL_SUBJECT,
        credentials=(SMTP_USERNAME, SMTP_PASSWORD),
        secure=()  # Use () for TLS
    )
    smtp_handler.setFormatter(FORMATTER)
    smtp_handler.setLevel(logging.CRITICAL)  # Only for CRITICAL
    logger.addHandler(smtp_handler)
    
    # HTTP обработчик для критических сообщений
    http_handler = CustomHTTPHandler(
        host=HTTP_HOST,
        url=HTTP_URL,
        method=HTTP_METHOD
    )
    http_handler.setFormatter(FORMATTER)
    http_handler.setLevel(logging.CRITICAL)  # Only for CRITICAL
    logger.addHandler(http_handler)
    
    return logger

if __name__ == "__main__":
    logger = get_logger("my_app_logger")
    logger.info("Start logging")
    logger.debug("Some debug message")
    
    # Test critical message
    # logger.critical("This is a CRITICAL error that should trigger email and HTTP alerts!")
    
    while True:
        try: 
            time.sleep(1)
            logger.info("Keep logging")
        except KeyboardInterrupt:
            logger.critical("Application terminated by user")
            break
        except Exception as e:
            logger.critical(f"Critical error occurred: {str(e)}")
            break
