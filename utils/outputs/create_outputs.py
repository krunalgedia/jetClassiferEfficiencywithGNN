from typing import List

import utils
from utils.configs.dataset import DatasetConfig
from utils.configs.dataset_handling import DatasetHandlingConfig
from utils.configs.model import ModelConfig
from utils.configs.working_points_set import WorkingPointsSetConfig
from utils.data.jet_events_dataset import JetEventsDataset
from utils.logging import set_up_logging_sinks
from utils.outputs.deepcsv_histogram import create_deepcsv_discriminator_histogram
from utils.outputs.efficiency_map_plots import create_efficiency_map_histogram_plots
from utils.outputs.jet_multiplicity_histogram import (
    create_jet_multiplicity_histogram_by_flavour,
    create_jet_multiplicity_histogram_inclusive,
)
from utils.outputs.jet_variable_histograms import create_jet_variable_histograms
from utils.outputs.mistag_rates import save_light_jet_mistag_rates


def create_outputs(
    dataset_config: DatasetConfig,
    working_points_set_configs: List[WorkingPointsSetConfig],
    dataset_handling_configs: List[DatasetHandlingConfig],
    efficiency_map_model_configs: List[ModelConfig],
):
    dataset_output_dir_path = utils.paths.dataset_outputs_dir(
        dataset_name=dataset_config.name,
        mkdir=True,
    )

    set_up_logging_sinks(
        dir_path=dataset_output_dir_path,
        base_filename=utils.filenames.dataset_outputs_log,
    )

    jds = JetEventsDataset.read_in(
        dataset_config=dataset_config,
        branches=None,
    )

    create_jet_variable_histograms(
        dataset_config=dataset_config,
        output_dir_path=dataset_output_dir_path,
        jds=jds,
    )

    create_jet_multiplicity_histogram_inclusive(
        dataset_config=dataset_config,
        output_dir_path=dataset_output_dir_path,
        jds=jds,
    )

    create_jet_multiplicity_histogram_by_flavour(
        dataset_config=dataset_config,
        output_dir_path=dataset_output_dir_path,
        jds=jds,
    )

    create_deepcsv_discriminator_histogram(
        dataset_config=dataset_config,
        output_dir_path=dataset_output_dir_path,
        jds=jds,
    )

    for working_points_set_config in working_points_set_configs:
        save_light_jet_mistag_rates(
            dataset_config=dataset_config,
            working_points_set_config=working_points_set_config,
            output_dir_path=dataset_output_dir_path,
            jds=jds,
        )

    for dataset_handling_config in dataset_handling_configs:
        for working_points_set_config in working_points_set_configs:
            for model_config in efficiency_map_model_configs:
                create_efficiency_map_histogram_plots(
                    dataset_config=dataset_config,
                    dataset_handling_config=dataset_handling_config,
                    working_points_set_config=working_points_set_config,
                    model_config=model_config,
                    output_dir_path=dataset_output_dir_path,
                )
