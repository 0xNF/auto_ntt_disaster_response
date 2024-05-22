from selenium import webdriver
import sys, os

directory = os.path.dirname(os.path.realpath(__file__))


def init() -> webdriver.Firefox:
    # Create a FirefoxOptions object
    options = webdriver.FirefoxOptions()

    # Set the Firefox browser to run in headless mode
    options.headless = True

    # Create a WebDriver instance with the specified options
    driver = webdriver.Firefox(options=options)

    return driver

def load_script():
    with open(os.path.join(directory, 'auto.js'), 'r') as f:
        s = f.read()
        return s
    
# Function to print console logs
def print_console_logs(driver: webdriver):
    logs = driver.get_log('browser')
    for log in logs:
        print(log['message'])
    
def launch_browser(url: str):
    script = load_script()
    page = url
    if not (page.startswith('http://') or page.startswith('https://') or page.startswith('file://')):
        page = f'https://{page}'
    driver = init()
    # Navigate to a website
    print("Opening page...")
    driver.get(page)
     # Perform some automation tasks
    title = driver.title
    print("Title of the webpage:", title)

    print("Getting console.logs")
    driver.execute_script(script)

    # print_console_logs(driver)

    # Close the WebDriver when done
    driver.quit()

def main() -> int:
    page = sys.argv[1]
    launch_browser(page)
    return 0


if __name__ == "__main__":
    sys.exit(main())