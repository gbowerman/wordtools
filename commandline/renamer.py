'''renamer - tool to rename file names'''
'''
--ext [rename all files with this extension]
--remove [remove this string]
--trunc [remove from last occurrence of this string up to extension]
'''
import argparse
import glob
import os

count = 0

def rename_file(old_name, ext, remove, replace, trunc, pre, append):
    # remove extension from name
    extn_len = 0 - (len(ext) + 1)
    working_name = old_name[:extn_len]
    
    # apply changes here
    if remove is not None:
        working_name = working_name.replace(remove, '')
    if replace is not None:
        working_name = working_name.replace(replace[0], replace[1])    
    if trunc is not None:
        idx = working_name.rfind(trunc)
        working_name = working_name[:idx]
    if pre is not None:
        working_name = ''.join([pre, working_name])
    if append is not None:
        working_name = ''.join([working_name, append])
    
    # reassemble filename
    new_name = working_name + '.' + ext
    if new_name != old_name:
        print('Renaming \"' + old_name + '\" to \"' + new_name + '\".')
        os.rename(old_name, new_name)
        return True
    else:
        return False


def main():
    '''Main routine. Start by parsing args..'''
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--ext', '-e', required=True, action='store', help='File extension to match')   
    arg_parser.add_argument(
        '--remove', '-d', action='store', help='Remove this string')
    arg_parser.add_argument(
        '--replace', '-r', nargs=2, action='store', help='Replace the string')    
    arg_parser.add_argument(
        '--trunc', '-t', action='store', help='Remove from last occurence of this string, up to extension')
    arg_parser.add_argument(
        '--pre', '-p', action='store', help='Prepend this string to every file') 
    arg_parser.add_argument(
        '--append', '-a', action='store', help='Append this string to filename, before extension')

    args = arg_parser.parse_args()

    count = 0
    for filename in glob.glob('*.' + args.ext):
        if rename_file(filename, args.ext, args.remove, args.replace, args.trunc, args.pre, args.append) is True:
            count += 1

    print(str(count) + ' files renamed.')

if __name__ == "__main__":
    main()
