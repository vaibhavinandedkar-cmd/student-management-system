# Deployment Guide

## Quick Start

### Development
```bash
chmod +x start.sh
./start.sh dev
```

### Production (Local)
```bash
./start.sh prod
```

### Docker
```bash
./start.sh docker
```

---

## Development Setup

### Prerequisites
- Python 3.9+
- PostgreSQL 12+

### Steps

1. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize database**
   ```bash
   python init_db.py
   python seed_db.py
   ```

4. **Run development server**
   ```bash
   FLASK_DEBUG=1 python run.py
   ```

Access: `http://localhost:5001/dashboard`

---

## Production Deployment (Gunicorn)

### Prerequisites
- Python 3.9+
- PostgreSQL 12+ (remote recommended)
- Nginx (optional, recommended)

### Installation

1. **Setup system user**
   ```bash
   sudo useradd -m -s /bin/bash student_mgmt
   sudo -u student_mgmt mkdir -p /home/student_mgmt/app
   ```

2. **Clone repository**
   ```bash
   sudo -u student_mgmt git clone <repo> /home/student_mgmt/app
   cd /home/student_mgmt/app
   ```

3. **Setup Python environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with production settings
   nano .env
   ```

5. **Initialize database**
   ```bash
   python init_db.py
   ```

6. **Create systemd service**
   ```bash
   sudo tee /etc/systemd/system/student_mgmt.service > /dev/null << EOF
[Unit]
Description=Student Management System
After=network.target postgresql.service

[Service]
Type=notify
User=student_mgmt
Group=student_mgmt
WorkingDirectory=/home/student_mgmt/app
Environment="PATH=/home/student_mgmt/app/venv/bin"
Environment="FLASK_ENV=production"
EnvironmentFile=/home/student_mgmt/app/.env
ExecStart=/home/student_mgmt/app/venv/bin/gunicorn -c gunicorn_config.py run:app
ExecReload=/bin/kill -s HUP $MAINPID
Restart=on-failure
RestartSec=10s

[Install]
WantedBy=multi-user.target
EOF
   ```

7. **Start service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable student_mgmt
   sudo systemctl start student_mgmt
   ```

8. **Check status**
   ```bash
   sudo systemctl status student_mgmt
   journalctl -u student_mgmt -f
   ```

### Configure Nginx

```bash
sudo tee /etc/nginx/sites-available/student_mgmt > /dev/null << 'EOF'
upstream flask_app {
    server 127.0.0.1:5001;
}

server {
    listen 80;
    server_name yourdomain.com;

    client_max_body_size 20M;

    location / {
        proxy_pass http://flask_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /home/student_mgmt/app/app/static;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Enable gzip
    gzip on;
    gzip_types text/plain text/css application/json application/javascript;
}
EOF
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/student_mgmt /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### SSL/TLS with Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

---

## Docker Deployment

### Using Docker Compose

1. **Build and start**
   ```bash
   docker-compose up -d
   ```

2. **View logs**
   ```bash
   docker-compose logs -f web
   ```

3. **Database management**
   ```bash
   docker-compose exec web python init_db.py
   docker-compose exec web python seed_db.py
   ```

4. **Stop services**
   ```bash
   docker-compose down
   ```

### Docker Swarm / Kubernetes

Create `docker-stack.yml` for Swarm or `kube-deployment.yaml` for Kubernetes.

---

## AWS Deployment (EC2 + RDS)

### RDS Setup
1. Create PostgreSQL RDS instance
2. Configure security groups
3. Get endpoint and credentials

### EC2 Setup
1. Launch EC2 instance (Ubuntu 20.04 LTS)
2. Install dependencies: `sudo apt update && sudo apt install python3.9 python3.9-venv nginx`
3. Follow Gunicorn setup above
4. Update `.env` with RDS endpoint

### Auto Scaling
Configure AWS Auto Scaling Group with launch template

---

## Database Backup & Restore

### Backup
```bash
pg_dump -U student_app -h localhost student_management > backup.sql
# Or with compression
pg_dump -U student_app -h localhost -Fc student_management > backup.dump
```

### Restore
```bash
psql -U student_app -h localhost -d student_management < backup.sql
# Or from compressed
pg_restore -U student_app -h localhost -d student_management backup.dump
```

### Automated Backup (Cron)
```bash
0 2 * * * /home/student_mgmt/app/backup.sh
```

Create `backup.sh`:
```bash
#!/bin/bash
BACKUP_DIR=/home/student_mgmt/backups
mkdir -p $BACKUP_DIR
DATE=$(date +\%Y\%m\%d_\%H\%M\%S)
pg_dump -U student_app student_management | gzip > $BACKUP_DIR/backup_$DATE.sql.gz
# Keep only last 30 days
find $BACKUP_DIR -name "backup_*.sql.gz" -mtime +30 -delete
```

---

## Performance Tuning

### PostgreSQL Configuration
```bash
# /etc/postgresql/12/main/postgresql.conf
max_connections = 200
shared_buffers = 256MB
effective_cache_size = 1GB
work_mem = 4MB
```

### Gunicorn Configuration
```bash
# gunicorn_config.py
workers = (cpu_count * 2) + 1  # For CPU-bound tasks
worker_class = 'sync'           # or 'gevent' for I/O-bound
```

### Nginx Caching
```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=api_cache:10m;

location /api {
    proxy_cache api_cache;
    proxy_cache_valid 200 1h;
}
```

---

## Monitoring & Logging

### Application Logs
```bash
# Development
tail -f logs/app.log

# Production (Systemd)
journalctl -u student_mgmt -f
```

### Database Monitoring
```bash
# Connect to PostgreSQL
psql -U student_app -d student_management

# Check connections
SELECT count(*) FROM pg_stat_activity;

# Check slow queries
SELECT query, calls, mean_time FROM pg_stat_statements ORDER BY mean_time DESC;
```

### System Monitoring
```bash
# CPU/Memory usage
htop

# Disk usage
du -sh /home/student_mgmt/app

# Network connections
netstat -tulpn | grep 5001
```

---

## Security Checklist

- [ ] Change default SECRET_KEY
- [ ] Use strong PostgreSQL password
- [ ] Enable HTTPS/SSL
- [ ] Configure firewall
- [ ] Set up automated backups
- [ ] Enable audit logging
- [ ] Configure rate limiting
- [ ] Use strong admin credentials
- [ ] Regular security updates
- [ ] Monitor error logs
- [ ] Configure CORS properly
- [ ] Enable CSRF protection

---

## Troubleshooting

### Port Already in Use
```bash
lsof -i :5001
kill -9 <PID>
```

### Database Connection Error
```bash
# Test connection
psql -U student_app -d student_management

# Check environment variables
env | grep DATABASE
```

### Permission Denied
```bash
sudo chown -R student_mgmt:student_mgmt /home/student_mgmt/app
sudo chmod +x /home/student_mgmt/app/venv/bin/*
```

### Out of Memory
- Increase swap space
- Optimize database queries
- Scale horizontally with load balancer

---

## Rollback Procedure

1. **Keep previous version**
   ```bash
   git tag v1.0.0
   git checkout v1.0.0
   ```

2. **Restore database backup**
   ```bash
   pg_restore backup.dump -U student_app -d student_management
   ```

3. **Restart service**
   ```bash
   sudo systemctl restart student_mgmt
   ```

---

## Support

For deployment issues, check logs and consult documentation.
