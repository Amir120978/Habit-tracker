from setuptools import setup, find_packages

setup(
    name="habit-tracker",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pandas", "matplotlib"],
    entry_points={
        "console_scripts": [
            "habit-tracker=habit_tracker.main:main"
        ]
    },
)
