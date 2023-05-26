## Table-driven Agent

This is deemed practically infeasible

## Simple reflex Agent (SRA)

SRAs are “the starter agent”, really simple and acting on the *current* percept, ignoring the past stimuli

*e.g.* Simple automated vacuum cleaner &rarr; its decision to clean is based solely on its current location

![1 1](pictures/1%201.png)


## Model-based reflex Agent (MBRA)

![2 1](pictures/2%201.png)

This kind of agent maintains some sort of internal state depending on percept history

*Changes*. These can be agent-dependent or agent-independent, and can be summarized in the term **Transition model**

*The effect of changes.* Defined in the **Sensor model**

These two allow the definition of the **Model-based Agent** to exist

## Goal-based Agent (GBA)

![](pictures/3.png)

The notion of GBA comes from the fact that *it’s often NOT enough to rely on the current state,* therefore introducing the notion of **goal**

A goal is an objective that the agent has and pursues (by searching and planning)

*Parallelism between reflex and goal* (AIMA, pg. 72)

The reflex agent brakes when it sees brake lights, period. **It has no idea why**. 

A goal-based agent brakes when it sees brake lights because **that’s the only action that it predicts will achieve its goal of not hitting other cars.**

## Utility-based Agent (UBA)

UBAs are a subclass of GBA