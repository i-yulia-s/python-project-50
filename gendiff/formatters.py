def jsonize_value(value):
        match value:
            case None:
                return "null"
            case False:
                return "false"
            case True:
                return "true"
        return value

def jsonize_dict(dikt, depth):
    output = '{\n'
    indent = '    ' * depth
    for key in dikt.keys():
        if isinstance(dikt.get(key), dict):
            value = jsonize_dict(dikt.get(key), depth + 1)
        else:
            value = dikt.get(key)
        output += f'{indent}    {key}: {value}\n'
    output += indent + '}'
    return output

def format_changes(diff, depth):
    output = ''
    if isinstance(diff.value1, dict):
        val1 = jsonize_dict(diff.value1, depth + 1)
    else:
        val1 = jsonize_value(diff.value1)
    if isinstance(diff.value2, dict):
        val2 = jsonize_dict(diff.value2, depth + 1)
    else:
        val2 = jsonize_value(diff.value2)
    indent = '    ' * depth
    match diff.change:
        case None:
            output += f'{indent}    {diff.key}: {val1}\n'
        case "delete":
            output += f'{indent}  - {diff.key}: {val1}\n'
        case "add":
            output += f'{indent}  + {diff.key}: {val2}\n'
        case "change":
            output += f'{indent}  - {diff.key}: {val1}\n'
            output += f'{indent}  + {diff.key}: {val2}\n'
    # print(f'Formatted as {output}')
    return output

def format_as_json(diff):
    def read_nodes(nodes, depth):
        result = '{\n'
        indent = '    ' * depth
        for node in nodes:
            if node.children:
                result += f'{indent}    {node.key}: {read_nodes(node.children, depth + 1)}\n'
            else:
                result += format_changes(node, depth)
        result += indent + '}'
        return result
    return read_nodes(diff, 0)
