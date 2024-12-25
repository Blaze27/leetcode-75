def deep_copy(obj):
    if obj is None or isinstance(obj, (int, float, str, bool)):
        return obj

    if isinstance(obj, list):
        return [deep_copy(item) for item in obj]

    if isinstance(obj, dict):
        return {deep_copy(key): deep_copy(value) for key, value in obj.items()}

    if isinstance(obj, set):
        return {deep_copy(item) for item in obj}

    if hasattr(obj, '__dict__'):
        copy_obj = obj.__class__.__new__(obj.__class__)

        for key, value in obj.__dict__.items():
            setattr(copy_obj, key, deep_copy(value))

        return copy_obj

    raise TypeError(f"Unsupported object type: {type(obj)}")


original = {
    'a': 1,
    'b': [1, 2, {'x': 10}],
    'c': {'d': 3}
}

copy = deep_copy(original)

copy['b'][2]['x'] = 99

print(original)
print(copy)

print(id(original), id(copy))