# Battery Pack Calculator
Calculates how to distribute cells in a battery pack to reduce capacity difference between packs.

# Algorithm

Initially spreads the cells from higher to lower capacity in doing an "S" around packs.
Then it tries to reduce the difference by swapping cells between packs. First  tries to reduce the difference between
the packs with bigger delta in capacity, then picks them two by two... 
It will not find the best solution but probably fast enough and good enough for reasonable size pack. I believe
the perfect solution is NP Complete but given enough cells and given that measuring capacity has a margin of error
this algorithm should be good enough.

Configuration is almost self explanatory in the first couple of lines with the `cfg_` variables. Contact me if you 
need help.