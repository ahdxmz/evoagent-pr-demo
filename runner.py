import subprocess


def run_command(command):
    return subprocess.run(
        command,
        shell=False,
        capture_output=True,
        text=True,
        timeout=10,
        check=True,
    )
