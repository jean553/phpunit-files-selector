#!/usr/bin/python

'''
Routines to analyze file lines
'''
import sys

TEST_CLASS_DECLARATION_SUFFIX = 'class'
TEST_CLASS_WIP_GROUP = '/** @group wip */\n'

def is_line_class_declaration(line):
    '''
    Returns true if the given line 
    is the tests class declaration
    '''
    if line.startswith(TEST_CLASS_DECLARATION_SUFFIX):
        return True
    return False

def is_line_wip_group(line):
    '''
    Returns trye if the given line
    already contains the wip group
    '''
    if line.startswith(TEST_CLASS_WIP_GROUP):
        return True
    return False

def main(file_name):
    '''
    Main function
    '''
    with open(file_name, 'r+') as file_object:
        lines = file_object.readlines()

        file_object.seek(0)
        file_object.truncate()

        for line_number, line_content in enumerate(lines):

            if is_line_wip_group(line_content):
                lines.pop(line_number)
                break

            if is_line_class_declaration(line_content):
                lines.insert(line_number, TEST_CLASS_WIP_GROUP)
                break

        file_object.writelines(lines)

if __name__ == '__main__':
    main(sys.argv[1])
