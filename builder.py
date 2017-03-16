from flask import Blueprint, render_template, request, redirect, session

builder = Blueprint("builder", __name__, template_folder="templates")
