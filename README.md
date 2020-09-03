# gitAutomator
Automating the branching, change, and push of configured repos. [POC]

## Use Case
This utility is used in conjunction with a broader git ops solution for a branch based client serving architecture. This provides environmental segmentation and greater reduction in the chances of data compromise and a lessened plane for security risk.

## Git Ops Flow
1. Commit to SG-Automation(Revised)
  * create branch for client
  * edit all core files containing config for current makeup of SG rules
  * push to trigger action-based workflow to execute branch config
2. Commit to gitAutomator
  * create branch for client
  * edit all core files containing config for current Lambda fleet
3. Commit to CoreAutomationTF
  * create branch for client
  * edit TF plans containing config ECS components (Task Def, Service, ECR) and Lambda (Functions, Layers, Triggers)
    * requires resulting SG-id(s) from SG-Automation step as well as VPC, Subnet-ids, and Lambda results from gitAutomator
  * push to trigger action-based workflow to apply branch config
4. Commit to CoreAutomation
  * create branch for client
  * edit all core files containing config for current client application branching
  * push to trigger action-based execution of CoreAutomation along with pull and execution of gitAutomator
  
## Rationale
This selection of workflow was decided upon after consideration to speed, reliability, and familiarity. Workflow is always open to improvements and will be reviewed upon submission. 

## Possible Improvement
- It might be suggested to overhaul workflow to carry out all operations through TF and TF-incorporated bash scripting to carry out branching operations.
- It might be suggested to incorporate project management automation into this workflow, including the email correspondence tool which can be configured to send confirmation emails for availability, instead of releases.
