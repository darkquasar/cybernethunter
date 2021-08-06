#!/bin/sh
echo "[CYBERNETHUNTER] Making sure to drop into the right anaconda environment"

check_running_conda_env()
{
    conda_activate=$(conda activate cybernethunter)
    if [ $? -eq 0 ] ; then
        echo "[CYBERNETHUNTER] Successfully activated conda environment"
        exec "$@"
    else
        echo "[CYBERNETHUNTER] Could not activate conda environment. Sourcing .bashrc" >&2
        conda init
        . $ANACONDA_DIR/etc/profile.d/conda.sh
        check_running_conda_env
    fi
}

check_running_conda_env