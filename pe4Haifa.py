import wikipedia
import time
import concurrent.futures

# A. Sequentially download Wikipedia content
def download_sequentially():
    start_time = time.perf_counter()  # Start time
    
    # 1. Get a list of topics related to 'generative artificial intelligence'
    topics = wikipedia.search("generative artificial intelligence")
    
    # 2. Iterate over the topics and save references to .txt files
    for topic in topics:
        # Get page content
        page = wikipedia.page(topic, auto_suggest=False)
        # Get page title
        page_title = page.title
        # Get references
        references = page.references

        # Write references to a .txt file
        with open(f"{page_title}.txt", "w", encoding="utf-8") as f:
            for reference in references:
                f.write(reference + "\n")
    
    end_time = time.perf_counter()  # End time
    print("Sequential execution time:", end_time - start_time, "seconds")

# B. Concurrently download Wikipedia content
def download_concurrently():
    start_time = time.perf_counter()  # Start time
    
    # Get a list of topics related to 'generative artificial intelligence'
    topics = wikipedia.search("generative artificial intelligence")

    # Concurrently download Wikipedia content
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_and_save, topics)

    end_time = time.perf_counter()  # End time
    print("Concurrent execution time:", end_time - start_time, "seconds")

# Function to download and save references for a given topic
def download_and_save(topic):
    # Retrieve Wikipedia page for the topic
    page = wikipedia.page(topic, auto_suggest=False)
    
    # Get page title and references
    page_title = page.title
    references = page.references
    
    # Save references to a text file
    with open(f"{page_title}.txt", "w", encoding="utf-8") as f:
        for reference in references:
            f.write(reference + "\n")
            
    print(f"References saved for '{page_title}'")

def main():
    print("Sequential Download:")
    download_sequentially()
    print("\nConcurrent Download:")
    download_concurrently()

if __name__ == "__main__":
    main()
