

def substr (st):
  wnd = len (st)
  while (wnd > 0):
    start_idx = 0
    while ((start_idx + wnd) <= len(st)):
      piece = st[start_idx : start_idx + wnd]
      print (piece)
      start_idx += 1
    wnd = wnd - 1

def main():
  substr ('ABCD')

main()
