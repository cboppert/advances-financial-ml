# Chapter One Notes

## Meta-Strategy Paradigm

Doomed to failure if working on your own because effort to create one strategy is nearly the same as to produce 100.

This is because of the complexities involved with data procurement, warehousing, processing, software development, high performance computing infrastructure (HPC, essentially a bunch of GPUs working in coordination for data processing), execution simulators, backtesting, etc.

Instead you need to work as teams where each person becomes an expect at a particular task with a holistic vision of the effort as a whole in mind.

## Book Structure

Part one is about structuring data to be amenable to algorithms

Part two discusses doing research with ML algorithms on that data using a scientific process as opposed to wandering until a likely false positive result comes up.

Part three explains backtesting against historical data to verify correctness.

Part four explores feature extraction via innovate means.

Part five has recipes for HPC infrastructure.

## Post Deploy Oversight

After a strategy is deployed...

- *Embargo period* - During this period the strategy is run against data occurring post back test data and if strategy maintains consistency in results it will be moved to

- *Paper trading* - Trading against a live real time feed of data to ensure performance accuracy accounting for data delays, and differences in market between development and deployment

- *Graduation* - At this point the strategy is managing a real position either in solo or as part of an ensemble

- *Re-allocation* - Depending on performance re-allocation occurs and the position grows larger as the strategy continues to meet expectations over time

- *Decommission* - Eventually the strategy's alpha will diminish and the strategy will be decommissioned


## Solving Problems

- Program such that execution can be run in parallel (Chapters 20 and 22)

- Develop programs for quantum computers (Chapter 21)

- Memory preserving data transformations (Chapter 5)

- Value assessment via experiment (Chapters 11 - 15)

- Detect structural breaks (Chapters 17, 18)

- Queueing methods for problem partitioning (Chapter 20)

- Employ discrete methods (Chapter 21)

- Define a research process as opposed to trying to find strategies through innovating thinking (Chapters 7 - 9)

- Combine predictions (Chapter 10)

- Backtesting (Chapters 11 - 15)

- Asset allocation via techniques which don't overfit in-sample signals for out-of-sample performance (Chapter 16)
