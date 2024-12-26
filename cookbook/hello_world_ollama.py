"""
Basic Hello World example using local Ollama model
"""
from scrapegraphai.graphs import SmartScraperGraph

# Configure the graph with Ollama settings
graph_config = {
    "llm": {
        "model": "ollama/mistral",  # or whichever model you have pulled
        "temperature": 0,
        "format": "json",  # Ollama needs format specified
        # "base_url": "http://localhost:11434",  # default Ollama URL
    },
    "verbose": True,  # This will show the processing steps
    "headless": False  # Show browser for visual feedback
}

# Create the scraper instance
scraper = SmartScraperGraph(
    prompt="Tell me what this website is about and give me a brief summary.",
    source="https://github.com/VinciGit00/Scrapegraph-ai",  # Example URL
    config=graph_config
)

# Run the scraper and get results
print("Starting scraping process...")
result = scraper.run()

# Print the results
print("\nResults:")
print(result)

# Get detailed execution info
exec_info = scraper.get_execution_info()
print("\nExecution Info:")
for key, value in exec_info.items():
    print(f"{key}: {value}")
