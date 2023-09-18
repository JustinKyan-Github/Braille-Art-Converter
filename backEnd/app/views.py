import json
from flask import Blueprint, request, jsonify
#from .reviewScraper import getTSFunnyReview
#import whatever functions you need from review scraper here
from .Braille import convertToBraille
from flask_cors import CORS


views = Blueprint('view', __name__)
CORS(views)

@views.route('/', methods=['POST'])
def makeStuffWork():
    image = request
    brailleConversion = convertToBraille(image)
    return brailleConversion
