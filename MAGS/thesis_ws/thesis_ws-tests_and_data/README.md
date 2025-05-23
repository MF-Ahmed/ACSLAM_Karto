Tests to perform
================

## Data collected in the `.npy` file:
* Percentage map covered
* Number of actual points used vs number of total points detected
* Radius used
* Percentage used

### Files to store
* `.npy` file for simulation
* `.g2o` file for graph
* `.yaml` and `.pgm` for map through map saver

## Simulations and comparisons to perform
* 1 robot: 
    - [x] [new algorithm](/asynchronous_approach/R1/)
    - [ ] original algorithm
    - [ ] comparison of the occupied map over time

* 2 robots:
    * Simulations:
        - [x] [synchronous approach](/synchronous_approach/R2/)
        - [x] [asynchronous approach](/asynchronous_approach/R2/)
    * Comparisons:
        - [ ] percentage of merged map occupied over time

* 3 robots:
    * Simulations:
        - [x] [synchronous approach](/synchronous_approach/R3/)
        - [x] [asynchronous approach](/asynchronous_approach/R3/)
    * Comparisons:
        - [ ] percentage of merged map occupied over time


## Other tests
Keeping 2 or 3 robots as constants (check the computational weight to be easyly manageable):
- [ ] synchronous approach without limitations on number of points in the list (or by limiting it to 20-30 pts)
- [ ] asynchronous approach without limitations on number of points in the list (or by limiting it to 20-30 pts)