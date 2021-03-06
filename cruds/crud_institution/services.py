from flask import Blueprint, jsonify, request
from . import models
from backend import db
from . import serializer


institution = Blueprint("institution", __name__)


@institution.route('/institution_details/<institution_id>', methods=['GET'])
def institution_details(institution_id):
    return jsonify(institution=serializer.InstitutionSerializer().serialize(models.Institution.query.filter_by(id=institution_id).all()))
