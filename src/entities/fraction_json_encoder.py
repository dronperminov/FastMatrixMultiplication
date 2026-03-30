import json
from fractions import Fraction


class FractionJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Fraction):
            if obj.denominator == 1:
                return obj.numerator

            return f"{obj.numerator}/{obj.denominator}"

        return json.JSONEncoder.default(self, obj)
