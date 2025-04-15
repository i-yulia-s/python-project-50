def compare_flat(content1, content2):
    result = '{\n'
    all_keys = sorted(content1.keys() | content2.keys())
    for key in all_keys:
        if key not in content1.keys():
            result += f"  + {key}: {str(content2[key]).lower()}\n"
        elif key not in content2.keys():
            result += f"  - {key}: {str(content1[key]).lower()}\n"
        elif content1[key] != content2[key]:
            result += f"  - {key}: {str(content1[key]).lower()}\n"
            result += f"  + {key}: {str(content2[key]).lower()}\n"
        else:
            result += f"    {key}: {str(content2[key]).lower()}\n"
    result += '}'
    return result
