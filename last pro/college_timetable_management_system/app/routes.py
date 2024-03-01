from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, login_manager
from app.models import User, Schedule, Announcement
from app.forms import LoginForm, ScheduleForm, AnnouncementForm

# Define routes and controllers
