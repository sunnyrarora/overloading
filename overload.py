def add(flg, *args):
    if flg=='int':
      ret = 0
    if flg == 'str':
      ret = ''
    for i in args:
      ret = ret +i
    print ret
