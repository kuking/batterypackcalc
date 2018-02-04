# Battery Pack Calculator
Calculates how to distribute cells in a battery pack to reduce capacity difference between parallel packs.

i.e. you have 200 cells and you have measured each one's capacity, you want to build a S4P50 pack, so you need to
build 4 packs with 50 cells on each. This script will help you to decide which cells to put in each pack, 
so at the end each pack has a very close capacity.

# Algorithm

Initially spreads the cells from higher to lower capacity following an "S" pattern around the packs.


Then it tries to reduce the difference by swapping cells between packs. First  tries to reduce the difference between
the packs with bigger delta in capacity, then picks them two by two... 
It will not find the best solution but probably fast enough and good enough for reasonable size pack. I believe
the perfect solution is NP Complete but given enough cells and given that measuring capacity has a margin of error
this algorithm should be good enough.


Configuration is almost self explanatory in the first couple of lines with the `cfg_` variables. Contact me if you 
need help.