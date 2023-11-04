#!./mastermind_venv/bin/python3

import unittest
import argparse
import os
from inspect import isclass
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module


def import_tst_classes():
    # iterate through the modules in the current package
    tst_dir = os.path.join(Path(__file__).resolve().parent, "tst")

    for (_, module_name, _) in iter_modules([tst_dir]):
        if "_test.py" not in module_name:
            continue
        # import the module and iterate through its attributes
        module = import_module(f"tst.{module_name}")
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isclass(attribute):
                # Add the class to this package's variables
                globals()[attribute_name] = attribute


if __name__ == '__main__':
    import_tst_classes()
    parser = argparse.ArgumentParser(
        prog="./unittest_executor.py",
        description="Unittests for mastermind game"
    )

    parser.add_argument("-t", "--test", action="append", default=[],
                        help="Add a particular test class name to be executed")
    args = parser.parse_args()

    if len(args.test) > 0:
        cool_prompt = f'''
    ######################################################
    ############### Running Specific Test ################
    ######################################################
        '''
        print(cool_prompt)
        suites_list = []
        loader = unittest.TestLoader()
        for class_name in args.test:
            class_type = eval(class_name)
            suite = loader.loadTestsFromTestCase(class_type)
            suites_list.append(suite)

        big_suite = unittest.TestSuite(suites_list)
        testResult = unittest.TextTestRunner(verbosity=2).run(big_suite)
        unittest.main()
    else:
        cool_prompt = '''
    ######################################################
    ############ RUNNING ALL TESTS in TST dir ############
    ######################################################
        '''
        print(cool_prompt)
        test_loader = unittest.TestLoader()
        suite = test_loader.discover(
            start_dir="./tst", pattern="*_test.py"
        )
        testResult = unittest.TextTestRunner(verbosity=2).run(suite)
