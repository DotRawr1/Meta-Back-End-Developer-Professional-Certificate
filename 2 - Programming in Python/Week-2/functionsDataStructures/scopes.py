# Built in // print, def, etc
# global
# enclosing
# local

global_v = 10
def fn1():
    enclosed_v = 8
    def fn2():
        local_v = 5
        print("Access to Global", global_v)
        print("Access to enclosed", enclosed_v)
    fn2()
fn1()
# print("Cant access the local", local_v) // would throw an error
# print("Cant access the local", enclosed_v) // would throw an error