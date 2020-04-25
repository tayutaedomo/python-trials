#
# Refer: https://stackoverflow.com/questions/25912008/open-url-and-return-to-shell
#

# import webbrowser
#
# images = ['http://stackoverflow.com']
#
# for rP in images:
#     webbrowser.open(rP)
#     decision = str(input('Is image ' + str(rP) + ' ok?'))

from webbrowser import open as browse
from subprocess import check_output

images = ['http://stackoverflow.com']

for rP in images:
    # term = check_output(['/usr/bin/osascript', '-e',
    #     'copy path to frontmost application as text to stdout']).strip()
    term = check_output(['/usr/bin/osascript', '-e',
        'copy path to frontmost application as text to stdout'])
    term = term.decode('ascii').strip()
    browse(rP)
    check_output(['/usr/bin/osascript', '-e',
        'tell application "%s" to activate' % term])
    # decision = raw_input('Is image ' + str(rP) + ' ok? ')
    decision = input('Is image ' + str(rP) + ' ok? ')

