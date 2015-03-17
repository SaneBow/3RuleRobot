# 3RuleRobot

## A simple robot demonstration

I remember I saw this kind of simple rule robot experiment in a TV program on CCTV 9 when I was in high school. 
When I was in my fresh year of undergraduate, memory recalled and I decided to write a program to simulate it.
However, I can't find the source of this idea since I did't remember the TV programe name. 
I also forgot the exact rules, but I still remember the astonishing feeling.
It shows me how simple the rules can be and what the robots can accomplish.
After thinking for a day or two, I invent my version of "3 rules", which inspired by ants in some sense.
Then I write this python program to see if it works.
Suprisingly, it works well. 
Initially, some plates are put at random places, then we put some running 3-rule-robots into the pole.
It turns out that the plates will eventually be gathered by the robots and crowd around one spot.

In this demonstration, "robots" are represented by red circles and "plates" are green circles.

The robots obey only 3 simple rules as follows:
- When a non-loaded robot meets a plate, pick it up and turn back.
- When a loaded robot meets a plate, unload the plate and turn back 
- When meets wall or another robot, turn back.

To run this program, you need pygame module for python.
Tested on Windows system with python 2.7 and pygame 1.9.1 installed.