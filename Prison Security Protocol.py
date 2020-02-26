#question
There is a highly secure prison which holds most dangerous criminals in the world. On 2nd November 2019 the prison officials received a warning that there was an attack planned on the prison to free the criminals. So, the prison officials planned a quick evacuation plan. They planned to shift all the criminals in the prison to a different place. A military level armoured vehicle is waiting at the prison gate, they want to load all the prisoners inside the vehicle so they can be transferred to a secure location. The prison has certain number of cells and each cell has certain number of people and no cells are empty. As a safety method, the prison officials would like to group two cells together at one time, so prisoners from two cells will be moved to a dormitory. Once you narrow the prisoners to two dormitories, you can then combine them to send them into the armoured vehicle. Shifting one prisoner from one cell to another will take one minute.

For example, let’s say there are three cells A, B and C. Prisoner from any of the two cells are moved to a dormitory, let’s say we are combining cells A and B to form AB, now we are left with two blocks of prisoners, now we can add them to the vehicle, so what will be the minimum time taken in total to load all the prisoners into the vehicle?

Input Format

The first line of input has one integer input N, where N is the number of cells in the prison. The sedond line of input has N spaced integers specifying the number of prisoners in each cell and no cell is empty.

Constraints

2<=N<=10^9 1<=a[i]<=10^9 N - Number of cells a[i] - prisoner count in i'th cell

Output Format

Minimum possible integer

Sample Input 0

32
434681861 826106336 315246265 195198309 380643317 591750682 880003886 86499344 709046724 724859050 963537255 117790724 856010747 802310254 910747254 523424125 203996953 293655521 652630821 328477875 647628390 146328330 356102622 371434543 504310497 451735061 662649579 328832081 229174946 801508727 711995059 140142379
Sample Output 0

189498297338
