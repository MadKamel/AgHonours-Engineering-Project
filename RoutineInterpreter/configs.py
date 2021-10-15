def Read(configfile):
    configs_file = open(configfile + ".cfg", 'r').read()
    configs_array = configs_file.split('\n')
    configs_temparray = []
    configs = {}
    for i in range(len(configs_array)):
        configs_temparray.append((configs_array[i].split("=")[0], configs_array[i].split("=")[1]))
    configs = dict(configs_temparray)
    return configs
