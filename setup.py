from setuptools import find_packages, setup

setup(
    name="quickstart_snowflake",
    packages=find_packages(exclude=["quickstart_snowflake_tests"]),
    install_requires=[
        "dagster",
        "dagster-snowflake",
        "dagster-snowflake-pandas",
        "dagster-cloud",
        "boto3",
        "pandas",
        "matplotlib",
        "textblob",
        "tweepy",
        "wordcloud",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
