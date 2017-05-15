import re
import random

WORDS = ["DEGREES"]


def handle(text, mic, profile):
    random_number = random.random()
    random_degree = 24 + random_number
    random_rounded_degree = round(random_degree,2)
    mic.say("This room has a Temperature of %s degrees" % random_rounded_degree)


def isValid(text):
    return bool(re.search(r'\bdegrees\b', text, re.IGNORECASE))
