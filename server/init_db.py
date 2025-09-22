#!/usr/bin/env python3

from app import app
from models import db

with app.app_context():
    # Create all tables
    db.create_all()
    print("Database tables created successfully!")