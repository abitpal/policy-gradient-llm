from dataclasses import dataclass, field

@dataclass
class Config(): 
    seed = 42
    dataset_name: str = "AI-MO/NuminaMath-CoT"
    data_splits: list = field(
        default_factory=lambda: ['source', 'problem', 'solution', 'messages']
    )
    dataset_directory = "/data" # relative to root
    dataset_sample_buffer_size = 800