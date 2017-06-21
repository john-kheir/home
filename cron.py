import sys
va = sys.argv[1]
if va != "cron":
  print('not cron job')
else:
  print('this is a cron job')
