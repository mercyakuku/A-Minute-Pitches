from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user, login_required, logout_user