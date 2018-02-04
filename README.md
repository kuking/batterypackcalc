# Battery Pack Calculator
Calculates how to distribute cells in a battery pack to reduce capacity difference between parallel packs.

i.e. you have 200 cells and know each cell's capacity; you want to build a S4P50 pack, so you need to
group 4 packs with 50 cells on each. This script will help you to decide which cells to put in each pack, 
so in the end, all the packs have a very similar capacity.

# Algorithm

Initially spreads the cells from higher to lower capacity following an "S" pattern around the packs.

Then it tries to reduce the mAh difference by swapping cells between packs, if trying a swap, the difference between 
the twp packs' capacity becomes closer to the average capacity of all the packs, it leaves the cells swapped.

This does not warranty to find the best solution, but it will probably be fast enough and good enough given a
non-trivial pack size (i.e. +12 cells).
 
I believe the perfect solution requires NP time to solve; but given enough cells and given the capacity measurements
have indeed a margin of error; this algorithm is probably good enough.


Configuration is almost self explanatory in the first couple of lines with the `cfg_` variables. Contact me if you 
need help.

# Output example

```

Cells in file: 18
Discarding cells with less than 1900 mah
Viable cells: 16
putting cell 14 of 2444 mAh into 1P 1S
putting cell 3 of 2421 mAh into 1P 2S
putting cell 4 of 2367 mAh into 1P 3S
putting cell 13 of 2300 mAh into 2P 3S
putting cell 7 of 2270 mAh into 2P 2S
putting cell 1 of 2260 mAh into 2P 1S
putting cell 2 of 2200 mAh into 3P 1S
putting cell 11 of 2185 mAh into 3P 2S
putting cell 12 of 2180 mAh into 3P 3S
putting cell 17 of 2178 mAh into 4P 3S
putting cell 19 of 2150 mAh into 4P 2S
putting cell 20 of 2133 mAh into 4P 1S
putting cell 18 of 2095 mAh into 5P 1S
putting cell 8 of 2053 mAh into 5P 2S
putting cell 9 of 1993 mAh into 5P 3S
A-B Swapping cell 14 for 4 between pack 1 and pack 3 makes delta 40 mAh
A-B Swapping cell 1 for 7 between pack 1 and pack 2 makes delta 18 mAh
A-B Swapping cell 3 for 14 between pack 2 and pack 3 makes delta 20 mAh
A-B Swapping cell 20 for 19 between pack 1 and pack 2 makes delta 7 mAh

Finished:
---------
Pack 1 with 11082 mAh using cells [2, 18, 4, 7, 19]
Pack 2 with 11075 mAh using cells [11, 8, 1, 14, 20]
Pack 3 with 11072 mAh using cells [13, 12, 17, 9, 3]
Biggest difference is between packs 1 and 3 with 10 mAh (0.09%).
1 cells left unused [10] ; unused capacity is 1960 mAh.

```