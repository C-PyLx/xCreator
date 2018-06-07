#__Author__: Learning :~#
#Fast & powerful python wordlist creator

import os
import sys
import time
import string
import msvcrt
import argparse
import itertools

class color:
    blue = '\033[34m'
    red = '\033[31m'
    green = '\033[32m'
    bold = '\033[1m'
    under = '\033[7m'
    end = '\033[0m'

def createWordList(chrs, min, max, out):
    if min > max:
        print (color.red + '[!] `min length` Must smaller or same as with `max length`.', color.end)
        sys.exit()
    
    print (color.blue + color.bold + color.under + '[#] Started at: %s' % time.strftime('%H : %M : %S'), color.end)
    time.sleep(1)
    print (color.green + '[+] Writing words into: %s\n' % out, color.end)

    out = open(out, 'w')

    for word in range(min, max+1):
        for words in itertools.product(chrs, repeat=word):
            chars = ''.join(words)
            out.write("%s\n" % chars)
            sys.stdout.write('\r%s[>] Adding character: %s~>%s %s %s<~' %(color.green, color.end, color.bold+color.blue, chars, color.end))
            sys.stdout.flush()
    out.close()

    print (color.bold + color.blue + color.under + '\n[x] Time elapsed: %s' % time.strftime('%H : %M : %S'), color.end)
    print (color.green + color.bold + '[+] Passwords saved to: %s' % out.name, color.end)
    print (color.bold + color.red + color.under + '\n[-] Press any key to exit:', color.end)

    msvcrt.getche()

if __name__ =='__main__':
    try:
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            description='\033[92m[~] Python Professional Word List Generator [~]\033[0m')
        
        parser.add_argument('-chr', '--chars',
        default=None, help='Characters for wordlist')
        parser.add_argument('-min', '--min_length',
        default=1, type=int, help='Minimum length for characters')
        parser.add_argument('-max', '--max_length',
        default=2, type=int, help='Maximum length for characters')
        parser.add_argument('-out', '--output',
        default='output.txt', help='Output for save words [TXT]')

        args = parser.parse_args()
        if args.chars is None:
            args.chars = string.printable.replace(' \t\n\r\x0b\x0c', '')

        createWordList(args.chars, args.min_length, args.max_length, args.output)
    except KeyboardInterrupt:
        print (color.red + color.bold + '\n\n[!] Operation stopped at: %s' % time.strftime('%H : %M : %S'), color.end)
        sys.exit(1)
else:
    sys.exit(1)