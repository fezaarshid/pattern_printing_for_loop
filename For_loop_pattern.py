
# n=5
# for i in range(n):
#     for j in range(n-i):
#
#         print("*",end=" ")
#     print()
#
# output

# * * * * *
# * * * *
# * * *
# * *
# *

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# output

# *
# * *
# * * *
# * * * *
# * * * * *


# triangle pattern
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(" * ",end=" ")
#     print()

#output

# *
# * *
# * * *
# * * * *
# * * * * *


# square pattern
# n=5
# for i in range(n):
#     for j in range(n):
#       print(" ", end="")
#     for j in range(n):
#       print("*",end=" ")
#     print()

#output
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


#
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#             print("*",end=" ")
#     print()

# output
#           *
#         * *
#       * * *
#     * * * *
#   * * * * *


# down right triangle
# n=5
# for i in range(n):
#     for j in range(i+1):
#       print("  ",end=" ")
#     for j in range(n-i):
#         print(" * ",end="")
#     print()

#output

# * * * * *
# * * * *
# * * *
# * *
# *


#
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#output
# * * * * *
# *       *
# *       *
# *       *
# * * * * *


#
# n=10
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1 or i==j or j==n-i-1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#output
# * * * * * * * * * *
# * *             * *
# *   *         *   *
# *     *     *     *
# *       * *       *
# *       * *       *
# *     *     *     *
# *   *         *   *
# * *             * *
# * * * * * * * * * *


# diagonal
# n=10
# for i in range(n):
#     for j in range(n):
#         if i==j or j==n-i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#output
# *                 *
#   *             *
#     *         *
#       *     *
#         * *
#         * *
#       *     *
#     *         *
#   *             *
# *                 *



#
# n=10
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==n-1 or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#output
# * * * * * * * * * *
#   *               *
#     *             *
#       *           *
#         *         *
#           *       *
#             *     *
#               *   *
#                 * *
#                   *


#
# n=10
# for i in range(n):
#     for j in range(n):
#         if i==n-1 or j==n-1 or j==n-i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#output
#                   *
#                 * *
#               *   *
#             *     *
#           *       *
#         *         *
#       *           *
#     *             *
#   *               *
# * * * * * * * * * *


# triangle
# n=6
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(" * ",end=" ")
#     print()


#output
   #         *
   #       *   *
   #     *   *   *
   #   *   *   *   *
   # *   *   *   *   *


# reverse triangle
# n = 5
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(n - i):
#         print(" * ", end=" ")
#     print()

#output
# *   *   *   *   *
#    *   *   *   *
#      *   *   *
#        *   *
#          *


# diamond
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print(" * ",end=" ")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print(" * ",end=" ")

#output
 #         *
 #       *   *
 #     *   *   *
 #   *   *   *   *
 # *   *   *   *   *
 #   *   *   *   *
 #     *   *   *
 #       *   *
 #         *


#
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j or j==n-i-1 or i==0 or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#output
# * * * * *
#   *   *
#     *
#   *   *
# * * * * *