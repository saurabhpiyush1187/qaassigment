# QA Assignment submitted by **Saurabh Piyush**
This repo contains the UI as well as API automation cases that were developed as part of the assignment, to qualify for the post of Senior Automation Engineer at Sennder

## Index
1. [Framework](#Framework)
2. [Run the Automation Suite](#Run-the-Automation-Suite)
    1. [Method A Windows](#Method-A-Windows)
    2. [Method B Mac](#Method-B-Mac)
3. [API Automation](#---API-Automation)
4. [CI CD Support](#CI-CD-Support)
5. [Framework Architecture](#Framework-Architecture)
6. [Data Flow API](#Data-Flow-API)
7. [Data Flow UI](#Data-Flow-UI)
8. [Why this framework?](#Why-this-framework?)
9. [Contact](#Contact)

## **Framework**
For this assignment, I used pytest framework - a python-based test automation framework suite. It is a Test Driven Development (TDD) framework comprising of the following packages:
- **pytest** (for executing test plans in TDD format)
- **requests library** (to automate API)
- **selenium-webdriver** (to automate UI and saving failed scenarios screenshots)
- **pytest-html** (for reporting)
- **logging module** (for logging - tracking events that occur while software runs)

### **Run the Automation Suite**
First you need to clone the repo to your local

- Clone with HTTPS:     
    `git clone https://github.com/saurabhpiyush1187/qaassigment.git`

Then you need to follow either of the below two methods
#### **Method A**: Windows
**Requirements** 
--python 3.7 and above

Open the command line and point it to the directory of the repo on your system. Switch to the virtual environment by executing "set_up.bat"
    
    C:\~\qaassigment> set_up.bat
That's it.
It will switch to virtual environment and install necessary modules. After executing above batch file, the user will enter the virtual environment. Execute another file to run all the api and ui cases

    (venv)C:\~\qaassigment> run.bat
This will start the execution of all the test cases

**View HTML Report**
The automation framework is created with the support of **pytest--html**.To view results after execution. Open

>reports/report.html

**Troubleshooting**

I have included the chromedriver.exe in the project. However, chrome cases may fail due to chromedriver installation issues or binaries not set.If the chrome fails to launch, you can set the binaries to the installed chrome on your machine:

Edit file: ./tests/conftest.py

Sample code:
        
        
        def setup(browser):
        global driver
        capabilities = {'browserName': 'chrome',
        "chromeOptions": {
          'binary': "C:\Program Files\Google\Chrome\Application\chrome.exe"
                        }
                        }
        
        if browser=='chrome':
            if platform == "win32":
                driver=webdriver.Chrome(executable_path="."+os.sep +"browsers"+os.sep +"chromedriver.exe",desired_capabilities=capabilities)
                print("Launching chrome browser in Windows.........")
            elif platform =="darwin":
                driver=webdriver.Chrome(executable_path="."+os.sep +"browsers"+os.sep +"chromedriver")
                print("Launching chrome driver in Mac")
        return driver

In the above snippet , binary is set to chrome path installed in my system, you can change it you yours.


#### **Method B**: Mac

Requirements
–python 3.7 and above

Since virtual environments cannot be shared accross Operating systems, I have freezed the requirements to 

>./requirements.txt

Please follow the steps below:

1. **Open the terminal and point it to the directory of the repo on your system**
    
2. **Execute the following commands**



            python3 -m venv env
            source venv/bin/activate
            pip3 install -r requirements.txt
            
            or
        
            python3 -m venv env
            source env/bin/activate
            pip3 install -r requirements.txt

    This will install all the dependent libraries

3. **Run the script**

    Now, simply run the command


    python3 -m pytest -s -v -m "smoke" --html=./reports/report.html --browser chrome

         or

    py -m pytest -s -v -m "smoke" --html=./reports/report.html --browser chrome
4. **Troubleshooting in Mac**
    
    If you have any issue with chromedriver, you can copy **./Browsers/chromedriver** to **/usr/local/bin**

    

## **API Automation**
I have also automate the cases through cases through api.Automated API tests provide much faster test results and significantly accelerate development workflows. To start with, API tests do not need to wait for GUI to be ready and can be performed early in the agile development cycle, which helps you speed up the feedback loop and catch issues faster.

If you want to run only API cases, simply run the command(Mac) or edit the same in **run.bat**(Windows):
    
    python3 -m pytest -s -v -m "api" --html=./reports/report.html

If you want to run only UI cases, simply run the command(Mac) or edit the same in **run.bat**(Windows):

    python3 -m pytest -s -v -m "ui" --html=./reports/report.html --browser chrome

## **CI CD Support**

I have used github Actions to support CI/CD. The job will automatically run cases in case of any push into main branch.
Please see runs here

    https://github.com/saurabhpiyush1187/qaassigment/actions
![](github_ci_cd.PNG)

## **Framework Architecture**
![](architecture.png)

## **Data Flow API**
![](dfd_api_sennder.png)

## **Data Flow UI**
![](dfd_ui_sennder.PNG)

## **Why this framework?**
- ### **Open Source and Compatible**
    Pytest is open source and compatible with other test frameworks like BDD. Moreover,it can be used by development teams, test teams, teams that are practicing Test Driven Development(TDD), as well as in open-source projects. Finally,It also support Fixtures & Classes, which makes it easier to create common test objects available throughout a module/session/function/class.The framework architecture avoids and encourages non-hardcoded services as it parameterizes as much as possible.
  
- ### **Auto-Discovery of Tests**
    Pytest's default finds tests with the file name with the preface, "test," or the suffix "_test.py." However, we can configure Pytest to discover custom names by changing the Pytest configuration file “pytest.ini.” By adding the following extension, Pytest automatically discovers tests with the filename “verify.”
  
            [pytest]  
            python_files = verify_*.py 
            python_classes = Verify 
            python_functions = *_verify 
  

- ### **Command line execution**
    Pytest provides several options to run tests from the command line.

            pytest -v -s #verbosity and execution time of test
            e.g:pytest –v –s  

            pytest <file_name>   #run tests in module/file  
             e.g:pytest test_demo.py
            
            pytest –k <name>  #run all the test with matching name 
             e.g:pytest –k add #runs all the test with add  
            
            pytest filename::testName #runs only one test 
             e.g:pytest test_demo::test_addition 

- ### **Supports reporting**
    The Pytest community has a rich test of plug-ins to extend the module's functionality. One of them is pytest-html that generates a HTML report for test results.  


- ### **Integrated API automation**
    The framework uses python requests which is simple, yet elegant HTTP library. There is no need for any third party application to test and automate APIs.The accelerated execution speed of automated API tests leads to more effective resource consumption and lower overall testing costs.

- ### **Support for CI/CD**
    Pytest supports generating reports in JUnit format. By creating the XML file CI/CD systems like Jenkins can read the log files.
    
        pytest --junitxml=path 
    


## **Contact**
Let me know if you would like to know more about the architecture or have any feedback. I would like to talk more about the framework suite and architecture in detail.

With best regards,

Saurabh
