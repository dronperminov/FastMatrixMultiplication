import json

from entities.fraction_json_encoder import FractionJsonEncoder


class JsonDepthStringifier:
    def stringify(self, value, depth: int, max_depth: int, indent: int) -> str:
        if isinstance(value, (str, bool, int, float)) or value is None:
            return json.dumps(value, ensure_ascii=False)

        if isinstance(value, tuple):
            value = list(value)

        if isinstance(value, (dict, list)):
            if 0 < max_depth <= depth:
                result = json.dumps(value, separators=(', ', ': '), indent=None, cls=FractionJsonEncoder)
                return result

            if isinstance(value, list):
                if len(value) == 0:
                    return "[]"

                items = ",\n".join(f"{self.__indent(indent, depth + 1)}{self.stringify(item, depth + 1, max_depth, indent)}" for item in value)
                return f"[\n{items}\n{self.__indent(indent, depth)}]"
            else:
                if len(value) == 0:
                    return "{}"

                props = []
                for key, val in value.items():
                    indent_str = self.__indent(indent, depth + 1)
                    key_str = json.dumps(str(key), ensure_ascii=False)
                    val_str = self.stringify(val, depth + 1, max_depth, indent)
                    props.append(f"{indent_str}{key_str}: {val_str}")

                props = ",\n".join(props)
                return f"{{\n{props}\n{self.__indent(indent, depth)}}}"

        raise ValueError(f"invalid json value: {type(value)}")

    def __indent(self, indent: int, level: int):
        return " " * (indent * level)
