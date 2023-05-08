import requests

jenkins_file_url = "muhsinamajeed:1110ae529e9ca8cfd767f8fb50a46236ab http://192.168.0.71:8080/job/demo3/config.xml"
response = requests.get(jenkins_file_url)

if response.status_code == 200:
    num_lines = len(response.text.split("\n"))
    print(f"Number of lines in Jenkins file: {num_lines}")
else:
    print("Error: Could not retrieve Jenkins file")