# Gunicorn configuration
import os
import multiprocessing

# Server socket
bind = os.getenv("GUNICORN_BIND", "0.0.0.0:5001")
backlog = 2048

# Worker processes
workers = os.getenv("GUNICORN_WORKERS", max(2, multiprocessing.cpu_count() - 1))
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
timeout = 120
keepalive = 2

# Logging
accesslog = os.getenv("GUNICORN_ACCESS_LOG", "-")
errorlog = os.getenv("GUNICORN_ERROR_LOG", "-")
loglevel = os.getenv("GUNICORN_LOG_LEVEL", "info")
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None

# SSL
keyfile = None
certfile = None

# Application
pythonpath = None
raw_env = []
