## Install required software

You need to install the CLIs to create and manage your Kubernetes clusters in the IBM Cloud Kubernetes Service and to deploy containerized apps.

This section shows you how to install the following CLIs and plug-ins:

- IBM Cloud CLI, Version 0.5.0 or later
- IBM Cloud Kubernetes Service plug-in
- IBM Cloud Container Registry plug-in
- Kubernetes CLI, Version 1.7.4 or later
- Docker, Version 1.9. or later

If you already have the CLIs and plug-ins, you can skip the next section.

### Install the IBM Cloud command-line interface (CLI)

1. Install the [IBM Cloud command-line interface](https://clis.ng.bluemix.net/ui/home.html). After it’s installed, you can access IBM Cloud from your command line with the prefix `ibmcloud`.

2. Log in to the IBM Cloud CLI:

   ```
   ibmcloud login.
   ```

   **For a federated ID:** If you have a [federated ID](https://console.bluemix.net/docs/overview/glossary/index.html#x2763229), use `ibmcloud login –sso` to log in to the IBM Cloud CLI. Enter your user name and use the provided URL in your CLI output to retrieve your one-time passcode. You know you have a federated ID if the login fails without the `–sso` and succeeds with the `–sso` option.

### Install the IBM Cloud Kubernetes Service plug-in

1. Create Kubernetes clusters and manage worker nodes by installing the IBM Cloud Kubernetes Service plug-in:

   `ibmcloud plugin install container-service -r Bluemix`

   **Tip:** The prefix for running commands by using the IBM Cloud Kubernetes Service plug-in is `ibmcloud cs`.

2. Verify that the plug-in is installed properly:

   `ibmcloud plugin list`

   The plug-in is displayed in the results as container-service.

### Install the IBM Cloud Container Registry plug-in

Use this plug-in to set up your own namespace in a multi-tenant, highly available, and scalable private image registry that is hosted by IBM, and to store and share Docker images with other users. Docker images are required to deploy containers into a cluster.

**Tip**: The prefix for running registry commands is `ibmcloud cr`.

1. Manage a private image repository by installing the IBM Cloud Container Registry plug-in:

   `ibmcloud plugin install container-registry -r Bluemix`

2. Verify that the plug-in is installed properly:

   `ibmcloud plugin list`

   The plug-in is displayed in the results as `container-registry`.

### Install the Kubernetes CLI (kubectl)

Install the version of [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) that is the same [Kubernetes version for IBM Cloud Container Service](https://console.bluemix.net/docs/containers/cs_versions.html#cs_versions). Using an older kubectl with a newer server might produce validation errors.

### Install Docker

To locally build images and push them to your registry namespace, [install Docker](https://www.docker.com/community-edition#/download). The Docker CLI is used to build applications into images.

**Tip:** The prefix for running commands by using the Docker CLI is `docker`.
