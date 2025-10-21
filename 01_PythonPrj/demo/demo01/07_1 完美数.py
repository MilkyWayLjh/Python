# // 它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身
#         // 如果一个数恰好等于它的真因子之和，则称该数为“完全数”。第一个完全数是6，第二个完全数是28，第三个完全数是496
#         function findNum(num) {
#             var sum = 0;
#             for (var i = 1; i < num; i++) {
#                 if (num % i == 0) {
#                     sum = sum + i;
#                 }
#             }
#             if (sum == num) {
#                 return true;
#             }
#             return false;
#         }
#
#         for (var i = 1; i <= 1000; i++) {
# /*          if (findNum(i) == true) {
#                 document.write(i + "<br>");
#             }*/
#             if (findNum(i)) {
#                 document.write(i + "<br>");
#             }
#         }


