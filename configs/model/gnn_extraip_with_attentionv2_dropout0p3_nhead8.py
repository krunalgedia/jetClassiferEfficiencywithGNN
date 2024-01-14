import copy

from configs.model.gnn_extraip_with_attentionv2_dropout0p1_nhead8 import model_config as gnn_model_config
from utils.preprocessing.identity import Identity
from utils.preprocessing.normalizer import Normalizer

model_config = copy.deepcopy(gnn_model_config)

model_config.name = "gnn_with_attentionv2_dropout0p3_nhead8"

model_config.model_init_kwargs["node_features_cols"].extend(
    [
        "Jet_nConstituents",
        "nJet",
        "Jet_mass",
        "Jet_area",
    ]
)

model_config.model_init_kwargs["preprocessing_pipeline"].column_preprocessors.update(
    {
        "Jet_nConstituents": Identity(),
        "nJet": Normalizer(),
        "Jet_mass": Normalizer(),
        "Jet_area": Normalizer(),
    }
)