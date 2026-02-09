# print("program started")

# try :
#     a = 10
#     b = a/2
#     print(b)
# except Exception as e:
#     print(e)
# else:
#     print("no errors")
# finally:
#     print("always executable")

# print("program ended")


try :
    # print(a)
    a = 10+"abc"
except NameError as e:
    print(e)
except TypeError as e:
    print(e)
