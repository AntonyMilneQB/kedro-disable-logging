from setuptools import setup

setup(
    name="kedro-disable-logging",
    version="0.1",
    entry_points={
        "kedro.init": ["disable_logging = plugin:disable_logging"],
    },
)
