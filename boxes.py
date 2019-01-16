#!/usr/bin/python                                                                     

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Implementation of closest point detection and testing using hypothesis.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###########################################
###               IMPORTS               ###
###########################################

from hypothesis import given, settings
import hypothesis.strategies as st

###########################################
###            FUNCTION DEFS            ###
###########################################

#============================================================================#
# Find nearest points (returned as tuple of tuples).
def find_nearest(chart):
    height = len(chart)
    width = len(chart[0])

    # Find all 'x' coords
    xs = []
    for r in range(height):
        for c in range(width):
            if chart[r][c] == 'x':
                xs.append((r, c))

    # Box can at maximum have radius the maximum of height and width of the chart.
    for r in range(1, height + width):
        # For each r, we iterate over all points with manhattan
        # distance r from each x and see if we encounter a 'y'.
        for (x_row, x_col) in xs:
            for c in range(0, r + 1): 
                query_points = [
                    (c, r - c),
                    (-c, r - c),
                    (c, -(r - c)),
                    (-c, -(r - c))
                ]

                for (d_row, d_col) in query_points:
                    q_row = x_row + d_row
                    q_col = x_col + d_col

                    if 0 <= q_row and q_row < height and 0 <= q_col and q_col < width:
                        if chart[x_row + d_row][x_col + d_col] == 'y':
                            return ((x_row, x_col), (q_row, q_col))

    return None

#============================================================================#
# Find all nearest points (returned as list of tuples of tuples) (brute force)
def find_nearest_brute_force(chart):
    height = len(chart)
    width = len(chart[0])

    # Find all 'x' and 'y' coords
    xs = []
    ys = []
    for r in range(height):
        for c in range(width):
            if chart[r][c] == 'x':
                xs.append((r, c))
            elif chart[r][c] == 'y':
                ys.append((r, c))

    best_pair = []
    best_dist = height + width

    for (x_row, x_col) in xs:
        for (y_row, y_col) in ys:
            dist = abs(x_row - y_row) + abs(x_col - y_col)
            if dist < best_dist:
                best_dist = dist
                best_pair = [((x_row, x_col), (y_row, y_col))]
            elif dist == best_dist:
                best_pair.append(((x_row, x_col), (y_row, y_col)))

    return best_pair

###########################################
###              Testing                ###
###########################################         

# Basic tests
test1 = ([
    [ 'x', ' '],
    [ 'y', ' ']
], ((0,0), (1,0)))

test2 = ([
    [ 'x', 'y'],
    [ ' ', 'y']
], ((0,0), (0,1)))

test3 = ([
    [ 'x', ' ', ' ' ],
    [ ' ', ' ', ' ' ],
    [ ' ', 'y', 'y' ]
], ((0,0), (2,1)))

test4 = ([
    [ 'x', ' ', ' ' ],
    [ ' ', ' ', 'x' ],
    [ ' ', 'y', 'y' ]
], ((1,2), (2,2)))

test5 = ([
    [ 'x', ' ', ' ' ],
    [ ' ', ' ', 'x' ],
    [ 'x', ' ', ' ' ],
    [ ' ', ' ', 'y' ],
    [ ' ', 'y', ' ' ],
    [ ' ', ' ', 'y' ]
], ((1,2), (3,2)))
   
tests = [ test1, test2, test3, test4, test5 ]

def test_basic():
    for (test, expect) in tests:
        assert(find_nearest(test) == expect)
        
    for (test, expect) in tests:
        assert(find_nearest_brute_force(test) == [expect])

# Property testing using hypothesis
def gen_chart(xs, ys):
    chart = [ [ ' ' for _ in range(101) ] for _ in range(101) ]
    for (x_row, x_col) in xs:
        chart[x_row][x_col] = 'x'
    for (y_row, y_col) in ys:
        chart[y_row][y_col] = 'y'

    return chart

@given(xs = st.lists(st.tuples(st.integers(min_value=0, max_value=100), st.integers(min_value=0, max_value=100))), ys = st.lists(st.tuples(st.integers(min_value=0, max_value=100), st.integers(min_value=0, max_value=100))))
@settings(deadline=None, max_examples=500)
def test_boxes_matches_brute_force(xs, ys):
    chart = gen_chart(xs, ys)
    nearest_pairs = find_nearest_brute_force(chart)
    found_pair = find_nearest(chart)
    assert ((found_pair is None and nearest_pairs == []) or found_pair in nearest_pairs)

###########################################
###            Main Function            ###
###########################################         

if __name__ == '__main__':
    test_basic()
    test_boxes_matches_brute_force()
