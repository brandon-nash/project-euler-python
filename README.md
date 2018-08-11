# project-euler-python

Back in college, my Machine Learning professor turned me on to <a href="https://projecteuler.net/">Project Euler</a>. I didn't initially get too far through the challenges
due to other projects, school work etc. taking up most of my time; I think I was doing the challenges mostly in C++ too which isn't the easiest language to start churning these problems out in. 

A couple of years ago I decided to pick back up on the Project Euler challenges using Python. I've completed about 30 of the ~600 some-odd challenges, a pretty
minimal percentage, I know but you have to start somewhere right? 

It's been about a year since I have been regularly working on the challenges. My hope is that by checking my solutions in I'll be motivated to start working through more of the challenges. Also, some of these solutions
exhibit <strong>extreme</strong> brute force mentality and could really be better optimized which is something I'd also like to re-visit.

The original questions aren't included in the solutions but can be found at https://projecteuler.net/archives. It's not hard to find solutions for the 
challenges either in case you want to fact check me or find a better solution than mine, I'll admit, I've had to visit a couple of these solutions myself
to see how others approached solving them.

## How to Run the Solutions
I've broken down each solution into its own file. Most of the files make use of a timer for benchmarking. Some of the earlier brute force solutions
were refactored to be quicker and more efficient, mostly measured by execution time, leading to timers being used in many of the solutions.
Each solution outputs the answer which should also be commented in the code as well. 

The solutions should be compilable with Python 2.7. The only additional library I've really made use of is Numpy. I don't expect to use any other
libraries going forward but I wouldn't rule that out just yet. I'd like to keep my solutions as vanilla as possible, I mean if I'm not writing the 
algorithms myself does it really count as a "solution"? I personally enjoy using the <a href="https://www.jetbrains.com/pycharm/">PyCharm</a> IDE from 
Jetbrains but of course that's just my personal preference. 

## Some Goals Going Forward:
<ul>
  <li>Obviously, solving more of the challenges.</li>
  <li>Optimizing existing solutions.</li>
  <li>Better organization of the source code. Maybe being able to run and output the solution to a challenge given the challenge # from a prompt?</li>
  <li>Implementing the solutions in different languages?</li>
</ul>
