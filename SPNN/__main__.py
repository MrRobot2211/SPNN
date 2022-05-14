import sys
from SPNN.core import run_SPNN

if __name__ == "__main__":
    # Default parameters
    ini_ener_log = -3
    fin_ener_log = 1
    npoints = 1000

    # Input parameters via terminal
    projectile = sys.argv[1]
    projectile_mass = float(sys.argv[2])
    target = sys.argv[3]
    target_mass = float(sys.argv[4])
    if len(sys.argv) > 5:
        ini_ener_log = int(sys.argv[5])
        fin_ener_log = int(sys.argv[6])
        npoints = int(sys.argv[7])

    run_SPNN(
        projectile,
        projectile_mass,
        target,
        target_mass,
        ini_ener_log,
        fin_ener_log,
        npoints,
    )