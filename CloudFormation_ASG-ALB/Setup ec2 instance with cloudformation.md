## How to Create an ec2 instance with using Cloudforma tion service

## First Option (By using Cloudformation snippet and CloudFormation linter)

1. Open VSCode and create new file with yaml or yml extension
2. Write cfn in the newly created yaml file
3. Choose cfn-lite from the list
4. Customize the description with your own words
5. For resources part, write ec2ins and choose AWS::ec2 from the list
6. Remove unnecessary parts
7. Customize LogcalId with a string using your own words
8. For Image ID, look up on the AWS console for the AMI ID that corresponds to your region and
enter that id.
9. For instance type write t2.micro (or another instance type you want)
10. For tags, enter values like Key:Name Value:Cfn
11. For security groups enter a security group name from the console or create a new security group
on the console and enter its name. Do not forget to add inbound rule for ssh connection
12. For keyname enter your key name without using the .pem extension
13. Save the file
14. Go to Cloudformation service
15. Create a stack
16. Upload the yaml file that you created
17. Give your stack a anme and choose next to go with default options
18. Click on create stack at the end and you are done

## Second Option

1. Open VSCode and create new file with yaml or yml extension
2. Open Google and serach for Cloudformation template anatomy
3. Click and go to the aws website  link from the seearch result
4. Copy the YAML template
5. Paste it to the newly created file
6. Fill the form and remove unnecessary parts.
7. Save the file
8. Go to Cloudformation service
9. Create a stack
10. Upload the yaml file that you created
11. Give your stack a anme and choose next to go with default options
12. Click on create stack at the end and you are done