from pymem import Pymem


# get process id

a = input("process name: ")

try:
    pm = Pymem(a)
    print('Process id: %s' % pm.process_id)
except Exception as e:
    print(e)
