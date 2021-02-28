import os


def replace_quotes(target_file, rule):
    """
    """
    
    new_file = 'temp.py.bak'
    common_quote = {
        'double-to-single': ['\"', '\''],
        'single-to-double': ['\'', '\"'],
    }
    replace_rule = common_quote[rule]

    if replace_rule is None:
        raise Exception('Unknown rule')


    with open(target_file, 'r') as read_py:
        copy_py = open(new_file, 'w')

        for line in read_py.readlines():
            copy_py.write(line.replace(replace_rule[0], replace_rule[1]))

        os.remove(target_file)
        os.rename(new_file, target_file)



