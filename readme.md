# AI-guided Symbolic Execution

This is a framework for supervisor "ensemble" creation for GNN supervised learning

# Features

* Multiprocessing
* Flexible config
* Any SE Engine integration is possible

# How to use

## Steps to run client

### 1. Create venv, install deps

```sh
conda create -n agent_env python=3.10.9
conda activate agent_env
bash install_script.sh
```

### 2. Launch training

1. configure `MAX_STEPS` and `SERVER_COUNT` in [config](./config.py)
2. `python3 launch_servers.py`
3. `python3 main.py`

# Evaluation

### UTBot test suite / 5k step limit / 100 sec time limit
|                    | Avg. coverage (more is better) | Avg. steps count to 100% (less is better) | Avg. tests generated (less is better) | Avg. errors generated (more is better) |
|--------------------|--------------------------------|-------------------------------------------|---------------------------------------|----------------------------------------|
| AI-guided searcher |              87.76             |                   61.02                   |                  2.34                 |                  0.59                  |
| BFS                |              88.25             |                   83.01                   |                  3.81                 |                  0.87                  |
| FORK_DEPTH         |              88.55             |                    82.5                   |                  3.56                 |                  1.26                  |
| FORK_DEPTH_RANDOM  |              88.45             |                   76.93                   |                  3.68                 |                  0.92                  |

### SBST comp.: guava / 5k step limit / 100 sec time limit:
|                    | Avg. coverage (more is better) | Avg. steps count to 100% (less is better) | Avg. tests generated (less is better) | Avg. errors generated (more is better) |
|--------------------|--------------------------------|-------------------------------------------|---------------------------------------|----------------------------------------|
| AI-guided searcher |              79.39             |                   63.03                   |                  1.65                 |                  0.34                  |
| BFS                |              80.74             |                   154.95                  |                  1.98                 |                  0.58                  |
| FORK_DEPTH         |              79.62             |                   77.08                   |                  1.81                 |                  1.23                  |
| FORK_DEPTH_RANDOM  |              80.74             |                   124.25                  |                  1.88                 |                  0.47                  |
