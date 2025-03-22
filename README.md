# ToPi git template
Template repository for ToPi retreat 2025.

Indico: https://indico.global/event/13854/overview

This collects the materials and instructions for the exercises which are performed during the coding sessions.

## Instructions

The detailed instructions are listed in the `instructions` directory:

0. [Prerequisites](./instructions/0-Prerequisites.md)
0. [Choose a Role](./instructions/1-Roles.md)
0. [Project setup](./instructions/2-Setup.md)
0. [Exercise A: Basic Fitting](./instructions/3-Exercise-A.md)
0. [Exercise B: Non-trivial Fitting](./instructions/4-Exercise-B.md)
0. [Exercise C: Getting more advanced](./instructions/5-Exercise-C.md)

## Exercise A

How to sync:

0. `$ git switch main`
1. `$ git pull`
2. `$ git switch your_branch`
3. `$ git merge main`
4. `$ git push`

Enforcing code formatting:

0. `$ cd topi-git-template`
1. `$ . env/bin/activate`
2. `$ pip install black`
3. `$ pip install pre-commit`
4. `$ pre-commit install`
