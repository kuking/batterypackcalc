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

Cells in file: 26
Discarding cells with less than 1950 mah
Viable cells: 24
Initial setup ...
adding cell 14 of 2444 mAh into 1p1s (5P4S)
adding cell 3 of 2421 mAh into 1p2s (5P4S)
adding cell 4 of 2367 mAh into 1p3s (5P4S)
adding cell 13 of 2300 mAh into 1p4s (5P4S)
adding cell 7 of 2270 mAh into 2p4s (5P4S)
adding cell 1 of 2260 mAh into 2p3s (5P4S)
adding cell 2 of 2200 mAh into 2p2s (5P4S)
adding cell 11 of 2185 mAh into 2p1s (5P4S)
adding cell 12 of 2180 mAh into 3p1s (5P4S)
adding cell 17 of 2178 mAh into 3p2s (5P4S)
adding cell 15 of 2160 mAh into 3p3s (5P4S)
adding cell 19 of 2150 mAh into 3p4s (5P4S)
adding cell 20 of 2133 mAh into 4p4s (5P4S)
adding cell 21 of 2127 mAh into 4p3s (5P4S)
adding cell 16 of 2123 mAh into 4p2s (5P4S)
adding cell 18 of 2095 mAh into 4p1s (5P4S)
adding cell 8 of 2053 mAh into 5p1s (5P4S)
adding cell 25 of 2031 mAh into 5p2s (5P4S)
adding cell 28 of 2009 mAh into 5p3s (5P4S)
adding cell 26 of 2006 mAh into 5p4s (5P4S)
A-B Swapping cell 11 for 19 between pack 1 and pack 4 makes delta 30 mAh
A-B Swapping cell 25 for 26 between pack 2 and pack 4 makes delta 9 mAh

Finished:
---------
Pack 1 with 10922 mAh using cells [8, 12, 14, 18, 19]
Pack 2 with 10928 mAh using cells [2, 3, 16, 17, 26]
Pack 3 with 10923 mAh using cells [1, 4, 15, 21, 28]
Pack 4 with 10919 mAh using cells [7, 11, 13, 20, 25]
Biggest difference is between packs 2 and 4 with 9 mAh (0.08%).
4 cells left unused [9, 10, 22, 23] ; unused capacity is 7902 mAh.

```