# *
# **
# ***
# ****
# *****

# stars = 1
# for i in range(5):
#     for i in range(stars):
#         print("*",end="")
#     print()
#     stars+=1


# *****
# ****
# ***
# **
# *


# lines = 5
# stars = lines
# for i in range(lines):
#     for i in range(stars):
#         print("*",end="")
#     print()
#     stars-=1


#     * 
#    **
#   ***
#  ****
# *****

# lines = 5
# stars = 1
# space = lines-1
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for i in range(stars):
#         print("*",end="")
#     print()
#     stars+=1
#     space-=1

# *****
#  ****
#   ***
#    **
#     *


# lines = 5
# stars = lines
# space = 0
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for i in range(stars):
#         print("*",end="")
#     print()
#     stars-=1
#     space+=1

#    *
#   ***
#  *****
# *******
  
#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# lines = 5
# stars = 1
# space = lines-1
# for j in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for i in range(stars):
#         print("*",end="")
#     print()
#     stars+=2
#     space-=1


#     *
#    ***
#   *****
#    ***
#     *

# lines = 5
# stars = 1
# space = lines-1
# mid = (lines//2)
# for j in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for i in range(stars):
#         print("*",end="")
#     print()
#     if j<mid:
#         stars+=2
#         space-=1    
#     else:
#         stars-=2
#         space+=1


        
# *      *
# * *  * *
# *  *   * 
# * *  * *
# *      *