import json
from fractions import Fraction


class FractionJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Fraction):
            if obj.numerator % obj.denominator == 0:
                return str(obj.numerator // obj.denominator)

            return f"{obj.numerator}/{obj.denominator}"

        return json.JSONEncoder.default(self, obj)
