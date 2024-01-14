from configs.model.direct_tagging import model_config as direct_tagging_model_config
from configs.model.eff_map_pt_eta import (
    model_config as eff_map_pt_eta_model_config,
)

from configs.model.gnn_lr0p0002_with_attentionv2_drop0p1_nhead8_epoch40 import model_config as gnn_lr0p0002_with_attentionv2_drop0p1_nhead8_epoch40 
from configs.model.gnn_extraip_emb6_lr0p0002_with_attention_drop0p1_nhead8_epoch30 import model_config as gnn_extraip_emb6_lr0p0002_with_attention_drop0p1_nhead8_epoch30 
from configs.model.gnn_extraip_lr0p0002_with_attentionv2_drop0p1_nhead8  import model_config as gnn_extraip_lr0p0002_with_attentionv2_drop0p1_nhead8
from configs.model.gnn_lr0p0002_emb4_with_attention_drop0p1_nhead8    import model_config as gnn_model_config_lr0p0002_emb4_with_attention_drop0p1_nhead8 
from configs.model.gnn_lr0p0002_emb4_with_attentionv2_drop0p1_nhead8   import model_config as gnn_model_config_lr0p0002_emb4_with_attv2_drop0p1_nhead8 
from configs.model.gnn_lr0p0002_with_attentionv2_drop0p1_nhead8_bootstrap  import model_config as gnn_model_config_lr0p0002_with_attv2_drop0p1_nhead8 
from configs.model.gnn_extraip_lr0p0002_with_attention_drop0p1_nhead8 import model_config as gnn_model_config_extraip_lr0p0002_with_attention_drop0p1_nhead8
from configs.model.gnn_extraip_embedding6_lr0p0004 import model_config as gnn_model_config_extraip_embedding6_lr0p0004
from configs.model.gnn_extraip_embedding6_lr0p0002 import model_config as gnn_model_config_extraip_embedding6_lr0p0002
from configs.model.gnn_extraip_embedding6 import model_config as gnn_model_config_extraip_embedding6
from configs.model.gnn_embedding6 import model_config as gnn_model_config_embedding6
from configs.model.gnn_embedding4 import model_config as gnn_model_config_embedding4
from configs.model.gnn_extraip  import model_config as gnn_model_config_extraip 
from configs.model.gnn_lr0p0004 import model_config as gnn_model_config_lr0p0004
from configs.model.gnn import model_config as gnn
from utils.configs.evaluation_model import EvaluationModelConfig
from utils.configs.evaluation_model_selection import EvaluationModelSelectionConfig


evaluation_model_selection_config = EvaluationModelSelectionConfig(
    name=f"individual_{gnn.name}_and_median",
    evaluation_model_configs=[
        EvaluationModelConfig(
            model_config = gnn,
            run_selection="all",
            run_aggregation="median",
            is_comparison_base=True,
            display_name="GNN",
            only_bootstrap_runs=True,
        ),
        EvaluationModelConfig(
            model_config = gnn,
            run_selection="all",
            run_aggregation="individual",
            is_comparison_base=False,
            display_name="GNN bootstrap",
            only_bootstrap_runs=True,
        ),
    ],
)