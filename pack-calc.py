#!/usr/bin/env python3

import csv
import operator
import sys
from collections import OrderedDict

cfg_S = 4
cfg_P = 5
cfg_min_mah = 1950  # don't include in cells with less than X mah
cfg_delta_mah_happy = 25  # stop optimising when pack has less than X mah among themselves

cfg_csv = 'cells.csv'
cfg_csv_col_no = 0
cfg_csv_col_mah = 3


def group_capacity(group, cells):
    return sum(map(lambda cell_no: cells[cell_no], group))


def capacities(groups, cells):
    result = {}
    for no, all_cell_no in groups.items():  # this can be one big expression
        result[no] = group_capacity(all_cell_no, cells)
    return result


def calc_avg_capacity(capacities):
    total = 0
    for n in capacities.keys():
        if n is not 0:
            total = total + capacities[n]
    return total / (len(capacities.keys()) - 1)


def calc_max_delta(capacities):
    max_delta = 0
    delta_a = -1
    delta_b = -1
    for a in range(1, len(capacities)):
        for b in range(a, len(capacities)):
            delta = abs(capacities[a] - capacities[b])
            if max_delta < delta:
                max_delta = delta
                delta_a = a
                delta_b = b
    return max_delta, delta_a, delta_b


def find_swap_to_minimize_difference_to(group_a, group_b, cells, target_mah):
    cap_a = group_capacity(group_a, cells)
    cap_b = group_capacity(group_b, cells)
    best_diff = abs(cap_a - target_mah) + abs(cap_b - target_mah)
    best_swap = None, None, 0
    if best_diff == 0:
        return best_swap

    for cell_a in group_a:
        for cell_b in group_b:
            test_group_a = list(group_a)
            test_group_b = list(group_b)
            test_group_a.remove(cell_a)
            test_group_b.remove(cell_b)
            test_group_a.append(cell_b)
            test_group_b.append(cell_a)

            test_cap_a = group_capacity(test_group_a, cells)
            test_cap_b = group_capacity(test_group_b, cells)

            test_diff = abs(test_cap_a - target_mah) + abs(test_cap_b - target_mah)

            if best_diff > test_diff:
                best_diff = test_diff
                best_swap = cell_a, cell_b, best_diff

    return best_swap


cells = {}

with open(cfg_csv) as csv_file:
    for row in csv.reader(csv_file):
        try:
            cell_no = int(row[cfg_csv_col_no])
            cell_mah = int(row[cfg_csv_col_mah])
            cells[cell_no] = cell_mah
        except ValueError:
            pass  # blindly assumes some cells to be wrong

print("Cells in file:", len(cells))
print("Discarding cells with less than %i mah" % cfg_min_mah)
cells = dict((k, v) for k, v in cells.items() if v > cfg_min_mah)
print("Viable cells:", len(cells))

if len(cells) < cfg_S * cfg_P:
    print("I'm sorry but for building a %iS%iP you need at least %i cells, but you got %i."
          % (cfg_S, cfg_P, cfg_S * cfg_P, len(cells)))
    sys.exit(-1)

cells = OrderedDict(sorted(cells.items(), key=operator.itemgetter(1)))

groups = {0: list(cells.keys())}
for i in range(1, cfg_S + 1):
    groups[i] = []

print("Initial setup ...")
# iteration 1, put one on each pack ordered by higher rate to lower rate following an 'S' shape to make it more likeky
# to be balanced

for p in range(1, cfg_P + 1):
    for s in range(1, cfg_S + 1):
        cell_no = groups[0].pop()
        if p % 2 == 0:
            this_s = cfg_S - s + 1
        else:
            this_s = s
        print("adding cell %i of %i mAh into %ip%is (%iP%iS)" % (cell_no, cells[cell_no], p, this_s, cfg_P, cfg_S))
        groups[this_s].append(cell_no)

curr_capacities = capacities(groups, cells)
avg_capacity = calc_avg_capacity(curr_capacities)
max_delta, a, b = calc_max_delta(curr_capacities)
something_changed = True
while max_delta > cfg_delta_mah_happy and something_changed:
    something_changed = False

    for a in range(1, len(groups)):
        for b in range(a, len(groups)):
            cell_a, cell_b, delta = find_swap_to_minimize_difference_to(groups[a], groups[b], cells, avg_capacity)
            if cell_a is not None and cell_b is not None:
                print("A-B Swapping cell", cell_a, "for", cell_b, "between pack", a, "and pack", b,
                      "makes delta", int(delta), "mAh")
                groups[a].remove(cell_a)
                groups[b].remove(cell_b)
                groups[b].append(cell_a)
                groups[a].append(cell_b)
                curr_capacities = capacities(groups, cells)
                avg_capacity = calc_avg_capacity(curr_capacities)
                something_changed = True

    max_delta, a, b = calc_max_delta(curr_capacities)

print()
print("Finished:")
print("---------")
if max_delta > cfg_delta_mah_happy:
    print("I could not achieve target of", cfg_delta_mah_happy, "mAh delta... ")
    print("It does not means it does not exist, but i'm a greedy algorithm.")
    print()

for n in range(1, len(groups)):
    print("Pack", n, "with", curr_capacities[n], "mAh using cells", sorted(groups[n]))

print ("Biggest difference is between packs %i and %i with %i mAh (%2.2f%%)."
       % (a, b, max_delta, max_delta * 100.0 / curr_capacities[1]))

if len(groups[0]) == 0:
    print("All the cells used in the packs!")
else:
    print(len(groups[0]), "cells left unused", sorted(groups[0]), "; unused capacity is", curr_capacities[0], "mAh.")
