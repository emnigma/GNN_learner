import json
import logging
import pathlib
import os
import torch
from aiohttp import web
import time
from config import GeneralConfig
from common.game import GameState
from ml.data_loader_compact import ServerDataloaderHeteroVector
from ml.predict_state_vector_hetero import PredictStateVectorHetGNN

from inference_provider_server import run_inference

MODEL_PATH = pathlib.Path("./test_model.pth")
MODEL = GeneralConfig.EXPORT_MODEL_INIT()
MODEL.load_state_dict(torch.load(MODEL_PATH))


def main():
    # with open("./game_modified/game_mock.json", "r") as game_mock:
    #     data = json.load(game_mock)

    # print(json.dumps(data, indent=4))

    base = pathlib.Path("./usvm_graphs/")

    for json_graph_path in os.listdir(base):
        with open(base / json_graph_path) as test_graph_file:
            test_graph = GameState.from_json(test_graph_file.read())

        print(run_inference(MODEL, test_graph))


if __name__ == "__main__":
    main()
