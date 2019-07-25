# nqueens
Improvement 3 - Staircase Placement
	It’s still too slow. After scouring the Wikipedia page, I came across the representation of N-Queens placement as a math problem. I thought that explicit placement of queens would be much faster than a search, and I was right. It’s much, much faster, completing 10 million N in 3.5 seconds (Whoo 🤪🤪). The formula is based off the remainder of (N-2)/6. The remainder can be either 0, odd, or some other even number that isn't 0. 

The case of even remainder not = 0 is the easiest, because it just looks like a staircase. Place the queen on row 0 at position 1, and move 2 spaces right for every row until row = N/2. At row = N/2 + 1, place the queen at position 0 and continue the L pattern from before. For example, when N = 6, the solution is [1, 3, 5, 0, 2, 4]. This solution is also all the odd numbers up to N, followed by all the even numbers. Yet another way to think about this solution is the most compact way to organize queens that don’t attack each other (the L pattern), repeated and offset for the second half. Why does this work? We know that the board is good for rows 0 to N/2, and for rows N/2 + 1. How we can be sure that the queens in the first half won’t attack the queens in the second half is a better question to ask. Since the second half of the board is a horizontal offset of the first half by 1, and a vertical offset by N/2, both vertical and diagonal collisions are not possible. A vertical offset of N/2 with no horizontal offset results in every queen (except the first and last placed) having a diagonal collision, so offsetting horizontally by 1 would remove all of these collisions. But what about the first and last queens? If we set the first half of the board as even numbers, and the second half as odd numbers, the first and last queens will end up attacking each other. The way to fix this (i spoiled it with the picture above) is the set the top half as odd numbers, and the bottom half as even numbers. With this solution, the two big diagonals are left open, which will be really important later. Another way to visualize this proof is to give “equations” to each queen’s diagonal. Any two queens with the same equation will be in the path of each other. Since we know that the queens won’t attack each other in their respective halves, we only need to make an equation for slopes parallel to the y = x line. The coordinate (0,0) is the bottom left corner of the board, and (1,1) is the top right corner of the bottom left square. All diagonal slopes are 1, so we only need to check the b values (in y = mx + b) to make sure any two queens don’t have the same equation. Assigning b values to queens in the first half turns out to be a sequence, b=N-2 for row 0 and decreases by 3 for each row. For the second half, b starts at N/2 - 1, and decreases by 3 for each row. Checking if the b values at row 0 and N/2 - 1 have the same modulo of 3 is enough to check if any b values are the same, because both halves have b decreasing by 3 each row. If (N-2)%6 isn’t 0 and N is even (which is the case we’re looking at), then (N-2)%3 is either 1 or 2, and (N/2 - 1)%3 will never be equal to (N-2)%3, because N%3 is either 0 or 1 respectively, and N/2 multiplies the modulus with respect to 3 by 2. Taking that all together, (N-2)%3 is either 1 or 2, and (N/2 - 1)%3 is either 2 or 0 respectively. That’s a difference of 2 for each, which can be seen in the graph. (i know 1 isn’t 1 away from 2, but the mod function makes absolute differences fuzzy so it seems like a difference of 1.) Thus, any two b values will never be the same and the solution always works when (N-2)%6 isn’t equal to 0. I think b values are how the proof was formed, or at least a more mathematical rendition of what I said, which is really cool! I didn’t fail my first actual proof! The formula can also be altered so that (N-2)%3 isn’t 0, instead of (N-2)%6, because the b values change by 3 for each row. I think 6 was used in the formula to better differentiate between even and odd numbers.














This is a graph of the first (red) and middle (blue) b values shows that they will never be equal for N ≠ 3K + 2 (When N%6 is 2, the graphs come to the same point, which I’ll talk about next)

The case for the even remainder = 0 is a little more complicated. (When using the method from before, the b values are the same and all queens except the first and the last attack each other, which is why the lines intersect at y = 3. They meet at y = 0 because of the other way to make a staircase solution, with even numbers on the top half and odd numbers on the bottom half. In this solution, only the first and last queens attack each other.) To circumvent this, we need to choose b values for row 0 and row N/2 + 1 that don’t have the same modulo of 3. Placing the first queen on position N+2 and beyond runs out of spaces on the right hand side faster than the rows are used up, so we  need to “roll over” the queen and place it like we kept counting from the end. With rolling over, we now need to make sure b0 % 3 isnt equal to bn/2 + 1 % 3, and that pos0 % 2 isn’t equal to posn/2 + 1 % 2, so that there are no vertical collisons. (I tried to write a small program to do this, where “b” was just N-pos-1, and pos0 and posn/2 + 1  were the variables I wanted to get, but this proved to be really frustrating because there were always more things to account for and i gave up :/. Some problems arise when trying to roll queens over, because it’s really hard to check the b value of the overlap from the row N/2 + 1 queen alone. Even thinking graphically, it is impossible to account for the opposite diagonal with a simple mod function (for overlapping). I even tried nested mod functions to make sure I didn’t get any extraneous b values, but that just left me more confused than before.) The interesting thing (ironically i wrote this next section just as an observation, but it’s the thing that helped me finish the proof :) about these puzzles is that the first (N+2)/4 (rounded up) rows and the last (N+2)/4 rows are just reflections of each other. The middle rows can be split into 2 halves, which are reflections too. (by reflections i mean over both the x and the y axis, which go through the middle of the board.) Graphing b values is still a correct way to prove the solution, but its really icky and the graphs are not at all intuitive. The reason we need two graphs is because the amount the queens overlap by isn’t constant. It can either be 0 or 1 spaces to the right of the left edge, and I think the amount switches for every board. For example, N=8 has the first overlapping queen 1 space from the edge, while N=14 has it on the edge. By extension, N=24 should have the first overlapping queen one space off from the edge. Because of this, we need 2 graphs, one for 8 + 12k, and one for 14 + 12k. The first graph below is the 8 + 12k case, and the second is the 14 + 12k. Lots of questions come from these graph. Why are there only 3 functions? Aren’t there 4 sections? Yes! This seems contradictory, like the solution should not work because there are 4 sections, and at least 2 of those sections have to have the same modulo of 3. This happens, but the solution circumvents it in a clever way. The only 2 sections that never have a chance to hit diagonally are the middle 2 sections, because they are offset horizontally by 4. (the second middle section starts at N/2 + 3) This also means that if the middle queens were extended on the other section, they would collide. The first function is the b value mod of the first section, the second function is the middle section, and the third function is the third section. The ceil function is used for the rounding up part of the function, which actually turns out be to important. I never used the ceil function before this class. (the second graph might not look like an actual solution, but it is since there are 3 distinct mod values that i highlighted)





















These two graphs show that the b values will never be equal when N = 3K + 2 

***This leaves us with the question : Why do the overlaps not attack each other and their respective halves? Honestly, I don’t know. I know it has something to do with the fact that (N-2)%3 is 0, because this same overlapping strategy doesn’t work when (N-2)%3 isn’t 0. I’m sure you could construct mod equations for the b values and simplify, but the problem gets so much more complicated due to the fact that the amount the queens overlap by isn’t constant. It can either be 0 or 1 spaces to the right of the left edge, and I think the amount switches for every board. For example, N=8 has the first overlapping queen 1 space from the edge, while N=14 has it on the edge. Basically, this is really hard, and I think I need more time (years) to think about it.*** I left this section in to show you the challenges I faced, and that I actually gave up before coming back to the problem. 


	






There is a reason I left odd boards for last, and it’s because they’re the easiest. In both even board cases, the major diagonals were left open. Increasing the board size by one means we have an extra column and row, so the new queen can be stuck in the corner than expands the board.





I tilted it so it looks like the ones I’ve been showing you




