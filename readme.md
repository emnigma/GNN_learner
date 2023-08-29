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
| AI-guided searcher |              88.43             |                   174.11                  |                  2.3                  |                   0.5                  |
| BFS                |              88.3              |                   232.67                  |                  3.74                 |                  0.86                  |
| FORK_DEPTH         |              88.67             |                   250.1                   |                  3.28                 |                  1.25                  |
| FORK_DEPTH_RANDOM  |              88.45             |                   232.54                  |                  3.84                 |                  0.93                  |

### SBST comp.: guava / 5k step limit / 100 sec time limit:
|                    | Avg. coverage (more is better) | Avg. steps count to 100% (less is better) | Avg. tests generated (less is better) | Avg. errors generated (more is better) |
|--------------------|--------------------------------|-------------------------------------------|---------------------------------------|----------------------------------------|
| AI-guided searcher |              79.58             |                   418.56                  |                  1.54                 |                  0.27                  |
| BFS                |              80.74             |                   887.71                  |                  1.98                 |                  0.58                  |
| FORK_DEPTH         |              79.62             |                   924.1                   |                  1.81                 |                  1.23                  |
| FORK_DEPTH_RANDOM  |              80.74             |                   866.11                  |                  1.88                 |                  0.47                  |

