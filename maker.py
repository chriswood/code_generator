
import sys

def make_int(parameters):
    """
        Return string of integers in format for function call requiring
        individual paramters
    """
    return "%s" %(' ,'.join(parameters)
    
def make_string(parameters):
    """
        just return a big string of all passed in things
    """
    return "'%s'" %(''.join(parameters))

def resolve_parameters(param_type, param_list):
    types = {
        'int' : make_int,
        'string' : make_string,
    }
    
    f = types[param_type]
    result = f(param_list)
    return result

def code_edit(handler, verb, param_type, param_list=None, indent=None):
    line = "%s(%s)" %(verb, resolve_parameters(param_type, param_list))
    handler.write('\n' + line)
    
if(len(sys.argv) < 3):
    print('error: try maker.py <file handler type (a-append, w-rewrite>) <string to do something with>')
    
file_directive = sys.argv[1]
param_list = sys.argv[2:]

handler = open('robot_code.py', file_directive)

########################## generate some crap ################
code_edit(handler, 'print', 'string', param_list)
########################## stop ##############################

handler.close()

print('start')
import robot_code
print('stop')