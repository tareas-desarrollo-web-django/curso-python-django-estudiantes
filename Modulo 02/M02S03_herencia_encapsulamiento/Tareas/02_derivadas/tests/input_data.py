import math
input_values = [
    {
        # Namespace: str
        'namespace':'Funcion',
        # Constructors arguments: list[obj]
        'init_args':[(lambda x: x,)],
        # Constructors exceptions: list[Exeption]
        # If an exception is expected, only the first exeption must
        # be specifies, all previous instantiations must be None
        'constructors_except':[],
        # Names to execute: list[str]
        'names':['derivada'],
        # Names inputs, in the same order as names: list[str]
        'names_inputs':[(10, 0.0001)],
        # Expected results in the same order as names: list[obj]
        # If the expected result is an exception, specify the name
        # the exception.
        'expected_results':[1.0],
        # Standard outputs via print, input, etc: list[str]
        'std_outputs':[],
        # Prefix error message
        'error_msg':''
    },
    {
        # Namespace: str
        'namespace':'Funcion',
        # Constructors arguments: list[obj]
        'init_args':[(lambda x: x*x,)],
        # Constructors exceptions: list[Exeption]
        # If an exception is expected, only the first exeption must
        # be specifies, all previous instantiations must be None
        'constructors_except':[],
        # Names to execute: list[str]
        'names':['derivada'],
        # Names inputs, in the same order as names: list[str]
        'names_inputs':[(8, 0.0001)],
        # Expected results in the same order as names: list[obj]
        # If the expected result is an exception, specify the name
        # the exception.
        'expected_results':[16.0],
        # Standard outputs via print, input, etc: list[str]
        'std_outputs':[],
        # Prefix error message
        'error_msg':''
    },
    {
        # Namespace: str
        'namespace':'Funcion',
        # Constructors arguments: list[obj]
        'init_args':[(lambda x: x*x*x,)],
        # Constructors exceptions: list[Exeption]
        # If an exception is expected, only the first exeption must
        # be specifies, all previous instantiations must be None
        'constructors_except':[],
        # Names to execute: list[str]
        'names':['derivada'],
        # Names inputs, in the same order as names: list[str]
        'names_inputs':[(15, 0.0001)],
        # Expected results in the same order as names: list[obj]
        # If the expected result is an exception, specify the name
        # the exception.
        'expected_results':[675.0],
        # Standard outputs via print, input, etc: list[str]
        'std_outputs':[],
        # Prefix error message
        'error_msg':''
    },
    {
        # Namespace: str
        'namespace':'Funcion',
        # Constructors arguments: list[obj]
        'init_args':[(lambda x: math.cos(x),)],
        # Constructors exceptions: list[Exeption]
        # If an exception is expected, only the first exeption must
        # be specifies, all previous instantiations must be None
        'constructors_except':[],
        # Names to execute: list[str]
        'names':['derivada'],
        # Names inputs, in the same order as names: list[str]
        'names_inputs':[(3.141526, 0.0001)],
        # Expected results in the same order as names: list[obj]
        # If the expected result is an exception, specify the name
        # the exception.
        'expected_results':[-0.0],
        # Standard outputs via print, input, etc: list[str]
        'std_outputs':[],
        # Prefix error message
        'error_msg':''
    },
    {
        # Namespace: str
        'namespace':'Funcion',
        # Constructors arguments: list[obj]
        'init_args':[(lambda x: math.sin(x),)],
        # Constructors exceptions: list[Exeption]
        # If an exception is expected, only the first exeption must
        # be specifies, all previous instantiations must be None
        'constructors_except':[],
        # Names to execute: list[str]
        'names':['derivada'],
        # Names inputs, in the same order as names: list[str]
        'names_inputs':[(3.141526, 0.0001)],
        # Expected results in the same order as names: list[obj]
        # If the expected result is an exception, specify the name
        # the exception.
        'expected_results':[-1.0],
        # Standard outputs via print, input, etc: list[str]
        'std_outputs':[],
        # Prefix error message
        'error_msg':''
    },
    {
        # Namespace: str
        'namespace':'Funcion',
        # Constructors arguments: list[obj]
        'init_args':[(lambda x: math.cos(x),)],
        # Constructors exceptions: list[Exeption]
        # If an exception is expected, only the first exeption must
        # be specifies, all previous instantiations must be None
        'constructors_except':[],
        # Names to execute: list[str]
        'names':['derivada'],
        # Names inputs, in the same order as names: list[str]
        'names_inputs':[(15, 0.0001)],
        # Expected results in the same order as names: list[obj]
        # If the expected result is an exception, specify the name
        # the exception.
        'expected_results':[-0.65],
        # Standard outputs via print, input, etc: list[str]
        'std_outputs':[],
        # Prefix error message
        'error_msg':''
    },
    {
        # Namespace: str
        'namespace':'Funcion',
        # Constructors arguments: list[obj]
        'init_args':[(lambda x: math.sin(x),)],
        # Constructors exceptions: list[Exeption]
        # If an exception is expected, only the first exeption must
        # be specifies, all previous instantiations must be None
        'constructors_except':[],
        # Names to execute: list[str]
        'names':['derivada'],
        # Names inputs, in the same order as names: list[str]
        'names_inputs':[(15, 0.0001)],
        # Expected results in the same order as names: list[obj]
        # If the expected result is an exception, specify the name
        # the exception.
        'expected_results':[-0.76],
        # Standard outputs via print, input, etc: list[str]
        'std_outputs':[],
        # Prefix error message
        'error_msg':''
    }
]
