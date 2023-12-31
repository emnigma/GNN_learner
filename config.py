import logging
from dataclasses import dataclass
from pathlib import Path
from shutil import rmtree

import torch

import ml.model_modified
import ml.models


class GeneralConfig:
    SERVER_COUNT = 16
    NUM_GENERATIONS = 20
    NUM_PARENTS_MATING = 22
    KEEP_ELITISM = 2
    NUM_RANDOM_SOLUTIONS = 60
    NUM_RANDOM_LAST_LAYER = 18
    MAX_STEPS = 5000
    MUTATION_PERCENT_GENES = 5
    LOGGER_LEVEL = logging.INFO
    IMPORT_MODEL_INIT = lambda: ml.models.StateModelEncoder(
        hidden_channels=32, out_channels=8
    )
    EXPORT_MODEL_INIT = lambda: ml.model_modified.StateModelEncoderExport(
        hidden_channels=32, out_channels=8
    )
    DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


class BrokerConfig:
    BROKER_PORT = 8080
    BROKER_HOST = "0.0.0.0"
    GET_WS_HANDLE = "get_ws"
    POST_WS_HANDLE = "post_ws"
    SEND_RES_HANDLE = "send_res"
    RECEIVE_RES_HANDLE = "recv_res"


class ServerConfig:
    SERVER_INSTANCES_START_PORT = 8100


@dataclass(slots=True, frozen=True)
class DumpByTimeoutFeature:
    enabled: bool
    timeout_sec: int
    save_path: Path

    def create_save_path_if_not_exists(self):
        if self.enabled:
            if self.save_path.exists():
                rmtree(self.save_path)
            self.save_path.mkdir()


@dataclass(slots=True, frozen=True)
class SaveEpochsCoveragesFeature:
    enabled: bool
    save_path: Path

    def create_save_path_if_not_exists(self):
        if self.enabled:
            if self.save_path.exists():
                rmtree(self.save_path)
            self.save_path.mkdir()


@dataclass(slots=True, frozen=True)
class OnGameServerRestartFeature:
    enabled: bool
    wait_for_reset_retries: int
    wait_for_reset_time: float


class FeatureConfig:
    VERBOSE_TABLES = True
    SHOW_SUCCESSORS = True
    NAME_LEN = 7
    DISABLE_MESSAGE_CHECKS = True
    DUMP_BY_TIMEOUT = DumpByTimeoutFeature(
        enabled=True, timeout_sec=1800, save_path=Path("./report/timeouted_agents/")
    )
    SAVE_EPOCHS_COVERAGES = SaveEpochsCoveragesFeature(
        enabled=True, save_path=Path("./report/epochs_tables/")
    )
    ON_GAME_SERVER_RESTART = OnGameServerRestartFeature(
        enabled=True, wait_for_reset_retries=10 * 60, wait_for_reset_time=0.1
    )


class GameServerConnectorConfig:
    CREATE_CONNECTION_TIMEOUT_SEC = 1
    WAIT_FOR_SOCKET_RECONNECTION_MAX_RETRIES = 10 * 60
    RESPONCE_TIMEOUT_SEC = (
        FeatureConfig.DUMP_BY_TIMEOUT.timeout_sec + 1
        if FeatureConfig.DUMP_BY_TIMEOUT.enabled
        else 1000
    )
    SKIP_UTF_VALIDATION = True
