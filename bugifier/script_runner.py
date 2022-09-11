def python_script_runner(filename):
    exec(open(filename).read())

    all_variables = dir()
    variable_names = []
    for name in all_variables:
        if not name.startswith('__'):
            variable_names.append(name)
    return variable_names
