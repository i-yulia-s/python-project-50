from gendiff.formatters import format_as_json


class Diff:
    def __init__(self, key, value1, value2, change, children):
        self.key = key
        self.value1 = value1
        self.value2 = value2
        self.change = change
        self.children = children

    @staticmethod
    def create(key, value1, value2, change):
        return Diff(key, value1=value1, value2=value2, 
                    change=change, children=None)
    
    @staticmethod
    def create_parent(key, children):
        return Diff(key, value1=None, value2=None, 
                    change=None, children=children)


# def compare_flat(content1, content2):
#     result = '{\n'
#     all_keys = sorted(content1.keys() | content2.keys())
#     for key in all_keys:
#         if key not in content1.keys():
#             result += f"  + {key}: {str(content2[key]).lower()}\n"
#         elif key not in content2.keys():
#             result += f"  - {key}: {str(content1[key]).lower()}\n"
#         elif content1[key] != content2[key]:
#             result += f"  - {key}: {str(content1[key]).lower()}\n"
#             result += f"  + {key}: {str(content2[key]).lower()}\n"
#         else:
#             result += f"    {key}: {str(content2[key]).lower()}\n"
#     result += '}'
#     return result


def compare(content1, content2, formatter="stylish"):
    def write_nodes(arr1, arr2):
        result = []
        all_keys = sorted(arr1.keys() | arr2.keys())
        print(all_keys)
        for key in all_keys:
            value1 = arr1.get(key)
            value2 = arr2.get(key)
            if (isinstance(value1, dict) 
                and isinstance(value2, dict)):
                children = write_nodes(value1, value2)
                result.append(Diff.create_parent(key, children))
            else:
                if (key in arr1.keys()) and (key in arr2.keys()):
                    change = 'change'
                if value1 == value2:
                    change = None
                if key not in arr1.keys():
                    change = 'add'
                if key not in arr2.keys():
                    change = 'delete'
                result.append(Diff.create(key, value1, value2, change))
        return result
    match formatter:
        case 'stylish':
            return format_as_json(write_nodes(content1, content2))