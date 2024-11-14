from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#test update1

# Path to your Chrome user data directory
user_data_dir = r"C:\temp"
profile_name = "Profile 4"

# Set Chrome options
options = Options()
options.add_argument(f"user-data-dir={user_data_dir}")
options.add_argument(f"profile-directory={profile_name}")

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Navigate to the Jira URL
jira_url = 'https://cfainstitute.atlassian.net/jira/servicedesk/projects/ITHD/queues/custom/433'
driver.get(jira_url)

print("Opened Jira with existing session.")

try:
    
    # # # Wait for the button to be clickable
    # # driver.find_element(By.ID, "createGlobalItem").click()
    # driver.find_element(By.ID, 'createGlobalItem').click()

    create_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'createGlobalItem'))
    )
    create_button.click()
    print("Clicked on create button.")

    time.sleep(5)

 
    project_picker = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'issue-create.ui.modal.create-form.project-picker.project-select'))
    )
    project_picker.click()
    print("Clicked on project picker.")

    

    # Find the specific option by its text
    option_xpath = "//div[@data-testid='issue-field-select-base.ui.format-option-label.c-label' and text()='IT Security Operations - Incident Response (IR)']"
    option = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, option_xpath))
    )
    option.click()
    print("Selected IT Security Operations - Incident Response (IR).")
    
    time.sleep(5)

    request_type_picker = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "issue-create.ui.modal.create-form.type-picker.request-type-select"))
    )
    request_type_picker.click()
    print("Clicked on request type picker.")

    #Locate the "Mass Download" option and click it using its class
    mass_download_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@data-test-id='issue-create.ui.modal.create-form.type-picker.request-type-select.label' and text()='Mass Download']"))
    )
    mass_download_option.click()
    print("Selected Mass Download request type.")

    time.sleep(5)

 
    # Prompt user to enter the JIRA alert link directly in the terminal
    alert_link = input("Please enter the JIRA alert link: ")
    
    # Open the entered alert link in a new tab
    driver.execute_script("window.open(arguments[0], '_blank');", alert_link)
    print("Opened JIRA alert link in a new tab.")

    time.sleep(5)  # Wait for the new tab to load

    driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab

    # Wait for the title element to be present and get its text
    alert_title_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(@class, 'css-1y22fjq')]"))  # Adjust as needed
    )
    alert_title = alert_title_element.text  # Get the title text
    print(f"Copied alert title: {alert_title}")

    
 
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[1])
    #css-tqt2s7 ejdug3l0
    time.sleep(4)
    incident_info_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'css-veywga')]"))  # Adjusted to the parent div class
    )
    incident_info_text = incident_info_element.text  # Get the full text of the incident info
    print(f"Full incident info: {incident_info_text}")

    time.sleep(4)

    if "Incident name:" in incident_info_text:
        # Split the text and extract the incident name
        specific_text = incident_info_text.split("Incident name:")[-1].strip().split("\n")[0]  # Take the first line after "Incident name:"
        print(f"Extracted specific text: {specific_text}")

    time.sleep(3)   

    driver.switch_to.window(driver.window_handles[0])

    time.sleep(3)

    summary_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'summary-field'))
    )
    summary_input.click()  # Click to focus on the input box
    summary_input.clear()   # Clear any existing text
    summary_input.send_keys(f"{alert_title} - {specific_text}")  # Paste the copied title
    print(f"Entered summary: {alert_title}-{specific_text}")   

    time.sleep(4)

    # Now select the component
    #components-field-select css-1f7ebe5-container
    components_container = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'components-container'))
    )
    components_container.click()  
    print("Clicked on components container.")

    time.sleep(2)  

    clear_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'css-136ns2m'))
    )
    clear_button.click()  # Click the clear button
    print("Clicked to clear all existing components.")
    

    components_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@class='components-field-select__input']"))
    )
    components_input.click()  # Click to focus on the input field
    components_input.clear()   # Clear any existing text
    components_input.send_keys("Mass Download")  # Type the component name
    print("Typed 'Mass Download' into components input.") 

    time.sleep(2)  

    # Press Enter to select the "Mass Download" option
    components_input.send_keys(Keys.ENTER)  # Select the component
    print("Selected Mass Download component using Enter key.")

   

    time.sleep(5)
        # Now add the description
    description_area = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'ak-editor-textarea'))
    )
    description_area.click()  # Focus on the description area

    # Clear any placeholder text (optional, depending on how your editor behaves)
    description_area.clear()  # If this works; if not, it might not be needed

    # Type the incident_info_text into the description area
    description_area.send_keys(incident_info_text)  # Paste the incident info
    print(f"Entered description: {incident_info_text}")

    time.sleep(5)

    # assignee selection
    # assignee_field = WebDriverWait(driver, 10).until(
    # EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'css-1ff36h2')]//div[contains(@class, 'fabric-user-picker__input-container')]//input[contains(@class, 'fabric-user-picker__input')]"))
    # )

    # actions = ActionChains(driver)
    # actions.move_to_element(assignee_field).click().perform()  # Focus on the input field
    # print("Clicked on assignee field using ActionChains.")
    # time.sleep(2)  # Adding a small delay to ensure field is ready for input

    # # Step 2: Type the name of the assignee (Dhyey Vachhani) into the input field
    # assignee_field.send_keys("Dhyey Vachhani")
    # print("Typed 'Dhyey Vachhani' into the assignee field.")

    # # Step 3: Wait for the div that contains the name to appear or be updated
    # assignee_div = WebDriverWait(driver, 10).until(
    # EC.presence_of_element_located(
    #     (By.XPATH, "//div[@class='css-1g7l433' and text()='Dhyey Vachhani - CW']")
    # )
    # )

    # # Step 4: Click the div containing the correct assignee name
    # assignee_div.click()
    # print("Selected the assignee.")

    # # Optional: Wait for the change to reflect before proceeding
    time.sleep(2)

    #priority field selection
    priority_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='priority-container']//div[@class='css-1f7ebe5-container']"))
    )
    priority_field.click()  # Focus on the input field
    print("Clicked on priority input field.")
    time.sleep(2)


  
    low_priority_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='priority-container']//div[@class='css-1f7ebe5-container']//div[@class='_2lx21bp4 _1e0c1txw _1bsb1osq']//div[@data-testid='issue-field-select-base.ui.format-option-label.c-label' and text()='Low']"))
    )
    time.sleep(2)

    low_priority_option.click()  # Click the "Low" option
    print("Selected 'Low' priority by clicking on it.")
 

    time.sleep(30)



except Exception as e:
    print(f"An error occurred: {e}")

# Keep the browser open
print("Browser will remain open. Close it manually when done.")
