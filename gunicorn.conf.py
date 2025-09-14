# Gunicorn configuration file
bind = "0.0.0.0:1000"
workers = 1
worker_class = "sync"
timeout = 120
keepalive = 2
max_requests = 1000
max_requests_jitter = 100
