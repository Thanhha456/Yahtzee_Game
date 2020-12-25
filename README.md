This project is for assessment in Principles of Computing (Part 1) from Rice University.  
https://www.coursera.org/learn/principles-of-computing-1  

#**MiniProject: Yahtzee**

*Overview*

Yahtzee is a dice game played with 5 dice where you try to score the most points by matching certain combinations. You can play the game her
e. In Yahtzee, you get to roll the dice three times on each turn. After the first roll, you may hold as many dice as you would like and roll
 the remaining free dice. After this second roll, you may again hold as many dice as you would like and roll the rest. Once you stop (either
 because you have exhausted your three rolls or you are satisfied with the dice you have), you score the dice in one box on the score card.

To simplify the mini-project, we will only consider scores corresponding to the "upper" section of the scorecard. Boxes in the upper section
 correspond to numbers on the dice. 

Your task is to implement the following four functions: scoree, expected_value, gen_all_holds, and strategy. These four functions should do
the following:

- score(hand): This function takes as input a tuple hand that represents the die values in the given Yahtzee hand. Since ordering of the d
ie values in Yahtzee hands is unimportant, tuples corresponding to Yahtzee hands will always be stored in sorted order to guarantee that eac
h tuple corresponds to a unique Yahtzee hand. The function score(hand) computes a score for hand as the maximum of the possible values for e
ach choice of box in the upper section of the Yahtzee scorecard.
- expected_value(held_dice, num_die_sides, num_free_dice): This function computes the expected value of the scores for the possible Yahtze
e hands that result from holding some dice and rolling the remaining free dice. The dice being held are specified by the sorted tuple held_d
ice. The number of sides and the number of dice that are free to be rolled are specified by num_die_sides and num_free_dice, respectively. Y
ou should use gen_all_sequences to compute all possible rolls for the dice being rolled. As an example, in a standard Yahtzee game using fiv
e dice, the length of held_dice plus num_free_dice should always be five.
- gen_all_holds(hand): This function takes a sorted tuple hand and returns the set of all possible sorted tuples formed by discarding a su
bset of the entries in hand. The entries in each of these tuples correspond to the dice that will be held. If the tuple hand has the entries
 (h0,h1,...,hm−1), the returned tuples should have the form (hi0,hi1,...,hik−1) where 0≤k≤m0 and the integer indices satisfy 0≤i0<i1<...<ik−
1<m. In the case where values in the tuple hand happen to be distinct, the set of tuples returned by gen_all_holds will correspond to all po
ssible subsets of hand.  
- strategy(hand, num_die_sides): This function takes a sorted tuple hand and computes which dice to hold to maximize the expected value of
 the score of the possible hands that result from rolling the remaining free dice (with the specified number of sides). The function should
return a tuple consisting of this maximal expected value and the choice of dice (specified as a sorted tuple) that should be held to achieve
 this value. If there are several holds that generate the maximal expected value, you may return any of these holds.





