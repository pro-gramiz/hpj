#question
Cupid, is the Roman god of love. It is beleived that if we get shot by the cupids arrow, love will find us. Some people beleive its true whereas few people beleive its just a myth. Once Cupid wants your help to make a match! There are N people in a hall standeing in a straight line, for a valentines day event and each person will be given a random number from 1 to n (all numbers need not be present and repeated numbers are also preesent). Two numbers are chosen at random from those numbers, and how many least members can be removed so that those two members can be brought together.
Input Format
The first line of input has one integer input N which corresponds to the number of people standing in the line The second line of input has N spaced integers as input which corresponds to the numbers given to each person The third line of input has two spaced integers which will denote two chosen numbers
Constraints
1<=N<=10^9 where N is the number of people in the line 1<=a[i]<=10^9 where a[i] corresponds to one of the number for each person
Output Format
The minimum number of people to be removed from the line to bring them together
Sample Input 0
294
262 669 733 92 404 201 64 936 146 427 545 978 787 601 1 975 501 716 588 687 69 98 857 293 663 411 661 411 164 112 343 683 60 760 599 419 496 784 288 109 658 828 251 646 194 700 149 481 57 703 512 238 720 907 106 150 925 384 750 798 825 532 761 750 191 154 260 762 811 454 415 365 700 500 649 259 22 122 440 426 198 847 980 732 320 751 887 197 609 888 785 193 243 264 657 799 197 977 272 433 664 881 618 743 171 592 417 458 923 947 307 968 263 325 388 598 219 372 785 790 557 693 634 860 60 82 649 899 954 559 283 344 119 579 765 289 322 511 310 250 948 77 344 465 491 932 683 211 588 581 401 287 671 188 2 160 473 188 905 114 167 252 268 314 815 703 949 885 211 207 169 917 180 33 7 476 354 750 994 414 23 505 77 819 264 281 221 722 288 696 171 86 643 586 696 572 626 277 548 653 492 620 3 860 881 132 343 794 298 373 6 58 165 270 768 727 514 161 766 14 317 800 857 803 730 438 493 677 276 790 271 162 266 621 780 929 401 329 72 302 598 832 111 170 166 299 319 88 707 3 508 906 853 516 253 540 244 934 456 995 702 322 374 924 845 801 560 822 697 11 569 222 216 69 358 257 81 320 491 889 706 368 32 269 987 407 33 677 245 357 634 689 34 464
784 787
Sample Output 0
24
************************************************************************************************************************************
#answer
n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=[]
if(x.count(a)==1 and x.count(b)==1):
    print(x.index(a)-x.index(b)-1 if x.index(a)>x.index(b) else x.index(b)-x.index(a)-1)
elif(x.count(a)>1 or x.count(b)>1):
    for i in range(n):
        if a==x[i]:
            c.append(i)
        elif b==x[i]:
            d.append(i)
    z=n
    for i in c:
        for j in d:
            if i>j and i-j<=z:
                z=i-j-1
            elif j>i and j-i<=z:
                z=j-i-1
    print(z)
