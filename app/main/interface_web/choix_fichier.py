from flask import Flask, request, redirect, url_for, render_template
import os
import json
import glob
from uuid import uuid4

app = Flask(__name__)

