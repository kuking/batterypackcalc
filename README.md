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

# Output example

```

Cells in file: 14
Discarding cells with less than 2000 mah
Viable cells: 10
putting cell 14 of 2444 mAh into 1P 1S
putting cell 3 of 2421 mAh into 1P 2S
putting cell 4 of 2367 mAh into 1P 3S
putting cell 13 of 2300 mAh into 2P 3S
putting cell 7 of 2270 mAh into 2P 2S
putting cell 1 of 2260 mAh into 2P 1S
putting cell 2 of 2200 mAh into 3P 1S
putting cell 11 of 2185 mAh into 3P 2S
putting cell 12 of 2180 mAh into 3P 3S
A-B Swapping cell 2 for 12 between pack 1 and pack 3 makes delta 17 mAh

Finished:
---------
Biggest delta is 17 mAh between pack 1 and 3
Pack 1, cells [14, 1, 12]  capacity: 6884 mAh
Pack 2, cells [3, 7, 11]  capacity: 6876 mAh
Pack 3, cells [4, 13, 2]  capacity: 6867 mAh
Cells left [8] unused capacity is 2053 mAh
Biggest difference between packs is 17 mAh between pack 1 and 3.

```