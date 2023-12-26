# Advent of Code 2023 — Jonathan Chen

My solutions to days 1–12 of this year's [Advent of Code](https://adventofcode.com/2023), in Python 3.9.

Example use:

```sh
cd day_1
python3 soln.py A < input.txt
```

## Reflection

This year I completed 12 days of ~~Christmas~~ Advent of Code challenges. This was my first year tracking my progress with Git, and my first with this directory structure with the sys imports.

I decided to take a break from the midnight puzzle-solving after day 3 to focus on classwork. I resumed working from day 4 onward once I returned for winter break, working at a leisurely pace. Although I did not get as far as I did last year (15 days), I've had a lot of fun working through the challenges and trying out new things along the way. This year's Advent featured a lot more math than I recall from this website. Last year I got stuck on a hard DP for day 16; this year I finish with an albeit easier DP for day 12.

It seems my semesters as a TA for Fundamentals of CS 1 have conditioned me to write code in a modular and flexible way, and although I didn't follow any strict practices, you will find a multitude of helper functions strewn all over the code. It does help when reusing code in part B.

Here are the high-level strategies and techniques I used to solve each challenge. Needless to say this will include **spoilers**.

| Day                        | Part 1                                                                        | Part 2                                                                                   |
| -------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [Day 1](./day_1/soln.py)   | Use regex to remove non-numbers, then combine first and last characters.      | Parse forwards and backwords for something matching a number.                            |
| [Day 2](./day_2/soln.py)   | Keep track of running max red, green, blue to see if a game is valid.         | Reuse max r, g, b from part 1 and multiply them.                                         |
| [Day 3](./day_3/soln.py)   | Locate all numbers, then check adjacent spaces for symbols.                   | Locate all numbers, add asterisks to hash table `gear -> [adjacent numbers]`, using OOP. |
| [Day 4](./day_4/soln.py)   | Count wins using set intersection, raise 2^n using bit shift.                 | Build an array to keep track of number of scratch card repeats.                          |
| [Day 5](./day_5/soln.py)   | Turn each map into a function, chain them together, try all inputs.           | Reverse the maps and brute force from output=0.                                          |
| [Day 6](./day_6/soln.py)   | Use quadratic formula to get possible range formula, tweak edge cases.        | Regex to keep only digits, them feed into part 1.                                        |
| [Day 7](./day_7/soln.py)   | (Stable) Sort first pairwise, then type-wise to get rank.                     | Replace jokers with the most common other card, then same as part 1.                     |
| [Day 8](./day_8/soln.py)   | Traverse the graph until you reach ZZZ.                                       | Try all possible starts separately, then get their LCM.                                  |
| [Day 9](./day_9/soln.py)   | Behavior lines up with polynomials, extrapolate Lagrange interpolation.       | Same as part 1.                                                                          |
| [Day 10](./day_10/soln.py) | Find a pipe out of S, follow it until we reach S to get cycle length.         | Remove all extra pipes, use Jordan curve theorem row-by-row (left is always outside).    |
| [Day 11](./day_11/soln.py) | Map coordinates using prefix sum, then compute Manhattan distances.           | Same as part 1.                                                                          |
| [Day 12](./day_12/soln.py) | Use iterative 2-D DP to build up arrangements of broken locations and counts. | Same as part 1.                                                                          |

Advent of Code was a lot of fun! Maybe I'll do more days, maybe not. But hopefully I'll be back next year for more.
