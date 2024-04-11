import logging
import os
from pathlib import Path

package_name='mongodb_connect'
list_of_files=[
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    # "src/components/data_transformation.py",
    # "src/components/model_trainer.py",
    # "src/components/model_evaluation .py",
    # "src/pipeline/__init__.py",
    # "src/pipeline/training_pipeline.py",
    # "src/pipeline/prediction_pipeline.py",
    # "src/utils/__init__.py",
    # "src/utils/utils.py",
    # "src/logger/logging.py",
    # "src/exception/exception.py",
    "tests/unit/__init__.py",
    "test/unit/unit.py"
    "tests/integration/__init__.py",
    "test/integration/int.py",
    "init_setup.sh",
    "requirement   .txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.in",
    #"experiment/experiments.ipynb",
    "experiment/experiments.py"

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")


    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass

