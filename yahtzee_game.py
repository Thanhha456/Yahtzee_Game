"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
# import codeskulptor
#
# codeskulptor.set_timeout(20)


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.
    hand: full yahtzee hand
    Returns an integer score
    """
    score = []
    for die in hand:
        num = hand.count(die)
        score.append((num*die))
        max_score = max(score)
    return max_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    all_seq = gen_all_sequences(range(1, num_die_sides + 1), num_free_dice)
    sum_value = 0
    for seq in all_seq:
        if held_dice != 0:
            hand = held_dice + seq
        else:
            hand = seq
        sum_value += score(hand)
        print(seq, score(hand))
    exp_value = sum_value/len(all_seq)
    return exp_value


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """


    if hand == tuple([]):
        return set([()])
    else:
        hand = list(hand)
        result = set([()])
        for seq in gen_all_holds(tuple(hand[:-1])):
            seq_0 = list(seq)
            seq_0.append(hand[-1])
            result.add(tuple(seq_0))
        result.update(gen_all_holds(tuple(hand[:-1])))

        return result

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    max_expect_score = []
    held_seqs = gen_all_holds(hand)
    for held_seq in held_seqs:
        num_free_dice = len(hand) - len(held_seq)
        hand_score = expected_value(held_seq, num_die_sides, num_free_dice)
        max_expect_score.append((hand_score, held_seq))
    max_score = max(max_expect_score)

    return max_score


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)


#
# hand = (1, 2, 3, 4, 5)
# num_die_sides = 6
# print(score(hand))
# print(expected_value((2, 2), 6, 2))
# print(expected_value(0, 3, 3))
# print(gen_all_holds(hand))
# print(strategy(hand, num_die_sides))
run_example()
import poc_holds_testsuite
poc_holds_testsuite.run_suite(gen_all_holds)