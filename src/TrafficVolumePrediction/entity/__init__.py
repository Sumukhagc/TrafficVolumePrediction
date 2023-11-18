from pathlib import Path
from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    root_dir:Path
    source_url:Path
    local_dir:Path
    unzip_dir:Path
