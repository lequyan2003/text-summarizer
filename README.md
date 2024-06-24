# text-summarizer

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py

# How to run?

### STEPS:

Clone the repository

```bash
https://github.com/lequyan2003/text-summarizer.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n summary python=3.8 -y
```

```bash
conda activate summary
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up you local host and port
```

<!-- ```bash
Author: An (Abel) Le
Email: lequyan2003@gmail.com

``` -->

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

    # with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws


    # Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

    # Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image

    - Save the URI: 891377084283.dkr.ecr.us-east-1.amazonaws.com/text-summarizer

## 4. Create EC2 machine (Ubuntu)

    - Ubuntu
    - t2.xlarge
    - Create text-summarizer-key key pair
    - Network settings: 3 ticks
    - 30 GiB

## 5. Open EC2 and Install docker in EC2 Machine:

    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade -y

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

# 6. Configure EC2 as self-hosted runner:

    Settings>Actions>Runners>New self-hosted runner>Runner image: Linux
    >Run commands from Download to Configure

# 7. Setup github secrets:

    Settings>Secrets and variables>Actions>

    (text-summarizer_accessKeys.csv)
    AWS_ACCESS_KEY_ID=first

    AWS_SECRET_ACCESS_KEY=second

    AWS_REGION = us-east-1 (Choose your AWS region)

    AWS_ECR_LOGIN_URI = demo>>  891377084283.dkr.ecr.us-east-1.amazonaws.com

    ECR_REPOSITORY_NAME = text-summarizer

# 8. Setup EC2 instance:

    Instances>Instance ID>Security>Security groups>Edit inbound rules

    >Add rule: Custom TCP, TCP, 8080, Anywhere, 0.0.0.0/0>Save rules

    >Copy Public IPv4 adress and add port 8080

# 9. Clear Resources

    EC2: Instances>Terminate instance

    ECR: Repositories>Delete

    IAM: Users>Delete
