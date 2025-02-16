"""
Example of Search Graph

"""


# python -m venv scrapegraph_env

# scrapegraph_env\Scripts\activate

# pip install scrapegraphai

# playwright install

# deactivate

# cree le fichier requirements
# pip freeze > requirements.txt


# installe le fichier requirements
# pip install -r requirements.txt



import os
from dotenv import load_dotenv
from scrapegraphai.graphs import SearchGraph
from scrapegraphai.utils import prettify_exec_info

load_dotenv()

FILE_NAME = "inputs/example.json"
curr_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(curr_dir, FILE_NAME)

with open(file_path, 'r', encoding="utf-8") as file:
    text = file.read()

# ************************************************
# Initialize the model instances
# ************************************************

graph_config = {
    "llm": {
        "api_key": os.environ["AZURE_OPENAI_KEY"],
        "azure_endpoint": os.environ["AZURE_OPENAI_ENDPOINT"],
        "model": "azure_openai/gpt-4o",
        "api_version":"gpt-4o"
    },
    "verbose": True,
    "headless": False
}

# ************************************************
# Create the SearchGraph instance and run it
# ************************************************

search_graph = SearchGraph(
    prompt="List me the best escursions near Trento",
    config=graph_config
)

result = search_graph.run()
print(result)

# ************************************************
# Get graph execution info
# ************************************************

graph_exec_info = search_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))

# Save to json and csv
# convert_to_csv(result, "result")
# convert_to_json(result, "result")