# *****
# *****
# *****
# *****
# *****

# len=15
# for j in range(len):
#     for i in range(len):
#         print("*",end="")
#     print()

# len=15
# for j in range(len):
#     print("*"*len)

# *
# **
# ***
# ****
# *****

# lines = 9
# for i in range(lines):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# lines = 9
# for i in range(lines):
#     print("*"*(i+1))


# *****
# ****
# ***
# **
# *

# lines = 9
# for i in range(lines):
#     for j in range(lines-i):
#         print("*",end="")
#     print()


# lines = 9
# for i in range(lines,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()


#     *
#    **
#   ***
#  ****
# *****


lines = 5
# for i in range(lines):
#     for k in range(lines-(i+1)):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()

# for i in range(lines):
#     print(" "*(lines-(i+1)),"*"*(i+1))


# *****
#  ****
#   ***
#    **
#     *

# lines = 9
# for i in range(lines):
#     for k in range(i):
#         print(" ",end="")
#     for j in range(lines-i):
#         print("* ",end="")
#     print()

#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *

# for i in range(lines):
#     print(" "*(lines-(i+1)),"* "*(i+1))

#     *
#    * *
#   * * *
#    * *
#     *

# lines = 5
# for i in range(lines):
#     for k in range(lines-(i+1)):
#         print(" ",end="")
#     for j in range(i+1):
#         print("* ",end="")
#     print()
# for i in range(lines-1):
#     for k in range(i+1):
#         print(" ",end="")
#     for j in range(lines-(i+1)):
#         print("* ",end="")
#     print()




# lines = 5
# for i in range(lines):
#     for k in range(lines-(i+1)):
#         print(" ",end="")
#     for j in range(i+1):
#         if j==0 or j==(i):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
# for i in range(lines-1):
#     for k in range(i+1):
#         print(" ",end="")
#     for j in range(lines-(i+1)):
#         if j==0 or j==(lines-(i+2)):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()