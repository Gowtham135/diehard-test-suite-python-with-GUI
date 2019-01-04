# Diehard-test-suite-python-with-GUI

Diehard is a combination of statistical test suites for quality analyses of any random number generator. The diehard library can be used in the command line to test our data. To ease the implementation we have developed a GUI (Graphical User Interface) for Diehard using Tkinter in python 3. List of the tests that can be performed using Diehard are listed below 
```bash
test no(d)     Test Name 
0		       diehard_birthdays
1		       diehard_operm5
2		       diehard_rank_32x32
3		       diehard_rank_6x8
4		       diehard_bitstream
5		       diehard_opso
6		       diehard_oqso
7		       diehard_dna
8		       diehard_count_1s_str
9		       diehard_count_1s_byt
10		       diehard_parking_lot
11		       diehard_2dsphere
12		       diehard_3dsphere
13		       diehard_squeeze
14		       diehard_sums
15		       diehard_runs
16		       diehard_craps
17		       marsaglia_tsang_gcd
100		       sts_monobit
101		       sts_runs
102		       sts_serial
201		       rgb_minimum_distance
202		       rgb_permutations
203		       rgb_lagged_sum
204		       rgb_kstest_test
205		       dab_bytedistrib
206		       dab_dct
207		       dab_filltree
208		       dab_filltree2
209		       dab_monobit2

```
## Requirements
Python 3
Linux

## Installation
```bash
sudo apt-get install dieharder
```

## Usage
1.  Run the diehard_gui.py. GUI opens as shown below.
![GUI 1](https://github.com/Gowtham135/diehard-test-suite-python-with-GUI/blob/master/Images/diehard_Gui_1.PNG)
2.  Select the test that you want to perform from the list of tests available. If you want to run all the test select All Test 
![GUI 2](https://github.com/Gowtham135/diehard-test-suite-python-with-GUI/blob/master/Images/diehard_Gui_2.PNG)
3.  Select the binary file which contains the bits that are to be tested.
![GUI 3](https://github.com/Gowtham135/diehard-test-suite-python-with-GUI/blob/master/Images/diehard_Gui_3.PNG)
4.  Create an output file where the output of the test should be stored.
![GUI 4](https://github.com/Gowtham135/diehard-test-suite-python-with-GUI/blob/master/Images/diehard_Gui_4.PNG)
5.  If you want to append the results to the file, then select Append, else you want to rewrite the file choose Erase/Write.
6.  Click on start test to start the test.
![GUI 5](https://github.com/Gowtham135/diehard-test-suite-python-with-GUI/blob/master/Images/diehard_Gui_5.PNG)

