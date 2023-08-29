import json
import logging
import pathlib

import torch
from aiohttp import web
import time
from config import GeneralConfig
from common.game import GameState
from ml.data_loader_compact import ServerDataloaderHeteroVector
from ml.predict_state_vector_hetero import PredictStateVectorHetGNN

routes = web.RouteTableDef()

# logging.basicConfig(
#     level=GeneralConfig.LOGGER_LEVEL,
#     filename="inference_provider_server.log",
#     filemode="w",
#     format="%(asctime)s - p%(process)d: %(name)s - [%(levelname)s]: %(message)s",
# )
from ml.model_modified import StateModelEncoderExportCompact

MODEL_PATH = pathlib.Path("test_model.pth")
MODEL = GeneralConfig.EXPORT_MODEL_INIT()
# MODEL = StateModelEncoderExportCompact(hidden_channels=32, out_channels=8)
# MODEL = torch.load(MODEL_PATH, map_location=torch.device("cpu"))
MODEL.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device("cpu")))


def run_inference(model: torch.nn.Module, game_state: GameState) -> int:
    data, state_map = ServerDataloaderHeteroVector.convert_input_to_tensor(game_state)
    predicted_state = PredictStateVectorHetGNN.predict_state_single_out(
        model, data, state_map
    )
    return predicted_state


@routes.post("/run_inference")
async def dequeue_instance(request):
    game_state_raw = await request.read()
    game_state = GameState.from_json(game_state_raw.decode("utf-8"))

    predicted_state = run_inference(MODEL, game_state)
    return web.Response(text=str(predicted_state))


def main():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, port=8080)

    # with open("./game_modified/game_mock.json", "r") as game_mock:
    #     data = json.load(game_mock)

    # print(json.dumps(data, indent=4))


if __name__ == "__main__":
    main()
