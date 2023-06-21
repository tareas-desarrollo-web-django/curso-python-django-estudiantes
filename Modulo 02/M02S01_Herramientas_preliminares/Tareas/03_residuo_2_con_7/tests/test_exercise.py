import pytest
import src.exercise
from tests.input_data import input_values
import inspect
from collections.abc import Iterable
import pdb


@pytest.mark.parametrize('test_data', input_values)


def test_excercise(test_data):
    # Override input and print for the ecercise script.
    output = []
    def mock_input(input_s=None):
        output.append(input_s if input_s is not None else "")
        return value.pop(0)
    src.exercise.input = mock_input
    src.exercise.print = lambda *args: output.append(" ".join(map(str, args)))
    
    # Unpack test data
    namespace = test_data.get("namespace", None)
    init_args = test_data.get("init_args", [])
    names = test_data.get("names", [])
    names_inputs = test_data.get("names_inputs", [])
    expected_results = test_data.get("expected_results", [])
    std_outputs = test_data.get("std_outputs", [])
    error_msg = test_data.get("error_msg", "")
    
    if (namespace is None) or (namespace.strip() == ""):
        space_sequence = []
    else:
        space_sequence = namespace.split(".")
    
    # Process the namespace path, where the root is the script 'src.exercise'
    # If class names are encountered, they are created using the constructor
    # arguments given in 'init_args'.
    space = src.exercise
    for elem in space_sequence:
        elem = elem.strip()
        if elem == "":
            continue

        if inspect.isclass(getattr(space, elem)):
            # Is a class
            argv = init_args.pop(0)
            if argv is None:
                argv = []
            elif not isinstance(argv, Iterable):
                argv = [argv]
            space = getattr(space, elem)(*argv)
        else:
            # Asume is an object
            space = getattr(space, elem)
    #
    
    # Now that 'space' is the final namespace in the chain, execute the methods
    # and consult the attributes, to validate the results.
    for name in names:
        name = getattr(space, name)
        xpect_result = expected_results.pop(0) if len(expected_results) > 0 else None
        
        if callable(name):
            # If is a method or function
            inputs = names_inputs.pop(0) if len(names_inputs) > 0 else None

            if inputs is None:
                inputs = []
            
            if not inspect.isclass(xpect_result):
                result = name(*inputs)
                assert result == xpect_result, error_msg
            elif issubclass(xpect_result, Exception):
                with pytest.raises(xpect_result):
                    result = name(*inputs)
        else:
            # Asume is an atribute
            if xpect_result is None:
                assert name is None, error_msg
            else:
                assert name == xpect_result, error_msg
    #
#