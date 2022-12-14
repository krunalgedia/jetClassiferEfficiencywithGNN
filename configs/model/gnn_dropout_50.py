import copy

from configs.model.gnn import model_config as gnn_model_config

model_config = copy.deepcopy(gnn_model_config)

model_config.name = "gnn_dropout_50"

model_config.model_init_kwargs["edge_network_dropout"] = 0.5
model_config.model_init_kwargs["node_network_dropout"] = 0.5
model_config.model_init_kwargs["jet_efficiency_net_dropout"] = 0.5
